from data_structures.linked_list import create_linked_list
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



        