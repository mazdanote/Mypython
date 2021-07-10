import glob

filelist=glob.glob('/Users/takuyamatsuda/Desktop/tenki.jp')

import openpyxl

out_workbook=openpyxl.workbook()
out_sheet=out_workbook.active
out_sheet.title='世界の天気'

out_sheet['A1'].value='日付'
out_sheet['B1'].value='国名'

out_workbook.save('/Users/takuyamatsuda/Desktop/tenki.jp')