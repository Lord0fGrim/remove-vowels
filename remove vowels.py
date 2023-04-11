#Write a program that takes a string as input and removes all the vowels from it.

def split(word):
    return list(word)

x = input("Your word: ")

list_x = split(x)
vowels = ["a","e","i","o","u"]
new_list = []

for i in list_x:
    if i not in vowels:
        new_list.append(i)
        
y = ''.join(new_list)

print(y)
        