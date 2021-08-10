from pytube import YouTube
from tkinter import *

root = Tk()





def myClick(FirstLabel, e, SecondLabel, d, myButton, SAVE_PATH, link):
    SAVE_PATH = e.get()
    link = d.get()

    e.pack_forget()
    FirstLabel.pack_forget()
    d.pack_forget()
    SecondLabel.pack_forget()
    myButton.pack_forget()

    loadingLabel = Label(root, text = "loading...")
    loadingLabel.pack()


    YTdownFunc(SAVE_PATH, link, loadingLabel)

def YTdownFunc(SAVE_PATH, link, loadingLabel):
    try:
        yt = YouTube(link)
    except:
        loadingLabel.pack_forget()
        cError = Label(root, text ="CONNECTION ERROR.")
        cError.pack()

    mp4files = yt.streams.filter(progressive=True)
    d_video = yt.streams.get_by_itag(22)
    try:
        d_video.download(SAVE_PATH)
    except:
        loadingLabel.pack_forget()
        dError = Label(root, text ="DOWNLOAD ERROR.")
        dError.pack()

    loadingLabel.pack_forget()
    downloadedLabel = Label(root, text='Video is downloaded to ' + SAVE_PATH + " !")
    downloadedLabel.pack()

def main():
    SAVE_PATH = "C:/Users/Public/Downloads"
    link = "https://www.youtube.com/watch?v=xWOoBJUqlbI"


    FirstLabel = Label(root, text="Enter the Save Path Here:")
    FirstLabel.pack()
    e = Entry(root, width=50, borderwidth=5)
    e.pack()
    e.insert(0, "C:/Users/Public/Downloads")
    SecondLabel = Label(root, text="Enter the YouTube link Here:")
    SecondLabel.pack()
    d = Entry(root, width=50, borderwidth=5)
    d.pack()

    myButton = Button(root, text= "Enter", command = lambda: myClick(FirstLabel, e, SecondLabel, d, myButton, SAVE_PATH, link))
    myButton.pack()
    SAVE_PATH = e.get()
    link = d.get()
    print(SAVE_PATH)
    print(link)

    root.mainloop()



main()