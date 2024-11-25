# Tugas-2-Kecerdasan-Artifisial-2208107010028
# Klasifikasi Gambar CIFAR-10 menggunakan CNN

Proyek ini mengimplementasikan model klasifikasi gambar untuk mengklasifikasikan gambar dari dataset **CIFAR-10** menggunakan **Convolutional Neural Networks (CNN)**. Model ini dirancang untuk mengklasifikasikan 10 kelas gambar yang berbeda, termasuk pesawat, mobil, burung, kucing, rusa, anjing, katak, kuda, kapal, dan truk.

## Ringkasan Proyek

Model ini menggunakan **Convolutional Neural Network (CNN)** untuk mengekstrak fitur dari gambar dan mengklasifikasikannya ke dalam salah satu dari 10 kelas. Dataset yang digunakan adalah **CIFAR-10**, yang berisi 60.000 gambar berukuran 32x32 piksel dengan label salah satu dari 10 kelas.

## Dataset

- **Nama**: CIFAR-10
- **Link**: [CIFAR-10 Dataset](https://www.cs.toronto.edu/~kriz/cifar.html)
- **Deskripsi**: CIFAR-10 adalah subset berlabel dari dataset 80 juta gambar kecil. Dataset ini terdiri dari 60.000 gambar berwarna berukuran 32x32 piksel, yang dibagi menjadi 50.000 gambar untuk pelatihan dan 10.000 gambar untuk pengujian.

## Arsitektur Model

Model ini menggunakan **Convolutional Neural Network (CNN)** dengan arsitektur berikut:
1. **Conv2D** (3 lapisan konvolusi) untuk mengekstrak fitur dari gambar.
2. **MaxPooling2D** (2 lapisan pooling) untuk mengurangi dimensi data.
3. **Flatten** untuk meratakan output dari lapisan konvolusi menjadi vektor.
4. **Dense** (2 lapisan fully connected), dengan lapisan tersembunyi berisi 64 node dan lapisan output yang memiliki 10 node untuk klasifikasi.

### Rincian Lapisan

1. **Conv2D**: 32 filter, 64 filter, dan 64 filter pada masing-masing lapisan.
2. **MaxPooling2D**: Menggunakan ukuran pool (2x2) pada dua lapisan.
3. **Flatten**: Meratakan hasil konvolusi menjadi vektor 1D dengan 1024 elemen.
4. **Dense**: Lapisan tersembunyi dengan 64 node dan lapisan output dengan 10 node.

## Fungsi Aktivasi

- **ReLU** digunakan pada semua lapisan tersembunyi untuk menangani non-linearitas.
- **Softmax** digunakan pada lapisan output untuk menghasilkan probabilitas klasifikasi ke dalam 10 kelas.

## Optimisasi

Model ini menggunakan **Adam Optimizer** untuk proses pembelajaran, yang merupakan metode optimisasi adaptif yang efisien dan cocok untuk model dengan banyak parameter.
