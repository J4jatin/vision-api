from flask import Flask, request, jsonify
from transformers import pipeline
from PIL import Image

app = Flask(__name__)

# Load AI model
model = pipeline("image-classification", 
                model="google/vit-base-patch16-224")

@app.route('/')
def home():
    return "Vision API is running!"

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    image = Image.open(request.files['image'])
    results = model(image)
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)