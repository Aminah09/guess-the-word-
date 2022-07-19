import string

def list_length(list, length):
    """
    cuts the length of alphabet list into sets of lists equal to the length of word
    """
    newlist= list
    listlen = len(newlist)//length
    nlist = []

    for i in range(listlen):
        l = newlist[:length]
        del newlist[:length]
        nlist.append(l)
    nlist.append(newlist)
    return nlist


def word_guesser(list,n):
    """
    """
    return list[n]


def main():
    """
    The main function
    """
    alphabets = list(string.ascii_lowercase)
    word_length = int(input("How many letters are there in your word? : "))

    alist = list_length( alphabets, word_length)

    print (alist )

    nlist = []
    for i in range(word_length):
        word_group=int(input("\n" + "Which group is the letter " + str(i+1) + " of your guess (count starts from 1): "))-1
        nlist.append(alist[word_group])
    for i in range(len(nlist)):
        print (" | ".join(nlist[i]))
    word=[]
    for i in range(word_length):
        index = int(input("\n" + "Which column is the letter " + str(i+1) + " of your guess (count starts from 1): "))
        word.append(word_guesser(nlist[i],index-1))
    print ("\nThe word you guessed is " + ''.join(word) + " !")

main()

