import json


def parse_ids():
    video_ids = []

    data = json.load(open('data.json'))
    for item in data['items']:
        id_obj = item['id']
        if id_obj['kind'] == 'youtube#video':
            video_ids.append(id_obj['videoId'])

    return video_ids
