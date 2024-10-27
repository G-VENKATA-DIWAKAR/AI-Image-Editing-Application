# AI-Powered Image Editing Application

This is a simple AI-powered image editing application built using Flask for the backend and React for the frontend. The application allows users to upload images, enhance them, and remove backgrounds using basic image processing techniques.

## Features

- Upload images
- Enhance brightness and contrast
- Remove backgrounds
- Basic framework for future features like style transfer and face enhancement

## Tech Stack

- **Backend:** Flask, Flask-Cors, Pillow, OpenCV
- **Frontend:** React, Axios

## Requirements

### Backend

Make sure you have Python and pip installed. Then, create a virtual environment and install the required libraries:

```bash
# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install required packages
pip install Flask Flask-Cors Pillow opencv-python
