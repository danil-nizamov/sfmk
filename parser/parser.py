import pandas as pd
import functools
from ids import parse_ids


class VideoInfoRetriever:
    API_KEY = 'AIzaSyBJc4FUTH7BMQn5Sw3STGhoM6DA61aP3v4'

    def __get_url(self, video_id):
        return f'https://youtube.googleapis.com/youtube/v3/videos?part=contentDetails&part=statistics&part=topicDetails&id={video_id}&key={self.API_KEY}'

    def get_details(self, video_id):
        import requests
        data = requests.get(self.__get_url(video_id))
        return data.json()


def video_as_json_to_series(video_details):
    video_object = video_details['items'][0]
    video_object_dict = {}
    video_object_dict['id'] = video_object['id']
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
    data.to_csv('video_dataset.csv')


def load_videos(filename='video_dataset.csv'):
    return pd.read_csv('video_dataset.csv')


if __name__ == "__main__":
    update_dataset()
