from pytube import YouTube
from sys import argv

if (len(argv) == 1):
    print("\n >>> WARNING: no link specified \n")

else:
    # Get the link specified
    link = argv[1]
    yt = YouTube(link)
    print("\n >>> Downloading video: '{}' ".format(yt.title))

    # Download folder
    download_folder = "/Users/giuliorusso/Downloads" # your download folder path

    # Download video
    yd = yt.streams.get_highest_resolution()
    yd.download(download_folder)
    print("\n >>> Video saved at: '{}' \n".format(download_folder))