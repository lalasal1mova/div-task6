def count_words(text):
    words = text.lower().split(" ")
    d = {}
    
    for i in words:
        count = 0
        for j in range(len(words)):
            if i == words[j]:
                count += 1

        d[i] = count
        

    return d

text = str(input("Enter a text: "))
print(count_words(text))
