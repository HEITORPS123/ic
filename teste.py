import igraph
g = igraph.Graph.GRG(100, 0.1)
g.to_directed(mutual="True")
a = 0

for i in g.get_edgelist():
    v = g.get_eid(i[0],i[1])
    if(a % 2 == 0):
        g.delete_edges(v)
    a = a + 1

comp = g.components(mode = "WEAK")
layout = g.layout("kk")
igraph.plot(comp, layout = layout)