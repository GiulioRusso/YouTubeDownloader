from pytube import YouTube
from sys import argv

DOWNLOAD_FOLDER = "" # your download folder path

if (len(argv) == 1):
    print("\n >>> WARNING: no link specified \n")

else:
    # Get the link specified
    link = argv[1]
    yt = YouTube(link)
    print("\n >>> Downloading video: '{}' ".format(yt.title))

    # Download video
    yd = yt.streams.get_highest_resolution()
    yd.download(DOWNLOAD_FOLDER)
    print("\n >>> Video saved at: '{}' \n".format(DOWNLOAD_FOLDER))