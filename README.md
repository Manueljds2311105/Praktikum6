# Praktikum 6

Nama: Manuel Johansen Dolok Saribu

Nim: 312410493

Mata Kuliah: Bahasa Pemograman

Dosen Pengampu: Agung Nugroho, S.Kom., M.Kom.,
## Flowchart
![Foto](https://github.com/Manueljds2311105/foto/blob/dd004c36cf835c344d2042b4dc13a838fab9086d/lab06.drawio.png)
## Penjelasan
```python
data_mahasiswa = {}
```
- Menyimpan data mahasiswa dalam format {nama: {nim, tugas, uts, uas}}.
```python
def tampilkan_data():
```
- Tujuan: Menampilkan daftar nilai mahasiswa yang ada.
- Jika data_mahasiswa ada/tidak kosong:
  - Menampilkan header tabel nilai.
  - Menghitung nilai akhir dengan formula:
      - nilai akhir = (tugas*0.3)+(uts*0.35)+(uas*0.35)
  - Menampilkan setiap data mahasiswa dalam format tabel.
- Jika data_mahasiswa kosong:
  - Menampilkan pesan "TIDAK ADA DATA".
```python
def tambah_data():
```
- Tujuan: Menambahkan data mahasiswa baru.
  - Meminta input nama, NIM, dan nilai (tugas, UTS, UAS).
  - Menyimpan data ke dalam data_mahasiswa dengan format:
      ```python
      {nama: {'nim': nim, 'tugas': tugas, 'uts': uts, 'uas': uas}}
      ```
```python
def hapus_data():
```
- Tujuan: Menghapus data mahasiswa berdasarkan nama.
  - Meminta nama mahasiswa.
  - Jika nama ditemukan dalam data_mahasiswa, hapus data.
  - Jika nama tidak ditemukan, tampilkan pesan kesalahan.
```python
def ubah_data():
```
- Tujuan: Mengubah data mahasiswa berdasarkan nama.
  - Meminta nama mahasiswa.
  - Jika nama ditemukan, meminta data baru (NIM, tugas, UTS, UAS) untuk menggantikan data lama.
  - Jika nama tidak ditemukan, tampilkan pesan kesalahan.
### Loop Menu Utama
```python
while True:
    print("[(L)ihat, (T)ambah, (U)bah, (H)apus, (K)eluar]")
    pilihan = input("Pilih menu: ").lower()
```
- Tujuan: Mengelola navigasi antar fungsi.
  - l: Memanggil tampilkan_data.
  - t: Memanggil tambah_data.
  - h: Memanggil hapus_data.
  - u: Memanggil ubah_data.
  - k: Keluar dari program.
  - Lainnya: Menampilkan pesan kesalahan jika input tidak valid.
## Hasil Kode Program
![Foto](https://github.com/Manueljds2311105/foto/blob/dd004c36cf835c344d2042b4dc13a838fab9086d/lab06.py%20-%20Visual%20Studio%20Code%20%5BAdministrator%5D%2011_30_2024%2012_33_28%20PM.png)
