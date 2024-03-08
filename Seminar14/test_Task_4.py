# Задача 4:
import pytest
from Task_1 import clear_text


def test_no_changes():
	assert clear_text('hello world') == 'hello world', "Error"


def test_registr():
	assert clear_text('Hello world') == 'hello world', "Error"


def test_delete_punctuation():
	assert clear_text('Hello world!') == 'hello world', "Error"


def test_delete_foreign_alpha():
	assert clear_text('Hello мир') == 'hello ', "Error"


def test_all():
	assert clear_text('Hello, world или мир!') == 'hello world  ', "Error"


if __name__ == '__main__':
	pytest.main()
