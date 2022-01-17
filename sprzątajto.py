class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


class Binary_Tree:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = Binary_Tree(new_node)
        else:
            t = Binary_Tree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = Binary_Tree(new_node)
        else:
            t = Binary_Tree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_key(self, key):
        self.key = key

    def get_root_key(self):
        return self.key
        


def build_parse_tree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = Binary_Tree('')
    pStack.push(eTree)
    current_tree = eTree
    for i in fplist:
        if i == '(':
            current_tree.insert_left('')
            pStack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i in ['+', '-', '*', '/', '**']:
            current_tree.set_root_key(i)
            current_tree.insert_right('')
            pStack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i.isalpha(): #i is a letter
            current_tree.set_root_key(i)
            current_tree = pStack.pop()
        elif i.isdigit(): #i is a digit
            current_tree.set_root_key(int(i))
            current_tree = pStack.pop()
        elif i in ['sin', 'cos', 'tg', 'ctg', 'log', 'exp']:
            current_tree = pStack.pop()
            current_tree.left_child = None
            current_tree.set_root_key(i)
            current_tree.insert_right('')
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = pStack.pop()
        else:
            raise ValueError
    return eTree

class ErrorComplexExpression(Exception):
    pass
class ErrorInvalidTree(Exception):
    pass


def printexp(tree):
    sVal = ""
    if tree:
        sVal = '(' + printexp(tree.get_left_child())
        sVal = sVal + str(tree.get_root_key())
        sVal = sVal + printexp(tree.get_right_child())+')'
    return sVal


def variable_in_expression(tree, variable):
    if tree:
        return tree.get_root_key() == variable or variable_in_expression(tree.get_left_child(), variable) or variable_in_expression(tree.get_right_child(), variable)     
    else:
        return False


