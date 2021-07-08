import pytube
import os
import sys
from pathlib import Path
from pytube import YouTube
path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))

try:
    url="https://www.youtube.com/watch?v=uc0Hh-IrqL4"
    yt=YouTube(url)
except pytube.exceptions.PytubeError as error:
    print(error)
else:
    stream=yt.streams.get_lowest_resolution() 
    stream.download(output_path=path_to_download_folder)