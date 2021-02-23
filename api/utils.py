from io import BytesIO

from PIL import Image


def get_params(request):
    params = {'api_key': 'DEMO_KEY',
              'date': request.get_json()['date'],
              'hd': request.get_json()['hd'],
              'thumbs': request.get_json().get('thumbs', 'True')
              }
    return params


def bytearray_to_img(byte_array, date):
    Image.open(BytesIO(byte_array)).save(f'{date}.jpg')
    return 'saved'
