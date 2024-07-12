#1
def createUser(userData):
  userDict = {}

  for user in userData:
      userInfo = {}
      for i in range(0, len(user), 2):
          key = user[i]
          value = user[i + 1]
          userInfo[key] = value

      firstName = userInfo.get("First Name")

      if firstName in userDict:
          if userDict[firstName] != userInfo:
              userDict[firstName].update(userInfo)
      else:
          userDict[firstName] = userInfo

  return userDict

userData = [
  ["First Name", "Bob", "Last Name", "Alice", "Job Title", "Instructor", "Company", "SE Factory"],
  ["First Name", "Anis", "Last Name", "Ismail", "Job Title", "Instructor", "Company", "SE Factory"],
  ["First Name", "Bob", "Last Name", "Alice", "Job Title", "Instructor", "Company", "SE Factory"],
  ["First Name", "Manuella", "Last Name", "Germanos", "Job Title", "Instructor", "Company", "SE Factory"]
]


result = createUser(userData)
print(result)


#2 INSERTION SORT 

def insertionSort(list1): #O(n^2), where n is the length of the list
  for border in range(1,len(list1)): #O(n)
    print(list1)
    current=border # the first element of my unsorted list
    while current>0 and list1[current].lower() < list1[current-1].lower(): #O(n)
      # 1, 5, 6,10 , 2
      list1[current],list1[current-1] =list1[current-1],list1[current] # swap
      current-=1
      # current=current-1

  print(list1)

insertionSort(['Zebra','apple','BeAr'])

#MERGE SORT

def mergeSort(list1,start,end):
  #base case
  if start == end: # the length of the list is 1, the list is sorted
    return
  mid = (start+end)//2

  # 54 10 23  31 45 56
  #divide
  mergeSort(list1,start,mid)
  mergeSort(list1,mid+1,end)
  # conquer
  merge(list1,start,end)
  print(list1,start,end)

def merge(list1,start,end):
  mid = (start+end)//2
  #fist list is from start to mid
  #second list is from mid+1 till the end

  # 10 12
  # 5 26
  # the indices that keep track of which elements I copied so far
  ind1=start
  ind2=mid+1

  copy_list=[] # I add the elements here
  # I compare the elements of both sublists
  while ind1<=mid and ind2<=end:
    if list1[ind1].lower()<list1[ind2].lower():
      copy_list.append(list1[ind1])
      ind1+=1
    else:
      copy_list.append(list1[ind2])
      ind2+=1
  # I copy the remaning elements of the first sublist
  while ind1<=mid:
    copy_list.append(list1[ind1])
    ind1+=1
  # I copy the elements of the second sublist that are left
  while ind2<=end:
    copy_list.append(list1[ind2])
    ind2+=1

  list1[start:end+1]=copy_list

list1=['Zebra','apple','BeAr']
mergeSort(list1,0,len(list1)-1)



#3
def findIndices(list, target):
  resultIndices = []
  for i in range(len(list)):
      if target in list[i]:
          resultIndices.append(i)
  return resultIndices
  
list = [(1, 1), (1, 10), (2, 1), (3, 0), (3, 1)]
target = 3
result = findIndices(list, target)
print(result)