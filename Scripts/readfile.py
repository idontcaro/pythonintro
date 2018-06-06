afile = open('file.txt', 'w+') #open file
afile.write('some stuff') #write to file
afile.close() #close file

afile = open('file.txt', 'r') #reopen closed file
stuff = afile.readline() #read from file
print stuff #printing to console
afile.close() #close file again