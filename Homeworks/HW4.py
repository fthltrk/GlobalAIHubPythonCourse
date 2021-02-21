import random

print("!! İyi Şanslar !!\n")
words = ['globalaihub', 'ödev', 'kodlama', 'fuatbeşer', 
		'ezgisubaşı', 'kutayakalın', 'python', 'öğrenmek', 
		'proje', '', 'ömercengiz', 'yapayzeka'] 

word = random.choice(words)
print("Harf tahmini yap!!")
tahmin = ''
tryy = 10

while tryy > 0:
	fail = 0
	for char in word: 
		if char in tahmin: 
			print(char)
		else: 
			print("_")
			fail += 1
			
	if fail == 0:
		print("***Kazandın***") 
		print("Bulduğun kelime: ", word) 
		break
	guess = input("Harf tahmininiz:")
	tahmin += guess 
	if guess not in word:
		tryy -= 1
		print("Yanlış Tahmin!!")
		print("Son", + tryy, 'tahminin kaldı.')
		if tryy == 0:
			print("*!*Kaybettin*!*")