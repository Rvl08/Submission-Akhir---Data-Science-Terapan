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

Link Dashboard: https://public.tableau.com/shared/X72N3HCZM?:display_count=n&:origin=viz_share_link

## Menjalankan Sistem Machine Learning
Untuk menjalankan sistem machine learning pada streamlit, maka ada beberapa tahapan yang harus dilakukan. Tahapan - tahapan tersebut antara lain:
1. Buka / klik tab "Prediksi" pada tampilan yang muncul
2. Isi beberapa inputan yang diwajibkan untuk diisi
3. Unit Kurikulum: Jumlah unit kurikulum yang disetujui pada semester tertentu
4. Status Pembayaran Biaya Kuliah: Status pembayaran biaya kuliah (sudah dibayar atau belum)
5. Status Hutang: Status apakah mahasiswa memiliki hutang (ya atau tidak)
6. Status Beasiswa: Status apakah mahasiswa menerima beasiswa (ya atau tidak)
7. Usia Saat Mendaftar: Usia siswa saat mendaftar
8. Jenis Kelamin: Jenis kelamin siswa (laki-laki atau perempuan)
9. Mode Aplikasi: Mode aplikasi atau metode pendaftaran

Link Aplikasi: https://submission-akhir-data-science-terapan-spyzbuuwfujwwagbjnc3zw.streamlit.app/

## Conclusion
Proyek ini memiliki tujuan untuk mengidentifikasi faktor-faktor yang paling berpengaruh terhadap dropout siswa. Analisis korelasi digunakan untuk melihat korelasi antar variabel, terutama antara variabel status dengan variabel lain, sehingga diperoleh kesimpulan variabel yang paling berpengaruh terhadap status yaitu (Curricular_units_2nd_sem_approved, Curricular_units_2nd_sem_grade, Curricular_units_1st_sem_approved, 'Curricular_units_1st_sem_grade', Tuition_fees_up_to_date, Scholarship_holder, Age_at_enrollment, Debtor, Gender, Application_mode). Hasil analisis juga menunjukkan bahwa faktor keuangan dan performa akademik memiliki pengaruh signifikan terhadap dropout. Penggunaan model machine learning juga digunakan untuk melakukan prediksi terhadap data baru sesuai dengan variabel-variabel penting yang sudah ditentukan melalui analisis korelasi.

### Rekomendasi Action Items
1. Implementasi Program Bimbingan: Menerapkan program bimbingan khusus untuk siswa yang teridentifikasi berisiko tinggi melakukan dropout. Beberapa kriteria utama yang menjadi faktor terpenting dalam mengidentifikasi apakah siswa akan diberikan bimbingan yaitu nilai yang rendah pada semester 1 dan 2. Program bimbingan akan mencangkup peninjauan performa akademik tiap semester, strategi belajar, serta diskusi mengenai masalah-masalah yang mungkin mempengaruhi studi siswa.
   
2. Bantuan Keuangan: Memberikan bantuan keuangan seperti beasiswa kepada siswa yang memiliki masalah keuangan. Beberapa kriteria penerima beasiswa yaitu siswa berusia 25 - 30 tahun, siswa yang orang tuanya memiliki pekerjaan kasar (buruh, pekerja konstruksi, dll), siswa yang memiliki performa akademik yang baik namun terkendala masalah keuangan. Jenis beasiswa yang disediakan dapat bervariasi menyesuaikan dengan kriteria siswa yang memenuhi persyaratannya, seperti beasiswa prestasi yang ditujukan untuk siswa yang memiliki performa akademik yang baik, ataupun beasiswa bantuan keuangan khusus yang ditujukan untuk siswa yang berasal dari keluarga dengan latar belakang ekonomi rendah.
    
3. Peningkatan Sistem Pemantauan: Meningkatkan sistem pemantauan performa akademik siswa untuk deteksi masalah yang dapat menyebabkan dropout. Sistem pemantauan dapat diimplementasikan dengan database instansi untuk melihat performa akademis siswa secara real-time. Sistem pemantauan yang dibuat juga harus mencangkup pemantuan nilai ujian tiap semester, partisipasi dalam kelas, kehadiran, hingga riwayat pengumpulan tugas masing-masing siswa.
