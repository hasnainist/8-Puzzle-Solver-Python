import queue
import time

inputArray=[1,2,0,3,4,5,6,7,8]
goal=[0,1,2,3,4,5,6,7,8]


def printArr(arr):
    print("")
    print('{} {} {}'.format(arr[0],arr[1],arr[2]))
    print('{} {} {}'.format(arr[3],arr[4],arr[5]))
    print('{} {} {}'.format(arr[6],arr[7],arr[8]))
    print("")


#printArr(goal)

def up(index):
    return index-3

def down(index):
    return index+3

def left(index):
    return index-1

def right(index):
  if index not in (2,5,8):
    return index+1
  else:
    return 10

def swap(index1,index2,arr):
    arr2=arr[:]
    if index2<=8 and index2>=0:
        temp=arr2[index1]
        arr2[index1]=arr2[index2]
        arr2[index2]=temp
    return arr2

def dfs(inputArray):
    visited=[]
    STACK=[]
    STACK.append((inputArray,0))
    node=0

   
    while len(STACK) !=0:
        toExplore,depth=STACK.pop()
        printArr(toExplore)
        node+=1

        if toExplore==goal:
            return node,depth
            
        
       
        if toExplore not in visited:

            
            visited.append(toExplore)
            index=toExplore.index(0)
            l=swap(index,left(index),toExplore)
            r=swap(index,right(index),toExplore)
            u=swap(index,up(index),toExplore)
            d=swap(index,down(index),toExplore)

                
            if u not in visited:
                STACK.append((u,depth+1))
                
            if d not in visited:
                STACK.append((d,depth+1))
            
            if l not in visited:
                STACK.append((l,depth+1))
            
            if r not in visited:
                STACK.append((r,depth+1))
    
        else:
            pass
    
    #print("Nodes visited : "+str(node))
    return node
    
        
def bfs(inputArray):
      
        count=0
        visited=[]
        QUEUE=queue.Queue()
        visited.append(inputArray)
        QUEUE.put((inputArray,0))
        while QUEUE.empty()==False:
            toExplore,depth=QUEUE.get()
            count+=1
            printArr(toExplore)
            if toExplore==goal:
                return count,depth
            index=toExplore.index(0)
         

            l=swap(index,left(index),toExplore)
            r=swap(index,right(index),toExplore)
            u=swap(index,up(index),toExplore)
            d=swap(index,down(index),toExplore)
          

            if l not in visited:
            
                visited.append(l)
                QUEUE.put((l,depth+1))

            if r not in visited:
            
                visited.append(r)
                QUEUE.put((r,depth+1))
            
            if u not in visited:
            
                visited.append(u)
                QUEUE.put((u,depth+1))

            if d not in visited:

                visited.append(d)
                QUEUE.put((d,depth+1))

        #print("Nodes visited : "+str(count)
        return count,depth

def ids(inputArray,maxDepth):
    
    

    for i in range(1,maxDepth):

        visited=[]
        STACK=[]
        depth=0
        STACK.append((inputArray,depth))
        node=0
    
        while len(STACK) !=0:
            toExplore,current_depth = STACK.pop()
            node+=1
            printArr(toExplore)
        
            if toExplore==goal:
                return node,current_depth
                

            if toExplore not in visited and current_depth<=i:
                
                visited.append((toExplore,current_depth))
                index=toExplore.index(0)
                l=swap(index,left(index),toExplore)
                r=swap(index,right(index),toExplore)
                u=swap(index,up(index),toExplore)
                d=swap(index,down(index),toExplore)

                if u not in visited:
                    STACK.append((u,current_depth+1))
                    
                if d not in visited:
                    STACK.append((d,current_depth+1))

                if l not in visited:
                    STACK.append((l,current_depth+1))

                if r not in visited:
                    STACK.append((r,current_depth+1))
    
    return node
                
        
    


print("")
print("BFS Algorithm") 
start=time.time()
nodes,path=bfs(inputArray)
curr=time.time()

print("Time Taken: "+str(curr-start)+" secs.")
print("Nodes visited : "+str(nodes))
print("Path Cost : "+str(path))
print("-----------------------------------------")




# print("")
# print("DFS Algorithm")
# start=time.time()
# node,path=dfs(inputArray)
# curr=time.time()

# print("Time Taken: "+str(curr-start)+" secs.")
# print("Nodes visited : "+str(node))
# print("Path Cost : "+str(path))
# print("-----------------------------------------")


# print("")
# print("IDS Algorithm")
# start=time.time()
# nodes,path=ids(inputArray,10)
# curr=time.time()
# print("Time Taken: "+str(curr-start)+" secs.")
# print("Nodes visited : "+str(nodes))
# print("Path Cost : "+str(path))
# print("")
