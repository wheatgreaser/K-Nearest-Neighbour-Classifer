import math

#these are the datapoints, modify them to suit your needs
list = [
  [0, 0, 'A'], 
  [1, 1, 'A'], 
  [1, 2, 'A'],
  [0, 4, 'A'], 
  [-1, -3, 'B'],
  [-1, 3, 'B'],
  [-4, 2, 'B']
] 

distanceList = []
ogList = []

#this is the datapoint to be classified
n = [-1, -3]

for i in range(len(list)):
  d = math.sqrt((math.pow(n[0] - list[i][0], 2) + math.pow(n[1] - list[i][1], 2)))
  distanceList.append(d)
  ogList.append(d)

print(distanceList)

print("Nearest Neighbour Classifier:")
minDis = min(distanceList)
index = distanceList.index(minDis)
print(f"data point belongs to {list[index][2]}")


print("K-Nearest Neighbour Classification")

print("Enter K")
k= int(input())
minList =[]
for i in range(k):
  minList.append(min(distanceList))
  distanceList.remove(min(
   distanceList))
  

print(minList)
c = 0
for i in range(len(minList)):
   index = ogList.index(minList[i])
   if list[index][2]=="A":
  
    c=c+1

if(c > k/2):
  print("data point belongs to A")
else:
  print("data point belongs to B")
 
   


 

