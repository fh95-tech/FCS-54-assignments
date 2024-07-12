
#ex1
def recursiveBinarySearch(list,item):
  def findPosition(start,end):
    if item>list[end] or item<list[start]:
      return False

    mid=(start+end)//2

    if list[mid]==item:
      return True
    elif list[mid]>item:
      return findPosition(start,mid-1)
    else:
      return findPosition(mid+1,end)


  return findPosition(0,len(list)-1)

list1=[-5,1,2,3,5,7,8,9,10]
print(recursiveBinarySearch(list1,5))


#ex2
def generateCombinations(list,n):
    def combinator(comb,n):

        if len(comb) == n:
            print(comb)
            return
        for i in list:
            combinator(comb+i,n)

    combinator("",n)

list1=["a","b","c"]
n=3
generateCombinations(list1,n)

#ex3

items={
  1:{"name":"labne","price":5000},
  2:{"name":"bread","price":1500},
  3:{"name":"chocolate","price":1000},
  4:{"name":"eggs","price":8000}
}


def execution():
  sysStart=input("Would you like to start a new receipt? ").lower()
  print()
  if sysStart!="yes" and sysStart!="no":
    print("please enter a valid answer !")
    print()
    execution()

  elif sysStart=="no":
    print("shutting down")

  elif sysStart=="yes":
    def takeOrder():

      receipt=[]
      totAmount=0

      while True:
        barcode=int(input("please scan the barcode: "))
        if barcode in items:
          quantity = int(input("Enter quantity: "))
          print()
          item = items[barcode]
          cost = item["price"] * quantity
          totAmount += cost
          receipt.append((item["name"], quantity, cost))
        else:
          print("Item not found.")
        newItem = input("Would you like to add another item? ").lower()
        print()
        if newItem!="yes":
            break

      def processOrder():
        for item in receipt:
          print(item)
        print("total amount= " + str(totAmount))
        print()
        execution()

      processOrder()

    takeOrder()      

execution()










