nim = input('Masukkan NIM      : ')
nama = input('Masukkan Nama Mhs : ')
alamat = input('Masukkan Alamat   : ')
print('')

teks = "{}|{}|{}\n".format(nim, nama, alamat)
data = open('d:\data mahasiswa.txt', 'w')
data.write(teks)
data.close()
tanya = input("Ulangi input lagi (y/n)? ")
print('')

while tanya == 'y' :
    nim2 = input('Masukkan NIM      : ')
    nama2 = input('Masukkan Nama Mhs : ')
    alamat2 = input('Masukkan Alamat   : ')
    print('')
    teks2 = "{}|{}|{}\n".format(nim2, nama2, alamat2)
    data2 = open('d:\data mahasiswa.txt', 'a')
    data2.write(teks2)
    data2.close()
    tanya = input("Ulangi input lagi (y/n)? ")
    print('')
    if tanya == 'n':
        break




