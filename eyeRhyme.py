#Version : 2
def eyeRhyme2(pairOfLines):
    word1,word2 = pairOfLines.split("\t")
    return word1[-3:0] == word2[-3:0]
# Version : 1
def eyeRhyme(pairOfLines):
    word_1 = pairOfLines.split("\t")[0]
    word_2 = pairOfLines.split("\t")[1]
    len_1 = len(word_1)
    len_2 = len(word_2)
    last_three_1 =  word_1[( len_1-3 )] + word_1[(len_1 - 2)] + word_1[(len_1 - 1)]
    last_three_2 = word_2[(len_2 - 3)] + word_2[(len_2 - 2)] + word_2[(len_2 - 1)]

    return last_three_1 == last_three_2
print(eyeRhyme("cough\tbough"))
