password = input("Введите пароль: ")
length = len(password)


def is_very_long(password):
    return length > 12


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_letters(password):
    return any(char.isalpha() for char in password)


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_symbols(password):
    return any(not char.isalnum() for char in password)


score = 0

conditions = [
    is_very_long(password),
    has_digit(password),
    has_letters(password),
    has_upper_letters(password) and has_lower_letters(password),
    has_symbols(password)
]


for condition in conditions:
    if condition:
        score += 2


print('Рейтинг пароля: ', score)