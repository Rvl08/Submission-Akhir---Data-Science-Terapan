# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini, Jaya Jaya Institut telah mencetak banyak lulusan dengan reputasi yang sangat baik. Namun, institusi ini juga menghadapi masalah besar dengan jumlah siswa yang tidak menyelesaikan pendidikan mereka alias dropout. Tingginya angka dropout menjadi perhatian utama karena berdampak negatif terhadap reputasi dan operasional institusi.

### Permasalahan Bisnis
Jaya Jaya Institut memiliki masalah serius dengan tingginya jumlah siswa yang tidak menyelesaikan pendidikan mereka alias dropout. Hal ini tentunya akan berdampak negatif pada reputasi institusi maupun operasionalnya.

### Cakupan Proyek
1. Analisis data untuk mengidentifikasi pola dan faktor yang mempengaruhi dropout.
2. Membangun model machine learning untuk memprediksi siswa yang berpotensi dropout.
3. Membuat dashboard interaktif untuk memudahkan pemantauan dan analisis data oleh pihak institusi.
4. Mengimplementasikan model machine learning pada streamlit untuk dapat melakukan prediksi berdasarkan data baru sesuai dengan user input.

### Persiapan

Sumber data: [data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:
1. Install Anaconda atau Miniconda di komputer
2. Buka Terminal / Anaconda Prompt
3. Buat environment baru dengan perintah conda create -n env python=3.9
4. Aktifkan environment yang sudah dibuat menggunakan perintah conda activate env
5. Install library yang dibutuhkan pip install -r requirements.txt
6. Jalankan Jupyter Notebook dengan perintah jupyter notebook

## Business Dashboard
Business dashboard yang telah dibuat bertujuan untuk memberikan gambaran yang jelas tentang performa siswa dan faktor-faktor yang mempengaruhi dropout. Beberapa chart yang menggambarkan faktor-faktor penyebab dropout seperti nilai pada semester 1 dan 2, informasi keuangan (ketepatan pembayaran, status hutang, status beasiswa), dan lain sebagainya ditampilkan pada dashboard untuk dapat memudahkan pihak institusi dalam menganalisis data secara komprehensif. Dashboard ini memungkinkan pihak institusi untuk mengidentifikasi siswa yang berisiko tinggi melakukan dropout dan segera mengambil tindakan preventif yang diperlukan.

## Menjalankan Sistem Machine Learning
Untuk menjalankan sistem machine learning pada streamlit, maka ada beberapa tahapan yang harus dilakukan. Tahapan - tahapan tersebut antara lain:
1. Buka Terminal / Comand Prompt / Power Shell
2. Arahkan lokasi path saat ini menjadi lokasi tempat folder proyek diletakkan `cd folder path`
3. Tulis perintah `streamlit run .\app.py` pada terminal
4. Buka / klik tab "Prediksi" pada tampilan yang muncuk setelah menjalankan perintah sebelumnya
5. Isi beberapa inputan yang diwajibkan untuk diisi
6. Unit Kurikulum: Jumlah unit kurikulum yang disetujui pada semester tertentu
7. Status Pembayaran Biaya Kuliah: Status pembayaran biaya kuliah (sudah dibayar atau belum)
8. Status Hutang: Status apakah mahasiswa memiliki hutang (ya atau tidak)
9. Status Beasiswa: Status apakah mahasiswa menerima beasiswa (ya atau tidak)
10. Usia Saat Mendaftar: Usia siswa saat mendaftar
11. Jenis Kelamin: Jenis kelamin siswa (laki-laki atau perempuan)
12. Mode Aplikasi: Mode aplikasi atau metode pendaftaran

## Conclusion
Proyek ini memiliki tujuan untuk mengidentifikasi faktor-faktor yang paling berpengaruh terhadap dropout siswa. Analisis korelasi digunakan untuk melihat korelasi antar variabel, terutama antara variabel status dengan variabel lain, sehingga diperoleh kesimpulan variabel yang paling berpengaruh terhadap status yaitu (Curricular_units_2nd_sem_approved, Curricular_units_2nd_sem_grade, Curricular_units_1st_sem_approved, 'Curricular_units_1st_sem_grade', Tuition_fees_up_to_date, Scholarship_holder, Age_at_enrollment, Debtor, Gender, Application_mode). Hasil analisis juga menunjukkan bahwa faktor keuangan dan performa akademik memiliki pengaruh signifikan terhadap dropout. Penggunaan model machine learning juga digunakan untuk melakukan prediksi terhadap data baru sesuai dengan variabel-variabel penting yang sudah ditentukan melalui analisis korelasi.

### Rekomendasi Action Items
1. Implementasi Program Bimbingan: Menerapkan program bimbingan khusus untuk siswa yang teridentifikasi berisiko tinggi melakukan dropout.
2. Bantuan Keuangan: Memberikan bantuan keuangan seperti beasiswa kepada siswa yang memiliki masalah keuangan.
3. Peningkatan Sistem Pemantauan: Meningkatkan sistem pemantauan performa akademik siswa untuk deteksi masalah yang dapat menyebabkan dropout.
