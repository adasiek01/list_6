from ssl import get_default_verify_paths


class Node():
    """
    Binary tree Node class
    """
    def __init__(self, key, value, left=None, right=None, parent=None):
        """
        Function that creates new node
        :param key: Node's key
        :param value: Node's value
        :param left: Node's left child (None by default)
        :param right: Node's right child (None by default)
        """
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def get_left_child(self):
        """
        Function that returns Node's left child
        """
        return self.left_child

    def get_right_child(self):
        """
        Function that returns Node's right child
        """
        return self.right_child

    def has_left_child(self):
        """
        Function that returns bool info about
        having a left child
        """
        return not self.left_child == None
    
    def has_right_child(self):
        """
        Function that returns bool info about
        having a right child
        """
        return not self.right_child == None
    
    def is_left_child(self):
        """
        Function that returns bool info about
        being a left child of a Node
        """
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        """
        Function that returns bool info about
        being a left child of a Node
        """
        return self.parent and self.parent.right_child == self

    def has_any_children(self):
        """
        Function that returns bool info about
        having any children 
        """
        return self.right_child or self.left_child

    def has_both_children(self):
        """
        Function that returns bool info about
        having both children 
        """
        return self.right_child and self.left_child

    def is_root(self):
        """
        Function that returns bool info about
        bein a root of a Node
        """
        return not self.parent

    def set_new_data(self, new_key, new_value, new_left_child, new_rgiht_child):
        """
        Function that sets new data for a given Node
        :param new_key: new Node's key
        :param new_value: new Node's value
        :param new_left_child: new Node's left child
        :param new_right_child: new Node's right child
        """
        self.key = new_key
        self.value = new_value
        self.left_child = new_left_child
        self.right_child = new_rgiht_child

        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def find_min(self):
        """
        Function that finds node with minimum key
        """
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

    def find_successor(self):
        """
        Function that finds successor for deleted Node
        Return Node that can be self's successor
        """
        succ = None
        if self.has_right_child():
            succ = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                     succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self
        return succ


    def spliceOut(self):
        """
        Function that "cut out" self Node
        from BinarySearchTree
        """
        if not self.has_any_children(): #if self is a leaf
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                    self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent
    
    ####################################
    #  Additional methods helpful for  #
    #  displaying results.             #
    ####################################

    def get_left_key(self):
        """
        Function that returns Node's left child's key
        """
        return self.left_child.key

    def get_right_key(self):
        """
        Function that returns Node's right child's key
        """
        return self.right_child.key

    ####################################


