from data_structures.doubly_linked_list import DoublyLinkedList
import pytest


class TestDoublyLinkedList:

    def setup_method(self):
        self.linked_list = DoublyLinkedList()

   
    @pytest.mark.parametrize("values, expected_forward, expected_backward",[
        ([], [], []),
        ([1,-2,4], [1,-2,4], [4,-2,1]),
        ([5,6,7], [5,6,7], [7,6,5])
    ])
    def test_append_and_traverse(self, values, expected_forward, expected_backward):
        print(expected_forward)
        for value in values:
            self.linked_list.append(value)

        # Test traverse forward
        node = self.linked_list.head
        for expected_val in expected_forward:
            print(node.value)
            print(expected_val)
            assert node.value == expected_val
            node = node.next

        # Test traverse backward
        node = self.linked_list.tail
        for expected_val in expected_backward:
            assert node.value == expected_val
            node = node.previous


