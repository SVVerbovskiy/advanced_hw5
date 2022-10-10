from datetime import datetime


def log_decorator(oldfunction):
    def foo(*args, **kwargs):
        date_time = datetime.now()
        str_time = date_time.strftime('%Y-%m-%d время %H-%M-%S')
        func_name = oldfunction.__name__
        result = oldfunction(*args, **kwargs)
        with open('log/decorator_logs_3.txt', 'a', encoding='utf-8') as file:
            file.write(f'\nДата вызова функции {str_time}\n'
                       f'Имя функции {func_name}\n'
                       f'Аргументы функции {args, kwargs}\n'
                       f'Функция возвращает значение {result}\n'
                       f'{"-"*50}\n')
        return result
    return foo
