import os

import requests
from flask import jsonify, Blueprint, current_app

from api.request import Request
from api.schemas import PayloadSchema
from api.utils import (
    save_image,
    get_jwt,
    get_json,
    get_media_path,
    get_file_name
)

apod_api = Blueprint('apod', __name__)


@apod_api.route('/apod', methods=['POST'])
def apod():
    url = current_app.config['APOD_URL']
    params = {'api_key': get_jwt(),
              **get_json(PayloadSchema())}

    apod_request = Request(url, params=params)

    response = apod_request.get().json()

    if 'thumbnail_url' in response:
        image_url = response['thumbnail_url']
    else:
        image_url = (
            response['hdurl'] if bool(params['hd']) is True
            else response['url']
        )

    content = requests.get(image_url).content

    path = get_media_path()
    file_name = get_file_name(params['date'])

    save_image(content, path, file_name)

    return jsonify(
        {
            'status': 'Success! Image saved.',
            'path': os.path.join(path, file_name),

        })
