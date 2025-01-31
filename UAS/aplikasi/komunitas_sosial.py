import sqlite3

# Membuat koneksi dan cursor
conn = sqlite3.connect('komunitas.db')
cursor = conn.cursor()

# Membuat tabel komunitas, anggota, dan acara
def create_tables():
    cursor.execute('''CREATE TABLE IF NOT EXISTS komunitas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nama TEXT,
                        deskripsi TEXT
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS anggota (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nama TEXT,
                        komunitas_id INTEGER,
                        FOREIGN KEY(komunitas_id) REFERENCES komunitas(id)
                    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS acara (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nama TEXT,
                        tanggal TEXT,
                        komunitas_id INTEGER,
                        FOREIGN KEY(komunitas_id) REFERENCES komunitas(id)
                    )''')
    conn.commit()

# Menambahkan komunitas baru
def add_komunitas(nama, deskripsi):
    cursor.execute("INSERT INTO komunitas (nama, deskripsi) VALUES (?, ?)", (nama, deskripsi))
    conn.commit()
    print(f"Komunitas '{nama}' telah ditambahkan.")

# Menambahkan anggota baru ke komunitas
def add_anggota(nama, komunitas_id):
    cursor.execute("INSERT INTO anggota (nama, komunitas_id) VALUES (?, ?)", (nama, komunitas_id))
    conn.commit()
    print(f"Anggota '{nama}' telah ditambahkan ke komunitas.")

# Menambahkan acara untuk komunitas
def add_acara(nama, tanggal, komunitas_id):
    cursor.execute("INSERT INTO acara (nama, tanggal, komunitas_id) VALUES (?, ?, ?)", (nama, tanggal, komunitas_id))
    conn.commit()
    print(f"Acara '{nama}' telah ditambahkan untuk komunitas.")

# Menampilkan daftar komunitas
def show_komunitas():
    cursor.execute("SELECT * FROM komunitas")
    komunitas = cursor.fetchall()
    for k in komunitas:
        print(f"ID: {k[0]} - Nama: {k[1]} - Deskripsi: {k[2]}")

# Menampilkan anggota berdasarkan komunitas
def show_anggota(komunitas_id):
    cursor.execute("SELECT * FROM anggota WHERE komunitas_id=?", (komunitas_id,))
    anggota = cursor.fetchall()
    for a in anggota:
        print(f"ID: {a[0]} - Nama: {a[1]}")

# Menampilkan acara berdasarkan komunitas
def show_acara(komunitas_id):
    cursor.execute("SELECT * FROM acara WHERE komunitas_id=?", (komunitas_id,))
    acara = cursor.fetchall()
    for a in acara:
        print(f"ID: {a[0]} - Nama: {a[1]} - Tanggal: {a[2]}")

# Menu interaktif untuk pengguna
def menu():
    while True:
        print("\n1. Tambah Komunitas")
        print("2. Tambah Anggota")
        print("3. Tambah Acara")
        print("4. Lihat Komunitas")
        print("5. Lihat Anggota Komunitas")
        print("6. Lihat Acara Komunitas")
        print("7. Keluar")

        pilihan = input("Pilih opsi (1-7): ")

        if pilihan == '1':
            nama = input("Nama Komunitas: ")
            deskripsi = input("Deskripsi Komunitas: ")
            add_komunitas(nama, deskripsi)
        elif pilihan == '2':
            nama = input("Nama Anggota: ")
            komunitas_id = int(input("ID Komunitas: "))
            add_anggota(nama, komunitas_id)
        elif pilihan == '3':
            nama = input("Nama Acara: ")
            tanggal = input("Tanggal Acara (YYYY-MM-DD): ")
            komunitas_id = int(input("ID Komunitas: "))
            add_acara(nama, tanggal, komunitas_id)
        elif pilihan == '4':
            show_komunitas()
        elif pilihan == '5':
            komunitas_id = int(input("ID Komunitas: "))
            show_anggota(komunitas_id)
        elif pilihan == '6':
            komunitas_id = int(input("ID Komunitas: "))
            show_acara(komunitas_id)
        elif pilihan == '7':
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Opsi tidak valid. Coba lagi.")

# Menjalankan aplikasi
create_tables()
menu()

# Menutup koneksi
conn.close()
