operator = str (input('pilih operator "penambahan", "Pengurangan", "Perkalian", "Pembagian": '))
number1 = int (input("masukan angka pertama: "))
number2 = int (input("masukan angka kedua: "))

if operator == 'penambahan' :
	res = number1 + number2
elif operator == 'penambahan' :
	res = number1 - number2
elif operator == 'penambahan' :
	res = number1 * number2
elif operator == 'penambahan' :
	res = number1 / number2
	
print(f'{operator} dari {number1} dan {number2} adalah {res}' )
