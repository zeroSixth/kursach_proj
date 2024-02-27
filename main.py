import json
from datetime import datetime

# Данные операций, представленные в виде списка словарей
operations = [
    # Пример данных операций
]

# Функция для фильтрации и сортировки операций
def filter_and_sort_operations(operations):
    executed_operations = [op for op in operations if op.get('state') == 'EXECUTED']
    executed_operations.sort(key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    return executed_operations[:5]

# Функция для маскирования информации о счетах и номерах карт
def mask_account_info(operation):
    if 'from' in operation:
        account_from = operation['from']
        if ' ' in account_from:  # Это номер карты
            parts = account_from.split(' ')
            operation['from'] = f'{parts[0]} {parts[1][:2]}** **** {parts[-1]}'
        else:  # Это счет
            operation['from'] = f'Счет **{account_from[-4:]}'
    if 'to' in operation:
        account_to = operation['to']
        if ' ' in account_to:  # Это номер карты
            parts = account_to.split(' ')
            operation['to'] = f'{parts[0]} {parts[1][:2]}** **** {parts[-1]}'
        else:  # Это счет
            operation['to'] = f'Счет **{account_to[-4:]}'

# Функция для форматирования и вывода информации об операции
def format_operation(operation):
    date_str = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
    description = operation['description']
    from_acc = operation.get('from', '')
    to_acc = operation.get('to', '')
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']
    print(f'{date_str} {description}\n{from_acc} -> {to_acc}\n{amount} {currency}\n')

# Применение функций
filtered_operations = filter_and_sort_operations(operations)
for op in filtered_operations:
    mask_account_info(op)
    format_operation(op)

