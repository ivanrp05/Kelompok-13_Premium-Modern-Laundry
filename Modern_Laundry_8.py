
import os #import os
import datetime #import library realtime
import csv #import library csv
#Bismillah ga revisi
#Mulai
#function for opening title
def opening():
    print("=========================")
    print("Welcome to Ronz's Premium Laundry")
    print("Jl. Doang Jadian Kaga No.12 - Surakarta")
    print("Telepon : 0857-6567-0269")
    print("'Kami selalu menuruti keinginan pelanggan meskipun keinginannya aneh aneh.'")
    print("-------------------------")

#function for printing menus
def menus():
    print("Silahkan pilih menu dibawah ini :")
    print("[1] Laundry + Setrika ")
    print("[2] Setrika ")
    print("[3] Exit")

#Penambahan detail append untuk cart
shopping_cart = []
laundry = []
delivery = []
setrika = []
price =[]

#call datetime function
datetime_laundry = datetime.datetime.now()

#function for delivery
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
        delivery.append("{} km".format(distance))
        price.append(deliv_cost)
    elif deliv == 2:
        print("Anda tidak menggunakan layanan delivery")
        delivery.append("-")
    else:
        print("Perintah yang anda masukkan salah, ulangi lagi.")


#function for printing bills
def bills():
    print("-\n-\n-\nmencetak nota\n-\n-\n-")
    print("==================================")
    print("   Ronz's Premium Laundry Bill's   ")
    print("Jl. Doang Jadian Kaga No.12 - Surakarta")
    print("    Telepon : 0857-9875-1234")
    print("----------------------------------")

    print("Tanggal   :",datetime_laundry)
    print("Pelanggan : {}".format(cust_name))
    print("No.HP     : {}".format(cust_phone))
    print("Alamat    : {}".format(cust_address))
    print("----------------------------------")
    print("             Detail\n")
    show_cart()
    print("\n          Total Harga : Rp{}".format(sum(price)))
    print("----------------------------------")


#function for count laundry by
def laundry_kg():
    weight_count = int(input("Masukkan berat laundry anda (Laundy + Setrika = Rp5.000/kg) : "))
    weight_price = weight_count * 5000
    print("{} kg = Rp{},".format(weight_count, weight_price))
    shopping_cart.append("Laundry     ({} kg)\tRp{}".format(weight_count,weight_price))
    laundry.append("{} kg".format(weight_count))
    price.append(weight_price)

#function for count setrika
def setrika_kg():
    s_weight_count = int(input("Masukkan berat laundry anda (Setrika saja = Rp3.000/kg) : "))
    s_weight_price = s_weight_count * 3000
    print("{} kg = Rp{},".format(s_weight_count, s_weight_price))
    shopping_cart.append("Setrika     ({} kg)\tRp{}".format(s_weight_count,s_weight_price))
    setrika.append("{} kg".format(s_weight_count))
    price.append(s_weight_price)

def show_cart():
    if len(shopping_cart) <= 0:
        print("Belum ada laundry")
    else:
        for cart in shopping_cart:
            print(cart)


def laundry_voucher():
    loop = 1

    global hasil, diskon
    while loop == 1:
        print("Apakah anda memiliki kode Voucher ? Ya (1) Tidak (2)")
        voucher_act = int(input(">>> "))
    
        if voucher_act == 1:
            voucher = input("Masukkan kode Voucher anda : ")
            if voucher == 'EKONOMI':
                diskon = 5000
                hasil = sum(price) - diskon
                break
            if voucher == 'MasWildanTerbaik':
                diskon = 15000
                hasil = sum(price) - diskon
                break
            if voucher == 'JuaraCuci':
                diskon = 3000
                hasil = sum(price) - diskon
                break
            if voucher == 'RonzSelaludiDepan':
                diskon = 7000
                hasil = sum(price) - diskon
                break 
            else :
                print("Kode yang anda masukkan salah!")
                break
        if voucher_act == 2:
            bills()
        else:
            print("Masukkan perintah dengan benar!")

