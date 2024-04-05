from data_structures.strings import string_reverser, anagram_checker, word_flipper
class TestStrings:

    def test_string_reverser(self):
        assert 'retaw' == string_reverser('water')
        assert '!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')
        assert '3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')

    
    def test_anagram_checker(self):
        assert not anagram_checker('water','waiter')
        assert anagram_checker('Dormitory','Dirty room')
        assert anagram_checker('Slot machines', 'Cash lost in me')
        assert not (anagram_checker('A gentleman','Elegant men'))
        assert anagram_checker('Time and tide wait for no man','Notified madman into water')

    def test_word_flipper(self):
        assert 'retaw' == word_flipper('water')
        assert 'sihT si na elpmaxe' == word_flipper('This is an example')
        assert 'sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')