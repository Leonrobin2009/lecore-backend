from flask import Flask, request, jsonify
from PIL import Image, UnidentifiedImageError
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
import io

app = Flask(__name__)

from transformers import BlipProcessor, BlipForConditionalGeneration

import os

HF_TOKEN = os.environ.get("HF_TOKEN")

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base",
    use_auth_token=HF_TOKEN
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base",
    use_auth_token=HF_TOKEN
)




def str(ex):
    pass


class BaseException:
    pass


class Exception:
    pass


@app.route("/analyze", methods=["POST"])
def analyze_image():
    try:
        if "image" not in request.files:
            return jsonify({"result": "No image uploaded"}), 400

        image_file = request.files["image"]
        image = Image.open(image_file.stream).convert("RGB")

        # Optional: Resize large images to 1024x1024 max
        max_size = (1024, 1024)
        image.thumbnail(max_size)

        inputs = processor(images=image, return_tensors="pt")
        out = model.generate(**inputs, max_length=50)
        caption = processor.decode(out[0], skip_special_tokens=True)

        return jsonify({"result": f"🧠 I see: {caption}"})
    except Exception as e:
        return jsonify({"result": f"⚠️ Failed to process image: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
