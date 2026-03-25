class Node:
    def __init__(self,data=None):
    self.data=data
    self.next=None
class singlylinkedlist:
    def __init__(self):
    self.first=None
    def prenpend(self.data):
       newnode=None(data)
       if self.first==None:
          self.first=newnode
       else:
           newnode.self.next=self.first
           self.first=newnode

    def removefirst(self):
       if (self.first==None):
           print("list is empty")
      else:
          current=self.first
          self.first=self.first.next
          print("the delet element is :"current.data)
    def display(self):
       
        if (self.first=None):
             print("list is empty")
             return
        else:
             current=self.first
             while(current):
                  print("current.data",end=" ")
                  current=current.next
    def Search(self,item):
       if self.first==None:
           print("list is empty")
           return
       current=self.first
    found = False
    while current!=None and not found:
       if current.data=item:
           found=True
       else:
           current = current.next
    if found:
        print("item is found")
    else:
        print("item is not found")
s1=singlylinkedlist()
while(True):
    choice=int(input("\n enter your choice 1-insert 2-delete 3-search 4-display 5-exit:")
    if(choice==1):
        item=input("enter the element to insert:")
        s1.prepend(item)
        s1.display()
    elif(choice==2):
        s1.removefirst()
        s1.display()
    elif(choice==3):
        item=input("enter the element to search:")
        s1.search(item)
    elif(choice==4):
        s1.display()
    else:
        break
               
               
    
         
               
                         
  
                    

     
