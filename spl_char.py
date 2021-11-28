def special_character():
    spl_char='[@!#$%^&*()_?{}<>~:;\|]'
    string=input('Enter string: ')
    x=[]
    for i in string:
        if i not in spl_char:
            continue
        else:
            x.append(i)
    return "special char {} found in given string are: ",x
print(special_character())