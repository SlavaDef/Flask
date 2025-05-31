from utils.search import find

# pip install pytest встановити для тестування


#@patch('requests.get')
def test_find(self):

    # Викликаємо метод
    result = self.find('santabarbara','ab')

    # Перевіряємо результати
    expected = ['a','b']
    self.assertEqual(result, expected)


def test_find_basic():
    # Базовий тест
    assert find("hello", "hel") == ["e", "h", "l"]

def test_find_empty_letters():
    # Тест з пустим рядком letters
    assert find("hello", "") == []

def test_find_empty_phrase():
    # Тест з пустим рядком phrase
    assert find("", "abc") == []

def test_find_no_matches():
    # Тест коли немає збігів
    assert find("hello", "xyz") == []

def test_find_case_insensitive():
    # Тест на регістронезалежність
    assert find("Hello", "hElLo") == ["e", "h", "l", "l", "o"]

def test_find_duplicates():
    # Тест з повторюваними літерами
    assert find("hello", "ll") == ["l", "l"]

def test_find_special_characters():
    # Тест зі спеціальними символами
    assert find("hello!", "!h") == ["!", "h"]

def test_find_spaces():
    # Тест з пробілами
    assert find("hello world", "w d") == [" ", "d", "w"]

def test_find_numbers():
    # Тест з цифрами
    assert find("hello123", "123") == ["1", "2", "3"]

def test_find_unicode():
    # Тест з Unicode символами
    assert find("привіт", "прт") == ["п", "р", "т"]

