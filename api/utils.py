from io import BytesIO

from PIL import Image
from flask import jsonify


def bytearray_to_img(byte_array, date):
    Image.open(BytesIO(byte_array)).save(f'{date}.jpg')
    return 'saved'


def jsonify_message(message):
    return jsonify({'message': message})
