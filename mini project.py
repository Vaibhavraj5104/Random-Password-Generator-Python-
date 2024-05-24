

# import random as ra
# import string as st

# n = int(input("Length of Password: "))

# def generate_password(length):
#     specific_punctuation = '!@#$%^&*'
#     allchar_list = st.ascii_letters + st.digits + specific_punctuation
#     password = "".join([ra.choice(allchar_list) for _ in range(length)])
#     print("Your", length, "character password is:", password)

# generate_password(n)

# def reverse_words_order_and_swap_cases(sentence):
#     word = []
#     for char in sentence:
#         word.append(char)
#     word.reverse()
#     new_sentence = ""
#     for val in word:
#         new_sentence += val
#     return new_sentence
# print(reverse_words_order_and_swap_cases("ABCDE"))
sentence = "awesome is coding"
words = sentence.split()
    
reversed_words = words[::-1]
print(reversed_words)