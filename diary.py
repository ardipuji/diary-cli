import datetime

while True:
    print("\n============== DIARY ==============")
    print("1. Login/sudah punya akun")
    print("2. Buat akun baru")
    print("3. Keluar")
    print("===================================")
    pilihan_akun = input("Masukkan pilihan anda: ")

    if pilihan_akun == "1":
        print("\n========== HALAMAN LOGIN ==========")
        print("Selamat datang di diary harian anda!")
        input_user = input("Masukkan username anda: ")
        input_pass = input("Masukkan password anda: ")

        login_sukses = False

        try:
            with open("akun.txt", "r") as file_akun:
                for baris in file_akun:
                    if not baris.strip():
                        continue

                    data = baris.strip().split(",")
                    username_tersimpan = data[0]
                    password_tersimpan = data[1]

                    if input_user == username_tersimpan and input_pass == password_tersimpan:
                        login_sukses = True
                        break
        except FileNotFoundError:
            login_sukses = False

        if login_sukses:
            lanjutkan = True
            nama_catatan = f"catatan_{input_user}.txt"

            while lanjutkan:
                print("\n========== MENU DIARY ==========")
                print(f"Selamat datang kembali, {input_user.upper()}!")
                print("1. Menambahkan catatan harian ke file")
                print("2. Melihat catatan harian anda")
                print("3. Menghapus catatan harian")
                print("4. Keluar")
                print("================================")
                pilihan = input("Masukkan pilihan anda: ")

                if pilihan == "1":
                    print("\n========== MENAMBAHKAN CATATAN ==========")
                    waktu_sekarang = datetime.datetime.now()
                    timestamp = waktu_sekarang.strftime("%Y-%m-%d %H:%M:%S")
                    
                    catatan_baru = input("Masukkan catatan harian anda: ")
                    catatan_final = f"[{timestamp}] {catatan_baru}\n"
                    
                    with open(nama_catatan, "a") as file:
                        file.write(catatan_final)
                    print("\n---> Data catatan berhasil disimpan ke file!")

                elif pilihan == "2":
                    print("\n========== DIARY BOOK ANDA ==========")
                    try:
                        with open(nama_catatan, "r") as file:
                            for idx, t in enumerate(file, 1):
                                print(f"{idx}. {t.strip()}")
                    except FileNotFoundError:
                        print("\n---> Belum ada catatan. File tidak ditemukan.")

                elif pilihan == "3":
                    print("\n========== HAPUS CATATAN ==========")
                    try:
                        with open(nama_catatan, "r") as file:
                            isi_catatan = file.readlines()

                        for idx, t in enumerate(isi_catatan, 1):
                            print(f"{idx}. {t.strip()}")

                        nomor_hapus = int(input("\nMasukkan NOMOR catatan yang ingin dihapus: "))
                        
                        if 1 <= nomor_hapus <= len(isi_catatan):
                            isi_catatan.pop(nomor_hapus - 1)
                            with open(nama_catatan, "w") as file:
                                file.writelines(isi_catatan)
                            print("\n---> Proses penghapusan catatan selesai!")
                        else:
                            print("\n---> Nomor catatan tidak ditemukan!")
                    except FileNotFoundError:
                        print("\n---> Belum ada catatan yang bisa dihapus.")
                    except ValueError:
                        print("\n---> Input harus berupa angka!")

                elif pilihan == "4":
                    lanjutkan = False
                    print("\n---> Anda sudah keluar dari diary anda!")
                    
                else:
                    print("\n---> Pilihan tidak valid, silakan ketik angka 1, 2, 3, atau 4.")

        else:
            print("\n---> Login gagal! Username atau password salah atau akun belum terdaftar. Silakan coba lagi.")

    elif pilihan_akun == "2":
        print("\n========== HALAMAN DAFTAR AKUN ==========")
        print("PENTING! INGAT PASSWORD DAN USERNAME ANDA")
        username_pengguna_baru = input("Masukkan username anda: ")
        password_pengguna_baru = input("Masukkan password anda: ")
        
        register_akun_final = f"{username_pengguna_baru},{password_pengguna_baru}\n"

        with open("akun.txt", "a") as file:
            file.write(register_akun_final)
        print("\n---> Akun sudah berhasil ditambahkan, silahkan login.")

    elif pilihan_akun == "3":
        print("\n---> Program selesai. Sampai jumpa!")
        break

    else:
        print("\n---> Pilihan tidak valid, silakan ketik angka 1, 2, atau 3.")