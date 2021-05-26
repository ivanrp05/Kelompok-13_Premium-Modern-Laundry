#Penugasan Besar Praktikum Programa Komputer
#Daftar Anggota :
#Ivanindra Rizky P / I0320054
#Larasati Fadhilah A / I0320055
#Muhammad Ahnaf H / I0320060
#Nadiya Salma R / I0320071

#Asisten Pengampu : Muhammad Wildan Rusydani

#Fitur Program  :
# - Sistem Login
# - Menu utama
# - Pembayaran
# - Kode diskon / referal
# - Struk




#Mulai
#Pembukaan
print("-------------------------")
print("Welcome to Ronz's Premium Laundry")
print("-------------------------")
print("")
print("Silahkan masuk")
#input nama, no hp, alamat, dan tanggal
cust_name = str(input("Silahkan masukkan nama customer : "))
print("")
cust_phone = int(input("Silahkan masukkan nomer HP customer : "))
print("")
cust_address = str(input("Silahkan masukkan alamat customer : "))
print("")
date = input("Silahkan masukkan tanggal (DD-MM-YYYY) : ")

#Masuk ke opsi pemilihan layanan
print("\nSelamat datang, Tn/Ny {}".format(cust_name))
print("")
print("Silahkan pilih menu dibawah ini :")
print("")
print("[1] Laundry (include setrika) ")
print("")
print("[2] Setrika saja")
print("")
print("[3] Exit")

#Penambahan detail append untuk cart
shopping_cart = []

#Masuk kepada rumus perhitungan ongkir
#Ongkir dipatok 1 km = Rp.3000
def deliv():
    deliv = int(input("Apakah ingin menggunakan layanan delivery kami ? (1) = Ya (2) = Tidak : "))
    if deliv == 1:
        print("Layanan delivery = 3000/km")
        print("Masukkan jarak rumah anda (dalam km)")
        distance = int(input(">>> "))
        deliv_cost = distance * 3000
        print("Biaya delivery anda : Rp{}".format(deliv_cost))
    elif deliv == 2:
        print("Anda tidak menggunakan layanan delivery")

#Rumus untuk ngeprint bill
#Pake English supaya keren :)
def bills():
    print("==================================")
    print("  Ronz's Premium Laundry Bill's   ")
    print("----------------------------------")

    print("Date      : {}".format(date))
    print("Customer  : {}".format(cust_name))
    print("Phone Num : 0{}".format(cust_phone))
    print("Address   : {}".format(cust_address))
    print("----------------------------------")
    print("             Details")
    print("under maintenance...")
    print("----------------------------------")

parameter = 1

#Fungsi utama untuk menghitung biaya dan mendata laundry
while parameter == 1:
    action = int(input(">>> "))
    if action == 1:
        print("[Laundry]")
        deliv()
        #Harga standart per pcs yaitu 5000
        laundry_weight = int(input("Masukkan jumlah laundry anda (5000/pcs) : "))
        print("Jumlah laundry yang anda masukkan sebanyak {} pcs".format(laundry_weight))
        #Dikasih detail jenis pakaian agar mendapatkan perlakuan khusus
        print("Apakah ada pakaian yang butuh perlakuan khusus? Yes (1) No (2)")
        note = int(input(">>> "))
        if note==1:
            print("under maintenance...")
        elif note==2:
            print("under maintenance...")
        else:
            print("404 not found")

        #Fungsi untuk ngeprint bill masing" layanan
        bills()
    if action == 2:
        print("[Setrika]")
        deliv()

        #for printing bills
        bills()
    if action == 3:
        print("--------------------------------")
        print("\nThanks for using this program!")
        parameter=0


#Note : Pemrograman ini belum lengkap
#Selesai
