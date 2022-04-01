import numpy as np
import pandas as pd
# import pygraphviz as pgv
# from pathlib import Path

C = {'P1':'1', 'P2':'2', 'P3':'3', 'P4':'4', 'P5':'5', 'P6':'6', 'P7':'7', 'P8':'8', 'TO':' -> '}

class Game:
    def __init__(self, file):
        self.file = file 
        self.state = []
        self.time = 0
        self.node_count = 0

        # Open the data file.
        handle = pd.read_csv(file)

        
        # Create a data structure which is a little easier to use
        # when generating graphs.
        for i in range(len(handle)):
            x = {}
            for k, v in handle.iteritems():
                x[k] = v[i]

            # We don't need the time because the data structure created
            # above is keyed by time.
            del x['TIME']
            self.state.append(x)

        # Figure out how many nodes the graph will have.
        for n in self.state[0].keys():
            if "LAPTOP" in n:
                self.node_count += 1

    def edges(self, time):
        edges = []

        for k,p in time.items(): 

            # We are only concerned with edges with a probabiliy greater
            # than 0.
            if str(p) != '0':
                tokens = k.split('_')
                if "LAPTOP" in k:
                    edges.append((C[tokens[0]], C[tokens[0]], str(p)))
                    continue

                tokens = k.split('_')
                edges.append((C[tokens[0]], C[tokens[2]], str(p)))

        return edges


    def template(self, shape='circle', ext='dot'):
        template_dir = Path("templates")
        template_name = shape + str(self.node_count) + "." + ext
        return str(template_dir / template_name)


    def render(self, time, file=None, format='png', prog='neato'):
        graph = pgv.AGraph(self.template())
        edge_list = self.edges(self.state[time])

        # Add the time stamp to the image.
        graph.graph_attr['label'] = f"Timestamp: {time}"
        # Add each of the edges between nodes with edge weight.
        for item in edge_list:
            graph.add_edge(item[0], item[1], arrowsize=str(item[2]), penwidth=str(item[2]))

        return graph.draw(file, format, prog)
