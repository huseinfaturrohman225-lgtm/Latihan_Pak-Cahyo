#contoh 1 
x = 3
if (x%2)==1:
    print("Bilangan Ganjil")

#contoh 2
x = 3
if (x%2)==1:
    print("Bilangan Ganjil")
if x==3:
    print("Angka Tiga")

#if elif else
x = float(input("masukkan angka:"))
if (float(x) .is_integer())!=True:
    print("bukan bilangan bulat")
elif (x%2)==1:
    print("bilangan ganjil")
else:
    print("bilangan genap")

#if,and
x = 3
if ((x%2)==1) and (x==3) :
    print("x adalah bilangan ganjil")

#if,or
x = 3
if ((x%2)==1) or (x==3):
    print("x adalah bilangan ganjil")

#if,elif,else
x = 10
if ((x%2)==1):
    if (x>10):
        print("x diatas 10")
elif (x==3):
    print("x adalah 3")
else:
    print("x dibawah 10")

#mengetahui bilangan ganjil dan genap
x= int(input("masukkan x:"))
print(("bilangan genap", "bilangan ganjil")[((x%2)==1)])