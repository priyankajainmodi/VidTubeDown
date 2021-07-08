import os
import sys
from pathlib import Path
import pytube
from pytube import YouTube
path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
try:
    url=sys.argv[1]
    yt=YouTube(url)
except pytube.exceptions.PytubeError as error:
    print(error)
else:
    stream=yt.streams.filter(only_audio=True).first()
    output=stream.download(output_path=path_to_download_folder)
    base, ext = os.path.splitext(output)
    new_file = base + '.mp3'
    os.rename(output, new_file)