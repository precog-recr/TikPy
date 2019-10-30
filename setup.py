from distutils.core import setup
setup(
  name = 'TikPy',         # How you named your package folder (MyLib)
  packages = ['TikPy'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  long_description="""
  # TikTok API

TikTok has no public API. TikPy is a **light weight API**, without the requirement of any browser sessions, to collect the public data available at [www.tiktok.com](https://www.tiktok.com). Collect trending posts, video metadata, user metadata, hashtags, music, related hashtags, related music and, download videos with the API. Everything is returned in a JSON object. 

## Instlling
```python
pip install TikPy
```
## Quick Start
```python
from TikPy import TikAPI

api = TikAPI.API()
api.get_user_info('leenabhushan')
```

## Documentation

`get_user_info(name)` 
Takes in user name, returns user information available on tiktok.com/@<name>

`get_user_videos(name)` 
Takes user name, returns the first 10 videos available on tiktok.com/@<name>

`get_trending_posts()` 
returns a list of trending posts. 

`get_video_info(url)` 
Takes url of a video and returns video info. 

`get_hash_recommend_list(hashtag)` 
Returns four related hashtags as lited on TikTok, of the input. 

`get_hash_videos(hashtag)` Returns the first 10 videos related to a hashtag. 

`get_videos_from_music(music_id, name)` Returns videos related to music. 

`get_music_recommend_list(music_id, name)` Returns four related music recommendations as listed on TikTok.

`download_video(url, post_name=None)` if post_name is None, video is returned in the form of chunk. Else the video is saved with post_name. 


  """,

  long_description_content_type='text/markdown',
  # description = 'https://github.com/precog-recr/TikPy/README.md',   # Give a short description about your library
  author = 'Vishwesh Kumar',                   # Type in your name
  author_email = 'vishwesh18119@iiitd.ac.in',      # Type in your E-Mail
  url = 'https://github.com/precog-recr/TikPy',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/precog-recr/TikPy/archive/v_05.tar.gz',    # I explain this later on
  keywords = ['TikTok', 'API'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'bs4',
          'newspaper3k'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    # 'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    # 'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)