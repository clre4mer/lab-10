#импортирую библиотеку лога и провожу её стандартную настройку
import logging
logging.basicConfig(filename="4thLog.log", 
                    format='%(asctime)s %(name)s %(levelname)s %(message)s',
                    datefmt='%H: %M: %S',
                    level=logging.DEBUG)
#создаю функцию проверки на ошибки ввода
def errorCheck(n):
    try:
        n = int(n)
    except Exception:
        logging.error('Неверный ввод!')
        return -1
    return n
N = - 1
#цикл ввода значений
while N == -1:
    N = int(input('Введите натуральное число:\n'))
    N = errorCheck(N)
    if N<=0:
        print('Необходимо ввести НАТУРАЛЬНОЕ число\n')
        N=-1
        logging.error('Неверный ввод!')
logging.info(f'Пользователь ввёл значение {N}')
#задаю массив купюр
kup=[64,32,16,8,4,2,1]
print('Для выдачи набранной суммы наименьшим количеством купюр будет использовано:\n')
#основной цикл программы, выявляющий оптимальный набор кюпюр, для их наименьшего количества
for i in kup:
    num=N//i
    logging.info(f'Количество купюр наминалом {i}: {num}')
    N=N-(num*i)
    logging.info(f'Оставшаяся число: {N}')
    if num!=0:
        print(f'{num} : номиналом ({i}) ', end='')
    if N==0:
        break;