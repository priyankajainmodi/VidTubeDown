import os
import sys
from pathlib import Path
from pytube import YouTube
import pytube

path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
try:
    
    
    yt=YouTube('https://www.youtube.com/watch?v=1TR9riaDzY8')
    print(yt)
except pytube.exceptions.PytubeError as error:
    print(error)
else:
    
    stream=yt.streams.get_audio_only()
   
    stream.download(output_path=path_to_download_folder)
    
    
    