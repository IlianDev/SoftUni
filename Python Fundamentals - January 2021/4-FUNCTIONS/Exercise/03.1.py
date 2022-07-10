def chars_in_range(a, b):
    a = ord(a)
    b = ord(b)
    for i in range(a + 1, b):
        print(chr(i), end=' ')


char_1 = input()
char_2 = input()
chars_in_range(char_1, char_2)