import requests

resp = requests.get('https://ovni.herokuapp.com/api/apparition')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /api/apparition/ {}'.format(resp))
else:
    print('Apparitions: {} '.format(resp.json()))