def payment_method():
    global act

    payment = 1
    
    while payment == 1:
        print("[METODE PEMBAYARAN]\n")
        print("1. Tunai\n")
        print("2. Transfer\n")
        print("3. Debit/Kredit\n")
        print("4. Dana\n")
        print("5. Ovo\n")
        print("6. Apple Pay\n")
        print("7. Samsung Pay\n")
        print("\n\nPilih metode pembayaran")
        pilihan = int(input(">>> "))

        if pilihan == 1:
            metode = 'Tunai'
            break
        elif pilihan == 2:
            metode = 'Transfer'
            act = 'Segera transfer ke No.Rek 125125151 A/N Ipul'
            print(metode)
            break
        elif pilihan == 3:
            metode = 'Debit/Kredit'
            act = 'Silahkan berikan kartu anda!'
            print(metode)
            break
        elif pilihan == 4:
            metode = 'Dana'
            act = 'Silahkan scan/tap barcode ini!'
            print(metode)
            break
        elif pilihan == 5:
            metode = 'Ovo'
            act = 'Segera lakukan pembayaran ke 0857-9875-1234'
            print(metode)
            break
        elif pilihan == 6:
            metode = 'Apple Pay'
            act = 'Silahkan scan/tap barcode ini!'
            print(metode)
            break
        elif pilihan == 7:
            metode = 'Samsung Pay'
            act = 'Silahkan scan/tap barcode ini!'
            print(metode)
            break
        else:
            print("Masukkan perintah dengan benar!")


#after voucher
def after_bills():
    print("-\n-\n-\nmencetak nota\n-\n-\n-")
    print("==================================")
    print("   Ronz's Premium Laundry Bill's   ")
    print("Jl. Doang Jadian Kaga No.12 - Semarang")
    print("    Telepon : 0857-9875-1234")
    print("----------------------------------")

    print("Tanggal   :",datetime_laundry)
    print("Pelanggan : {}".format(cust_name))
    print("No.HP     : {}".format(cust_phone))
    print("Alamat    : {}".format(cust_address))
    print("----------------------------------")
    print("             Detail\n")
    show_cart()
    print("\n          Total Harga : Rp{}".format(sum(price)))
    print("\n               Diskon : Rp{}".format(diskon))
    print("          Harga Bayar : Rp{}".format(hasil))
    print("----------------------------------")
    print("----------------------------------")

parameter = 1
flag = 1

#main function for laundry program
opening()

cust_name = str(input("Silahkan masukkan nama customer : "))
#validation customer phone number
while flag == 1:
    cust_phone = input("Silahkan masukkan nomer HP customer (10-12 digit) : ")
    if type(cust_phone) != int and len(str(cust_phone)) < 10 or len(str(cust_phone)) > 12 :
        print("Masukkan nomer HP dengan benar!")
    else:
        flag = 0
        break

cust_address = str(input("Silahkan masukkan alamat customer : "))

#welcoming text
print("==========================================")
print("Selamat datang, Tn/Ny {}".format(cust_name))
print("------------------------------------------")
print("|Kami selalu menuruti keinginan pelanggan meskipun keinginannya aneh aneh.|")
print("------------------------------------------")
menus()

while parameter == 1:
    action = int(input(">>> "))
    if action == 1:
        print("------------------------------------------")
        print("[Laundry + Setrika]")
        laundry_kg()
        print("------------------------------------------")
       
        param = 1
        while param == 1:
            print("Apakah ada jasa yang ingin digunakan lagi ? (1) Ya (2) Tidak")
            exit1 = int(input(">>> "))
            if exit1 == 1:
                menus()
                break
            elif exit1 == 2:
                deliv()
                bills()
                laundry_voucher()
                payment_method()
                after_bills()
                print("Terimakasih sudah mempercayakan")
                print("laundry kepada kami!")
                parameter = 2
                break
            else:
                print("Perintah kamu salah!")
    if action == 2:
        print("------------------------------------------")
        print("[Setrika]")
        setrika_kg()
        param = 1

        while param == 1:
            print("Apakah ada jasa yang ingin digunakan lagi ? (1) Ya (2) Tidak")
            exit1 = int(input(">>> "))  
            if exit1 == 1:
                menus()
                break
            elif exit1 == 2:
                deliv()
                bills()
                laundry_voucher()
                payment_method()
                after_bills()
                print("Terimakasih sudah mempercayakan")
                print("laundry kepada kami!")
                parameter = 2
                break
            else:
                print("Perintah kamu salah!")
    if action == 3:
        print("--------------------------------")
        print("\nThanks for using this program!")
        parameter=0



#input to csv file
with open("new.csv", "a", newline='') as csv_file:
    myFile = csv.writer(csv_file, delimiter=',')
    myFile.writerow(["Name","PhoneNum", "Address", "Laundry", "Setrika", "Delivery", "Total Biaya", "Diskon", "Bayar"])
    myFile.writerow([cust_name, cust_phone, cust_address, laundry, setrika, delivery, sum(price), diskon, hasil])