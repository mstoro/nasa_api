import base64

import requests
from flask import request, jsonify, Blueprint

from api.request import Request
from api.schemas import PayloadSchema
from api.utils import get_params, bytearray_to_img
from api.wrappers import token_required

apod_api = Blueprint('apod', __name__)


@apod_api.route('/apod', methods=['POST'])
@token_required
def apod(current_user):
    url = 'https://api.nasa.gov/planetary/apod'

    user_params = get_params(request)

    schema = PayloadSchema()
    params = schema.load(user_params)

    apod_request = Request(url, params=params)

    response = apod_request.get().json()

    if 'thumbnail_url' in response:
        image_url = response['thumbnail_url']
    else:
        image_url = response['hdurl'] if bool(params['hd']) is True \
            else response['url']

    content = requests.get(image_url).content
    bytearray_to_img(content, user_params.get('date'))
    return jsonify(
        {
            'status': 'Success! Image saved.',
            'bytes': str(base64.b64decode(content)),

        })
