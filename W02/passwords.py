# This program tests the strength of passwords.
# I made it where it saves the strength 5 passwords to a file for later use.

LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

def main():
    password = ''
    while password.lower() != 'q':
        password = input('Password: ')
        strength = password_strength(password)
        print(f'Strength: {strength}')
        if strength == 5:
            save_password(password)
            print('Strong password saved')

def word_in_file(word, filename, case_sensitive):
    word_in_file = False
    with open(filename, "r",encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if case_sensitive:
                line = line.lower()
                word = word.lower()
            if line == word:
                word_in_file = True
    return word_in_file

def word_has_character(word, character_list):
    has_character = False
    for letter in word:
        for character in character_list:
            if letter == character:
                has_character = True
    return has_character

def word_complexity(word):
    word_has_lower = word_has_character(word, LOWER)
    word_has_upper = word_has_character(word, UPPER)
    word_has_digits = word_has_character(word, DIGITS)
    word_has_special = word_has_character(word, SPECIAL)
    complexity = 1
    if word_has_lower == True:
        complexity += 1
    if word_has_upper == True:
        complexity += 1
    if word_has_digits == True:
        complexity += 1
    if word_has_special == True:
        complexity += 1
    return complexity

def password_strength(password, min_length=10, strong_length=16):
    word_in_toppasswords = word_in_file(password, r'W02\toppasswords.txt', True)
    word_in_wordlist = word_in_file(password, r'W02\wordlist.txt', False)
    password_complexity = word_complexity(password)
    if word_in_toppasswords == True:
        print('Password is a commonly used password and is not secure.')
        password_complexity = 0
        return password_complexity
    if word_in_wordlist == True:
        print('Password is a dictionary word and is not secure.')
        password_complexity = 0
        return password_complexity
    if len(password) < min_length:
        print('Password is too short and is not secure.')
        password_complexity = 1
        return password_complexity
    if len(password) >= strong_length:
        print('Password is long, length trumps complexity this is a good password.')
        password_complexity = 5
        return password_complexity
    return password_complexity

def save_password(password):
    with open(r'W02\strongpasswords.txt',"a",encoding="utf-8") as file:
        file.write(password + '\n')

if __name__ == "__main__":
    main()