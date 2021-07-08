import os
import sys
from pathlib import Path
from pytube import YouTube
import pytube



path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
try:
    
    
    yt=YouTube(sys.argv[1])
except pytube.exceptions.PytubeError as error:
    print(error)
else:
    print("sleep")
    stream=yt.streams.get_highest_resolution()
    print(stream)
    print(stream.filesize)
    print(stream.download())
    
    
    