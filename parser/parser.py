import pandas as pd
import functools
import json


def parse_ids():
    video_ids = []

    data = json.load(open('data.json'))
    for item in data['items']:
        id_obj = item['id']
        if id_obj['kind'] == 'youtube#video':
            video_ids.append(id_obj['videoId'])

    return video_ids


class VideoInfoRetriever:
    API_KEY = 'AIzaSyBJc4FUTH7BMQn5Sw3STGhoM6DA61aP3v4'

    def __get_url(self, video_id):
        return f'https://youtube.googleapis.com/youtube/v3/videos?part=contentDetails&part=snippet&part=statistics&part=topicDetails&id={video_id}&key={self.API_KEY}'



    def get_details(self, video_id):
        import requests
        data = requests.get(self.__get_url(video_id))
        return data.json()


def video_as_json_to_series(video_details):
    video_object = video_details['items'][0]
    video_object_dict = {}
    video_object_dict['id'] = video_object['id']

    snippet = video_object['snippet']
    video_object_dict['published_datetime'] = snippet['publishedAt']
    video_object_dict['title'] = snippet['title']
    video_object_dict['description'] = snippet['description']
    try:
        video_object_dict['thumbnail_medium'] = snippet['thumbnails']['medium']['url']
    except KeyError:
        video_object_dict['thumbnail_medium'] = None
    try:
        video_object_dict['thumbnail_maxres'] = snippet['thumbnails']['maxres']['url']
    except KeyError:
        video_object_dict['thumbnail_maxres'] = None
    try:
        video_object_dict['tags'] = snippet['tags']
    except KeyError:
        video_object_dict['tags'] = None

    video_object_dict['duration'] = video_object['contentDetails']['duration']
    video_object_dict['definition'] = video_object['contentDetails']['definition']
    video_object_dict['rating'] = video_object['contentDetails']['contentRating']
    video_object_dict['views'] = int(video_object['statistics']['viewCount'])
    video_object_dict['likes'] = int(video_object['statistics']['likeCount'])
    #video_object_dict['comments'] = int(video_object['statistics']['commentCount'])
    cats = []
    for item in video_object['topicDetails']['topicCategories']:
        cats.append(item[item.rfind('/') + 1::])
    video_object_dict['categories'] = cats
    return video_object_dict


def update_dataset(filename='video_dataset.csv'):
    v = VideoInfoRetriever()
    ids = parse_ids()
    series = [video_as_json_to_series(v.get_details(id)) for id in ids]
    data = pd.DataFrame(series)
    data.to_csv(filename)


def load_videos(filename='video_dataset.csv'):
    return pd.read_csv(filename)


if __name__ == "__main__":
    update_dataset()