class Binary_Search_Tree:
    """
    Binary Seatch Tree class
    """
    def __init__(self):
        """
        Function that creates new Binary Search Tree
        Tree's Node is set to None by default
        Tree's size is 0 by default.
        """
        self.root = None
        self.size = 0

    def length(self):
        """
        Function returning number of Nodes in a Tree
        """
        return self.size

    def __len__(self):
        """
        Function that overloads an operator.
        Return number of Nodes in a Tree
        """
        return self.size

    def __iter__(self):
        """
        Function that enable iteration over a Tree
        like over a dictionary 
        """
        return self.root.__iter__()

    def place(self, key, value, current_node):
        """
        Function that recursively locate Node to 
        keep order in a Tree
        :param key: key of a Node that must be located
                    in a Tree
        :param value: value of a Node that must be located
                      in a Tree
        :param current_node: Node when we start finding location
                             for placing Node with key = key and 
                             valule = value 
        """
        if key > current_node.key:
            if not current_node.has_right_child():
                current_node.right_child = Node(key, value, parent=current_node)
            else:
                self.place(key, value, current_node.right_child)
        else:
            if not current_node.has_left_child():
                current_node.left_child = Node(key, value, parent=current_node)
            else:
                self.place(key, value, current_node.left_child)        
        

    def put(self, key, value):
        """
        Function that place new Node in a right location.
        :param key: new Node's key
        :param value: new Node's value
        """
        if self.root:
            self.place(key, value, self.root)
        else:
            self.root = Node(key, value)
        
        self.size += 1

    def __setitem__(self,key,value): #overloading of [] operator
        """
        Function that enable putting elements into
        a Tree like into a dictrionary
        """
        self.put(key,value) 

    def find_same_key(self, key, current_node):
        
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node

        elif key > current_node.key:
            return self.find_same_key(key, current_node.right_child)
        else:
            return self.find_same_key(key, current_node.left_child)

    def get_node(self, key):
        """
        Function returning value of Node with
        given key
        :param key: key of Node which is looked for
        Return value of Node or None if node with given 
        key does not exist
        """
        if self.root:
            obtained_node = self.find_same_key(key, self.root)
            if obtained_node:
                return obtained_node.value
            else:
                return None
        else:
            return None

    def __contains__(self, key):
        """
        Function that returns bool info about
        presence of node with a given key in 
        a Tree
        """
        if self.find_same_key(key, self.root):
            return True
        else:
            return False

    def __getitem__(self,key): #overloading of [] operator
        """
        Function that overload an operator and
        enable getting value of Node with
        given key. It gives acces to Nodes like to
        elements in dictionary
        :param key: key of a Node which is searched
        Return value of Node or None if node with given 
        key does not exist
        """
        return self.get_node(key) 

    

    def remove(self, current_node):
        """
        Function that helps with deleting and 
        keeping an order in a Tree
        :param current_node: node which must be deleted
        """
        if not current_node.has_any_children(): # has no children
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None

        elif current_node.has_both_children():
            succ = current_node.find_successor()
            succ.spliceOut()
            current_node.key = succ.key
            current_node.value = succ.value

        else: # has one children (left or right)
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.set_new_data(current_node.left_child.key, current_node.left_child.value, 
                    current_node.left_child.left_child, current_node.left_child.right_child)

            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.set_new_data(current_node.right_child.key, current_node.right_child.value,
                    current_node.right_child.left_child, current_node.right_child.right_child)



    def delete(self, key):
        """
        Function that delete an element of a given key.
        When there's more than one element with this key,
        all of them are removed
        :param key: key of Node(s) that must be deleted
        raise Keyerror when key is not found in a Tree
        """
        if self.size > 1:
            
            node_to_remove = self.find_same_key(key, self.root)
            if node_to_remove != None:
                while node_to_remove != None and self.size >= 1:
                    current_node = node_to_remove.left_child
                    self.remove(node_to_remove)
                    self.size -= 1
                    node_to_remove = self.find_same_key(key, current_node)
            else:
                raise KeyError("Eroor! This key is not in tree!!")

        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        
        else:
            raise KeyError("Eroor! This key is not in tree!!")

    ####################################
    #  Additional methods helpful for  #
    #  displaying results.             #
    ####################################
    def get_key(self,current_node):
        """
        Function that returns given Node's key
        """
        return current_node.key

    def get_root_key(self):
        """
        Function that returns root's key
        """
        return self.root.key

    def get_root(self):
        """
        Function that returns a root
        """
        return self.root

    def get_left_key(self, current_node):
        """
        Function that returns left child's key 
        """
        return current_node.get_left_key()

    def get_right_key(self, current_node):
        """
        Function that returns right child's key 
        """
        return current_node.get_right_key()

    def get_left_child(self, current_node):
        """
        Function that returns left child 
        """
        return current_node.get_left_child()

    def get_right_child(self, current_node):
        """
        Function that returns right child 
        """
        return current_node.get_right_child()

    ####################################


if __name__ == "__main__":
    mytree = Binary_Search_Tree()
    mytree[2]="a"
    mytree[4]="b"
    mytree[15]="c"
    mytree[0]="d"
    mytree[7] = "w"
    mytree[7]="e"
    mytree[3]="f"
    mytree[11] = "u"
    mytree[2] = "A"
    mytree[2]="g"
    mytree[7]="h"
    mytree[7] = "i"

    root = mytree.get_root()
    root_key = mytree.get_root_key()
    left_child = mytree.get_left_child(root)
    right_child = mytree.get_right_child(root)
    r_l_child = mytree.get_right_child(left_child)
    r_r_child = mytree.get_right_child(right_child)

    left_child_key = mytree.get_left_key(root)
    right_child_key= mytree.get_right_key(root)
    r_l_child_key= mytree.get_right_key(left_child)
    r_r_child_key= mytree.get_right_key(right_child)


    print("root:", root_key, "\n left child:", left_child_key, "\n right_child:", right_child_key,"\n right left child:", r_l_child_key, "\n right right child:", r_r_child_key)

    print("root_before",mytree.get_root_key())
    print("before ",mytree.size)
    mytree.delete(7)
    print("after ",mytree.size)
    mytree.delete(2)
    print("after_2 ",mytree.size)
    print("root_after_2",mytree.get_root_key())
    mytree.put(15,"s")
    print("after_put",mytree.size)

    
