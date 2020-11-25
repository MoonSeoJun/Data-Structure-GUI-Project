class Node:
    def __init__(self, data:str, next=None):
        self.data = data
        self.next = next

def init_list():
    global node_A

    node_A = Node("HEAD")

    node_A.next = None


def Linked_insert_node(data:str):
    global node_A

    if data is None:
        return

    if data is '':
        return

    new_node = Node(data)
    node_P = node_A
    node_T = node_A

    while node_T:
        node_P = node_T
        node_T = node_T.next
    
    new_node.next = node_T
    node_P.next = new_node

def Linked_delete_node(del_data:str):
    global node_A

    pre_node = node_A
    next_node = pre_node.next

    if pre_node.data == del_data:
        node_A = next_node
        del pre_node
        return

    while next_node:
        if next_node.data == del_data:
            pre_node.next = next_node.next
            del next_node
            break
        pre_node = next_node
        next_node = next_node.next

def Linked_print_list():
    global node_A

    node_list = []

    node = node_A

    while node:
        node_list.append(node.data)
        node = node.next

    node_string = '  -->  '.join(node_list)

    return node_string

def reset_linkedlist():
    global node_A

    pre_node = node_A
    next_node = pre_node.next

    while next_node:

        print(pre_node)
        del pre_node

        pre_node = next_node
        next_node = next_node.next