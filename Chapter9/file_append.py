str = "\nHey Jilesh, you are amazing!"

f = open("myFile.txt", "a")    #Add "a" for open file in append mode, i.e., to add anything to the file
f.write(str)
f.close()