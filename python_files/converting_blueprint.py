from flask import Blueprint, request, Flask
import pytesseract
import cv2 as cv
import logging

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'
app = Flask(__name__)

converting_blueprint = Blueprint('converting_blueprint', __name__)


@converting_blueprint.route('/convert', methods=['POST'])
def index():
    image = request.get_json().get('image')

    img = cv.imread('uploads/' + image)

    rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    text = pytesseract.image_to_string(rgb_img, lang='fas+eng')

    return {
        "success": True,
        "message": text
    }
