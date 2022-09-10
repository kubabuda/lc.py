from typing import *
# https://leetcode.com/problems/clone-graph
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    def __repr__ (self):
        return f'Node #{id(self)} {self.val}:{[n.val for n in self.neighbors]}'

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.clone(node)
    
    def clone(self, node: 'Node', all_nodes = None) -> 'Node':
        if not node: return node
        all_nodes = all_nodes or {}
        if node.val not in all_nodes:
            all_nodes[node.val] = Node(node.val)
        cloned_node = all_nodes[node.val]
        for ne in node.neighbors:
            if ne.val not in all_nodes:
                cloned_ne = self.clone(ne, all_nodes)
            else:
                cloned_ne = all_nodes[ne.val]
            cloned_node.neighbors.append(cloned_ne)
        return cloned_node

from unittest import TestCase
import unittest
class TestTemplate(unittest.TestCase): 
    def testCases(self):
        param_list = [
            ([[2,4],[1,3],[2,4],[1,3]]),
            ([[]]),
            ([]),
        ]
        for nodes in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                root = buildGraph(nodes)
                # act
                result = s.cloneGraph(root)
                # assert
                assertEqualGraphNode(self, root, result)
    
def assertEqualGraphNode(self, node1: 'Node', node2: 'Node', visited = None):
    if not visited: visited = set()
    self.assertNotEqual(node1, node2)
    self.assertEqual(node1.val, node2.val)
    self.assertEqual(len(node1.neighbors), len(node2.neighbors))
    visited.add(node1)
    visited.add(node2)
    
    for i in range(0, len(node1.neighbors)):
        n1 = node1.neighbors[i]
        n2 = node2.neighbors[i]
        if n1 in visited:
            self.assertTrue(n2 in visited, (n1, n2, visited))
        else:
            self.assertFalse(n2 in visited)
            assertEqualGraphNode(self, n1, n2, visited)

def buildGraph(nodes: List[List[int]]) -> 'Node':
    if not nodes: return Node()
    new_nodes = { i: Node(i) for i in range(1, len(nodes) + 1)}
    # print(nodes, new_nodes)
    for i, neighbors in enumerate(nodes):
        node = new_nodes[i + 1]
        for neighbor in neighbors:
            node.neighbors.append(new_nodes[neighbor])
    return new_nodes[1]



if __name__ == '__main__':
    unittest.main()
