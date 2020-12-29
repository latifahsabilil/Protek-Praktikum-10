f_lama = open('d:/file.txt', 'r') 
f_baru = open('d:\Hasil No 5.txt', 'w')
data = f_lama.readlines()

for i in range(len(data)):
    angka = data[i]
    a, b = angka.split('|')
    c = int(a)
    d = int(b)
    hitung = c + d
    total = str(hitung)
    f_baru.write(total)
    f_baru.write('\n')
f_baru.close()
tujuan = open('d:\Hasil No 5.txt', 'r')
tujuan.read()
tujuan.close()
