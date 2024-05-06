def luhn_algorithm(card_number):
    # Убираем пробелы и переводим номер карты в список цифр
    card_digits = [int(digit) for digit in card_number.replace(" ", "")]

    # Удваиваем четные цифры, начиная с последней
    for i in range(len(card_digits) - 2, -1, -2):
        card_digits[i] *= 2
        if card_digits[i] > 9:
            card_digits[i] -= 9

    # Суммируем все цифры
    total = sum(card_digits)

    # Проверяем, делится ли сумма на 10 без остатка
    return total % 10 == 0

def main():
    card_number = input("Введите номер карты: ")
    if luhn_algorithm(card_number):
        print("Номер карты действителен по алгоритму Луна.")
    else:
        print("Номер карты недействителен по алгоритму Луна.")

if __name__ == "__main__":
    main()
