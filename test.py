from tkinter import *
import tkinter
import os
from PIL import Image, ImageTk

window = tkinter.Tk()
window.title('視窗')  # 窗口标题
windowWidth = 1600  # 視窗寬
windowHeight = 900  # 視窗高
screenWidth, screenHeight = window.maxsize()  # 獲得螢幕寬和高
window.geometry("1600x900")
window.wm_attributes('-topmost', 1)  # 視窗置頂


preview = ImageTk.PhotoImage(file="noimagefile.jpg")
preview_canvas = tkinter.Canvas(window, width=preview.width(), height=preview.height())
# canvas = tkinter.Canvas(window, width=preview.width(), height=preview.height())
preview_canvas.create_image(0, 0, image=preview, anchor=tkinter.NW)
preview_canvas.delete("all") #清空畫布
preview_canvas.create_image(0, 0, image=preview2, anchor=tkinter.NW)
preview_canvas.grid(column=1, row=0)
# lb = tkinter.Label(window, text="Result",  font=("arial", 15))
# btn_snapshot = tkinter.Button(window, width=10, height=1, text="Snapshot",
#                                            font=("arial", 15), bg='green', fg='white')
# btn_send = tkinter.Button(window, width=10, height=1, text="Recognize",
#                                        font=("arial", 15), bg='blue', fg='white')
# btn_quit = tkinter.Button(window, width=10, height=1, text="QUIT", command=window.quit,
#                                        font=("arial", 15), bg='red', fg='white')
# btn_delete = tkinter.Button(window, width=10, height=1, text="DELETE",
#                                          font=("arial", 15), bg='red', fg='green')
# listb = tkinter.Listbox(window, height=20, width=65, font=("arial", 15))


# listb.selection_handle(command=selection_event())

# canvas.grid(column=0, row=0)

# listb.grid(column=1, row=0)
# lb.grid(column=1, row=1)
# btn_snapshot.grid(column=1, row=2)
# btn_send.grid(column=1, row=3)
# btn_delete.grid(column=1, row=4)
# btn_quit.grid(column=1, row=5)

window.mainloop()


"""
from tkinter import *
import tkinter
import os
from PIL import Image, ImageTk
from tkinter import messagebox



class imageMangement:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title('視窗')  # 窗口标题
        # window.resizable(False, False)  # 固定視窗大小
        self.windowWidth = 1600  # 視窗寬
        self.windowHeight = 900  # 視窗高
        self.screenWidth, screenHeight = self.window.maxsize()  # 獲得螢幕寬和高
        self.window.geometry("1600x900")
        self.window.wm_attributes('-topmost', 1)  # 視窗置頂

        listb = tkinter.Listbox(self.window, height=20, width=65, font=("arial", 15))
        # listb.selection_handle(command=selection_event())
        #listb.grid(column=4, row=0)
        # listb.delete(2, last=listb.size() - 1)

        self.show_canvas()

        imlist = os.listdir('./images')
        for x in imlist:
            #self.show_Thumbnail(str(x))
            print(imlist.index(x),str(x))
            listb.insert(imlist.index(x), str(x))
        self.x_place=0
        self.y_place=0
        self.show_Thumbnail("a.jpg")
        self.show_Thumbnail("b.jpg")
        #self.show_Thumbnail()

        self.window.mainloop()
    # 空畫布
    def show_canvas(self):
        self.preview = ImageTk.PhotoImage(file="images/noimagefile.jpg")
        self.preview_canvas = tkinter.Canvas(self.window, width=self.preview.width(), height=self.preview.height())
        self.preview_canvas.create_image(0, 0, image=self.preview, anchor=tkinter.NW)
        #self.preview_canvas.delete("all")  # 清空畫布
        self.preview_canvas.grid(column=1, row=0)
        #self.preview_canvas.pack(side=LEFT, padx=5, pady=5)

    # 點擊縮圖顯示圖片事件
    def show_Image(self,event):
        label1 = tkinter.Label(self.window, text="嗨")
        label1.grid(column=3, row=0)
        #label1.pack(side=LEFT,padx=5, pady=5)

    #顯示縮圖
    def show_Thumbnail(self,imgName):
        self.w_box = 80
        self.h_box = 50
        self.x_place = self.x_place+100
        self.y_place = self.y_place+100
        self.pil_image = Image.open("images/"+imgName)
        self.pil_image2 = Image.open("images/bd.jpeg")  ###########
        self.w, self.h = self.pil_image.size   #獲取圖片的原始大小
        self.pil_image_resized = self.resize(self.w, self.h, self.w_box, self.h_box, self.pil_image.size)#縮放圖片让它保持比例，同時限制在一個矩形框範圍內
        self.tk_image = ImageTk.PhotoImage(self.pil_image_resized)
        self.tk_image2 = ImageTk.PhotoImage(self.pil_image2)############
        self.img = tkinter.Label(self.window, image = self.tk_image,width=self.w_box, height=self.h_box)
        self.img2 = tkinter.Label(self.window, image=self.tk_image2, width=self.w_box, height=self.h_box) #######ew###

        self.img.bind("<Button-1>",self.show_Image) #點擊左鍵，顯示圖片

        self.img.grid(column=2, row=0)
        #self.img.pack(side=LEFT,padx=5, pady=5)
        self.img.place(x=self.x_place,y=self.y_place)
        self.img2.place(x=self.x_place+500, y=self.y_place)   ################################
        self.img = tkinter.Label(self.window, image=self.tk_image2, width=self.w_box, height=self.h_box)  #######ew###
        self.img.place(x=self.x_place+800, y=self.y_place)

    def ImagePlacePlus(self,x,y):
        pass


    def resize(self,w, h, w_box, h_box, pil_image):
        self.f1 = 1.0 * w_box / w
        self.f2 = 1.0 * h_box / h
        self.factor = min([self.f1, self.f2])
        self.width = int(w * self.factor)
        self.height = int(h * self.factor)
        return self.pil_image.resize((self.width, self.height), Image.ANTIALIAS)











# 要檢查的檔案路徑
filepath = "./images"

# 檢查檔案是否存在
if os.path.isfile(filepath):
  print("檔案存在。")
else:
  print("檔案不存在。")

# label图片
# img_gif = tkinter.PhotoImage(file='img_gif.gif')
# label_img = tkinter.Label(root, image=img_gif)
# label_img.pack()

#PIL套件裡的
# img_open = Image.open('img_gif.jpg')
# img_png = ImageTk.PhotoImage(img_open)
# label_img = tkinter.Label(root, image = img_png)
# label_img.pack()

# 带图button，image
# button_img_gif = tkinter.PhotoImage(file='button_gif.gif')
# button_img = tkinter.Button(root, image=button_img_gif, text='带图按钮')
# button_img.pack()

# 带图button，bitmap
# button_bitmap = tkinter.Button(root, bitmap='error', text='带图按钮')
# button_bitmap.pack()

"""