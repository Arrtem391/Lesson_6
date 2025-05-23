def is_very_long(password):
    return len(password) > 12


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


def password_score(password):
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
    return score


if __name__ == "__main__":
    password = input("Введите пароль: ")
    score = password_score(password)
    print('Рейтинг пароля: ', score)
