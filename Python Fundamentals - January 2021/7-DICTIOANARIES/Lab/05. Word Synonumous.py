n = int(input())

synonyms_dict = {}

for x in range(n):
    word = input()
    synonym = input()
    if word not in synonyms_dict:
        synonyms_dict[word] = []
    synonyms_dict[word].append(synonym)

for key, values in synonyms_dict.items():
    print(f"{key} - {', '.join(values)}")

"""
    INPUT: 
3
cute
adorable
cute
charming
smart
clever
    OUTPUT:
cute - adorable, charming
smart - clever


2
task
problem
task
assignment

task – problem, assignment

"""
