from openpyxl import Workbook

workbook = Workbook ()
sheet = workbook.active

sheet [ "A1" ] = "Python"
sheet[  "B1" ] = "Scripting"
sheet[  "A2" ] = "For Network"
sheet[  "B2" ] = "Automation"

sheet.title = "Test Page"

workbook.save ( filename="test.xlsx" )