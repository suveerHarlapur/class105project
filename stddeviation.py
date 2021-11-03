import csv,math

with open('data.csv',newline='') as f:
    read_data = csv.reader(f)
    list_data = list(read_data)
length_data = 0

total = 0
data = list_data[0]
mean = 0
for i in data:
    total += int(i)
    length_data+=1
print(length_data)
mean = total/length_data
print(mean)
square =[]
for x in data:
    sumof = int(x)-mean
    square.append(sumof**2)
sumofall = 0
print(square)
for each in square:
    sumofall = sumofall+each
bottom = length_data -1
result = sumofall/bottom
print('std deviation is :'+str(math.sqrt(result)))