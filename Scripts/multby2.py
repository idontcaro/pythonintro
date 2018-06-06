#create a program that asks the user to input a number
#output to the CONSOLE the number multiplied by two (2)

#QUICK REFERENCE TYPES
#string type = '' or "" Example -> 'HI WORLD' or "HELLO WORLD"
#int type = 1234
#float type = 1.0f
#bool type = true or false
# aString = 'String'
# aInt = 1234
# aFloat = 1.0
# aBool = false


_input = raw_input('enter a number -> ') #poll and store user input
convert = int(_input) #convert string to integer
print convert * 2 #multiply integer by two (2)