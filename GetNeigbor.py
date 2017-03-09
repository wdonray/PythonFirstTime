'''Get Neighbor Module'''
import pygame


class Node(object):
    ''' A Node '''

    def __init__(self, value, identification):
        '''init'''
        self.id_ = identification
        self.value_ = value

    def print_info(self):
        ''' Prints Info '''
        print 'Node: ', self.id_, 'Value: ', self.value_


class Graph(object):
    ''' A Graph '''

    def __init__(self, dims):
        self.rows_ = dims[0]
        self.cols_ = dims[1]
        self.nodes_ = {}
        count = 0
        for i in range(0, self.rows_):
            for j in range(0, self.cols_):
                self.nodes_[count] = Node([i, j], len(self.nodes_))
                count += 1


def get_node(index, graph):
    '''Returns the node'''
    if index in graph.nodes_:
        return graph.nodes_[index]
    else:
        return None


def get_neighbors(node, graph):
    '''Gets the adjacent nodes'''
    neighbors = []
    right = get_node(node.id_ + graph.cols_, graph)
    top = get_node(node.id_ + 1, graph)
    left = get_node(node.id_ - graph.cols_, graph)
    down = get_node(node.id_ - 1, graph)
    if right is not None:
        neighbors.append(right)
    if top is not None and node.id_ % graph.cols_ != graph.cols_ - 1:
        neighbors.append(top)
    if left is not None:
        neighbors.append(left)
    if down is not None and node.id_ % graph.cols_ != graph.cols_ - 0:
        neighbors.append(down)
    return neighbors


def test_nodes():
    '''test the nodes'''
    graph = Graph([3, 3])
    node = get_node(4, graph)
    node.print_info()
    neighbors = get_neighbors(node, graph)
    for nod in neighbors:
        nod.print_info()


if __name__ == '__main__':
    test_nodes()
    pygame.init()
    screen = pygame.display.set_mode((900, 900))
    running = True
    while running:
        pygame.draw.circle(screen, (255, 255, 255), (450, 450), 100, 0)
        pygame.display.flip()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
    pygame.quit()
    raw_input()
