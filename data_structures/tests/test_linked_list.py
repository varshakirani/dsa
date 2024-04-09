import pytest
from data_structures.linked_list import create_linked_list, create_linked_list_better, LinkedList
class TestLinkedList:
    def test_create_linked_list(self,
                                 linkedlist_input_data1,
                                 linkedlist_input_data2,
                                 linkedlist_input_data3,
                                 linkedlist_output_data1,
                                 linkedlist_output_data2,
                                 linkedlist_output_data3):

        # Testcase 1
        head1 = create_linked_list(linkedlist_input_data1)
        assert head1.value == linkedlist_output_data1
        node = head1
        for value in linkedlist_input_data1[1:]:
            node = node.next
            assert node.value == value
        assert node.next is None

        # Testcase 2
        head2 = create_linked_list(linkedlist_input_data2)
        assert head2.value == linkedlist_output_data2
        assert head2.next is None

        # Testcase 3
        head3 = create_linked_list(linkedlist_input_data3)
        assert head3 == linkedlist_output_data3



    def test_create_linked_list_better(self,
                                 linkedlist_input_data1,
                                 linkedlist_input_data2,
                                 linkedlist_input_data3,
                                 linkedlist_output_data1,
                                 linkedlist_output_data2,
                                 linkedlist_output_data3):

        # Testcase 1
        head1 = create_linked_list_better(linkedlist_input_data1)
        assert head1.value == linkedlist_output_data1
        node = head1
        for value in linkedlist_input_data1[1:]:
            node = node.next
            assert node.value == value
        assert node.next is None

        # Testcase 2
        head2 = create_linked_list_better(linkedlist_input_data2)
        assert head2.value == linkedlist_output_data2
        assert head2.next is None

        # Testcase 3
        head3 = create_linked_list_better(linkedlist_input_data3)
        assert head3 == linkedlist_output_data3


    @pytest.fixture
    def empty_linked_list(self):
        return LinkedList()

    @pytest.mark.parametrize("append_values, after_append_head", [
        ([], None),
        ([1, 2, 3], 1),
        ([4, 10, 9, 8], 4)
    ])
    def test_append(self, empty_linked_list, append_values, after_append_head):
        for value in append_values:
            empty_linked_list.append(value)
        assert (empty_linked_list.head.value if empty_linked_list.head else None) == after_append_head

    @pytest.mark.parametrize("prepend_values, after_prepend_head", [
        ([], None),
        ([2, 3, 1], 1),
        ([3, 5, 1, 6], 6)
    ])
    def test_prepend(self, empty_linked_list, prepend_values, after_prepend_head):
        for value in prepend_values:
            empty_linked_list.prepend(value)
        assert (empty_linked_list.head.value if empty_linked_list.head else None) == after_prepend_head

    @pytest.mark.parametrize("append_values, search, search_result", [
        ([], 1, None),
        ([1, 2, 3], 3, 3),
        ([4, 10, 9, 8], 7, None)
    ])
    def test_search(self, empty_linked_list, append_values, search, search_result):
        for value in append_values:
            empty_linked_list.append(value)
        assert (empty_linked_list.search(search).value if empty_linked_list.search(search) else None) == search_result

    