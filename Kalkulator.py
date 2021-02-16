import pyfiglet
import os

s =pyfiglet.figlet_format("Kalkulator")
print(s)
print('Script Kalkulator By: Luck Voltia\nDibuat : Selasa 16 Februari 2020')
print('------------------------------------------------')


def bagi():
	os.system("clear")
	print(s)
	a1=int(input("Masukan Angka Pertama: "))
	a2=int(input("Masukan Angka Kedua: "))
	y2=input("Mau Nambah 1 Bilangan Lagi(y/n): ")
	if(y2 == "y"):
		a3=(int(input("Masukan Angka Ketiga: ")))
		print("===========================")
		print("Hasil Nya Adalah : ",a1/a2/a3,"||")
		print("===========================")
	else:
		print("======================================================")
		print("Hasil Pembagian Kedua Angka Yang anda masukan: ",a1/a2,"||")
		print("======================================================")
		
def kali():
	os.system("clear")
	print(s)
	a1=int(input("Masukan Angka Pertama: "))
	a2=int(input("Masukan Angka Kedua: "))
	y2=input("Mau Nambah 1 Bilangan Lagi(y/n): ")
	if(y2 == "y"):
		a3=(int(input("Masukan Angka Ketiga: ")))
		print("===========================")
		print("Hasil Nya Adalah : ",a1*a2*a3,"||")
		print("===========================")
	else:
		print("======================================================")
		print("Hasil Perkalian Kedua Angka Yang anda masukan: ",a1*a2,"||")
		print("======================================================")
		
def kurang():
	os.system("clear")
	print(s)
	a1=int(input("Masukan Angka Pertama: "))
	a2=int(input("Masukan Angka Kedua: "))
	y2=input("Mau Nambah 1 Bilangan Lagi(y/n): ")
	if(y2 == "y"):
		a3=(int(input("Masukan Angka Ketiga: ")))
		print("===========================")
		print("Hasil Nya Adalah : ",a1-a2-a3,"||")
		print("===========================")
	else:
		print("====================================================")
		print("Hasil Perkalian Kedua Angka Yang anda masukan: ",a1-a2,"||")
		print("====================================================")
		
def tambah():
	os.system("clear")
	print(s)
	a1=int(input("Masukan Angka Pertama: "))
	a2=int(input("Masukan Angka Kedua: "))
	y2=input("Mau Nambah 1 Bilangan Lagi(y/n): ")
	if(y2 == "y"):
		a3=(int(input("Masukan Angka Ketiga: ")))
		print("===========================")
		print("Hasil Nya Adalah : ",a1+a2+a3,"||")
		print("===========================")
	else:
		print("====================================================")
		print("Hasil Perkalian Kedua Angka Yang anda masukan: ",a1+a2,"||")
		print("====================================================")
		
		
def ganda():
		b1=int(input("Mau Angka Berapa yang di gandakan: "))
		b2=int(input("Mau Gandakan Berapa Kali: "))
		print(b1**b2)	
def menu():
	print("[1]Pembagian")
	print("[2]Perkalian")
	print("[3]Perkurangan")
	print("[4]Pertambahan")
	print("[5]Melipat Gandakan Angka")
	print("[6]Exit")
	y = input("Apa Yang Akan Anda Lakukan : ")
	if(y=="1"):
		os.system("clear")
		bagi()
	if(y=="2"):
		os.system("clear")
		kali()
	if(y=="3"):
		os.system("clear")
		kurang()
	if(y=="4"):
		tambah()
	
	if(y=="5"):
		ganda()

	if(y=="6"):
		os.system("clear")
		terima=pyfiglet.figlet_format("TERIMA KASIH")
		print(terima)
menu()	

		
while(True):
	ulang=str(input("Mau Melakukan Perhitungan Lagi (y/n): "))
	if(ulang == "y"):
		menu()
	else:
		os.system("clear")os.system("clear")
		terima=pyfiglet.figlet_format("TERIMA KASIH")
		print(terima)
menu()
		terima=pyfiglet.figlet_format("TERIMA KASIH")
		print(terima)
menu()
