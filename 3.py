bukafile = open('d:\data mahasiswa.txt', 'r')
data = bukafile.readlines()

dataMahasiswa = {}
listMhs = []
for i in range(len(data)):
    mahasiswa = data[i].split('|')
    mahasiswa[2] = mahasiswa[2].replace('\n', '')
    
    dMhs = {'nim' : mahasiswa[0], 'nama' : mahasiswa[1], 'alamat' : mahasiswa[2]}
    dataMahasiswa = dMhs

    listMhs.append(dataMahasiswa)

print(listMhs)
bukafile.close()
