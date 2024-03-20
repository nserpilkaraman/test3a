#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

boy = float(input("Boyunuzu giriniz (x.xx formatında): "))
kilo = float(input("Kilonuzu giriniz: "))

sonuc = kilo/(boy*boy)
print("Vücut kitle endeksininz "+ str(sonuc))

#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
 
maas = float(input("Maaşınızı giriniz : "))
zamOranı = float(input("Zam oranını(%) giriniz : "))

yeniMaas = maas + (maas * zamOranı/100)
print("Zamlı maaş: " + str(yeniMaas))


#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.

sayi1 = float (input("Birinci sayıyı giriniz: "))
sayi2 = float (input("İkinci sayıyı giriniz: "))
sayi3 = float (input("Üçüncü sayıyı giriniz: "))

if(sayi1 >= sayi2) and (sayi1 >= sayi3):
    enBuyuk = sayi1
elif(sayi2 >=sayi1 ) and (sayi2 >= sayi3):
    enBuyuk =sayi2
else:
    enBuyuk = sayi3

print("En büyük sayı: ", enBuyuk)

#4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)

r=float(input("Yarıçapı giriniz: "))
pi = 3.14
cevre = 2 * pi * r
alan = 3.14 * r * r

print("Çevre: ", cevre)
print("Alan: ",alan)

#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.

number = input("Bir sayı giriniz")
reverse = number[::-1]
if number == reverse:
    print("Sayınız palindromdur")
else:
    print("Sayınız palindrom değildir")