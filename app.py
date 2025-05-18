import streamlit as st
import cv2
import numpy as np
import pandas as pd
from PIL import Image
import io

# Set page config
st.set_page_config(
    page_title="Color Detection App",
    page_icon="🎨",
    layout="wide"
)

# Function to load the color dataset
@st.cache_data
def load_color_data():
    try:
        df = pd.read_csv('colors.csv')
        return df
    except FileNotFoundError:
        st.error("Colors dataset not found. Please ensure colors.csv is in the same directory.")
        return None

# Function to find the closest color name
def get_color_name(R, G, B, df):
    minimum = 1000
    color_name = ""
    
    for i in range(len(df)):
        d = abs(R - df.loc[i, "R"]) + abs(G - df.loc[i, "G"]) + abs(B - df.loc[i, "B"])
        if d <= minimum:
            minimum = d
            color_name = df.loc[i, "Color Name"]
    
    return color_name

# Main app
def main():
    st.title("🎨 Color Detection App")
    st.write("Upload an image and click anywhere to detect the color!")

    # Load color dataset
    df = load_color_data()
    if df is None:
        return

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file is not None:
        # Convert the file to an opencv image
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Create two columns
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Display the image
            st.image(image, caption='Uploaded Image', use_column_width=True)
            
            # Get image dimensions
            h, w = image.shape[:2]
            
            # Create sliders for X and Y coordinates
            st.write("Select pixel coordinates to detect color:")
            x = st.slider("X coordinate", 0, w-1, w//2)
            y = st.slider("Y coordinate", 0, h-1, h//2)
            
            # Draw a marker at selected point
            marked_image = image.copy()
            cv2.circle(marked_image, (x, y), 5, (255, 0, 0), -1)  # Red circle at selected point
            st.image(marked_image, caption='Selected Point', use_column_width=True)
            
            # Get RGB values
            B, G, R = image[y, x]
            
            # Get color name
            color_name = get_color_name(R, G, B, df)
            
            with col2:
                st.write("Selected Color Information:")
                st.markdown(f"**Position:** ({x}, {y})")
                st.markdown(f"**Color Name:** {color_name}")
                st.markdown(f"**RGB Value:** ({R}, {G}, {B})")
                
                # Display color box
                color_box = np.zeros((100, 100, 3), dtype=np.uint8)
                color_box[:] = [R, G, B]
                st.image(color_box, caption="Selected Color", use_column_width=True)

if __name__ == "__main__":
    main() 