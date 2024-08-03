def count(a):
    words=a.split()
    word_count={}
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
             word_count[word]=1
    return word_count

a="count the occurence of each word in of a given sentence"

obj=count(a)
print(obj)