def count_derivative(tree, variable):
    derivative_tree = Binary_Tree("")

    left_child = tree.get_left_child()
    right_child = tree.get_right_child()
    root_key = tree.get_root_key()

    if left_child and right_child:

        if root_key == '+':
            derivative_tree.set_root_key("+")
            derivative_tree.left_child = count_derivative(left_child, variable)
            derivative_tree.right_child = count_derivative(right_child, variable)

        elif root_key == '-':
            derivative_tree.set_root_key("-")
            derivative_tree.left_child = count_derivative(left_child, variable)
            derivative_tree.right_child = count_derivative(right_child, variable)

        elif root_key == '*':
            derivative_tree.set_root_key("+")

            derivative_tree.left_child = Binary_Tree("")
            derivative_tree.left_child.set_root_key("*")
            derivative_tree.left_child.left_child = count_derivative(left_child, variable)
            derivative_tree.left_child.right_child = right_child

            derivative_tree.right_child = Binary_Tree("")
            derivative_tree.right_child.set_root_key("*")
            derivative_tree.right_child.left_child = left_child
            derivative_tree.right_child.right_child = count_derivative(right_child, variable)
            
        elif root_key == '/':
            derivative_tree.set_root_key("/")

            derivative_tree.left_child = Binary_Tree("")
            derivative_tree.left_child.set_root_key("-")
            derivative_tree.left_child.left_child = Binary_Tree("")
            derivative_tree.left_child.right_child = Binary_Tree("")

            derivative_tree.left_child.left_child.set_root_key("*")
            derivative_tree.left_child.left_child.left_child = count_derivative(left_child, variable)
            derivative_tree.left_child.left_child.right_child = right_child

            derivative_tree.left_child.right_child.set_root_key("*")
            derivative_tree.left_child.right_child.left_child = left_child
            derivative_tree.left_child.right_child.right_child = count_derivative(right_child, variable)

            derivative_tree.right_child = Binary_Tree("")
            derivative_tree.right_child.set_root_key("**")
            derivative_tree.right_child.left_child = right_child
            derivative_tree.right_child.right_child = Binary_Tree("")
            derivative_tree.right_child.right_child.set_root_key(2)

        elif root_key == "**":
            left_has_variable = variable_in_expression(left_child, variable)
            right_has_variable = variable_in_expression(right_child, variable)

            if left_has_variable and right_has_variable:
                raise ErrorComplexExpression

            elif left_has_variable:
                derivative_tree.set_root_key('*')

                derivative_tree.left_child = right_child

                derivative_tree.right_child = Binary_Tree("")
                derivative_tree.right_child.set_root_key("**")
                derivative_tree.right_child.left_child = left_child

                derivative_tree.right_child.right_child = Binary_Tree("")
                derivative_tree.right_child.right_child.set_root_key('-')
                derivative_tree.right_child.right_child.left_child = right_child
                derivative_tree.right_child.right_child.right_child = Binary_Tree("")
                derivative_tree.right_child.right_child.right_child.set_root_key(1)

            elif right_has_variable:
                derivative_tree.set_root_key('*')

                derivative_tree.left_child = Binary_Tree("")
                derivative_tree.left_child.set_root_key("**")
                derivative_tree.right_child = Binary_Tree("")
                derivative_tree.right_child.set_root_key("*log")

                derivative_tree.left_child.left_child = left_child
                derivative_tree.left_child.right_child = right_child
                derivative_tree.right_child.right_child = left_child

            else: derivative_tree.set_root_key(0)

        else: raise ErrorInvalidTree

    elif right_child:
        if root_key == "log":
            derivative_tree.set_root_key("*")
            derivative_tree.left_child = Binary_Tree("")
            derivative_tree.left_child.set_root_key("/")
            derivative_tree.right_child = count_derivative(right_child, variable)
            derivative_tree.left_child.left_child = Binary_Tree("")
            derivative_tree.left_child.left_child.set_root_key(1)
            derivative_tree.left_child.right_child = right_child

        elif root_key == "sin":
            derivative_tree.set_root_key("*")
            derivative_tree.left_child = Binary_Tree("")
            derivative_tree.left_child.set_root_key("cos")
            derivative_tree.left_child.right_child = right_child
            derivative_tree.right_child = derivative_tree(right_child, variable)

        elif root_key == "cos":
            derivative_tree.set_root_key("*")
            derivative_tree.left_child = Binary_Tree("")
            derivative_tree.left_child.set_root_key("*")
            derivative_tree.left_child.left_child = Binary_Tree("")
            derivative_tree.left_child.left_child.set_root_key(-1)
            derivative_tree.left_child.right_child = Binary_Tree("")
            derivative_tree.left_child.right_child.set_root_key("sin")
            derivative_tree.left_child.right_child.right_child = right_child
            derivative_tree.right_child = count_derivative(right_child, variable)

        elif root_key == "tg":
            derivative_tree.set_root_key("*")
            derivative_tree.left_child = Binary_Tree("")
            derivative_tree.left_child.set_root_key("/")
            derivative_tree.left_child.left_child = Binary_Tree("")
            derivative_tree.left_child.left_child.set_root_key(1)
            derivative_tree.left_child.right_child = Binary_Tree("")
            derivative_tree.left_child.right_child.set_root_key("**")
            derivative_tree.left_child.right_child.left_child = Binary_Tree("")
            derivative_tree.left_child.right_child.left_child.set_root_key("cos")
            derivative_tree.left_child.right_child.right_child = Binary_Tree("")
            derivative_tree.left_child.right_child.right_child.set_root_key(2)
            derivative_tree.left_child.right_child.left_child.right_child = right_child
            derivative_tree.right_child = derivative_tree(right_child, variable)

        elif root_key == "ctg":
            derivative_tree.set_root_key("*")
            derivative_tree.left_child = Binary_Tree("")
            derivative_tree.left_child.set_root_key("/")
            derivative_tree.left_child.left_child = Binary_Tree("")
            derivative_tree.left_child.left_child.set_root_key(-1)
            derivative_tree.left_child.right_child = Binary_Tree("")
            derivative_tree.left_child.right_child.set_root_key("**")
            derivative_tree.left_child.right_child.left_child = Binary_Tree("")
            derivative_tree.left_child.right_child.left_child.set_root_key("cos")
            derivative_tree.left_child.right_child.right_child = Binary_Tree("")
            derivative_tree.left_child.right_child.right_child.set_root_key(2)
            derivative_tree.left_child.right_child.left_child.right_child = right_child
            derivative_tree.right_child = derivative_tree(right_child, variable)

        else:
            raise ErrorInvalidTree
    
    else:
        if root_key == variable:
            derivative_tree.set_root_key(1)
        else:
            derivative_tree.set_root_key(0)

    return derivative_tree

test_1 = build_parse_tree("( cos x )")
print(printexp(test_1))

print(printexp(count_derivative(test_1, "x")))






