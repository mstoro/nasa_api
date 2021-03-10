from flask import Blueprint, current_app, jsonify

from api.request import Request
from api.schemas import CMEPayloadSchema
from api.utils import get_jwt, form_cme_data, get_params

cme_api = Blueprint('cme', __name__)


@cme_api.route('/cme', methods=['GET'])
def cme():
    url = current_app.config['CME_URL']

    params = {'api_key': get_jwt(),
              **get_params(CMEPayloadSchema())}

    cme_request = Request(url, params=params)

    response = cme_request.get().json()

    cme_info = form_cme_data(response)

    return jsonify(cme_info)
