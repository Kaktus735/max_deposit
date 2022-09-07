def print_max_deposit(per_cent, money_str):
    if not money_str.isdigit():
        print('Введено некорректное значение суммы')
        return
    money = int(money_str)
    deposit = list(value * money for value in per_cent.values())
    max_deposit = max(deposit)
    if max_deposit.is_integer():
        max_deposit = int(max_deposit)
    print('Максимальная сумма, которую вы можете заработать —', max_deposit)

if __name__ == '__main__':
    per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
    money_str = input("Введите сумму денег, которую планируете положить под проценты\n")
    print_max_deposit(per_cent, money_str)