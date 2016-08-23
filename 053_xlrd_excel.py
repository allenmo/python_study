'''
--------------------------------
This code need module: xlrd, try: 
pip install xlrd
pip install xlutils
to get these modules before run.
--------------------------------
'''
print __doc__

import xlrd

data = xlrd.open_workbook('OT_Apply(2016-08-23).xls')
sheet_names = data.sheet_names()
print "sheet names", sheet_names

table = data.sheet_by_index(0)
nrows = table.nrows
print "rows numbers: ", nrows
ncols = table.ncols
print "cols numbers: ", ncols

print "The value of the 2nd row: ", table.row_values(1)
print "The value of the 2nd col: ", table.col_values(1)

print "The value of the 1st row of the 1st col: ", table.cell_value(0, 0)
print "The value of the 2nd row of the 1st col: ", table.cell_value(1, 0)
