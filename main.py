from pytube import YouTube
from tkinter import *

#creating the window
root = Tk()

#creating universal variables and labels
SAVE_PATH = "C:/Users/Public/Downloads"
link = "https://www.youtube.com/watch?v=xWOoBJUqlbI"
downloadedLabel = Label(root, text='Video is downloaded to ' + SAVE_PATH + " !")
clearButton = Button(root, text="New Download", command= lambda: main(clearButton, downloadedLabel))
clearButton.pack()


#defining click action for the download
def myClick(labels, entries, myButton):
    SAVE_PATH = entries[0].get()
    link = entries[1].get()

    for entry in entries:
        entry.pack_forget()
    for label in labels:
        label.pack_forget()
    myButton.pack_forget()

    YTdownFunc(SAVE_PATH, link)


#defining the pytube function
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

    downloadedLabel.pack()

    clearButton.pack()


def main(clearButton, downloadedLabel):
    #unpacking old items in case the user uses the clear button
    clearButton.pack_forget()
    downloadedLabel.pack_forget()
    labels = []
    entries = []


    #creating labels for initial window
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



main(clearButton, downloadedLabel)