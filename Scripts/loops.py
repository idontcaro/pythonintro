#print to the console the STRING 'Hello Python' 6 times using a 'for' loop
#for num in range(0 , 6): # iterate 6 times
#   print "Hello Python" #print to console

#write to a file the string 'Hello Python' 6 times using a 'for' loop
afile = open('loop.txt', 'w+') #open a file
for num in range(0 , 6): #iterate 6 times
    afile.write("Hello Python \n") #write to text file
afile.close()   #close file