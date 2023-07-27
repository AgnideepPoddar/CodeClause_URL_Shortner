from tkinter import *
import pyshorteners

root = Tk()
root.title('CodeClause | URL Shortner')
root.geometry('500x500')
root.config(background = "#03001C")  

#Main function
def shorten():
    if shorty.get():
        shorty.delete(0, END)
    if my_entry.get():
        #Convert Url to Short
        url = pyshorteners.Shortener().tinyurl.short(my_entry.get())
        #Output to window
        shorty.insert(END, url)

my_label = Label(root, text="URL Shortner",bg="#03001C",fg="#F9D949", font=("Helvetica",34))
my_label.pack(pady=30)

my_entry = Entry(root, font=("Helvetica",24))
my_entry.pack(pady=20)

my_btn = Button(root, command=shorten , text="Shorten Link",bg="#4bd6f2",font=("Helvetica",24))
my_btn.pack(pady=20)

short_label = Label(root, text="Shortened Link" ,fg="#fff" ,bg="#03001C", font=("Helvetica",18))
short_label.pack(pady=20)

shorty = Entry(root, font=("Helvetica",22),bg="#03001C", fg="#F9D949", justify=CENTER , width=30,bd=0)
shorty.pack(pady=30)

root.mainloop()
