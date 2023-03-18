import networkx as nx
from lcapy import Circuit, Vstep, R, C
import matplotlib.pyplot as plt
import numpy as np
from image2net import toNetlist


def main():
    netlist = toNetlist()
    cir = ""
    G = nx.Graph()
    # netlist = [[1, 'R0', 4, 1], [2, 'R1', 1, 2], [3, 'R2', 2, 3]]
    # netlist = [[1, "R1", 1, 2], [2, "R2", 1, 3], [3, "R3", 3, 4], [4, "C4", 5, 4], [5, "C5", 6, 5], [6, "D6", 2, 6]]
    posi = np.zeros((len(netlist), 2))
    for i, arr in enumerate(netlist):
        G.add_node(arr[0], label=f"{arr[0]}")
        G.add_edge(arr[2], arr[3])
    labels = nx.get_node_attributes(G, "label")
    # pos=nx.get_node_attributes(graph,'pos')
    pos = nx.spring_layout(G)
    options = {'pos': pos, 'node_color': 'orange', 'node_size': 300,
        'width': 3, 'labels': labels, 'font_weight': 'bold'}
    nx.draw(G, **options)
    
    for i in range(len(netlist)):
        # print(f"{netlist[i][1]} {netlist[i][2]} {netlist[i][3]}; right")
        cir += f"{netlist[i][1]} {netlist[i][2]} {netlist[i][3]}; right\n"
    cct = Circuit(cir)
    cct.draw()
    # array = []
    # for i, j in enumerate(G.edges):
    #     for x, y in enumerate(G.nodes):
    #         if ((j[0] == netlist[x][2]) and (j[1] == netlist[x][3])) or ((j[0] == netlist[x][3]) and (j[1] == netlist[x][2])):
    #             array.append(y - 1)
    # # print(array)
    # # print(G.edges, G.nodes)
    # for i in range(1, len(pos) + 1):
    #     posi[i - 1] = [pos[i][0], pos[i][1]]
    # cct = Circuit()
    # for i, j in enumerate(G.edges):
    #     if ((posi[j[0] - 1][1] - posi[j[1] - 1][1]) * 100) >= 70:
    #         cct.add(f'{netlist[array[i]][1]} {j[0]} {j[1]}; down')
    #     elif (((posi[j[0] - 1][1] - posi[j[1] - 1][1]) * 100) > 0) or (((posi[j[0] - 1][1] - posi[j[1] - 1][1]) * 100) > -70):
    #         if ((posi[j[0] - 1][0] - posi[j[1] - 1][0]) * 100) > 70:
    #             cct.add(f'{netlist[array[i]][1]} {j[0]} {j[1]}; left')
    #         else:
    #             cct.add(f'{netlist[array[i]][1]} {j[0]} {j[1]}; right')
    #     else:
    #         cct.add(f'{netlist[array[i]][1]} {j[0]} {j[1]}; up')
    # cct.draw()
    plt.show()


if __name__ == '__main__':
    main()
