data_mahasiswa = {}

def tampilkan_data():
    if data_mahasiswa:
        print("\nDaftar Nilai")
        print("="*66)
        print("| NO |       NAMA      |    NIM    | TUGAS | UTS | UAS |  AKHIR  |")
        print("="*66)
        no = 1
        for nama, data in data_mahasiswa.items():
            nilai_akhir = (data['tugas'] * 0.3) + (data['uts'] * 0.35) + (data['uas'] * 0.35)
            print(f"| {no:<2} | {nama:<15} | {data['nim']:<8} | {data['tugas']:<5.0f} | {data['uts']:<3.0f} | {data['uas']:<3.0f} | {nilai_akhir:<7.2f} |")
            no += 1
        print("="*66)
    else:
        print("\nDaftar Nilai")
        print("="*61)
        print("| NO |    NAMA    |    NIM    | TUGAS | UTS | UAS |  AKHIR  |")
        print("="*61)
        print("|                       TIDAK ADA DATA                      |")
        print("="*61)

def tambah_data():
    nama = input("Nama: ")
    nim = input("NIM: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
    data_mahasiswa[nama] = {'nim': nim, 'tugas': tugas, 'uts': uts, 'uas': uas}

def hapus_data():
    nama = input("Masukkan Nama: ")
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print("Data berhasil dihapus!")
    else:
        print("Data dengan Nama tersebut tidak ditemukan!")

def ubah_data():
    nama= input("Masukkan Nama: ")
    if nama in data_mahasiswa:
        print("Masukkan data baru:")
        data_mahasiswa[nama]['nim'] = input("Masukkan NIM: ")
        data_mahasiswa[nama]['tugas'] = float(input("Nilai Tugas: "))
        data_mahasiswa[nama]['uts'] = float(input("Nilai UTS: "))
        data_mahasiswa[nama]['uas'] = float(input("Nilai UAS: "))
        print("Data berhasil diubah!")
    else:
        print("Data dengan Nama tersebut tidak ditemukan!")

while True:
    print("[(L)ihat, (T)ambah, (U)bah, (H)apus, (K)eluar]")
    pilihan = input("Pilih menu: ").lower()

    if pilihan == 'l':
        tampilkan_data()
    elif pilihan == 't':
        tambah_data()
    elif pilihan == 'h':
        hapus_data()    
    elif pilihan == 'u':
        ubah_data()
    elif pilihan == 'k':
        print("Keluar dari program...")
        break
    else:
        print("Pilihan tidak valid, silakan pilih menu yang tersedia.")