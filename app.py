from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image, ImageEnhance
import numpy as np
import cv2
import os

app = Flask(__name__)
CORS(app)

# Directory for storing uploaded images
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    
    return jsonify({'message': 'File uploaded successfully', 'file_path': file_path}), 200

@app.route('/enhance', methods=['POST'])
def enhance_image():
    data = request.json
    file_path = data.get('file_path')
    brightness_factor = data.get('brightness', 1.0)
    contrast_factor = data.get('contrast', 1.0)

    try:
        # Open image using Pillow
        img = Image.open(file_path)
        # Adjust brightness and contrast
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(brightness_factor)
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(contrast_factor)

        enhanced_file_path = os.path.join(UPLOAD_FOLDER, 'enhanced_' + os.path.basename(file_path))
        img.save(enhanced_file_path)

        return jsonify({'message': 'Image enhanced successfully', 'enhanced_file_path': enhanced_file_path}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/remove-background', methods=['POST'])
def remove_background():
    data = request.json
    file_path = data.get('file_path')

    # Load image with OpenCV
    img = cv2.imread(file_path)
    # Basic background removal logic (for demonstration purposes)
    # You can implement advanced methods using deep learning models
    mask = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY_INV)

    result = cv2.bitwise_and(img, img, mask=mask)
    output_path = os.path.join(UPLOAD_FOLDER, 'bg_removed_' + os.path.basename(file_path))
    cv2.imwrite(output_path, result)

    return jsonify({'message': 'Background removed successfully', 'output_path': output_path}), 200

@app.route('/style-transfer', methods=['POST'])
def style_transfer():
    # Placeholder function for style transfer
    # Implement style transfer using a pre-trained model
    return jsonify({'message': 'Style transfer functionality not implemented yet.'}), 501

@app.route('/face-enhancement', methods=['POST'])
def face_enhancement():
    # Placeholder function for face enhancement
    # Implement face enhancement using a pre-trained model
    return jsonify({'message': 'Face enhancement functionality not implemented yet.'}), 501

if __name__ == '__main__':
    app.run(debug=True)
