from collections import deque
#Tree

""" class Tree:
    def __init__(self):
        self.root = None

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
 """

#binary tree
class Tree:
    def __init__(self):
        self.root = None

class Node:
    def __init__(self,value):
        self.value = value
        self.left_child = None
        self.right_child = None



gm = Node("GM")

vice_gm  = Node("ViceGM")

vice_gm2 = Node("ViceGM2")

gm.left_child = vice_gm

gm.right_child = vice_gm2

dep_vice_gm1 = Node("Dep_Vice_GMA")

dep_vice_gm2 = Node("Dep_Vice_GMB")

vice_gm.left_child = dep_vice_gm1

vice_gm.right_child = dep_vice_gm2

dep_vice_gm21 = Node("Dep_Vice_GM1")

dep_vice_gm22 = Node("Dep_Vice_GM2")

vice_gm2.left_child = dep_vice_gm21
vice_gm2.right_child = dep_vice_gm22


my_tree = Tree()
my_tree.root = gm

#breath_first_transversal
""" def breath_first_transversal(node):
    result = []
    transv = deque([node])

    while len(transv)>0:
        node = transv.popleft()
        result.append(node.value)
        if node.left_child: 
            transv.append(node.left_child)
        if node.right_child:
            transv.append(node.right_child)
    return result


print(breath_first_transversal(gm))
         """

def depth_first_transversal(node):
    result = []
    transv = [node]

    while len(transv)>0:
        popped = transv.pop()
        result.append(popped.value)

        if popped.right_child:
            transv.append(popped.right_child)
        if popped.left_child:
            transv.append(popped.left_child)

    return result

print(depth_first_transversal(gm))