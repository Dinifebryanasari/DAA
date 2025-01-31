Berikut adalah tabel yang lebih rapih untuk memperjelas struktur komunitas sosial dan acara yang dibangun dalam aplikasi:

### Jenis-Jenis Komunitas Sosial

| **Jenis Komunitas**  | **Deskripsi**                                                                                   |
|----------------------|-------------------------------------------------------------------------------------------------|
| **Komunitas Pedesaan**| Komunitas di wilayah pedesaan yang lebih berbasis agraris, seperti petani atau peternak.        |
| **Komunitas Perkotaan**| Komunitas di lingkungan perkotaan yang lebih individualis, seperti komunitas gamers atau startup.|
| **Komunitas Religius**| Komunitas berbasis keyakinan agama, seperti komunitas mengaji atau rohani.                       |
| **Komunitas Ekonomi** | Komunitas yang fokus pada aspek ekonomi, seperti UMKM atau pekerja tekstil.                    |

### Dampak Positif dan Negatif Interaksi Sosial

| **Dampak Positif**                             | **Dampak Negatif**                                      |
|------------------------------------------------|---------------------------------------------------------|
| Meningkatkan solidaritas dan kerja sama        | Konflik sosial dan ketegangan antar individu             |
| Meningkatkan kesejahteraan emosional anggota   | Penyebaran hoaks atau informasi palsu                   |
| Membantu pembentukan identitas sosial yang kuat| Diskriminasi sosial dan eksklusi terhadap kelompok lain  |

### Model Relasi antara `SocialCommunity` dan `Event`

| **Relasi**                | **Model Terkait**       | **Deskripsi**                                        |
|---------------------------|-------------------------|------------------------------------------------------|
| **1:N**                    | `Event`                 | Setiap komunitas memiliki banyak acara atau event.    |
| **N:M**                    | `User`                  | Banyak anggota dapat bergabung di banyak komunitas.   |

### Contoh Seeder untuk `SocialCommunity` dan `Event`

| **Nama Komunitas**            | **Deskripsi**                                              | **Kategori**  | **Tipe** | **Status** |
|-------------------------------|------------------------------------------------------------|---------------|----------|------------|
| Komunitas Petani Sejahtera     | Komunitas untuk pengembangan pertanian di daerah pedesaan  | Agraris       | Offline  | Active     |
| Komunitas Teknologi Masa Depan | Komunitas untuk berbagi info tentang teknologi terbaru     | Teknologi     | Online   | Active     |
| Komunitas Seni Rupa            | Komunitas untuk berbagi karya seni dan kreativitas         | Seni          | Offline  | Inactive   |

| **Judul Event**               | **Deskripsi**                                              | **Lokasi**          | **Tipe**  | **Tanggal**         |
|-------------------------------|------------------------------------------------------------|---------------------|-----------|---------------------|
| Pertemuan Petani Sejahtera     | Diskusi tentang teknik pertanian terbaru                   | Desa Bumi Makmur    | Offline   | 10 hari dari sekarang |
| Webinar Teknologi Masa Depan   | Pembahasan tren teknologi terkini                          | Online              | Online    | 15 hari dari sekarang |