from flask import Blueprint, current_app, jsonify

from api.request import Request
from api.schemas import CMEPayloadSchema
from api.utils import get_jwt, get_json, cme_form_data

cme_api = Blueprint('cme', __name__)


@cme_api.route('/cme', methods=['GET'])
def cme():
    url = current_app.config['CME_URL']

    params = {'api_key': get_jwt(),
              **get_json(CMEPayloadSchema())}

    cme_request = Request(url, params=params)

    response = cme_request.get().json()

    cme_info = cme_form_data(response)

    return jsonify(cme_info)
