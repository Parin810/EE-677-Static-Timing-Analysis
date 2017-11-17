from collections import defaultdict
global path_no 

class Graph:
	def __init__(self,nodes):
		self.V= nodes
		self.graph = defaultdict(list) 
	def addEdge(self,u,v):
		self.graph[u].append(v)
	def printAllPathsUtil(self, u, d, visited, path):		
		visited[u]= True
		path.append(u)
		path_no =1
		if u ==d:                     
			print "Path No =",path_no+1, path
			lenghtA=len(path)
			array=path
			
			#print lenghtA, u,d,visited
		else:
			for i in self.graph[u]:                               
				if visited[i]==False:
					self.printAllPathsUtil(i, d, visited, path)		
		path.pop()
		visited[u]= False
	#	print "Hi"
	def AllPaths(self,src, dest):		
		visited =[False]*(self.V)		
		path = []
		arr=self.printAllPathsUtil(src, dest,visited, path)		

##########################################################
		
nodes=[0,1,2,3,4,5,6,7,8,9]
Vertices=[(0, 1),(0, 4),(1, 2),(1, 9),(2, 3),(3, 7),(4, 5),(5, 6),(6, 0),(7, 8),(7, 6),(7, 9),(8, 9),(9, 4)]
g = Graph(len(nodes))
Verts=len(Vertices)
src = 2

dest = 4
print Vertices
print "Total Vertes are = ",Verts
for i in range (0,Verts):
      #  print(E[i][0]),(E[i][1])
        g.addEdge(Vertices[i][0],Vertices[i][1])

print ("All possible path from %d to %d :" %(src, dest))
g.AllPaths(src, dest)

