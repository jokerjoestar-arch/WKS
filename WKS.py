import wikipedia as wp

#languaje def:
wp.set_lang("en")

search=input("$")

rese=wp.search(search, results=3)
resu=wp.summary(search)

print(rese)
print(resu)
