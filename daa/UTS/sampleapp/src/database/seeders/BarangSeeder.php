<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;

class BarangSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run()
    {
        \App\Models\Barang::create([
            'name' => 'Laptop',
            'description' => 'Laptop gaming dengan spesifikasi tinggi',
            'price' => 15000000.00,
            'stock' => 10,
            'image' => 'laptop.jpg',
        ]);

        \App\Models\Barang::create([
            'name' => 'Mouse',
            'description' => 'Mouse gaming dengan DPI tinggi',
            'price' => 300000.00,
            'stock' => 25,
            'image' => 'mouse.jpg',
        ]);
    }
}
