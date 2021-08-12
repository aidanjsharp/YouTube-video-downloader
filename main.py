from pytube import YouTube
from tkinter import *

root = Tk()


def myClick(labels, entries, myButton):
    SAVE_PATH = entries[0].get()
    link = entries[1].get()

    for entry in entries:
        entry.pack_forget()
    for label in labels:
        label.pack_forget()
    myButton.pack_forget()

    YTdownFunc(SAVE_PATH, link)

def YTdownFunc(SAVE_PATH, link):
    loadingLabel = Label(root, text = "loading...")
    loadingLabel.pack()
    try:
        yt = YouTube(link)
    except:
        loadingLabel.pack_forget()
        cErrorLabel = Label(root, text ="CONNECTION ERROR.")
        cErrorLabel.pack()

    mp4files = yt.streams.filter(progressive=True)
    d_video = yt.streams.get_by_itag(22)
    try:
        d_video.download(SAVE_PATH)
    except:
        loadingLabel.pack_forget()
        dErrorLabel = Label(root, text ="DOWNLOAD ERROR.")
        dErrorLabel.pack()

    loadingLabel.pack_forget()
    downloadedLabel = Label(root, text='Video is downloaded to ' + SAVE_PATH + " !")
    downloadedLabel.pack()

    clearButton = Button(root, text="Clear", command= "boob")
    clearButton.pack()

def main():
    SAVE_PATH = "C:/Users/Public/Downloads"
    link = "https://www.youtube.com/watch?v=xWOoBJUqlbI"
    labels = []
    entries = []

    FirstLabel = Label(root, text="Enter the Save Path Here:")
    labels.append(FirstLabel)
    labels[0].pack()

    e = Entry(root, width=50, borderwidth=5)
    entries.append(e)
    entries[0].pack()
    entries[0].insert(0, SAVE_PATH)

    SecondLabel = Label(root, text="Enter the YouTube link Here:")
    labels.append(SecondLabel)
    labels[1].pack()

    d = Entry(root, width=50, borderwidth=5)
    entries.append(d)
    entries[1].pack()
    entries[1].insert(0, link)

    myButton = Button(root, text= "Enter", command = lambda: myClick(labels, entries, myButton))
    myButton.pack()


    root.mainloop()



main()