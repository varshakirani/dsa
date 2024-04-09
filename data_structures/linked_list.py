class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return
    
    def to_list(self):
        pylist = []
        node = self.head

        while node:
            pylist.append(node.value)
            node = node.next

        return pylist

    def prepend(self, value):
        """ Prepend a value to the beginning of the list. """
        node = self.head
        
        self.head = Node(value)
        self.head.next = node
        
        return

    def search(self, value):
        """ Search the linked list for a node with the requested value and return the node. """
        node = self.head
        
        while node:
            if node.value == value:
                return node
            node = node.next
            
        return None
        
def create_linked_list(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    if len(input_list) == 0:
        head = None
        return head
    
    head = Node(input_list[0])
    current_node = head
    for i in range(1,len(input_list)):
        current_node.next = Node(input_list[i])
        current_node = current_node.next
    
    return head

def create_linked_list_better(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    head = None
    tail = None

    for item in input_list:
        if head is None:
            head = Node(item)
            tail = head
        else:
            tail.next = Node(item)
            tail = tail.next
    
    return head