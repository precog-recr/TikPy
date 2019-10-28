# TikTok API

TikTok has no public API. This library is aimed at getting the public data available at [www.tiktok.com](https://www.tiktok.com). 

## Instlling
```python
pip install TikPy
```
## Quick Start
```python
from TikPy import TikAPI as API

api = API()
api.get_user_info('avinasht', from_video=False)
```

## Documentation

`get_user_info(name)` Takes in user name, returns user information available on tiktok.com/@<name>

`get_user_videos(name)` Takes user name, returns the first 10 videos available on tiktok.com/@<name>

`get_trending_posts()` returns a list of trending posts. 

`get_video_info(url)` Takes url of a video and returns video info. 

`get_hash_recommend_list(hashtag)` Returns four related hashtags as lited on TikTok, of the input. 

`get_hash_videos(hashtag)` Returns the first 10 videos related to a hashtag. 

`get_videos_from_music(music_id, name)` Returns videos related to music. 

`get_music_recommend_list(music_id, name)` Returns four related music recommendations as listed on TikTok.

`download_video(url, post_name=None)` if post_name is None, video is returned in the form of chunk. Else the video is saved with post_name. 

