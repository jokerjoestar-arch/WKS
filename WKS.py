import wikipedia as wp

languaje = open('languaje.txt', 'r')
lang = languaje.read()
wp.set_lang(lang)

search=input("\n$")

rese=wp.search(search, results=3)
resu=wp.summary(search)

print("\n")
print(rese)
print(resu)
