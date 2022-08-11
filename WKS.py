import wikipedia as wp



ruta = 'languaje.txt'
lang = open(ruta, 'r')
#languaje def:
wp.set_lang(lang.read())

search=input("$")

rese=wp.search(search, results=3)
resu=wp.summary(search)

print(rese)
print(resu)
