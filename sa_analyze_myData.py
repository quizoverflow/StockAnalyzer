from tkinter import *
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import FinanceDataReader as fdr
from tkinter.messagebox import *

global data_for_analyze
data_for_analyze = [0,0,0]
def getCode(entry_code):
    global data_for_analyze
    data_for_analyze[0]=entry_code.get()
    if len(str(data_for_analyze[0])) != 6 :
        showwarning("알맞은 종목코드 형식을 입력하세요\n ex) 005930")

def get_whatTime(entry_time):
    global data_for_analyze
    data_for_analyze[1]=entry_time.get()
    if len(data_for_analyze[1]) != 8 :
        showwarning("알맞은 날짜 형식을 입력하세요\n ex) 20220101")    

def radio_click(interval):
    global data_for_analyze
    data_for_analyze[2] = interval

def drawGraph(p_win,data,size,code):
    graphWin = Toplevel(p_win)
    graphWin.geometry("800x700+100+50")
    graphWin.title("graph")
    graph_frame = Frame(graphWin)
    graph_frame.pack(side="top")
    graphdata = {
    "time": [i for i in range(1,size+1)],
    "price" : data
    }
    data_f = DataFrame(graphdata,columns = ["time",'price'])
    data_figure = plt.Figure(figsize = (8,7),dpi=80)
    axis = data_figure.add_subplot(111)
    data_line = FigureCanvasTkAgg(data_figure,graph_frame)
    data_line.get_tk_widget().pack(side = 'top',fill = 'both',padx = 2, pady = 2)
    data_f = data_f[['time','price']].groupby('time').sum()
    data_f.plot(kind='line', legend=True, ax=axis, color='r', fontsize=8)
    axis.set_title(f'graph for {code}')

    des_btn = Button(graphWin,text="닫기",width=10,height=1,command=graphWin.destroy)
    des_btn.pack(side="top",pady=10)

def getData(preWin,entry_code,entry_time):
    global data_for_analyze
    data_for_analyze[0]=entry_code.get()
    data_for_analyze[1]=entry_time.get()
    data_code = data_for_analyze[0]
    start_date = data_for_analyze[1]
    interval_data = data_for_analyze[2]
    data_for_draw = []
    df = fdr.DataReader(str(data_code),start_date)
    tem_dict = df['Close'].to_dict()
    point_value_list = list(tem_dict.values())
    count = 1
    data_size = 0
    for i in point_value_list:
        if count % interval_data == 0:
            tem = int(i)
            data_for_draw.append(tem)
            data_size += 1
        count += 1
    drawGraph(preWin,data_for_draw,data_size,data_code)

def analyze_myData(win_name,org):
    newWin = Toplevel(org)
    newWin.geometry("500x400+100+50")
    newWin.title(f"{win_name}")
    
    main_frame = Frame(newWin)
    control_frame = Frame(main_frame)

    code_frame = Frame(control_frame)
    code_label = Label(control_frame,text="종목코드(ex 005930)",width = 18,height = 1)
    code_entry = Entry(code_frame)
    code_btn = Button(code_frame,text="확인",width =5, height= 1,command =lambda: getCode(code_entry) )

    moment_frame = Frame(control_frame)
    moment_label = Label(control_frame,text="매수 시점(ex 20220101)",width = 18,height = 1)
    moment_entry = Entry(moment_frame)
    moment_btn = Button(moment_frame,text="확인", width =5, height= 1,command= lambda:get_whatTime(moment_entry))

    interval_frame = Frame(control_frame)
    interval_label = Label(control_frame,text="그래프 설정",width =10,height = 1,font= (5),relief='solid')
    interval = IntVar()
    interval_radio_30 = Radiobutton(interval_frame,text = "5일", variable= interval, value = 1,command = lambda: radio_click(5))
    interval_radio_120 = Radiobutton(interval_frame,text = "10일", variable= interval, value = 2, command= lambda: radio_click(10))

    calculate_btn = Button(control_frame,text = "계산하기", width = 7, height = 1,command= lambda: getData(newWin,code_entry,moment_entry))

    titleLabel = Label(newWin, text = "내 주식 분석",width = 30, height = 2,font=(7),relief='flat')
    titleLabel.pack(side = "top", padx = 10,pady = 10)
    main_frame.pack(side = 'top',fill = 'both') 

    #originGraph(graph_frame)

    control_frame.pack(fill='both')
    interval_label.pack(side = 'top', padx = 5, pady = 5)
    code_label.pack(side ='top',padx=5, pady= 5)
    code_frame.pack(side = 'top', padx = 5, pady = 5)

    moment_label.pack(side ='top',padx=5, pady= 5) 
    moment_frame.pack(side = 'top', padx = 5, pady = 5)

    interval_frame.pack(side = 'top', padx = 5, pady = 5)
    calculate_btn.pack(side = 'top', padx = 5, pady = 5)

    code_entry.pack(side = 'left', padx = 5)
    code_btn.pack(side = 'right', padx = 5)

    moment_entry.pack(side = 'left', padx = 5)
    moment_btn.pack(side = 'right', padx = 5)

    
    interval_radio_30.pack(side = 'top', padx = 5, pady = 5)
    interval_radio_120.pack(side = 'top', padx = 5, pady = 5)

    





 