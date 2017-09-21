#File splits data into encoder and decoder data to be fed into seq2seq model

period = "."
exclamation = "!"
question = "?"

file = open("C:/Users/akash/Downloads/Chatbot - Copy/data/movieScript.txt", "r")
entireScript = file.read()
file1 = open("C:/Users/akash/Downloads/Chatbot - Copy/data/trainenc.txt", "w")
file2 = open("C:/Users/akash/Downloads/Chatbot - Copy/data/traindec.txt", "w")
i = 0

while i < len(entireScript):
    currLine1 = ""
    while (entireScript[i] != period) and (entireScript[i] != exclamation) and (entireScript[i] != question) and i < len(entireScript):
        currLine1 += entireScript[i]
        i += 1
    currLine1 += entireScript[i]
    i += 1
    file1.write(currLine1)

    currLine2 = ""
    if i >= len(entireScript):
        break
    while (entireScript[i] != period) and (entireScript[i] != exclamation) and (entireScript[i] != question) and i < len(entireScript):
        currLine2 += entireScript[i]
        i += 1
    currLine2 += entireScript[i]
    i += 1
    file2.write(currLine2)
file1.close()
file2.close()
file.close()

#File splits data into encoder and decoder data to be fed into seq2seq model

period = "."
exclamation = "!"
question = "?"

file = open("C:/Users/akash/Downloads/Chatbot - Copy/data/testMovieScript.txt", "r")
entireScript = file.read()
file1 = open("C:/Users/akash/Downloads/Chatbot - Copy/data/testenc.txt", "w")
file2 = open("C:/Users/akash/Downloads/Chatbot - Copy/data/testdec.txt", "w")
i = 0

while i < len(entireScript):
    currLine1 = ""
    while (entireScript[i] != period) and (entireScript[i] != exclamation) and (entireScript[i] != question) and i < len(entireScript):
        currLine1 += entireScript[i]
        i += 1
    currLine1 += entireScript[i]
    i += 1
    file1.write(currLine1)

    currLine2 = ""
    if i >= len(entireScript):
        break
    while (entireScript[i] != period) and (entireScript[i] != exclamation) and (entireScript[i] != question) and i < len(entireScript):
        currLine2 += entireScript[i]
        i += 1
    currLine2 += entireScript[i]
    i += 1
    file2.write(currLine2)
file1.close()
file2.close()
file.close()