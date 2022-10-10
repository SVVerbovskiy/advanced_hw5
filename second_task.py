from datetime import datetime
import requests
import os


def log_decorator(path):
    def _log_decorator(oldfunction):
        def foo(*args, **kwargs):
            date_time = datetime.now()
            str_time = date_time.strftime('%Y-%m-%d время %H-%M-%S')
            func_name = oldfunction.__name__
            result = oldfunction(*args, **kwargs)
            with open(f'{path}\log\decorator_logs_2.txt', 'a', encoding='utf-8') as file:
                file.write(f'\nДата вызова функции {str_time}\n'
                           f'Имя функции {func_name}\n'
                           f'Аргументы функции {args, kwargs}\n'
                           f'Функция возвращает значение {result}\n'
                           f'{"-" * 50}\n')
            return result
        return foo
    return _log_decorator


@log_decorator(path=os.getcwd())
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


@log_decorator(path=os.getcwd())
def get_status(*args):
    url = ','.join(args)
    response = requests.get(url=url)
    return response.status_code


if __name__ == '__main__':
    get_status('https://habr.com/ru/all/')
    factorial(6)
