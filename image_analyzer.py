from flask import Flask, request, jsonify
from PIL import Image, UnidentifiedImageError
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
import io
import os

app = Flask(__name__)

# Get Hugging Face token securely (set it in Render or .env)
HF_TOKEN = os.environ.get("HF_TOKEN")

# Load the BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base", token=HF_TOKEN)
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base", token=HF_TOKEN)


@app.route("/analyze", methods=["POST"])
def analyze_image():
    if "image" not in request.files:
        return jsonify({"result": "❌ No image uploaded"}), 400

    image_file = request.files["image"]
    prompt = request.form.get("prompt", "").strip()

    try:
        image = Image.open(image_file.stream).convert("RGB")
    except UnidentifiedImageError:
        return jsonify({"result": "❌ Failed to read image"}), 400

    try:
        # Use prompt if available
        if prompt:
            inputs = processor(images=image, text=prompt, return_tensors="pt")
        else:
            inputs = processor(images=image, return_tensors="pt")

        out = model.generate(**inputs, max_length=60)
        caption = processor.decode(out[0], skip_special_tokens=True)

        return jsonify({"result": f"🧠 I see: {caption}"}), 200

    except Exception as e:
        return jsonify({"result": f"❌ Server error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
