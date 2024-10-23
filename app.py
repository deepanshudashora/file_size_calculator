from flask import render_template, request, jsonify, send_file, Flask
import base64
import os

app = Flask(__name__)

# Setting the path for the images folder
IMAGES_FOLDER = os.path.join(app.static_folder, 'images')

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to get animal images
@app.route('/get_animal_image/<animal>')
def get_animal_image(animal):
    image_path = os.path.join(IMAGES_FOLDER, f'{animal}.jpg')
    
    # Check if the image exists and encode it in base64
    if os.path.exists(image_path):
        with open(image_path, 'rb') as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
        return jsonify({'image': encoded_image})
    else:
        return jsonify({'error': 'Image not found'}), 404

# Route to handle file uploads
@app.route('/upload_file', methods=['POST'])
def upload_file():
    # Check if file part is in request
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    # Check if a file is selected
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    file_size_bytes = len(file.read())
    file_size_mb = file_size_bytes / (1024 * 1024)  # Convert bytes to MB

    # Return file details
    file_info = {
        'name': file.filename,
        'size': f"{file_size_mb:.2f} MB",
        'type': file.content_type
    }

    return jsonify(file_info)

if __name__ == '__main__':
    app.run(debug=True)
