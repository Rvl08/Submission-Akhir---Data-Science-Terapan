import streamlit as st
import pandas as pd
import joblib

# Membaca model
with open("logistic_regression_model.pkl", "rb") as model_file:
    model_load = joblib.load(model_file)

st.set_page_config(page_title="Dropout Prediction", page_icon=":watermelon:", layout="wide")

# Set Title
st.title('Dropout Prediction App')
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

st.write('---')

st.header("Jaya Jaya Institute", divider='rainbow')

tab1, tab2 = st.tabs(['Deskripsi','Prediksi'])

feature_importance = ['Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade',
       'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
       'Tuition_fees_up_to_date', 'Scholarship_holder', 'Age_at_enrollment',
       'Debtor', 'Gender', 'Application_mode']

application_mode_options = {
    1: 'Fase 1 - Kontingen Umum',
    2: 'Peraturan No. 612/93',
    5: 'Fase 1 - Kontingen Khusus (Kepulauan Azores)',
    7: 'Pemegang Kursus Tinggi Lainnya',
    10: 'Peraturan No. 854-B/99',
    15: 'Mahasiswa Internasional (Sarjana)',
    16: 'Fase 1 - Kontingen Khusus (Pulau Madeira)',
    17: 'Fase 2 - Kontingen Umum',
    18: 'Fase 3 - Kontingen Umum',
    26: 'Peraturan No. 533-A/99, Item b2) (Rencana Berbeda)',
    27: 'Peraturan No. 533-A/99, Item b3 (Institusi Lain)',
    39: 'Usia di Atas 23 Tahun',
    42: 'Transfer',
    43: 'Perubahan Kursus',
    44: 'Pemegang Diploma Spesialisasi Teknologi',
    51: 'Perubahan Institusi/Kursus',
    53: 'Pemegang Diploma Siklus Pendek',
    57: 'Perubahan Institusi/Kursus (Internasional)'
}

def aplication_mode_convert(key):
    return application_mode_options[key]
    
# Deskripsi Jaya Jaya Institute dan Permasalahan Bisnis
with tab1:
    st.markdown("""
                Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. 
                Hingga saat ini, Jaya Jaya Institut telah mencetak banyak lulusan dengan reputasi yang sangat baik. Namun, 
                institusi ini juga menghadapi masalah besar dengan jumlah siswa yang tidak menyelesaikan pendidikan mereka alias dropout. 
                Tingginya angka dropout menjadi perhatian utama karena berdampak negatif terhadap reputasi dan operasional institusi.
                """)
    st.subheader('Cara Menggunakan model machine learning untuk melakukan prediksi',  divider='grey')
    st.markdown('Untuk menggunakan model machine learning klik tab "Prediksi", kemudian terdapat beberapa inputan yang harus diisi, antara lain:')
    st.text('1. Unit Kurikulum Disetujui Semester 1: Jumlah unit kurikuler yang disetujui pada semester 1')
    st.text('2. Nilai Unit Kurikulum Semester 1: Nilai rata-rata pada semester 1 (antara 0 dan 20)')
    st.text('3. Unit Kurikulum Disetujui Semester 2: Jumlah unit kurikuler yang disetujui pada semester 2')
    st.text('4. Nilai Unit Kurikulum Semester 2: Nilai rata-rata pada semester 2 (antara 0 dan 20)')
    st.text('5. Status Pembayaran Biaya Kuliah: Status pembayaran biaya kuliah (sudah dibayar atau belum)')
    st.text('6. Status Hutang: Status apakah mahasiswa memiliki hutang (ya atau tidak)')
    st.text('7. Status Beasiswa: Status apakah mahasiswa menerima beasiswa (ya atau tidak)')
    st.text('8. Usia Saat Mendaftar: Usia siswa saat mendaftar')
    st.text('9. Jenis Kelamin: Jenis kelamin siswa (laki-laki atau perempuan)')
    st.text('10. Mode Aplikasi: Mode aplikasi atau metode pendaftaran')

with tab2:
    # Informasi Akademik
    st.header('Informasi Akademik')

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        curricular_units_1st_sem_approved = st.number_input('Unit Kurikulum Disetujui Semester 1 (0 - 100)', min_value=0)
        
    with col2:
        curricular_units_1st_sem_grade = st.number_input('Nilai Unit Kurikulum Semester 1 (0 - 20)', min_value=0.0, max_value=20.0, step=0.01)
        
    with col3:
        curricular_units_2nd_sem_approved = st.number_input('Unit Kurikulum Disetujui Semester 2 (0 - 100)', min_value=0)
        
    with col4:
        curricular_units_2nd_sem_grade = st.number_input('Nilai Unit Kurikulum Semester 2 (0 - 20)', min_value=0.0, max_value=20.0, step=0.01)

    # Informasi Keuangan
    st.header('Informasi Keuangan')
    tuition_fees_up_to_date = st.selectbox('Status Pembayaran Biaya Kuliah', options=[0, 1], format_func=lambda x: 'Sudah Dibayar' if x == 1 else 'Belum Dibayar')
    debtor = st.selectbox('Status Hutang', options=[0, 1], format_func=lambda x: 'Ya' if x == 1 else 'Tidak')
    scholarship_holder = st.selectbox('Status Beasiswa', options=[0, 1], format_func=lambda x: 'Ya' if x == 1 else 'Tidak')

    # Informasi Pribadi
    st.header('Informasi Pribadi')
    age_at_enrollment = st.number_input('Usia Saat Mendaftar', min_value=0)
    gender = st.selectbox('Jenis Kelamin', options=[0, 1], format_func=lambda x: 'Perempuan' if x == 0 else 'Laki-laki')
    application_mode = st.selectbox('Mode Aplikasi', options=application_mode_options.keys(), format_func=aplication_mode_convert)

    btn_submit = st.button('Predict')

    if btn_submit:
        df = pd.DataFrame(data=[curricular_units_2nd_sem_approved, curricular_units_2nd_sem_grade, curricular_units_1st_sem_approved,
                                curricular_units_1st_sem_grade, tuition_fees_up_to_date, scholarship_holder, age_at_enrollment,
                                debtor, gender, application_mode], index=feature_importance).T
        
        result = model_load.predict(df)
        if(result[0] == 0):
            st.success('Siswa tidak dropout')
            st.balloons()
        else:
            st.error('Siswa dropout')
