class Node:                                                    
    def __init__(self, data):  
        self.data = data                                       
        self.next = None
        self.prev = None
  
class DoublyLinkedList:                                         
    def __init__(self):
        self.head = None                                        
        
    def insert(self,data):                                     
        newNode = Node(data)                                   
        
        if self.head is None:                                   
            self.head = newNode
        
        elif newNode.data<self.head.data:                      
            newNode.next = self.head                          
            self.head.prev = newNode                            
            self.head = newNode                                
        
        else:                                                   
            previous = self.head                                                  
            current = self.head.next
            
            while current is not None:                         
                if current.data > newNode.data:                
                    previous.next = newNode                     
                    newNode.prev = previous
                    newNode.next = current                     
                    current.prev = newNode
                    return                                   
                    
                previous = current                           
                current = current.next
            
            previous.next = newNode                            
            newNode.prev = previous
            return 
        
    def hasAlready(self,data):                                 
        current = self.head                                     
        while current is not None:
            if data==current.data:                             
                return True
            elif current.data>data:                            
                return False                                   
            current = current.next                              
        return False
    
    def printList(self):                                        
        current = self.head                                    
        while current is not None:                         
            print(current.data,end =" ")                        
            current = current.next
            
def rem_punc(string):                                          
    punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''              
    new = ""
    for i in string:
        if i not in punc:
            new+=i
    return new
            
            

            
newList = DoublyLinkedList()                                    
with open('sampletext.txt','r') as file:                        
    for line in file:                                           
        for word in line.split():                               
            t = rem_punc(word.lower())                         
            if not newList.hasAlready(t):                       
                newList.insert(t)
        
newList.printList()                                             
