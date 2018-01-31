##A program designed to count lines, words, and characters in a text file 
##Created by Arij Saleem

import Tkinter
import tkFileDialog

print "This program counts the number of lines, words, and characters in a text file. You may select any .txt file."
raw_input("Press enter to continue:")
print '\n'

Tkinter.Tk().withdraw() # Close the root window
in_path = tkFileDialog.askopenfilename()

#line counter
infile = open(in_path, 'r')
data = infile.readlines()
lines = len(data)
print "Lines: " + str(lines)

#word counter
words = []
for i in range(lines):
    words = words + (data[i].split(' '))
print "Words:", len(words)

#character counter
characters = []
for i in range(len(words)):
    characters.append(words[i].strip('\n'))

counter = 0
for i in range(len(characters)):
    counter = counter + len(characters[i])
print "Characters:", counter






    


    



