import streamlit as st
import numpy as np
from PIL import Image
import colorgram

# Function to extract colors from an image using Colorgram
def get_colors(image, num_colors):
    img = Image.open(image)
    colors = colorgram.extract(img, num_colors)
    return [tuple(c.rgb) for c in colors]

# Function to find the closest color in a list to a target color
def find_closest_color(colors, target):
    colors = np.array(colors)
    target = np.array(target)
    distances = np.sqrt(np.sum((colors - target) ** 2, axis=1))
    closest_color_index = np.argmin(distances)
    return colors[closest_color_index]

# Function to apply a color palette to an image
def apply_palette(colors, image):
    img = Image.open(image).convert("RGBA")
    pixels = np.array(img)

    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            closest_color = find_closest_color(colors, pixels[i, j][:3])
            pixels[i, j] = np.append(closest_color, 255)

    img = Image.fromarray(pixels, mode="RGBA")
    return img

# Main function
def main():
    # Set page title and favicon
    st.set_page_config(page_title="Color Palette App", page_icon=":art:")

    # Define page layout
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://i.imgur.com/UcRfRhr.png", width=100)
    with col2:
        st.title("Color Palette App")
        st.write("---")

    # Upload the images
    st.write("### Upload Images")
    st.write("Upload two images, the first one will be used to extract the color palette.")
    uploaded_file1 = st.file_uploader("Upload the first image", type=["jpg", "jpeg", "png"])
    uploaded_file2 = st.file_uploader("Upload the second image", type=["jpg", "jpeg", "png"])

    if uploaded_file1 and uploaded_file2:
        # Get the color palette of the first image
        st.write("### Color Palette Selection")
        num_colors = st.slider("Number of colors", min_value=2, max_value=20, value=5, step=1)
        colors = get_colors(uploaded_file1, num_colors)

        # Display the color palette
        st.write("Drag and drop the colors to rearrange the palette.")
        palette_container = st.container()
        with palette_container:
            for i, color in enumerate(colors):
                hex_color = '#{:02x}{:02x}{:02x}'.format(*color)
                selected_color = st.color_picker(f"Color {i+1}", hex_color, key=f"color{i}")
                colors[i] = tuple(int(selected_color.lstrip('#')[k:k+2], 16) for k in (0, 2, 4))

        # Apply the color palette to the second image
        st.write("### Result")
        if st.button("Apply Color Palette"):
            result_image = apply_palette(colors, uploaded_file2)
            st.image(result_image, caption="Result", use_column_width=True)

# Run the app
if __name__ == "__main__":
    main()
