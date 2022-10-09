# video_scripts

Various scripts to manipulate video content

- [x] Store and manipulate channels and videos metadata(youtube_dl)
- [x] Store and manipulate channels and videos metadata(selenium, bs4)
- [x] Download videos, audios and save(youtube_dl, ffmpeg)
- [x] Explore stored metadata(streamlit)
- [ ] Upload videos(google-api)

## Setup

```sh
$ git clone video_scripts.git
$ cd video_scripts
$ python -m venv .venv
$ source .venv/bin/activate
$ python -m pip install -r requirements.txt
```

## Run

### dwnld.py

```bash
$ python dwnld.py -h
usage: dwnld.py [-h] [--download] [--no_cache] links [links ...]

dwnld.py used for YouTube videos downloading with caching

positional arguments:
  links       links separated with spaces

optional arguments:
  -h, --help  show this help message and exit
  --download  use to download content from source
  --no_cache  avoid caching
```

### page_parser.py

```bash
$ python page_parser.py -h
usage: page_parser.py [-h] [--scrolls SCROLLS] url

page_parser.py used for YouTube videos metadata parsing

positional arguments:
  url                channel url

options:
  -h, --help         show this help message and exit
  --scrolls SCROLLS  number of page scroll down
```

### explorer.py

Streamlit dashboard

```bash
streamlit run explorer.py 
```
