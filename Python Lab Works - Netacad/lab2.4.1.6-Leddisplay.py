lst = [['###','  #','###','###','# #','###','###','###','###','###'],
       ['# #','  #','  #','  #','# #','#  ','#  ','  #','# #','# #'],
       ['# #','  #','###','###','###','###','###','  #','###','###'],
       ['# #','  #','#  ','  #','  #','  #','# #','  #','# #','  #'],
       ['###','  #','###','###','  #','###','###','  #','###','###']]
       
x = input("Enter a number: ")
#Registers keys entered
usrint = []
while x.isdigit() == False:
    print("Only whole numbers are accepted.")
    x = input("Please enter a number: ")

if x.isdigit() == True:
    for digit in x:
        y = int(digit)
        usrint.append(y)

newlst = []
for row in lst:
    newrow = []
    for i in usrint:
        newrow.append(row[i])
    newlst.append(newrow)

for row in newlst:
    x = ' '.join(row)
    print(x)