class Graph:
    def _init_(self):
        self.adj_list={} 

    def add_edge(self,u,v):
        if u not in self.adj_list:
            self.adj_list[u]=[]
        if v not in self.adj_list:
            self.adj_list[v]=[]
        self.adj_list[u].append(v)
        self.adj_list[v].append(u) 
    
g=Graph()
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.add_edge(4,5)