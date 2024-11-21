from tkinter import *
import requests
from PIL import Image,ImageTk
from io import BytesIO
from tkinter import ttk


def load_image():
    try:
        response = requests.get(url)
        print(response)
    #    print(response.content)
        image_data=BytesIO(response.content)
        print(image_data)
        img=Image.open(image_data)
        img.thumbnail((500,500))#подгоняем картинку под размер
        print(img)
        img=ImageTk.PhotoImage(img)

        t=Toplevel()
        m=Label(t, width=300, height=300)
        m.pack()
        m.image = img
        m.config(image=img)
    except Exception as e:
        print(e)



url="https://cataas.com/cat"
allowed_tags=['cute','green','small','orange','sleep','computer','fat']

window=Tk()
window.geometry("500x550")

tag=ttk.Combobox(values=allowed_tags)
tag.pack()


mainmenu=Menu(window)
window.config(menu=mainmenu)

file_menu=Menu(mainmenu,tearoff=0)
mainmenu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузка изображения", command=load_image)
file_menu.add_command(label="Выход", command=window.destroy)


window.mainloop()