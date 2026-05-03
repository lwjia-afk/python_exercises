from practice import first_10_squares, letter_position_dict
from practice import count_occurrences_manual, count_occurrences_counter, count_occurrences_defaultdict
from practice_02 import squares_of_evens, word_lengths, unique_first_letters, flatten, transpose_zip, pair_sums

def test_first_10_squares():
    expected = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    assert first_10_squares() == expected

def test_letter_position_dict():
    expected = {chr(i): i for i in range(97, 123)}
    assert letter_position_dict() == expected

def test_squares_of_evens():
    expected = [0, 4, 16, 36, 64, 100]
    assert squares_of_evens(10) == expected

def test_word_lengths():
    expected = {"hello": 5, "greetings": 9}
    assert word_lengths(["hi", "hello", "hey", "greetings"]) == expected

def test_count_occurrences():
   
    sample_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
    expected = {"apple": 3, "banana": 2, "orange": 1}
    
    assert count_occurrences_manual(sample_list) == expected
    assert count_occurrences_counter(sample_list) == expected
    assert count_occurrences_defaultdict(sample_list) == expected


def test_unique_first_letters():
    expected = {"h", "g"}
    assert unique_first_letters(["hi", "hello", "hey", "greetings"]) == expected    

def test_flatten():
    expected = [1, 2, 3, 4, 5]
    assert flatten([[1, 2], [3, 4], [5]]) == expected

def test_transpose_zip():
    expected = [[1, 4], [2, 5], [3, 6]]
    assert transpose_zip([[1, 2, 3], [4, 5, 6]]) == expected

def test_pair_sums():
    expected = [(0, 1, 3), (0, 2, 4), (0, 3, 5), (1, 2, 5), (1, 3, 6), (2, 3, 7)]
    assert pair_sums([1, 2, 3, 4]) == expected


