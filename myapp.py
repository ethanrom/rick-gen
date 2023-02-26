import streamlit as st
import numpy as np
from PIL import Image
import colorgram
import requests


def get_colors(image, num_colors):
    """
    Returns the dominant colors in the image using the colorgram library.
    """
    img = Image.open(image)
    colors = colorgram.extract(img, num_colors)
    return [tuple(c.rgb) for c in colors]

def apply_palette(colors, image):
    img = Image.open(image).convert("RGBA")
    pixels = np.array(img)

    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            closest_color = find_closest_color(colors, pixels[i, j][:3])
            pixels[i, j] = np.append(closest_color, 255)

    img = Image.fromarray(pixels, mode="RGBA")
    return img

def main():
    st.title("Color Palette App")

    # Upload the images
    image1 = st.file_uploader("Upload the first image", type=["jpg", "jpeg", "png"])
    image2 = st.file_uploader("Upload the second image", type=["jpg", "jpeg", "png"])

    if image1 and image2:
        # Get the color palette of the first image
        num_colors = st.slider("Number of colors", min_value=2, max_value=20, value=5, step=1)
        colors = get_colors(image1, num_colors)

        # Show the color palette
        st.subheader("Color Palette")
        col1, col2, col3, col4, col5 = st.columns(5)
        for i, color in enumerate(colors):
            hex_color = '#{:02x}{:02x}{:02x}'.format(*color)
            with col1 if i < 5 else col2 if i < 10 else col3 if i < 15 else col4 if i < 20 else col5:
                st.color_picker(f"Color {i+1}", hex_color)

        # Apply the color palette to the second image
        if st.button("Apply Color Palette"):
            image2 = apply_palette(colors, image2)
            st.image(image2, caption="Result", use_column_width=True)

if __name__ == "__main__":
    main()
