from pytube import YouTube # one video download
from tqdm import tqdm #progress bar
url = 'https://youtu.be/NHWTNgnlGs4'
video = YouTube(url)

#get video title
print("********************Video Title********************")
print(video.title)

#get video thumbnail
print("********************Tumbnail********************")
print(video.thumbnail_url)
#get stream(video) resolution
print("********************Download Video********************")
"""video = video.streams.get_lowest_resolution()
video.download()"""

#videos = video.streams.all() #All Format

videos = video.streams.filter(only_video = True) #only audio
vidlist = list(enumerate(videos))

for i in vidlist:
    print(i)

strm = int(input("Enter the required index of vidlist as input :"))
tqdm(videos[strm].download())
print("Download Successfully")



