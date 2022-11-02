from tkinter import *

def analyze_myData(win_name,org):
    newWin = Toplevel(org)
    newWin.geometry("800x500+100+100")
    newWin.title(f"{win_name}")
    
    titleLabel = Label(newWin, text = "내 주식 분석",width = 30, height = 2,font=(7))





    titleLabel.pack(side = "top", padx = 10,pady = 10)