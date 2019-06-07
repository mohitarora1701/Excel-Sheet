import xlwt
wb=xlwt.Workbook()
ws=wb.add_sheet("Sheets")
row=int(input("Enter the number of rows= "))
col=int(input("Enter the number of columns= "))
for i in range(row):
      for j in range(col):
          print("Row {} data".format(i))
          print("Column {} data".format(j))
          a=input("Enter your data= ")
          ws.write(i,j,a)
b=input("Enter your filename= ")
c=input("Enter your format= ")
e=(b+"."+c)
print(e)
wb.save(e)
