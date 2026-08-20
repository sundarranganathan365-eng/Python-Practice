def show_doc():
    file = open("article.txt","r")
    data = file.read()
    print(data)
    file.close()

    
def total_chara():
    file = open("article.txt","r")
    data = file.read()
 
    count=len(data)
    print(count)
    file.close()

def total_words():
    file = open("article.txt","r")
    data = file.read()
    words =data.split()
    count=len(words)
    print(count)
    file.close()

def count_words():
    count = 0
    user = input('Enter : ')
    found = False
    file = open("article.txt","r")
    data = file.read()
    words =data.split()
    for word in words:
        if user == word:
            count=1+count
            found=True
    print("Found",count,"times")
    if not found:
        print('Word Not Found ')
    file.close()


def long_word():
    file = open("article.txt","r")
    data = file.read()
    words =data.split()
    longest = ""

    for word in words :
        if len(word) > len(longest):
            longest = word

    print(longest)
    file.close()

def short_word():
    file = open("article.txt","r")
    data = file.read()
    words =data.split()
    longest = ""

    for word in words :
        if len(word) < len(longest):
            longest = word
            pass
     
        if len(word)<len(longest):
            longest = word

    print(longest)
    file.close()

def len_avg_word():
    file = open("article.txt","r")
    data = file.read()
    word = data.strip()
    len_word = len(word)
    words =data.split()
    count_avg = 0
    for word in words :
        count_avg = count_avg + len_word
    len_avg = count_avg/len(words)
    print(len_avg)
    file.close()




# show_doc()
# total_chara()
# total_words()      
#  count_words()
# long_word()
len_avg_word()