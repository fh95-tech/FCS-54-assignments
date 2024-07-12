#ex 1.1
def checkPalindrome(text) :
  stack=[]
  reversedText=''
  
  for char in text:
    stack.append(char)
  print(stack)
  
  
  for i in range(len(stack)):
    reversedText+=stack.pop()
    
  print('original text: ',text)
  print('reversed text: ',reversedText)
  
  if text == reversedText:
    print('the text is a palindrome')
  else:
    print('the text is not a palindrome')
  
text='ldsjfvh'
checkPalindrome(text)
print()
text2='neveroddoreven'
checkPalindrome(text2)

#ex 1.2

#ex 2
def decodeMessage(message):
  stack=[]
  decodedMessage=''
  
  for char in message:
    if char != '*':
      stack.append(char)
    elif char == '*':
      decodedMessage+=stack.pop()

  for i in range(len(stack)):
    decodedMessage+=stack.pop()
  print(decodedMessage)

secretMessage='SIVLE ****** DAED TNSI ***'
decodeMessage(secretMessage)


#ex3

class Node:

  def __init__(self, info, next):
    self.info = info
    self.next = next


class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0  #how many nodes are in my LL

  def addToHead(self, info):  #O(1)
    n = Node(info, None)
    if self.size == 0:  # LL is empty, I have no nodes inside
      self.head = n
      self.tail = n
      self.size = 1
    else:
      n.next = self.head
      self.head = n
      self.size += 1

  def addToTail(self, info):  #O(1)
    if self.size == 0:
      self.addToHead(info)
    else:
      n = Node(info, None)
      self.tail.next = n
      self.tail = n
      self.size += 1


  def deleteHead(self):  # O(1)
    if self.size == 0:  # empty
      return None
    elif self.size == 1:
      val = self.head.info
      self.head = None
      self.tail = None
      self.size = 0
      return val
    else:
      val = self.head.info
      self.head = self.head.next
      self.size -= 1
      return val


  def printLL(self):  #O(n), where n is the number of nodes in the list
    i = self.head
    while i != None:
      print(i.info, "->", end="")
      i = i.next
    print()


  def deleteTail(self): #O(n), where n is the length of my LL
    if self.size<=1:
      return self.deleteHead()
    else:
      val=self.tail.info
      #loop to find the element before the last
      i=self.head
      while i.next.next!=None: #I did not reach the node before the last
        i=i.next
      #update the tail and its next
      self.tail=i
      self.tail.next=None
      self.size-=1
      return val
      
  def deleteAtLocation(self, position):

    n = self.head

    for i in range(position - 1):
        n = n.next
        if n is None:
            break

    next = n.next.next

    n.next = None
    n.next = next
    

ll=LinkedList()

ll.addToHead(2)
ll.addToTail(4)
ll.addToHead(1)
ll.addToTail(5)


ll.printLL()

ll.deleteAtLocation(2)

ll.printLL()
  
    



