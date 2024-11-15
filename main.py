from calendar import c
import os
import platform
import pandas as pd

def clear_screen():
    """Membersihkan layar."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def login():
    while True:
        clear_screen()
        print("=" * 40)
        print("        SELAMAT DATANG DI TOKO KAMI")
        print("=" * 40)
        print("Pilih Mau Login Sebagai Apa?")
        print("1. Owner")
        print("2. Admin")
        print("3. Kasir")
        print("4. Pembeli")
        print("5. Keluar")
        print("-" * 40)
        choice = input("Masukkan Pilihan Anda [1-5]: ").strip()

        if choice == "1":
            username = input("Masukkan Username: ").strip()
            password = input("Masukkan Password: ").strip()
            if username == "Yuri" and password == "Ryujin":
                print("\nLogin Berhasil sebagai Owner!")
                input("Tekan Enter untuk melanjutkan...")
                return "Owner"
            else:
                print("[Error] Username atau password salah.")
        
        elif choice == "2":
            username = input("Masukkan Username: ").strip()
            password = input("Masukkan Password: ").strip()
            if username == "Admin" and password == "@dm1n":
                print("\nLogin Berhasil sebagai Admin!")
                input("Tekan Enter untuk melanjutkan...")
                return "Admin"
            else:
                print("[Error] Username atau password salah.")
        
        elif choice == "3":
            username = input("Masukkan Username: ").strip()
            password = input("Masukkan Password: ").strip()
            if username == "Kasir" and password == "K@sir":
                print("\nLogin Berhasil sebagai Kasir!")
                input("Tekan Enter untuk melanjutkan...")
                return "Kasir"
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
    """Menampilkan menu tabel dengan opsi."""
    print("=" * 40)
    print(f"{menu_title.center(40)}")
    print("=" * 40)
    for key, value in options.items():
        print(f"{key}. {value}")
    print("=" * 40)

def exit_program():
    """Keluar dari program."""
    clear_screen()
    print("Terima Kasih telah menggunakan sistem kami.")
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
                "5": "Keluar"
            }
        elif username == "Admin":
            menu_title = "MENU ADMIN"
            options = {
                "1": "Tambah Barang",
                "2": "Hapus Barang",
                "3": "Lihat Barang",
                "4": "Keluar"
            }
        elif username == "Kasir":
            menu_title = "MENU KASIR"
            options = {
                "1": "Lihat Barang",
                "2": "Keluar"
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
            elif choice == "5":
                exit_program()
            else:
                print("[Error] Pilihan tidak valid.")
        elif username == "Kasir":
            if choice == "1":
                lihatBarang()
            elif choice == "2":
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
    """Menampilkan daftar barang dan menyediakan fitur pencarian."""
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
            print(df.to_string(index=False))  
            while True:
                print("\nPilih Opsi:")
                print("1. Cari Barang")
                print("2. Kembali ke Menu Utama")
                choice = input("Masukkan pilihan Anda [1/2]: ").strip()
                if choice == "1":
                    keyword = input("\nMasukkan nama barang yang ingin dicari: ").strip().lower()
                    filtered_df = df[df["Nama Barang"].str.lower().str.contains(keyword)]
                    if not filtered_df.empty:
                        print("\nHasil Pencarian:")
                        print(filtered_df.to_string(index=False))
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
        print(df.to_string(index=False))
        
        cart = []  
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
                            cart.append({"Nama": item_name, "Jumlah": quantity, "Harga Satuan": price, "Total": price * quantity})
                            df.loc[df["Nama Barang"] == item_name, "Jumlah Barang"] -= quantity
                            print(f"{quantity} {item_name} berhasil ditambahkan ke keranjang.")
                    except ValueError:
                        print("Masukkan jumlah dalam angka.")
                else:
                    print(f"Maaf, {item_name} habis.")
            else:
                print("Barang tidak ditemukan. Pastikan nama barang benar.")
        
        if cart:
            print("\nBarang yang Akan Dibeli:")
            print("=" * 40)
            print(f"{'Nama':<20}{'Jumlah':<10}{'Harga Satuan':<15}{'Total':<10}")
            print("-" * 40)
            total_price = ""
            for item in cart:
                print(f"{item['Nama']:<20}{item['Jumlah']:<10}{item['Harga Satuan']:<15}{item['Total']:<10}")
                total_price += item['Total']
            print("-" * 40)
            print(f"Total Harga: {total_price}")
            confirm = input("\nKonfirmasi pembelian? (y/n): ").strip().lower()
            if confirm == "y":
                df.to_csv("items.csv", index=False)
                print("Pembelian berhasil! Terima kasih.")
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

if __name__ == "__main__":
    username = login()
    if username:
        print(f"Login berhasil sebagai {username}")
        menu(username)
    else:
        print("Login gagal.")
