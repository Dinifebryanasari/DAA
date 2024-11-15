<?php

use Illuminate\Support\Facades\Route;
use Livewire\Livewire;

/* NOTE: Do not remove - Livewire asset handling if using sub folder in domain */

// Mengatur rute untuk pembaruan Livewire
Livewire::setUpdateRoute(function ($handle) {
    return Route::post(
        env('ASSET_PREFIX', '').'/livewire/update',  // Menambahkan awalan jika ada subfolder
        $handle
    );
});

// Mengatur rute untuk mengambil skrip Livewire.js
Livewire::setScriptRoute(function ($handle) {
    return Route::get(
        env('ASSET_PREFIX', '').'/livewire/livewire.js',  // Menambahkan awalan jika ada subfolder
        $handle
    );
});

/*
 / END
*/

// Rute untuk halaman utama aplikasi
Route::get('/', function () {
    return view('welcome');  // Mengembalikan tampilan welcome sebagai halaman utama
});
