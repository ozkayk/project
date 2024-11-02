meme sözlüğü:
meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in meme_dict.keys():
    print(word + ":"+ meme_dict[word])
else:
    print("sözcükte böyle bir kelime yok")


rastgele seçme:
import random
sevdiklerim = ['oyun oynamak', 'uyumak']
print(random.choice(sevdiklerim))
#print(liste[random.randint(0, 1)])
