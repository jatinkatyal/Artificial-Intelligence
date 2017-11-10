''' Class for defining node '''
class Node:
    def __init__(self,l,c):
        self.label = l
        self.cost = c
        self.child = []
        addchild = True
        while addchild:
            c = input(" Add child to "+l+"?: ")
            if c=='Y':
                self.addChild()
            else:
                addchild=False

    def addChild(self):
        l=input("Enter label: ")
        c = int(input("Enter cost: "))
        self.child.append(Node(l,c))

    def display(self):
        print(self.label,end=='')
        if self.child:
            for c in self.child:
                print("--"+str(c.cost)+"-->",end='')
                c.display()
        else:
            print()

'''Sort priorityQueue accoding to cost of reaching nodes'''
def sortPriorityQueue(pq):
    for node in pq:
        if pq.index(node)<len(pq):
            for tempNode in pq[pq.index(node)+1:]:
                if tempNode.cost < node.cost :
                    node, tempNode = tempNode,node

''' Driver code'''
            
''' Create tree '''        
root = Node('S',0)
queue = [root]
visited = []
flag = True
goal = input("Goal node: ")
while flag and queue:
    print(queue)
    sortPriorityQueue(queue)
    print(queue)
    currentNode = queue.pop()
    print(type(currentNode))
    visited.append(currentNode.label)
    if currentNode.label == goal:
        flag=False
        break
    if currentNode.child:
        for child in currentNode.child:
            print(child.label)
            queue.append(child)
if flag:
    print("Node not found")
else:
    for n in visited:
        print(n+"-->",end='')
