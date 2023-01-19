import Core
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
import  matplotlib.pyplot as plt

class Visualaser: # Very good code
    def __init__(self, throne: Core.Throne, male_colour='red', female_colour='blue'):
        self.__male_colour = male_colour
        self.__female_colour = female_colour
        self.throne = throne
        self.graph = nx.Graph()
        self.graph.add_node(throne.kings[0].name)
        self.__construct_graph(0)
    
    def __construct_graph(self, king_ptr: int):
        if self.throne.kings[king_ptr].wife != None:
            self.graph.add_node(self.throne.kings[king_ptr].wife.name)
            self.graph.add_edge(self.throne.kings[king_ptr].name, self.throne.kings[king_ptr].wife.name)
        for i, king in enumerate(self.throne.kings):
            if king.father == self.throne.kings[king_ptr]:
                self.graph.add_node(king.name)
                self.graph.add_edge(self.throne.kings[king_ptr].name, king.name)
                self.__construct_graph(i)

    def draw(self, display=True):
        pos = graphviz_layout(self.graph, prog="dot")
        nx.draw(self.graph, pos, with_labels=True)
        plt.show()
