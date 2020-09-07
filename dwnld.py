import pickle, os, hashlib, time, argparse, json, logging
from youtube_dl import YoutubeDL

log = logging.getLogger(__name__)

def get_videos_data(url: str, options: dict, no_cache: bool):
    local_folder = os.getcwd()
    data_folder = ".dlcache"
    if not os.path.exists(data_folder):
        log.info("Creating missing .dlcache folder")
        os.mkdir(data_folder)
    link_hash = hashlib.sha1(url.encode('utf-8')).hexdigest()[10:]
    cache_path = os.path.join(local_folder, 
                                data_folder, 
                                str(int(time.time() / 10 ** 5)) + link_hash)
    try:
        f = open(cache_path, 'rb')  
        log.info(f'Loading {url} content from cache')
        result = pickle.load(f) 
    except (OSError, IOError) as e:
        log.info(f'Downloading {url} info')
        result = get_info(url, options)
        with open(cache_path, 'wb+') as cf:
            if not no_cache: pickle.dump(result, cf)
            log.info(f'Cached {cache_path}')
    return result

def get_info(url: str, options: dict) -> dict:
    with YoutubeDL(options) as ydl:
        return ydl.extract_info(url,download=False)

def download(url: str, options: dict):
    with YoutubeDL(options) as ydl:
        ydl.download([url])

def main():
    parser = argparse.ArgumentParser(description='%(prog)s used for YouTube videos downloading with caching')
    parser.add_argument('links', type=str, nargs='+', 
                        help="channel links separated with spaces", )
    parser.add_argument('--download', action="store_true", default = False,
                        help='use to download content from source', )
    parser.add_argument('--no_cache', action="store_true", default = False, 
                        help='avoid caching', )
    args = parser.parse_args()

    if not os.path.exists('Videos'):
        log.info("Creating missing Videos output folder")
        os.mkdir('Videos')

    options = {
        'merge-output-format': 'mp4',
        'format': 'bestvideo+bestaudio/best',
        'metadata-from-title': '%(id)s',
        'add-metadata': True,
        'continue_dl': True,
        'outtmpl': os.path.join('Videos', '%(title)s.mp4'),
        }   

    r = get_videos_data(*args.links, options, args.no_cache)

    if args.download:
        log.debug('Downloading videos')
        urls = [v.get('webpage_url') for v in [r]]
        [download(l, options) for l in urls]
   

if __name__=='__main__':
    main()

