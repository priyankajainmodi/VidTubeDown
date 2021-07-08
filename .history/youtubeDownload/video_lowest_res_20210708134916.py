import pytube
import os
import sys
from pathlib import Path
from pytube import YouTube
path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))

try:
    
    yt=YouTube(r'https://www.youtube.com/watch?v=AdKWXA8npgE&list=PLZbXA4lyCtqqDEAW1xPvcDl-ZRQs1u5oz&index=4')
except pytube.exceptions.PytubeError as error:
    print(error)
else:
    stream=yt.streams.first()
    stream.download(output_path=path_to_download_folder)