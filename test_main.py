import pytest
from main import filter_and_sort_operations, mask_account_info, format_operation
from datetime import datetime

# Данные для тестирования
test_operations = [
    # Добавьте примеры операций с различными состояниями и датами
]

# Тест фильтрации и сортировки операций
def test_filter_and_sort_operations():
    # Тест с предопределенными данными
    result = filter_and_sort_operations(test_operations)
    # Проверка количества операций после фильтрации
    assert len(result) <= 5
    # Проверка порядка операций
    dates = [op['date'] for op in result]
    assert dates == sorted(dates, reverse=True)

# Тест маскирования информации о счетах и номерах карт
def test_mask_account_info():
    operation = {
        'from': '1234 5678 9012 3456',
        'to': '9876 5432 1098 7654'
    }
    mask_account_info(operation)
    assert operation['from'] == '1234 56** **** 3456'
    assert operation['to'] == '9876 54** **** 7654'

# Тест форматирования и вывода информации об операции
def test_format_operation(capfd):  # capfd - фикстура pytest для перехвата вывода
    operation = {
        'date': '2023-01-01T12:00:00.000',
        'description': 'Test operation',
        'operationAmount': {'amount': 100, 'currency': {'name': 'USD'}},
        'from': '1234 5678 9012 3456',
        'to': '9876 5432 1098 7654'
    }
    format_operation(operation)
    out, _ = capfd.readouterr()
    assert '01.01.2023 Test operation\n1234 5678 9012 3456 -> 9876 5432 1098 7654\n100 USD\n' in out

# Добавьте дополнительные тесты при необходимости

