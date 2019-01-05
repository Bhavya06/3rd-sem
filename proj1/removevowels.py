vowel = ('a','e','i','o','u')
sent = input("Enter any sentence")
newsent = ""
for i in sent:
    if i not in vowel:
        newsent = newsent + i

print(newsent)