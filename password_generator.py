from random import choices, shuffle, choice

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nonchars = 'Il1o0O'

chars = lowercase_letters + uppercase_letters + digits
for c in nonchars:
    chars = chars.replace(c, '')


def generate_password(length, chars):
    password = ''
    password += choice([x for x in chars if x.islower()])
    password += choice([x for x in chars if x.isupper()])
    password += choice([x for x in chars if x.isdigit()])
    password += ''.join(choices(chars, k = length - 3))
    password = list(password)
    shuffle(password)
    password = ''.join(password)
    return password

amount_of_passwords, length = int(input('Введите количество паролей\n')), int(input('Введите длину пароля\n'))
for pasw in range(amount_of_passwords):
    print(generate_password(length, chars))