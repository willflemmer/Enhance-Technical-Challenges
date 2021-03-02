def checker(first_word, second_word):
    first_list = sorted(first_word)
    second_list = sorted(second_word)
    if first_list == second_list:
        return True
    else:
        return False

result = checker('trianlge', 'integral')
print(result)