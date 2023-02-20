# write_file.py

# open fil using "w" mode
file = open("mynote.txt", "w")
text1 = "Python is a programming languange\n"
file.write(text1)
file.write("Python is easy to learn")
file.close()

# these commands will creata a new file
# and write content in it
file2 = open("newnote.txt", "w")
file2.write("My Goals\n")
file2.write("========")
file2.close()

# these command will replace all contents in mynote.txt file
file2 = open("mynote.txt", "w")
file2.write("Okay")
file2.close()