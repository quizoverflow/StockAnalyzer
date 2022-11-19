from tkinter import *
from sa_command import *
import FinanceDataReader as fdr
from datetime import datetime


def view_mystock(listbox_name):
    global stocklist
    size_of_list = listbox_name.size() - 1
    listbox_name.delete(0,size_of_list)
    finance_value_names = "종목코드    종가     시가     저가      고가"
    listbox_name.insert(0,"===== 나의 주식 리스트 =====")
    listbox_name.insert(1,finance_value_names)
    try:
        with open(f"{os.path.dirname(os.path.abspath(__file__))}\My_current_stock_list.txt",'r') as stockFile:
            while True:
                line = stockFile.readline()
                if line == "\n":
                    continue
                if not line:
                    break
                
                stocklist.append(str(line).strip())
            stocklist = list(set(stocklist))

        now = datetime.now()

        for i in stocklist:
            stock_info = fdr.DataReader(i,now.date())
            info_dict = stock_info.to_dict()
            info_list = list(info_dict.values())
            count = 0
            line_count = 2
            data_string = str(i)
            for j in info_list:
                if count == 4:
                    break
                data_value = str(format(int(str(j.values())[13:-2]),'7')) + " "
                data_string += data_value
                count += 1
            listbox_name.insert(line_count,str(data_string))
            line_count += 1
        listbox_name.insert(line_count,"===== 오늘의 KOSPI =====")
        line_count += 1
        listbox_name.insert(line_count,"     code       저가     시작가       종가       고가      종목명")
        line_count += 1
        data_size = 100
        df_krx = fdr.StockListing('KRX')
        for index , row in df_krx.head(data_size).iterrows():
            rowlist = []
            input_data = ""
            rowlist.append(str(row['Code']))
            rowlist.append(str(row['Open']))
            rowlist.append(str(row['Close']))
            rowlist.append(str(row['High']))
            rowlist.append(str(row['Low']))
            rowlist.append(str(row['Name']))
            for i in rowlist:
                input_data += "{:>9}".format(i)
            listbox_name.insert(line_count,str(input_data))
            line_count += 1

    except:
        showinfo("..0o0..","저장된 종목과 해당 가격을 불러오는데 실패하였습니다")


#mainwindow 선언
mainWindow = Tk()
mainWindow.title("Stock Analyzer for SSCC 2022")
mainWindow.geometry("700x520+100+100")

# 새 창 띄우는 클래스 인스턴스 변수 선언
nw = pop_New_Window() 
#프레임 설정
titleframe = Frame(mainWindow)
contentframe = Frame(mainWindow)
listframe = Frame(contentframe)
btn_frame = Frame(contentframe)
main_view_mystock_listframe = Frame(contentframe)
listframe = Frame(main_view_mystock_listframe)
sbar_verti = Scrollbar(listframe)
listbtn_frame = Frame(main_view_mystock_listframe)
#위젯 설정
main_title = Label(titleframe, width = 30, height = 2, text = "주식 분석기 by cjw",font=(10))
main_btn_setMyStockData = Button(btn_frame, width = 15, height = 1, text = "내 주식 설정",command = lambda: nw.newWindow("내 주식 설정",mainWindow))
main_btn_analyzeMyData = Button(btn_frame, width = 15, height = 1, text = "내 주식 분석",command = lambda: nw.newWindow("주식 분석",mainWindow))
main_btn_RecommendStock = Button(btn_frame, width = 15, height = 1, text = "주식 분석 레포트",command = lambda: nw.newWindow("주식 분석 레포트",mainWindow))
main_btn_help = Button(btn_frame, width = 15, height = 1, text = "도움말",command = lambda: nw.newWindow("도움말",mainWindow))
main_view_mystock_list = Listbox(listframe,yscrollcommand = sbar_verti.set,height = 25,width= 70)
btn_refresh = Button(listbtn_frame, width = 20, height = 1, text = "오늘의 주식 불러오기",command = lambda: view_mystock(main_view_mystock_list))

#위젯 팩
titleframe.pack(side = "top",fill = 'x')
contentframe.pack(side = "top", fill = 'x')
btn_frame.pack(side = LEFT,padx = 60,pady = 10)
main_view_mystock_listframe.pack(side = RIGHT,padx = 20,fill = 'both')
listframe.pack(side = 'top')
sbar_verti.pack(side = 'right', fill = 'both')
main_view_mystock_list.pack(side ="left",fill='both')
listbtn_frame.pack(side="top",pady=5)
btn_refresh.pack()

main_title.pack()
main_btn_setMyStockData.pack(side = "top")
main_btn_analyzeMyData.pack(side = "top", pady = 5)
main_btn_RecommendStock.pack(side = "top", pady = 5)
main_btn_help.pack(side = "top", pady = 5)


mainWindow.mainloop()