# Vision API

A lightweight REST API that uses AI to identify what's in an image. 
Built with Flask and powered by Google's Vision Transformer model.

## What it does

Send any image to the API and it tells you what it sees — 
with a confidence score. That's it.

## Built with

- Python & Flask — for the API
- HuggingFace Transformers — for the AI model
- Google ViT (Vision Transformer) — the actual brain
- Docker — so it runs anywhere

## Getting started

Clone the repo and install dependencies:

pip install -r requirements.txt

Run the server:

python app.py

## Usage

Send a POST request to /analyze with an image file:

curl -X POST -F "image=@your_image.jpg" http://127.0.0.1:5000/analyze

You'll get back something like:

[
  {"label": "beagle", "score": 0.94},
  {"label": "dog", "score": 0.03}
]

## Docker

docker build -t vision-api .
docker run -p 5000:5000 vision-api

## Why I built this

I wanted to understand how computer vision models 
work in practice — not just theory. This project 
connects a real AI model to a real API endpoint 
that anyone can test with their own images.
