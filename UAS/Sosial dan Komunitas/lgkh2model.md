Untuk membuat model **Sosial dan Komunitas** sesuai dengan konsep yang kamu berikan, kita perlu menyesuaikan model, migration, dan seeder agar sesuai dengan fitur aplikasi komunitas yang mencakup pendaftaran anggota, kegiatan komunitas, diskusi, dan lainnya.

Berikut adalah langkah-langkah yang diperbarui:

---

### 1. **Model: SocialCommunity**

Model ini akan menggambarkan **komunitas sosial** dan hubungan antara anggota, acara, dan kegiatan.

#### Buat Model `SocialCommunity`

Jalankan perintah artisan untuk membuat model:

```bash
php artisan make:model SocialCommunity -ms
```

#### Model `SocialCommunity.php`

```php
// app/Models/SocialCommunity.php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class SocialCommunity extends Model
{
    use HasFactory;

    protected $fillable = [
        'name', 
        'description', 
        'category', 
        'location', 
        'type', // Misalnya: Online/Offline
        'status' // Status komunitas (aktif/non-aktif)
    ];

    // Hubungan dengan Event (1:N)
    public function events()
    {
        return $this->hasMany(Event::class);
    }

    // Hubungan dengan Member (N:M)
    public function members()
    {
        return $this->belongsToMany(User::class, 'community_user');
    }

    // Hubungan dengan Artikel Berita (1:N)
    public function articles()
    {
        return $this->hasMany(Article::class);
    }
}
```

---

### 2. **Migration: SocialCommunity Table**

Migration untuk membuat tabel `social_communities` yang menyimpan data komunitas sosial.

#### Migration `create_social_communities_table.php`

```php
// database/migrations/xxxx_xx_xx_xxxxxx_create_social_communities_table.php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateSocialCommunitiesTable extends Migration
{
    public function up()
    {
        Schema::create('social_communities', function (Blueprint $table) {
            $table->id();
            $table->string('name');         // Nama komunitas
            $table->text('description');    // Deskripsi komunitas
            $table->string('category');     // Kategori komunitas (misal: petani, teknologi, seni)
            $table->string('location');     // Lokasi komunitas
            $table->string('type');         // Tipe komunitas (online/offline)
            $table->enum('status', ['active', 'inactive'])->default('active'); // Status komunitas
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('social_communities');
    }
}
```

Setelah migration selesai, jalankan perintah untuk menjalankan migration:

```bash
php artisan migrate
```

---

### 3. **Seeder: SocialCommunitySeeder**

Seeder untuk mengisi data awal pada tabel `social_communities`.

#### Seeder `SocialCommunitySeeder.php`

```php
// database/seeders/SocialCommunitySeeder.php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use App\Models\SocialCommunity;

class SocialCommunitySeeder extends Seeder
{
    public function run()
    {
        SocialCommunity::create([
            'name' => 'Komunitas Petani Sejahtera',
            'description' => 'Komunitas yang berfokus pada pengembangan pertanian di daerah pedesaan.',
            'category' => 'Agraris',
            'location' => 'Pedesaan',
            'type' => 'Offline',
            'status' => 'active',
        ]);

        SocialCommunity::create([
            'name' => 'Komunitas Teknologi Masa Depan',
            'description' => 'Komunitas untuk berbagi informasi dan diskusi mengenai teknologi terbaru.',
            'category' => 'Teknologi',
            'location' => 'Online',
            'type' => 'Online',
            'status' => 'active',
        ]);

        SocialCommunity::create([
            'name' => 'Komunitas Seni Rupa',
            'description' => 'Komunitas seni rupa untuk berbagi karya seni dan kreativitas.',
            'category' => 'Seni',
            'location' => 'Offline',
            'type' => 'Offline',
            'status' => 'inactive',
        ]);
    }
}
```

Jalankan perintah berikut untuk menjalankan seeder dan mengisi data awal:

```bash
php artisan db:seed --class=SocialCommunitySeeder
```

---

### 4. **Model: Event**

Model ini menggambarkan **acara komunitas** yang diadakan oleh setiap komunitas, baik online maupun offline.

#### Buat Model `Event`

Jalankan perintah artisan berikut:

```bash
php artisan make:model Event -ms
```

#### Model `Event.php`

```php
// app/Models/Event.php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Event extends Model
{
    use HasFactory;

    protected $fillable = [
        'social_community_id',
        'title', 
        'description', 
        'date', 
        'location', 
        'type' // Jenis acara (offline/online)
    ];

    // Hubungan dengan SocialCommunity (N:1)
    public function socialCommunity()
    {
        return $this->belongsTo(SocialCommunity::class);
    }
}
```

---

### 5. **Migration: Event Table**

Migration untuk membuat tabel `events` yang berhubungan dengan komunitas sosial.

#### Migration `create_events_table.php`

```php
// database/migrations/xxxx_xx_xx_xxxxxx_create_events_table.php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateEventsTable extends Migration
{
    public function up()
    {
        Schema::create('events', function (Blueprint $table) {
            $table->id();
            $table->foreignId('social_community_id')->constrained()->onDelete('cascade'); // Relasi ke tabel social_communities
            $table->string('title');           // Judul acara
            $table->text('description');       // Deskripsi acara
            $table->dateTime('date');          // Tanggal acara
            $table->string('location');        // Lokasi acara
            $table->enum('type', ['online', 'offline']); // Jenis acara
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('events');
    }
}
```

Jalankan perintah berikut untuk menjalankan migration:

```bash
php artisan migrate
```

---

### 6. **Seeder: EventSeeder**

Seeder untuk mengisi data awal pada tabel `events`.

#### Seeder `EventSeeder.php`

```php
// database/seeders/EventSeeder.php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use App\Models\Event;

class EventSeeder extends Seeder
{
    public function run()
    {
        Event::create([
            'social_community_id' => 1,
            'title' => 'Pertemuan Petani Sejahtera',
            'description' => 'Diskusi tentang teknik pertanian terbaru.',
            'date' => now()->addDays(10),
            'location' => 'Desa Bumi Makmur',
            'type' => 'Offline',
        ]);

        Event::create([
            'social_community_id' => 2,
            'title' => 'Webinar Teknologi Masa Depan',
            'description' => 'Pembahasan tentang tren teknologi terkini.',
            'date' => now()->addDays(15),
            'location' => 'Online',
            'type' => 'Online',
        ]);
    }
}
```

Jalankan perintah berikut untuk mengisi data seeder:

```bash
php artisan db:seed --class=EventSeeder
```

---

### 7. **Filament Resource**

Setelah semua model, migration, dan seeder selesai, kamu bisa membuat resource untuk komunitas dan acara di Filament (Laravel Admin Panel).

Jalankan perintah berikut untuk membuat Filament Resource:

```bash
php artisan make:filament-resource SocialCommunity --generate
```

---

### Kesimpulan

Dengan langkah-langkah di atas, kamu dapat membangun aplikasi sosial dan komunitas yang memungkinkan pengguna bergabung, berinteraksi, dan berpartisipasi dalam acara komunitas, baik secara online maupun offline. Kamu bisa melanjutkan dengan menambahkan fitur-fitur lain seperti diskusi, mentoring, dan crowdfunding sesuai dengan kebutuhan aplikasi.