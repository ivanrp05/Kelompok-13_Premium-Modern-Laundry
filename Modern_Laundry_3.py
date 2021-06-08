import os

#Mulai
def opening():
    print("=========================")
    print("Welcome to Ronz's Premium Laundry")
    print("Jl. Doang Jadian Kaga No.666 - Surakarta")
    print("Telepon : 0821 - 3640 - 3111 ")
    print("-------------------------")

#opening
opening()

#input nama, no hp, alamat, dan tanggal
cust_name = str(input("Silahkan masukkan nama customer : "))
cust_phone = int(input("Silahkan masukkan nomer HP customer : "))
cust_address = str(input("Silahkan masukkan alamat customer : "))
date = input("Silahkan masukkan tanggal (dd-mm-yyyy) : ")

#Masuk ke opsi pemilihan layanan
print("==========================================")
print("Selamat datang, Tn/Ny {}".format(cust_name))
print("------------------------------------------")
print("|        Harga laundry = 4000/kg         |")
print("------------------------------------------")
print("Silahkan pilih menu dibawah ini :")
print("[1] Laundry + Setrika ")
print("[2] Setrika ")
print("[3] Exit")

def menus():
    print("Silahkan pilih menu dibawah ini :")
    print("[1] Laundry + Setrika ")
    print("[2] Setrika ")
    print("[3] Exit")

#Penambahan detail append untuk cart
shopping_cart = []

#Masuk kepada rumus perhitungan ongkir
#Ongkir dipatok 1 km = Rp.3000
def deliv():
    print("------------------------------------------")
    print("Apakah anda ingin menggunakan layanan delivery kami ? Ya (1) Tidak (2) ")
    deliv = int(input(">>> "))
    if deliv == 1:
        print("------------------------------------------")
        print("[LAYANAN DELIVERY]")
        print("Masukkan jarak rumah anda (3000/km)")
        distance = int(input(">>> "))
        deliv_cost = distance * 3000
        print("Biaya delivery anda : Rp{}".format(deliv_cost))
        shopping_cart.append("Delivery     ({} km)\tRp{}".format(distance,deliv_cost))
    elif deliv == 2:
        print("Anda tidak menggunakan layanan delivery")
    else:
        print("Perintah yang anda masukkan salah, ulangi lagi.")

#Rumus untuk ngeprint bill
#Pake English supaya keren :)
def bills():
    print("==================================")
    print("  Ronz's Premium Laundry Bill's   ")
    print("Jl. Doang Jadian Kaga No.12 - Semarang")
    print("    Telepon : 0857-9875-1234")
    print("----------------------------------")

    print("Date      : {}".format(date))
    print("Customer  : {}".format(cust_name))
    print("Phone Num : 0{}".format(cust_phone))
    print("Address   : {}".format(cust_address))
    print("----------------------------------")
    print("             Details")
    show_cart()
    #price_last()
    print("----------------------------------")

#function for count laundry based on by weight
def laundry_kg():
    weight_count = int(input("Masukkan berat laundry anda (Laundy + Setrika = Rp5.000/kg) : "))
    weight_price = weight_count * 5000
    print("{} kg = Rp{},".format(weight_count, weight_price))
    shopping_cart.append("Laundry     ({} kg)\tRp{}".format(weight_count,weight_price))

def setrika_kg():
    s_weight_count = int(input("Masukkan berat laundry anda (Setrika saja = Rp3.000/kg) : "))
    s_weight_price = s_weight_count * 3000
    print("{} kg = Rp{},".format(s_weight_count, s_weight_price))
    shopping_cart.append("Setrika     ({} kg)\tRp{}".format(s_weight_count,s_weight_price))

#function for special service = pakaian yang butuh perlakuan khusus
def special_serv():
    print("Apakah ada pakaian yang butuh perlakuan khusus? Yes (1) No (2)")
    serv = int(input(">>> "))

    if serv == 1:
        print("Masukkan jenis yang butuh perlakuan khusus")
    elif serv == 2:
        print("Tidak ada yang membutuhkan perlakuan khusus")
    else:
        print("Perintah yang anda masukkan salah, ulangi lagi.")

def show_cart():
    if len(shopping_cart) <= 0:
        print("Belum ada laundry")
    else:
        for cart in shopping_cart:
            print(cart)

def laundry_voucher():
    print("Apakah anda memiliki kode Voucher ? Ya (1) Tidak (2)")
    voucher_act = int(input(">>> "))

    if voucher_act == 1:
        voucher = input("Masukkan kode Voucher anda : ")
        if voucher == 'RONZLEBARAN':
            cost = total_price * 0.20
        else :
            print("Kode yang anda masukkan salah!")

#def price_last(new_price):
#    new_price += new_price

parameter = 1

#Fungsi utama untuk menghitung biaya dan mendata laundry
while parameter == 1:
    action = int(input(">>> "))
    if action == 1:
        print("------------------------------------------")
        print("[Laundry + Setrika]")
        laundry_kg()
        #delivery
        deliv()
        print("------------------------------------------")
        #Fungsi untuk ngeprint bill masing" layanan
        bills()
        print("Apakah ada jasa yang ingin digunakan lagi ? (1) Ya (2) Tidak")
        exit1 = int(input(">>> "))
        if exit1 == 1:
            menus()
        elif exit1 == 2:
            print("Terimakasih sudah laundry!")
            parameter = 2
        else:
            print("Perintah kamu salah!")

    if action == 2:
        print("------------------------------------------")
        print("[Setrika]")
        setrika_kg()
        deliv()
        bills()
        #for printing bills
        print("Apakah ada jasa yang ingin digunakan lagi ? (1) Ya (2) Tidak")
        exit1 = int(input(">>> "))
        if exit1 == 1:
            menus()
        elif exit1 == 2:
            print("Terimakasih sudah laundry!")
            parameter = 2
        else:
            print("Perintah kamu salah!")
    if action == 3:
        print("--------------------------------")
        print("\nThanks for using this program!")
        parameter=0

    #Note, program ini belum sepenuhnya selesai. Dimohon bersaba karena orang sabar disayang tuhan :D