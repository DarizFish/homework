#!-*- coding:utf8-*-

#每个单词一个节点

import networkx as nx
import matplotlib.pyplot as plt
import re

max_lenth = 0

def word2graph(wordlist):
    graph = nx.DiGraph()
    visitlist = []
    for index, word in enumerate(wordlist):
        # graph.add_node(index)
        for vid, vword in enumerate(visitlist):
            if word[0] == vword[-1]:
                graph.add_edge(vid, index)
            if word[-1] == vword[0]:
                graph.add_edge(index, vid)
        visitlist.append(word)
    return graph

def graph_next_code(graph, cur_code, code_route, code_index, routes):

    if next(graph.successors(cur_code), None) is None:
        # print(code_route)
        if len(code_route) > len(routes[0]):
            routes.clear()
            routes.append(code_route)
        elif len(code_route) == len(routes[0]):
            routes.append(code_route)
    else:
        flag = True
        for node in graph.successors(cur_code):
            if not node in code_route:
                code_route_next = code_route[:]
                code_route_next.append(node)
                flag = False
                graph_next_code(graph, node, code_route_next, code_index + 1, routes)
        if flag:
            # print(code_route)
            if len(code_route) > len(routes[0]):
                routes.clear()
                routes.append(code_route)
            elif len(code_route) == len(routes[0]):
                routes.append(code_route)
    return routes
#这里的routes是同一个变量吗，还是形参传递

def all_graph_route(graph):
    start_routes = []
    for start_node in list(graph):
        routes = graph_next_code(graph, start_node, [start_node], 1, [[]])
        start_routes.extend(routes)
    return start_routes

def all_longest_routes(r):
    longest_route = max(r, key=lambda l: len(l))
    all_longest_routes = [route for route in r if len(route) == len(longest_route)]
    return all_longest_routes

with open('wordtext.txt', 'r') as f:
    wordtext = f.read()
    wordlist = re.split(r'[\s,.\n\r]+', wordtext)
    wordlist = [s.lower() for s in wordlist]
    print(wordlist)

wordgraph = word2graph(wordlist)
wordroutes = all_graph_route(wordgraph)
word_longest_routes = all_longest_routes(wordroutes)

#show longest word routes
for one_route in word_longest_routes:
    str = '-'.join(wordlist[s] for s in one_route)
    print('longest words: ', str)

nx.draw(wordgraph)
plt.show()
