a = input("Első szám: ")
b = input("Második szám: ")

a = int(a) # átalakítjuk(castoljuk) a értékét egész számra, mert az input értékei stringek
b = int(b)

sum = a + b

print("Az összeg: " + str(sum)) # castolás stringre. ez azért lehet szükséges, mert stringet csak stringel lehet összefűzni
