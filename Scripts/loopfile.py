import os
#create a program that asks the user for a number
#the program will write to file the STRING 'Im Counting (x)'
#replace x with the current iteration of the loop
#after the operation, display the file to the user

#example
#enter a number -> 6
#file opens
#Im Counting (0)
#Im Counting (1)

_input = raw_input('Enter a number > ') #poll and store user input
start = 1 #define start of loop
end = int(_input) #convert string to integer
path = 'loopfile.txt' #define path of text file
afile = open(path , 'w+' ) #open a file


for i in range(start, end+1): #iterate end +1
    format = str.format("Im Counting ({0})\n", i) #define format of output
    afile.write(format) #write 'format' to text file

afile.close() #close file
os.system(path) #display text file to user