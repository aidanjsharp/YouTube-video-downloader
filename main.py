from pytube import YouTube

def main():
    SAVE_PATH = "C:/Users/Public/Downloads"
    link = "https://www.youtube.com/watch?v=xWOoBJUqlbI"

    try:
        yt = YouTube(link)
    except:
        print("CONNECTION ERROR.")

    mp4files = yt.streams.filter(progressive=True)

    d_video = yt.streams.get_by_itag(22)
    try:
        d_video.download(SAVE_PATH)
    except:
        print("DOWNLOAD ERROR.")
    print('Video is downloaded to ' + SAVE_PATH + " !")



main()