from typing import Any
class Node:
    def __init__(self,data: Any):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head = None) -> None:
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def insert(self, data:Any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def remove(self, data: Any) -> None:
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return
        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        previous_node.next = current_node.next
        current_node = None

    def reverse_iterative(self) -> None:
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next #current_nodeのnextのnodeをnext_nodeに設定する
            current_node.next = previous_node #current_nodeのnextの矢印の先をprevios_nodeに設定する
            previous_node = current_node
            current_node = next_node
        self.head = previous_node #headの矢印の先をprevios_nodeに設定する

    def reverse_recursive(self) -> None:
        def _reverse_recursive(current_node: Node, previous_node: Node):
            if not current_node:
                return previous_node
            next_node = current_node.next 
            current_node.next = previous_node 
            previous_node = current_node
            current_node = next_node
            return _reverse_recursive(current_node, previous_node)
        self.head = _reverse_recursive(self.head, None)

    def reverse_even(self) -> None:
        def _reverse_even(head: Node, previous_node: Node):
            if head is None:
                return None
            current_node = head
            while current_node and current_node.data % 2 == 0:
                next_node = current_node.next 
                current_node.next = previous_node 
                previous_node = current_node
                current_node = next_node
            if current_node != head:
                head.next = current_node
                _reverse_even(current_node, None)
                return previous_node
            else:
                head.next = _reverse_even(head.next, head)
                return head
        self.head = _reverse_even(self.head, None)

if __name__ == '__main__':
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(4)
    l.append(6)
    l.append(1)
    print("##############")
    l.reverse_even()
    l.print()
