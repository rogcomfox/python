#Array Biologi
Biologi = []

#Fungsi Tampil Data
def data_tampil():
    if len(Biologi) <= 0:
        print("Data Kosong")
    else:
        for no in range(len(Biologi)):
            print ("[%d] %s" % (no, Biologi[no]))

def insert_data():
    nama = input("Masukkan Nama: ")
    

print("Database Biologi")
print("1. Input Data")
print("2. Menampilkan Data")
print(" 1. Berdasarkan Famili")
print(" 2. Berdasarkan Genus")
print("3. Edit Data")
pilihan = int(input("Masukkan Pilihan: "))
if pilihan == 1:
    Nama = input("Masukkan Nama Tumbuhan: ")
    Genus = input("Masukkan Genus: ")
    Famili = input("Masukkan Famili: ") 
if pilihan == 2:
    data_tampil()
if pilihan == 3:
    print("OK")
else:
    print("Masukkan Salah")