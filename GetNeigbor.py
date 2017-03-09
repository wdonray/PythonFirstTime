class Node(object):
    	''' A Node '''
	def __init__(self, value, id):
		self.__id = id
		self.__value = value
		
	def print_info(self):
    	print 'Node: ', self.__id, 'Value: ', self.__value

class Graph(object):
	''' A Graph '''
	def __init__(self, pos):
		self.__pos = pos
		self.do_work()
		self.nodes = {}

	def do_work(self):				
		nodes = []
		for i in range(0, 3):
			for j in range(0, 3):
				node = Node([i,j], len(nodes))
				nodes.append(node)
		return nodes

def get_neighbors(N, G):
	node = G.get_node(N)
	if node is not None:
		front = G.get_node(N + 1)
		behind = G.get_node(N - 1)
	return [front.print_info(), behind.print_info()]

def get_node(index, g):
		if g.nodes.has_key(index):
			return g.nodes[index]


def test_nodes():
	graph = Graph([3, 3])
	node = get_node(2, graph)
	node.print_info()
	neighbors = get_neighbors(node, graph)
	for nod in neighbors:
		nod.print_info()

if __name__ == '__main__':
	test_nodes()