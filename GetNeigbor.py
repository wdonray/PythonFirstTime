import os
import random
import sys

class Node(object):
	''' A Node '''
	def __init__(self, value, id):
		self.__id = id
		self.__value = value
	def print_info(self):
		print "Value: ", self.value, "ID: ", self.id

class Graph(object):
	''' A Graph '''
	def __init__(self, nodes):
		self.__nodes = nodes

	def get_node(self, id):
		''' Get a node by an ID '''
		if self.nodes[id] in self.nodes:
			node = self.__nodes[id]
		return node

def CreateNode():
	''' Creates a Node that has a ID with it '''
	nodes = []
	for i in range(0, 25):
		node = Node(i*i , i)
		nodes.append(node)
	graph = Graph(nodes)
	gotnode = graph.get_node(10)
	gotnode.print_info()

CreateNode()
raw_input()
