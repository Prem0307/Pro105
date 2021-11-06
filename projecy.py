import csv
import math

with open("Project.csv",newline="")as f:
    reader=csv.reader(f)
    file_data=list(reader)
data=file_data[0]
print(data)
def mean(data):
    n=len(data)
    total=0

    for x in data:
        total +=int(x)
    mean=total/n
    print(total)
    print(mean)
    return mean

sq_list=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    sq_list.append(a)

sum=0
for i in sq_list:
    sum=sum+i 
print(len(data))

result=sum/(len(data)-1)
st_dev=math.sqrt(result)
print("standard deviation is"+str(st_dev))