import random
import time 

n = int(input("Masukkan jumlah tabel minesweeper yang  diinginkan ="))
bom = int(input("Masukkan Jumlah Bom yang diinginkan ="))

# Inisialisasi papan
papan = [[0 for _ in range(n)] for _ in range(n)]
papan_yg_dilihat = [[" " for _ in range(n)] for _ in range(n)]

# Cetak papan permainan
def atur_papan():
    print("\n\t\tMINESWEEPER", f"{n}x{n}\n")
    print("    " + "   ".join([str(i+1) for i in range(n)]))
    print("  +" + "---+" * n)
    for i in range(n):
        row = f"{i+1:2} | " + " | ".join(str(papan_yg_dilihat[i][j]) for j in range(n)) + " |"
        print(row)
        print("  +" + "---+" * n)

# Tempatkan ranjau secara acak
def atur_bom():
    hitung = 0
    while hitung < bom:
        row = random.randint(0, n-1)
        col = random.randint(0, n-1)
        if papan[row][col] != -1:
            papan[row][col] = -1
            hitung += 1

# Hitung angka di sekitar ranjau
def atur_angka_sekitar_bom():
    for i in range(n):
        for j in range(n):
            if papan[i][j] == -1:
                continue
            for x in range(-1, 2):
                for y in range(-1, 2):
                    ni, nj = i + x, j + y
                    if 0 <= ni < n and 0 <= nj < n and papan[ni][nj] == -1:
                        papan[i][j] += 1

# Menampilkan semua ranjau (saat kalah)
def menampilkan_bom():
    for i in range(n):
        for j in range(n):
            if papan[i][j] == -1:
                papan_yg_dilihat[i][j] = 'M'

# Cek apakah semua kotak aman sudah terbuka
def cek_menang():
    count = 0
    for i in range(n):
        for j in range(n):
            if papan_yg_dilihat[i][j] != " ":
                count += 1
    return count == n * n - bom


# =========================
# PROGRAM UTAMA
# =========================


# Setup permainan
atur_bom()
atur_angka_sekitar_bom()

#fitur waktu
waktu_mulai = time.time()


# Mulai game
over = False
while not over:
    atur_papan()
    baris_kolom = input("\nMasukkan baris dan kolom (contoh: 2 3): ").split()

    # Input tidak valid
    if len(baris_kolom) != 2:
        print("Masukkan dua angka: baris dan kolom.")
        continue

    # Jika masukkan baris & kolom
    try:
        row, col = int(baris_kolom[0]) - 1, int(baris_kolom[1]) - 1
    except:
        print("Input harus berupa angka.")
        continue

    # Validasi batas papan
    if not (0 <= row < n and 0 <= col < n):
        print("Di luar jangkauan papan!")
        continue

    # Kalau kena ranjau
    if papan[row][col] == -1:
        menampilkan_bom()
        atur_papan()
        print("\nKENA RANJAU! GAME OVER!")
        waktu_akhir = time.time()
        waktu_berlalu = int(waktu_akhir - waktu_mulai)
        print(f"Waktu bermain: {waktu_berlalu} detik")
        over = True
        break

    # Kalau buka kotak biasa
    papan_yg_dilihat[row][col] = papan[row][col]

    # Cek menang
    if cek_menang():
        menampilkan_bom()
        atur_papan()
        print("\nSELAMAT! Kamu menang!")
        waktu_akhir = time.time()
        waktu_berlalu = int(waktu_akhir - waktu_mulai)
        print(f"Waktu bermain: {waktu_berlalu} detik")
        over = True
        break
