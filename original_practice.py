import openpyxl
import datetime
from openpyxl.chart import BarChart, Reference,Series
book = openpyxl.Workbook()
book.save('Stock_analysis_us.xlsx')
now_date = datetime.datetime.now() #今日の日付を取得 


book=openpyxl.load_workbook('Stock_analysis_us.xlsx')
sheet=book.active
sheet['A1']='Stock Name'
sheet['A2']='Appl'
sheet['A3']='Appl'
sheet['A4']='Appl'
sheet['A5']='Appl'
sheet['A6']='CRWD'
sheet['A7']='CRWD'
sheet['A8']='CRWD'
sheet['A9']='CRWD'
sheet['A10']='ZM'
sheet['A11']='ZM'
sheet['A12']='ZM'
sheet['A13']='ZM'


sheet['B1']='Indicater' 
sheet['B2']='DPS' #
sheet['B3']='EPS'
sheet['B4']='CFPS'
sheet['B5']='SPS'
sheet['B6']='DPS'
sheet['B7']='EPS'
sheet['B8']='CFPS'
sheet['B9']='SPS'
sheet['B10']='DPS'
sheet['B11']='EPS'
sheet['B12']='CFPS'
sheet['B13']='SPS'

sheet['C1']='Y_17' 
sheet['C2']=float(0.6) #置換ってできないか
sheet['C3']=float(2.3)
sheet['C4']=float(3.06)
sheet['C5']=float(10.91)
sheet['C6']=float(0)
sheet['C7']=float(-3.38)
sheet['C8']=float(-1.4)
sheet['C9']=float(2.84)
sheet['C10']=float(0)
sheet['C11']=float(0)
sheet['C12']=float(0)


sheet['D1']='Y_18' 
sheet['D2']=float(0.68)
sheet['D3']=float(2.98)
sheet['D4']=float(3.87)
sheet['D5']=float(13.28)
sheet['D6']=float(0)
sheet['D7']=float(-3.12)
sheet['D8']=float(-0.51)
sheet['D9']=float(5.57)
sheet['D10']=float(0)
sheet['D11']=float(-0.01)
sheet['D12']=float(0.07)
sheet['D13']=float(0.56)

sheet['E1']='Y_19' 
sheet['E2']=float(0.75)
sheet['E3']=float(2.97)
sheet['E4']=float(3.73)
sheet['E5']=float(13.99)
sheet['E6']=float(0)
sheet['E7']=float(-0.96)
sheet['E8']=float(0.68)
sheet['E9']=float(3.25)
sheet['E10']=float(0)
sheet['E11']=float(0.03)#赤いシグナルは何か
sheet['E12']=float(0.19)
sheet['E13']=float(1.23)

sheet['F1']='Y_19' 
sheet['F2']=float(0.795)
sheet['F3']=float(3.28)
sheet['F4']=float(4.6)
sheet['F5']=float(15.66)
sheet['F6']=float(0)
sheet['F7']=float(-0.43)
sheet['F8']=float(1.64)
sheet['F9']=float(4.02)
sheet['F10']=float(0)
sheet['F11']=float(0.1)
sheet['F12']=float(0.6)
sheet['F13']=float(2.45)

sheet.row_dimensions[1].height = 30 #行の高さを設定 (ピクセル)
sheet.column_dimensions["A"].width = 20 #列の幅を設定 (文字数)
sheet.column_dimensions["B"].width = 20
sheet.column_dimensions["C"].width = 20
sheet.column_dimensions["D"].width = 20
sheet.column_dimensions["E"].width = 20
sheet.column_dimensions["F"].width = 20
sheet.column_dimensions["G"].width = 20

sheet.oddHeader.center.text = "Stock analysis APPL/CRWD/ZM"
#ヘッダーの中心に表示
sheet.oddHeader.right.text = now_date.strftime('%Y/%m/%d') #ヘッダーの右側に今日の日付を表示

values = Reference(sheet, min_col=3, min_row=1,max_col=6, max_row=5)
chart = BarChart() #棒グラフを作成
#先頭行をグラフのラベルにしてデータを追加
chart.add_data(values,titles_from_data=True) 
sheet.add_chart(chart, "H1") #セルG1にグラフを描画

sheet['G1'].number_format = "yyyy/mm/dd"
sheet['G1']='2021,8,21'
book.save('Stock_analysis_us.xlsx')

