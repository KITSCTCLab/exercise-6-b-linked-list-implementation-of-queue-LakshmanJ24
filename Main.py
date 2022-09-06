class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Queue:
  def __init__(self):
    self.head = None
    self.last = None

  def enqueue(self, data) -> None:
    # Write your code here
    new_node = Node(data)
    if(self.last!=None):
      self.last.next = new_node
      self.last = new_node
    else
      self.head = new_node
      self.last = new_node

  def dequeue(self) -> None:
    # Write your code here
    if(self.head!=None):
      temp = self.head
      self.head = temp.next

  def status(self) -> None:
    # Write your code here
    if(self.head!=None):
      temp = self.head
      while temp.next!=None:
        print(temp.data,end="")
        print("=>",end="")
        temp=temp.next
      print(temp.data,end="=>")
    print("None") 


# Do not change the following code
queue = Queue()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "enqueue":
    queue.enqueue(int(data[i]))
  elif operations[i] == "dequeue":
    queue.dequeue()
queue.status()
