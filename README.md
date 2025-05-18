# Color Detection App 🎨

A simple and intuitive color detection application that allows users to upload images and identify colors by clicking on any point in the image. Built with Python, OpenCV, and Streamlit.

## Features

- Upload and display images (JPG, JPEG, PNG formats)
- Click anywhere on the image to detect colors
- View color name and RGB values in real-time
- Visual color box display of the detected color
- Pre-defined color dataset with common color names

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/color-detection-app.git
cd color-detection-app
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Upload an image using the file uploader

4. Click the "Click to detect color" button and then click anywhere on the image to detect colors

## Project Structure

```
color-detection-app/
├── app.py              # Main application file
├── colors.csv          # Color dataset
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## Dependencies

- OpenCV (cv2)
- NumPy
- Pandas
- Streamlit
- PIL (Python Imaging Library)

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 