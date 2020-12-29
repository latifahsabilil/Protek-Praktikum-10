isi_nim = input('Masukkan nama yang dicari: ')

bukafile = open('d:\data mahasiswa.txt', 'r')
data = bukafile.readlines()
for i in range(len(data)):
    mahasiswa = data[i]
    nim, nama, alamat = mahasiswa.split('|')
    if isi_nim == nim :
        print('Data Mahasiswa')
        print('NIM    : ', nim, '\nNama   : ', nama,'\nAlamat : ', alamat)
        break
    else :
        break
if isi_nim not in nim:
    print('Data mahasiswa tidak ditemukan')
