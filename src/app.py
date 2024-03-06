from flask import Flask, request, jsonify
from flask_cors import CORS
import boto3
import base64
import dotenv
import os

app = Flask(__name__)
CORS(app)
dotenv.load_dotenv()

@app.route("/tarea3-201900462", methods=["POST"])
def analyze_image():
    content = request.json
    image_data = content["image"]
    image = base64.b64decode(image_data)

    client = boto3.client(
        "rekognition",
        region_name="us-east-1",
        aws_access_key_id=os.getenv("REKOGNITION_PUBLIC_KEY"),
        aws_secret_access_key=os.getenv("REKOGNITION_PRIVATE_KEY"),
    )

    response = client.detect_labels(Image={"Bytes": image})
    labels = response["Labels"]

    return jsonify(labels)


if __name__ == "__main__":
    app.run(debug=True)
