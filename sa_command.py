from tkinter import *
from sa_setStock import *
from sa_analyze_myData import *
from sa_analyze_research import *

class pop_New_Window():
    
    def newWindow(self,window_name,origin):
        size_small = "300x400+100+100"
        
        if window_name == "내 주식 설정":
            setMystock(window_name,origin)
        elif window_name == "주식 분석":
            analyze_myData(window_name,origin)

        elif window_name == "주식 분석 레포트":
            analyze_research(window_name,origin)
        else:
            newWin = Toplevel(origin)
            newWin.title(f"{window_name}")
            newWin.geometry(size_small)
            helptext = "도움말 \n 만든이 : 최진우 \n ver 1.00"
            helplabel = Label(newWin,width=20,height=30,text = helptext)
            helplabel.pack(side = "top",padx = 5,pady = 5,fill="both")







        

