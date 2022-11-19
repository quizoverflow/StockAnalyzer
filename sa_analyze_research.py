from tkinter import *
from tkinter.messagebox import *
import os
from research_make_report import *
import tkinter.ttk as ttk
from multiprocessing import Pool
import multiprocessing



def insertList(listbox):
    try:
        listbox.insert(0,"   === 분석 대상 종목 코드 ===  ")
        with open(f"{os.path.dirname(os.path.abspath(__file__))}\My_current_stock_list.txt",'r') as stockFile:
            stocklist = []
            while True:
                line = stockFile.readline()
                if line == "\n":
                    continue
                if not line:
                    break
                stocklist.append(str(line).strip())
            stocklist = list(set(stocklist))
            linecount = 1
            for i in stocklist:
                listbox.insert(linecount,f"{linecount} : {str(i)}")
                linecount += 1
            return stocklist
    except:
        showinfo("..0o0..","저장된 종목과 해당 가격을 불러오는데 실패하였습니다")


def getReport(stock_list,progress,pbar):
    global progress_count
    global total_num
    total_num = len(stock_list)
    progress_count = 0
    
    for i in range(total_num):
        makeReport(stock_list[i])
        progress.set((i+1)/total_num*100)
        pbar.update()

""" 
    stock_list_for_calculate = [[None for j in range(num_core)] for i in range(10)]
    tem0 = 0
    tem1 = num_core - 1
    tem_count = 0
    for i in stock_list_for_calculate:
        for j in stock_list[tem0:tem1]:
            i.append(j)
            tem0 = tem1 + 1
            tem1 += num_core + 1
            tem_count+=1
    print(stock_list)
    print(stock_list_for_calculate)
    for i in stpool = Pool(processes = num_core)
        pool.map(makeReport,stock_list)ock_list_for_calculate:
        pool = Pool(processes = num_core)
        pool.map(makeReport,stock_list)
        progress_count += 1
        progress.set(progress_count/tem_count*100)
        pbar.update()
        pool.close()
        pool.join()

         """

def analyze_research(win_name,org):
    global prog 
    prog = DoubleVar()
    newWin = Toplevel(org)
    newWin.geometry("300x400+100+100")
    newWin.title(f"{win_name}")
    
    titleLabel = Label(newWin, text = "레포트 만들기",width = 30, height = 2,font=(8))
    listframe = Frame(newWin)
    sbar = Scrollbar(listframe)
    stock_listbox = Listbox(listframe,yscrollcommand = sbar.set,height = 10,width= 35)
    

    slist = insertList(stock_listbox)
    analyze_progress = ttk.Progressbar(newWin,maximum= 100,length= 150,variable = prog)
    report_btn = Button(newWin,text = "레포트 만들기",width = 10, height = 1,command = lambda: getReport(slist,prog,analyze_progress))
    core_label = Label(newWin,text=f"활용 가능 코어 갯수 = {multiprocessing.cpu_count()}", width = 30, height = 2)

    titleLabel.pack(side = "top", padx = 10,pady = 10)
    listframe.pack(side = "top",pady = 5)
    stock_listbox.pack(side = "left")
    sbar.pack(side = 'right',fill='both')
    report_btn.pack(side = 'top',pady = 5)
    core_label.pack(side ="top",pady = 5)
    analyze_progress.pack(side ="top",pady = 5)
