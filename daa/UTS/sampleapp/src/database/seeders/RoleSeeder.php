<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;
use Spatie\Permission\Models\Role;

class RoleSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        // Menambahkan role sesuai dengan yang dibutuhkan
        DB::table('roles')->insert([
            [
                'name' => 'admin', // Ganti dengan role yang sesuai
                'guard_name' => 'web' // Pastikan sesuai dengan guard yang digunakan
            ],
            [
                'name' => 'user', // Role biasa untuk pengguna
                'guard_name' => 'web'
            ],
            [
                'name' => 'moderator', // Role moderator jika diperlukan
                'guard_name' => 'web'
            ]
        ]);
    }
}
