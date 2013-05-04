#/usr/bin/python
def nodes_from_raw(raw_graph):
  nodes = {x: Node(x) for x in raw_graph}
  for node in nodes.values():
    node.successors = [nodes[name] for name in raw_graph[node.name]]
  return nodes

def numbering_dfs(nodes):
  for (idx, node) in enumerate(nodes):
    if node.numbering_dfs_visit(idx):
      return True
  return False

def dfs(nodes):
  time = 0
  for node in sorted(nodes.itervalues(), reverse=True, key=lambda x: x.finish):
    if node.finish is None:
      time = node.dfs_visit(time)

def reverse(graph):
  new_nodes = {}
  for node in graph.itervalues():
    new_nodes[node.name] = Node(node.name)

  sorted(new_nodes.itervalues(), reverse=True, key=lambda x: x.finish)
  for node in sorted_items:
    for succ in graph[node.name].successors:
      new_nodes[succ.name].successors.append(node)

  return sorted_items

class Node:
  def __init__(self, name, finish=None):
    self.name = name
    self.finish = finish
    self.successors = []
    self.number = -1

  def __repr__(self):
    return "<Node {0}: {1} ({2})>".format(self.name, [s.name for s in self.successors], self.finish)

  def dfs_visit(self, time):
    self.finish = -1
    for successor in self.successors:
      if successor.finish is None:
        time = successor.dfs_visit(time)
    self.finish = time
    return time + 1

  def numbering_dfs_visit(self, number):
    if self.number is number:
      return True
    elif self.number is not -1:
      return False

    self.number = number
    for successor in self.successors:
      if successor.numbering_dfs_visit(number):
        return True
    return False

raw_graph = {0: [1, 2, 3], 1: [2, 3], 2: [3], 3: []}
nodes = nodes_from_raw(raw_graph)
dfs(nodes)
reverse_nodes = reverse(nodes)
print(numbering_dfs(reverse_nodes))
