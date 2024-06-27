letter = ''' dear (name)
you are selected 
(date)'''
a = input("enter your name ")
b = input("eneter date ")
letter.capitalize()
letter = letter.replace("(name)" , a)
letter = letter.replace("(date)" , b)
print(letter)
