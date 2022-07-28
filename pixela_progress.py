from datetime import datetime

import requests


USERNAME = 'ishkining'
TOKEN = 'idontknowwhyilovetoeat'
GRAPH_ID = 'trackprogress'

pixela_endpoint = 'https://pixe.la/v1/users'

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

headers = {
    'X-USER-TOKEN': TOKEN
}

pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

get_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{datetime.now().strftime("%Y%m%d")}'


def get_progress():
    get_response = requests.get(url=get_endpoint, headers=headers)
    try:
        result = str(int(get_response.json()['quantity']) + 1)
        print("Getting pixela is easy")
    except KeyError:
        result = None
    finally:
        return result


def update_progress():
    get_result = get_progress()
    if get_result is not None:
        pixel_data = {
            'date': datetime.now().strftime('%Y%m%d'),
            'quantity': get_result,
        }

    else:
        pixel_data = {
            'date': datetime.now().strftime('%Y%m%d'),
            'quantity': str(1),
        }
    response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
    print(response.text)


graph_params = {
    'date': datetime.now().strftime('%Y%m%d'),
    'mode': 'short',
    'appearance': 'dark',
}

#
# def show_graph():
#     get_response = requests.get(url=pixel_creation_endpoint, json=graph_params)
#     return BeautifulSoup(get_response.content.decode('utf-8')).get_text()
