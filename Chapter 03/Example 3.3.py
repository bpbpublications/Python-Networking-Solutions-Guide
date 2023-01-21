from openpyxl import load_workbook

filename="test.xlsx"
wb=load_workbook ( filename )

sheet=wb.active

b1=sheet['A1']
b2=sheet.cell ( row=1, column=1 )

print( b1.value )
print( b2.value )
print( b2 )