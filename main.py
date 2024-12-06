from calendar import c
import os
import platform
from turtle import clear
import pandas as pd
import datetime
import csv
import pyfiglet
from tabulate import tabulate

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def login():
    def user_exists(username, password, role=None):
        if not os.path.exists("User.csv"):
            print("[Error] File user.csv tidak ditemukan.")
            return False
        with open("user.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["username"] == username and row["password"] == password:
                    if role and row["role"] != role:
                        continue
                    return row["role"] 
        return False
    while True:
        clear_screen()
        print("=" * 40)
        masuk = pyfiglet.figlet_format(text= "AGROVERSE", font = "3d-ASCII", width = 100, justify = "center")
        print(masuk)
        print("=" * 40)
        print("Pilih Mau Login Sebagai Apa?")
        print("1. Owner")
        print("2. Admin")
        print("3. Kasir")
        print("4. Pembeli")
        print("5. Keluar")
        print("-" * 40)
        choice = input("Masukkan Pilihan Anda [1-5]: ").strip()
        if choice in ["1", "2", "3"]:
            roles = {"1": "Owner", "2": "Admin", "3": "Kasir"}
            role = roles[choice]
            username = input("Masukkan Username: ").strip()
            password = input("Masukkan Password: ").strip()
            user_role = user_exists(username, password, role)
            if user_role:
                print(f"\nLogin Berhasil sebagai {user_role}!")
                input("Tekan Enter untuk melanjutkan...")
                return user_role
            else:
                print("[Error] Username atau password salah.")
        elif choice == "4":
            print("\nLogin sebagai Pembeli.")
            input("Tekan Enter untuk melanjutkan...")
            return "Pembeli"
        elif choice == "5":
            print("\nKeluar dari sistem. Terima kasih!")
            return None
        else:
            print("[Error] Pilihan tidak valid. Silakan coba lagi.")
        input("Tekan Enter untuk kembali ke menu...")

def print_table(menu_title, options):
    print("=" * 40)
    print(f"{menu_title.center(40)}")
    print("=" * 40)
    for key, value in options.items():
        print(f"{key}. {value}")
    print("=" * 40)

def exit_program():
    clear_screen()
    terima_kasih_text = pyfiglet.figlet_format(text= "Terima Kasih", font = "3d-ASCII", width = 100, justify = "center")
    print(terima_kasih_text)
    exit()

def menu(username):
    while True:
        if username == "Owner":
            menu_title = "MENU OWNER"
            options = {
                "1": "Tambah Barang",
                "2": "Hapus Barang",
                "3": "Lihat Barang",
                "4": "Edit Barang",
                "5": "Tambah User",
                "6": "Keluar"
            }
        elif username == "Admin":
            menu_title = "MENU ADMIN"
            options = {
                "1": "Tambah Barang",
                "2": "Hapus Barang",
                "3": "Lihat Barang",
                "4": "Presensi",
                "5": "Keluar"
            }
        elif username == "Kasir":
            menu_title = "MENU KASIR"
            options = {
                "1": "Lihat Barang",
                "2": "Presensi",
                "3": "Keluar"
            }
        elif username == "Pembeli":
            menu_title = "MENU PEMBELI"
            options = {
                "1": "Lihat Barang",
                "2": "Checkout",
                "3": "Keluar"
            }
        else:
            print("[Error] Role tidak dikenali.")
            return
        clear_screen()
        print_table(menu_title, options)
        choice = input("Masukkan pilihan Anda: ").strip()
        if username in ["Owner", "Admin"]:
            if choice == "1":
                tambahBarang()
            elif choice == "2":
                hapusBarang()
            elif choice == "3":
                lihatBarang()
            elif choice == "4" and username == "Owner":
                editBarang()
            elif choice == "4" :
                presensi()
            elif choice == "5" and username == "Owner":
                tambahUser()
            elif choice == "5" or choice == "6":
                exit_program()
            else:
                print("[Error] Pilihan tidak valid.")
        elif username == "Kasir":
            if choice == "1":
                lihatBarang()
            elif choice == "2":
                presensi()
            elif choice == "3":
                exit_program()
            else:
                print("[Error] Pilihan tidak valid.")
        elif username == "Pembeli":
            if choice == "1":
                lihatBarang()
            elif choice == "2":
                checkout()
            elif choice == "3":
                exit_program()
            else:
                print("[Error] Pilihan tidak valid.")
        input("Tekan Enter untuk melanjutkan...")
        
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

def tambahUser():
    os.system("cls")
    print("Tambah User")
    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role: ")
    
    try:
        df = pd.read_csv("User.csv")
    except FileNotFoundError:
        print("User.csv not found, creating a new file.")
        df = pd.DataFrame(columns=["username", "password", "role"])
    
    df.loc[len(df)] = [username, password, role]
    df.to_csv("User.csv", index=False)
    print("User berhasil ditambahkan")
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
    clear_screen()  
    print("=" * 40)
    print("             LIHAT BARANG")
    print("=" * 40)
    try:
        df = pd.read_csv("items.csv")
        if df.empty:
            print("Tidak ada barang tersedia.")
        else:
            print("\nDaftar Barang:")
            print(tabulate(df, headers="keys", tablefmt="double_grid", showindex=False)) 
            while True:
                print("\nPilih Opsi:")
                print("1. Cari Barang")
                print("2. Kembali ke Menu Utama")
                choice = input("Masukkan pilihan Anda [1/2]: ").strip()
                if choice == "1":
                    clear_screen()
                    keyword = input("\nMasukkan nama barang yang ingin dicari: ").strip().lower()
                    filtered_df = df[df["Nama Barang"].str.lower().str.contains(keyword)]
                    if not filtered_df.empty:
                        print("\nHasil Pencarian:")
                        print(tabulate(filtered_df, headers="keys", tablefmt="double_grid", showindex=False))
                    else:
                        print("\n[Info] Barang tidak ditemukan.")
                elif choice == "2":
                    return  
                else:
                    print("[Error] Pilihan tidak valid.")
    except FileNotFoundError:
        print("\n[Error] File items.csv tidak ditemukan. Pastikan file tersedia.")
    input("\nTekan Enter untuk kembali ke menu...")

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

def checkout():
    os.system("cls")
    print("=" * 40)
    print("               CHECKOUT")
    print("=" * 40)
    
    try:
        df = pd.read_csv("items.csv")
        if df.empty:
            print("Tidak ada barang tersedia untuk dibeli.")
            input("Tekan Enter untuk kembali...")
            return
        
        print("\nDaftar Barang Tersedia:")
        print(tabulate(df, headers="keys", tablefmt="double_grid", showindex=False))
        
        cart = []  
        total_items_sold = 0  
        total_income = 0  
        
        while True:
            item_name = input("\nMasukkan nama barang yang ingin dibeli (atau ketik 'selesai' untuk checkout): ").strip()
            if item_name.lower() == "selesai":
                break
            if item_name in df["Nama Barang"].values:
                item_row = df[df["Nama Barang"] == item_name].iloc[0]
                stock = item_row["Jumlah Barang"]
                price = item_row["Harga Barang"]
                
                if stock > 0:
                    try:
                        quantity = int(input(f"Masukkan jumlah yang ingin dibeli (stok tersedia: {stock}): "))
                        if quantity <= 0:
                            print("Jumlah harus lebih besar dari 0.")
                        elif quantity > stock:
                            print(f"Maaf, stok tidak mencukupi. Stok tersedia hanya {stock}.")
                        else:
                            cart.append({"Nama Barang": item_name, "Jumlah Barang": quantity,"Harga Barang": price, "Total": price * quantity})
                            df.loc[df["Nama Barang"] == item_name, "Jumlah Barang"] -= quantity
                            total_items_sold += quantity
                            total_income += price * quantity
                            print(f"{quantity} {item_name} berhasil ditambahkan ke keranjang.")
                    except ValueError:
                        print("Masukkan jumlah dalam angka.")
                else:
                    print(f"Maaf, {item_name} habis.")
            else:
                print("Barang tidak ditemukan. Pastikan nama barang benar.")
        
        if cart:
            clear_screen()
            print("\nBarang yang Akan Dibeli:")
            print("=" * 40)
            print(f"{'Nama':<20}{'Jumlah':<10}{'Harga Satuan':<15}{'Total':<10}")
            print("-" * 40)
            for item in cart:
                print(f"{item['Nama Barang']:<20}{item['Jumlah Barang']:<10}{item['Harga Barang']:<15}{item['Total']:<10}")
            print("-" * 40)
            print(f"Total Barang Keluar: {total_items_sold}")
            print(f"Total Harga:{total_income}")
            print("\nPilih Metode Pembayaran:")
            print("1. Tunai")
            print("2. Kartu Kredit")
            print("3. Dompet Digital (e.g., OVO, GoPay)")
            
            payment_method = input("Masukkan nomor metode pembayaran: ").strip()
            payment_status = ""
            if payment_method == "1":
                print("\nMetode Pembayaran: Tunai")
                try:
                    amount_paid = float(input("Masukkan jumlah uang yang dibayarkan: "))
                    if amount_paid >= total_income:
                        change = amount_paid - total_income
                        payment_status = f"Tunai, Kembalian: Rp{change:.2f}"
                        print(f"Pembayaran berhasil! Kembalian: Rp{change:.2f}")
                    else:
                        print("Uang yang diberikan kurang. Pembelian dibatalkan.")
                        return
                except ValueError:
                    print("Masukkan jumlah uang dalam angka.")
                    return
            elif payment_method == "2":
                print("\nMetode Pembayaran: Kartu Kredit")
                card_number = input("Masukkan nomor kartu kredit (16 digit): ").strip()
                if len(card_number) == 16 and card_number.isdigit():
                    payment_status = "Kartu Kredit"
                    print("Pembayaran berhasil melalui kartu kredit.")
                else:
                    print("Nomor kartu kredit tidak valid. Pembelian dibatalkan.")
                    return
            elif payment_method == "3":
                print("\nMetode Pembayaran: Dompet Digital")
                wallet_id = input("Masukkan ID dompet digital Anda: ").strip()
                payment_status = f"Dompet Digital (ID: {wallet_id})"
                print("Pembayaran berhasil melalui dompet digital.")
            else:
                print("Metode pembayaran tidak valid. Pembelian dibatalkan.")
                return
            
            confirm = input("\nKonfirmasi pembelian? (y/n): ").strip().lower()
            if confirm == "y":
                clear_screen()
                df.to_csv("items.csv", index=False)
                transaction_data = {
                    "Tanggal": [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                    "Total Barang Keluar": [total_items_sold],
                    "Total Pendapatan": [total_income],
                    "Metode Pembayaran": [payment_status]
                }
                transaction_df = pd.DataFrame(transaction_data)
                if not os.path.exists("transactions.csv"):
                    transaction_df.to_csv("transactions.csv", index=False)
                else:
                    transaction_df.to_csv("transactions.csv", mode="a", header=False, index=False)
                
                print("\nPembelian berhasil! Terima kasih.")
                print(f"\n[Ringkasan Transaksi]\nTotal Barang Keluar: {total_items_sold}\nTotal Pendapatan: {total_income}")
            else:
                print("Pembelian dibatalkan.")
        else:
            print("\nKeranjang kosong. Tidak ada barang yang dibeli.")
        
        input("\nTekan Enter untuk kembali ke menu...")
    except FileNotFoundError:
        print("File items.csv tidak ditemukan. Pastikan file tersedia.")
        input("Tekan Enter untuk kembali ke menu...")


def pencarianBarang():
    os.system("cls")
    print("Pencarian Barang")
    nama = input("Enter nama barang: ")
    try:
        df = pd.read_csv("items.csv")
    except FileNotFoundError:
        print("items.csv not found.")
        return 

def presensi():
    clear_screen()
    print("=" * 40)
    print("                PRESENSI")
    print("=" * 40)
    if username in ["Admin", "Kasir"]:
        data = {"Tanggal": [datetime.datetime.now().strftime("%Y-%m-%d")],"Waktu": [datetime.datetime.now().strftime("%H:%M:%S")], "Nama": [username]}
        df = pd.DataFrame(data)
        file_path = "presensi.csv"
        try:
            if os.path.exists(file_path):
                df.to_csv(file_path, mode="a", header=False, index=False)
            else:
                df.to_csv(file_path, index=False)
            print("\n[Info] Data presensi berhasil disimpan.")
        except Exception as e:
            print(f"[Error] Terjadi kesalahan saat menyimpan presensi: {e}")
    else:
        print("[Error] Anda tidak memiliki akses untuk presensi.")
    input("\nTekan Enter untuk kembali ke menu...")
    
if __name__ == "__main__":
    username = login()
    if username:
        print(f"Login berhasil sebagai {username}")
        menu(username)
    else:
        clear_screen()
        terima_kasih_text = pyfiglet.figlet_format(text= "Login Gagal", font = "3d-ASCII", width = 100, justify = "center")
        print(terima_kasih_text)
