from pytube import YouTube
from tkinter import *

root = Tk()



def myClick():
    myLabel = Label(root, text = "nice")
    myLabel.pack()

def YTdownFunc(SAVE_PATH, link):
    try:
        yt = YouTube(link)
        print("Attempting Download...")
    except:
        print("CONNECTION ERROR.")

    mp4files = yt.streams.filter(progressive=True)
    d_video = yt.streams.get_by_itag(22)
    try:
        d_video.download(SAVE_PATH)
    except:
        print("DOWNLOAD ERROR.")
    print('Video is downloaded to ' + SAVE_PATH + " !")

def main():

    FirstLabel = Label(root, text = "Enter the Save Path Here:")
    FirstLabel.pack()
    e = Entry(root, width=50, borderwidth=5)
    e.pack()
    e.insert(0, "C:/Users/Public/Downloads")
    SecondLabel = Label(root, text = "Enter the YouTube link Here:")
    SecondLabel.pack()
    d = Entry(root, width=50, borderwidth=5)
    d.pack()


    myButton = Button(root, text= "Enter", command = myClick)
    myButton.pack()

    root.mainloop()

    SAVE_PATH = "C:/Users/Public/Downloads"
    link = "https://www.youtube.com/watch?v=xWOoBJUqlbI"
    #YTdownFunc(SAVE_PATH, link)

main()