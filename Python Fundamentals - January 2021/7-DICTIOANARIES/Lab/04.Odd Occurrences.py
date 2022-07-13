words = input().split()
my_dict = {}

for i in words:
    word_lower = i.lower()
    if word_lower not in my_dict:
        my_dict[word_lower] = 0
    my_dict[word_lower] += 1

for key, value in my_dict.items():
    if value % 2 == 1:
        print(key, end=' ')

"""
Java C# PHP PHP JAVA C java -> java c# c
3 5 5 hi pi HO Hi 5 ho 3 hi pi -> 5 hi
a a A SQL xx a xx a A a XX c -> a sql xx c
"""