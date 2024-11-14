import os
import pandas as pd


def login():
    os.system("cls")
    print("Selamat Datang Di Toko Kami")
    print("Pilih Mau login Sebagai Apa?")
    print("1. Owner")
    print("2. Admin")
    print("3. Kasir")
    print("4. Pembeli")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == "Yuri" and password == "Ryujin":
            return "Owner"
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == "Admin" and password == "@dm1n":
            return "Admin"
    elif choice == "3":
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == "Kasir" and password == "K@sir1":
            return "Kasir"
    elif choice == "4":
        return "Pembeli"
    else:
        print("Pilihan tidak valid")
        return None
    return None

def menu(username):
    if username == "Owner":
        print("Mau Apa Pak BOSS?")
        print("Menu Owner")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Lihat Barang")
        print("4. Edit Barang")
        print("5. Lihat Penjualan")
        print("6. Lihat Pengeluaran")
        print("7. Lihat Pendapatan")
        print("8. Lihat Keuntungan")
        print("9. Kurangi Barang")
        print("10. Keluar")
        choice = input("Enter your choice: ")
        if choice == "1":
            tambahBarang()
        elif choice == "2":
            hapusBarang()
        elif choice == "3":
            lihatBarang()
        elif choice == "4":
            editBarang()
        elif choice == "5":
            lihatPenjualan()
        elif choice == "6":
            lihatPengeluaran()
        elif choice == "7":
            lihatPendapatan()
        elif choice == "8":
            lihatKeuntungan()
        elif choice == "9":
            kurangibarang()
        elif choice == "10":
            exit_program()
        else:
            print("Pilihan tidak tersedia")
    elif username == "Admin":
        print("Mau Apa Min?")
        print("Menu Admin")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Lihat Barang")
        print("4. Keluar")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            tambahBarang()
        elif choice == "2":
            hapusBarang()
        elif choice == "3":
            lihatBarang()
        elif choice == "4":
            exit_program()
        else:
            print("Pilihan tidak tersedia")
    elif username == "Kasir":
        print("Mau Apa Pak Kasir?")
        print("Menu Kasir")
        print("1. Lihat Penjualan")
        print("2. Lihat Pengeluaran")
        print("3. Lihat Barang")
        print("4. Keluar")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            lihatPenjualan()
        elif choice == "2":
            lihatPengeluaran()
        elif choice == "3":
            lihatBarang()
        elif choice == "4":
            exit_program()
        else:
            print("Pilihan tidak tersedia")
    elif username == "Pembeli":
        print("Mau Apa Kakak?")
        print("Menu Pembeli")
        print("1. Lihat Barang")
        print("2. Checkout")
        print("3. Pencarian Barang")
        print("4. Keluar")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            lihatBarang()
        elif choice == "2":
            checkout()
        elif choice == "3":
            pencarianBarang()
        elif choice == "4":
            exit_program()
        else:
            print("Pilihan tidak tersedia")

def tambahBarang():
    os.system("cls")
    print("Tambah Barang")
    nama = input("Enter nama barang: ")
    harga = input("Enter harga barang: ")
    stok = input("Enter stok barang: ")
    
    try:
        df = pd.read_csv("items.csv")
    except FileNotFoundError:
        print("items.csv not found, creating a new file.")
        df = pd.DataFrame(columns=["Nama Barang", "Harga Barang", "Stok Barang"])
    
    df.loc[len(df)] = [nama, harga, stok]
    df.to_csv("items.csv", index=False)
    print("Barang berhasil ditambahkan")
    menu(username)

def hapusBarang():
    os.system("cls")
    print("Hapus Barang")
    nama = input("Enter nama barang: ")
    try:
        df = pd.read_csv("items.csv")
    except FileNotFoundError:
        print("items.csv not found.")
        return
    df = df[df["Nama Barang"] != nama]
    df.to_csv("items.csv", index=False)
    print("Barang berhasil dihapus")
    menu(username)

def lihatBarang():
    os.system("cls")
    print("Lihat Barang")
    try:
        df = pd.read_csv("items.csv")
        print(df)
    except FileNotFoundError:
        print("items.csv not found.")
    menu(username)

def editBarang():
    os.system("cls")
    print("Edit Barang")
    nama = input("Enter nama barang: ")
    try:
        df = pd.read_csv("items.csv")
    except FileNotFoundError:
        print("items.csv not found.")
        return
    
    if nama in df["Nama Barang"].values:
        df.loc[df["Nama Barang"] == nama, "Harga Barang"] = input("Enter harga barang: ")
        df.to_csv("items.csv", index=False)
        print("Barang berhasil diubah")
    else:
        print("Barang tidak ditemukan.")
    menu(username)

def lihatPenjualan():
    os.system("cls")
    print("Lihat Penjualan")
    try:
        df = pd.read_csv("penjualan.csv")
        print(df)
    except FileNotFoundError:
        print("penjualan.csv not found.")
    menu(username)

def lihatPengeluaran():
    os.system("cls")
    print("Lihat Pengeluaran")
    try:
        df = pd.read_csv("pengeluaran.csv")
        print(df)
    except FileNotFoundError:
        print("pengeluaran.csv not found.")
    menu(username)

def lihatPendapatan():
    os.system("cls")
    print("Lihat Pendapatan")
    try:
        df = pd.read_csv("pendapatan.csv")
        print(df)
    except FileNotFoundError:
        print("pendapatan.csv not found.")
    menu(username)

def lihatKeuntungan():
    os.system("cls")
    print("Lihat Keuntungan")
    try:
        df = pd.read_csv("keuntungan.csv")
        print(df)
    except FileNotFoundError:
        print("keuntungan.csv not found.")
    menu(username)

def kurangibarang():
    os.system("cls")
    print("Kurangi Barang")
    nama = input("Enter nama barang: ")
    try:
        df = pd.read_csv("items.csv")
    except FileNotFoundError:
        print("items.csv not found.")
        return
    df.loc[df["Nama Barang"] == nama, "Stok Barang"] = input("Enter stok barang: ")
    df.to_csv("items.csv", index=False)
    print("Barang berhasil dikurangi")
    menu(username)

def checkout():
    os.system("cls")
    print("Checkout")
    try:
        df = pd.read_csv("items.csv")
        print(df)
    except FileNotFoundError:
        print("items.csv not found.")
    menu(username)

def pencarianBarang():
    os.system("cls")
    print("Pencarian Barang")
    nama = input("Enter nama barang: ")
    try:
        df = pd.read_csv("items.csv")
    except FileNotFoundError:
        print("items.csv not found.")
        return 

def exit_program():
    os.system("cls")
    print("Terima Kasih")
    exit()

# Main execution
if __name__ == "__main__":
    username = login()
    if username:
        print(f"Login berhasil sebagai {username}")
        menu(username)
    else:
        print("Login gagal, silakan coba lagi.")
