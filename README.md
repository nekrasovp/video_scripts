# video_scripts

Various scripts to manipulate video content

- [x] Store and manipulate channels and videos metadata(youtube_dl)
- [x] Download videos, audios and save(youtube_dl, ffmpeg)
- [ ] Upload videos(google-api)

## dwnld.py

```text
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
