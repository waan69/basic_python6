#melihat daftar kontak
def daftar_kontak():
    file = open("kontak.txt", "a+")
    file.seek(0)
    text = file.read()
    print(text)
#menambah kontak
def tambah_kontak(text):
    file = open("kontak.txt", "a+")
    file.write("\n" + text)
    
def tanya_pengguna():
    tambah_kontak(input("Masukan Nama: "))
    tambah_kontak(input("Masukan Telepon: "))
    print("")
    print("Kontak Berhasil Ditambahkan")
    
loop = True

print("Selamat Datang!")
print("")
print("==================== Menu ====================")
print("1. Daftar Kontak")
print("2. Tambah Kontak")
print("3. Keluar")
while (loop):
    print('/n')
    menu = input("Pilih Menu: ")

    if menu == "1":
         daftar_kontak()
    elif menu == "2":
         tanya_pengguna()

    elif menu == "3":
        print("Program Selesai, Sampai jumpa!")
        quit()
    else: 
        print("Menu tidak tersedia")


