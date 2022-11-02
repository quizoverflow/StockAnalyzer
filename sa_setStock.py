from operator import indexOf
from tkinter import *
from tkinter.messagebox import *
import os


stocklist = []

def showError():
    showwarning("경고 상자","주식 종목은 여섯자리 숫자여야 합니다")

def show_stocklist_listbox(listbox_name):
    global stocklist
    size_of_list = listbox_name.size() - 1
    listbox_name.delete(0,size_of_list)
    for i in range(len(stocklist)):
        listbox_name.insert(i,stocklist[i])

def addStock(entry_name,listbox_name):
    stockCode = entry_name.get()
    if len(str(stockCode)) != 6:
        showError()
        return None
    global stocklist
    stocklist.append(stockCode)
    stocklist = list(set(stocklist))
    show_stocklist_listbox(listbox_name)

def delStock(entry_name,listbox_name):
    stockCode = entry_name.get()
    if len(stockCode) != 6:
        showError()
        return None
    global stocklist
    stocklist.remove(stockCode)
    show_stocklist_listbox(listbox_name)

def get_list(listbox_name):
    global stocklist
    try:
        stockFile = open(f"{os.path.dirname(os.path.abspath(__file__))}/My_current_stock_list.txt",'r')
        while True:
            line = stockFile.readline()
            if line == "\n":
                continue
            if not line:
                break
            stocklist.append(str(line).strip())
        stocklist = list(set(stocklist))
        show_stocklist_listbox(listbox_name)
    except:
        showinfo("..0o0..","저장된 종목 파일이 없습니다\n종목을 추가하고, 적용하기를 눌러주세요")
    
def apply_list():
    global stocklist
    fpath = os.path.dirname(os.path.abspath(__file__))
    with open(f"{fpath}/My_current_stock_list.txt","w",encoding="UTF-8") as stockFile:
        for i in stocklist:
            if i != None:
                stockFile.write(str(i)+"\n")
    stocklist = list(set(stocklist))

def setMystock(win_name,org):
    newWin = Toplevel(org)
    newWin.geometry("400x500+100+100")
    newWin.title(f"{win_name}")
    
    titleLabel = Label(newWin, text = "내 주식 설정",width = 30, height = 2,font=(7))
    
    contentframe = Frame(newWin)
    content_btn_frame = Frame(contentframe)
    stockframe = Frame(contentframe)
    refreshframe = Frame(newWin)

    btn_add_stock = Button(content_btn_frame,text = "추가하기",width= 15,height = 1,command= lambda: addStock(content_stock_entry,content_current_list))
    btn_del_stock = Button(content_btn_frame,text = "삭제하기",width= 15,height = 1,command = lambda: delStock(content_stock_entry,content_current_list))

    sbar_verti = Scrollbar(stockframe)
    content_main_Label = Label(contentframe, text = "종목 입력란", width = 30, height =2)
    content_stock_entry = Entry(contentframe)
    content_current_list = Listbox(stockframe, yscrollcommand=sbar_verti.set,width =35,height = 15)

    btn_get = Button(refreshframe,text = "불러오기", width = 15, height = 1,command = lambda:get_list(content_current_list))
    btn_apply = Button(refreshframe,text = "적용",width = 15, height = 1,command = apply_list)

    titleLabel.pack(side = "top", padx = 10,pady = 10)
    contentframe.pack(side = "top", padx = 10, pady = 10)
    content_main_Label.pack(side = "top",padx = 10)
    content_stock_entry.pack(side ='top',padx = 10 ,pady=5)
    content_btn_frame.pack(side = 'top')
    btn_add_stock.pack(side = 'left',pady = 2,padx  = 5)
    btn_del_stock.pack(side = 'right', pady = 2, padx = 5)

    stockframe.pack(side = 'top')
    content_current_list.pack(side = 'left')
    sbar_verti.pack(side = 'right')
    refreshframe.pack(side = "top")
    btn_get.pack(side = "left", padx = 10, pady = 5)
    btn_apply.pack(side = "right", padx = 10,pady=5)
