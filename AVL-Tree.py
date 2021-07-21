class NodeTree():
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
        self.node_bal = 0

    def __str__(self):
        return str(self.element)


class AVL(NodeTree):
    def __init__(self, node=None):
        if node != None:
            self.start = node
        else:
            self.start = NodeTree(None)
            self.start.element = None
        
        self.aux_pointer = self.start


    def create_tree(self, element):
        self.start.element = element
        self.size =+ 1


    def destroy_tree(self):
        self.start.element = None
        self.start.right = None
        self.start.left = None
        self.start = None
        self.size = None

    def insert_element(self, element):
        aux_parent = None
        aux_node = self.start
        while aux_node != None:
            aux_parent = aux_node
            if element < aux_node.element:
                aux_node = aux_node.left
            else:
                aux_node = aux_node.right

        if aux_parent == None:
            self.start = NodeTree(element)
        elif element < aux_parent.element:
            aux_parent.left = NodeTree(element)
        else:
            aux_parent.right = NodeTree(element)

        self.execbal()

    def max(self, node=None):
        if node == None:
            node = self.start
        
        while node.right != None:
            node = node.right
        
        return node.element

    def min(self, node =  None):
        if node == None:
            node = self.start
        
        while node.left != None:
            node = node.left

        return node.element


    def delete_node(self, elem, node=0):
        if node == 0:
            node = self.start

        if node.element == None:
            return node

        if elem < node.element:
            node.left = self.delete_node(elem, node.left)

        elif elem > node.element:
            node.right = self.delete_node(elem, node.right)

        else:
            if node.left == None:
                aux_node = node.right
                node = None
                return aux_node

            elif node.right == None:
                aux_node = node.left
                node = None
                return aux_node

            else:
                aux_node = self.min(node.right)
                node.element = aux_node
                node.right = self.delete_node(aux_node, node.right)
        
        self.execbal()

        return node




        
  

    

        


    def search(self, elem, node=0):
        if node == 0:
            node = self.start
        if node == None or node.element == elem:
            return BST(node)
        if elem < node.element:
            return self.search(elem, node.left)
        else:
            return self.search(elem, node.right)


    def in_order(self, node=None):
        #do menor para maior
        if node == None:
            node = self.start

        if node.left != None:

            self.in_order(node.left)

        print(node.element, end=' ')

        if node.right != None:

            self.in_order(node.right)

    def pos_order(self, node=None):
        if node == None:
            node = self.start

        if node.left != None:
            self.pos_order(node.left)

        if node.right != None:
            self.pos_order(node.right)

        print(node.element, end=' ')
        

    def pre_order(self, node = None):
        if node == None:
            node = self.start
        
        print(node.element, end=' ')

        if node.left != None:
            self.pre_order(node.left)

        if node.right != None:
            self.pre_order(node.right)

    def height(self, node=None):
        if node == None:
            node = self.start
        hl = 0
        hr = 0
        if node.left != None:
            hl = self.height(node.left)

        if node.right != None:
            hr = self.height(node.right)

        if hr > hl:
            return hr + 1
        
        else:
            return hl + 1

    def balance(self, node):
        hl = 0
        hr = 0
        hl = self.height(node.left) 
        hr = self.height(node.right)

        return int(hl - hr)

    def getbal(self, node=None):
        if node == None:
            node = self.start
        
        if node.left != None:
            return self.getbal(node.left)

        if node.right != None:
            return self.getbal(node.right)

        node.node_bal = self.balance(node)
        

    def execbal(self):
        self.getbal()
        node = self.start
        
        if node.node_bal > 1:
            if node.left.node_bal < 0:
                self.Rot_LL(node.left)
            self.Rot_LR(node)
            self.getbal
            
        if node.node_bal < -1:
            if node.right.node_bal > 0:
                self.Rot_LR(node.right)
            self.Rot_LL(node)
            self.getbal

        
        
    def Rot_LR(self, node):
        A = node
        B = node.left
        T = B.right.node

        node = B
        B.right.node = A
        A.left.node = T

    def Rot_LL(self, node):
        A = node
        B = node.right
        T = B.left.node

        node = B
        B.left.node = A
        A.right.node = T


def compare_tree(tree1, tree2):
    if tree1 and tree2 == None:
        return True

    if tree1.start.element == tree2.start.element:
        return compare_tree(tree1.start.right, tree2.start.right) and compare_tree(tree1.start.left, tree2.start.left)

    if tree1 == None and tree2 != None:
        return False

    if tree1 != None and tree2 == None:
        return False        
