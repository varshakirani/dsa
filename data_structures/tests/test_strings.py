from data_structures.strings import string_reverser
class TestStrings:

    def test_string_reverser(self):
        assert 'retaw' == string_reverser('water')
        assert '!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')
        assert '3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')

    