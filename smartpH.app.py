# Jalankan aplikasi dengan perintah `streamlit run filename.py`

import streamlit as st
import math
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Kalkulator pH", page_icon=":1234:", layout="wide")

# Fungsi untuk menghitung pH asam kuat
def perhitungan_pH_asam_kuat(konsentrasi, a):
    try:
        if konsentrasi <= 0 or a <= 0:
            raise ValueError("Konsentrasi dan valensi harus positif")
        H_plus = konsentrasi * a
        if H_plus <= 0:
            return 0, 0  # Nilai default jika terjadi error
        pH = -math.log10(H_plus)
        return H_plus, pH
    except ValueError as e:
        st.error(f"Error dalam perhitungan: {str(e)}")
        return 0, 0

# Fungsi untuk menghitung pH basa kuat
def perhitungan_pH_basa_kuat(konsentrasi, a):
    try:
        if konsentrasi <= 0 or a <= 0:
            raise ValueError("Konsentrasi dan valensi harus positif")
        OH_minus = konsentrasi * a
        if OH_minus <= 0:
            return 0, 0, 7  # Nilai default jika terjadi error
        pOH = -math.log10(OH_minus)
        pH = 14 - pOH
        return OH_minus, pOH, pH
    except ValueError as e:
        st.error(f"Error dalam perhitungan: {str(e)}")
        return 0, 0, 7

# Fungsi untuk menghitung pH asam lemah
def perhitungan_pH_asam_lemah(konstanta_asam, konsentrasi):
    try:
        if konstanta_asam <= 0 or konsentrasi <= 0:
            raise ValueError("Konstanta asam dan konsentrasi harus positif")
        H_plus = math.sqrt(konstanta_asam * konsentrasi)
        if H_plus <= 0:
            return 0, 7  # Nilai default jika terjadi error
        pH = -math.log10(H_plus)
        return H_plus, pH
    except ValueError as e:
        st.error(f"Error dalam perhitungan: {str(e)}")
        return 0, 7
    
# Fungsi untuk menghitung pH basa lemah
def perhitungan_pH_basa_lemah(konstanta_basa, konsentrasi):
    try:
        if konstanta_basa <= 0 or konsentrasi <= 0:
            raise ValueError("Konstanta basa dan konsentrasi harus positif")
        OH_minus = math.sqrt(konstanta_basa * konsentrasi)
        if OH_minus <= 0:
            return 0, 0, 7  # Nilai default jika terjadi error
        pOH = -math.log10(OH_minus)
        pH = 14 - pOH
        return OH_minus, pOH, pH
    except ValueError as e:
        st.error(f"Error dalam perhitungan: {str(e)}")
        return 0, 0, 7

# Fungsi untuk menghitung pH asam kuat dengan massa dan volume
def perhitungan_pH_asam_kuat_dengan_massa_volume(massa, volume_dalam_liter, BM, a):
    try:
        if massa <= 0 or volume_dalam_liter <= 0 or BM <= 0 or a <= 0:
            raise ValueError("Semua parameter harus positif")
        konsentrasi = massa / (volume_dalam_liter * BM)
        H_plus = konsentrasi * a
        if H_plus <= 0:
            return 0, 7  # Nilai default jika terjadi error
        pH = -math.log10(H_plus)
        return H_plus, pH
    except ValueError as e:
        st.error(f"Error dalam perhitungan: {str(e)}")
        return 0, 7
    
# Fungsi untuk menghitung pH basa kuat dengan massa dan volume
def perhitungan_pH_basa_kuat_dengan_massa_volume(massa, volume_dalam_liter, BM, a):
    try:
        if massa <= 0 or volume_dalam_liter <= 0 or BM <= 0 or a <= 0:
            raise ValueError("Semua parameter harus positif")
        konsentrasi = massa / (volume_dalam_liter * BM)
        OH_minus = konsentrasi * a
        if OH_minus <= 0:
            return 0, 0, 7  # Nilai default jika terjadi error
        pOH = -math.log10(OH_minus)
        pH = 14 - pOH
        return OH_minus, pOH, pH
    except ValueError as e:
        st.error(f"Error dalam perhitungan: {str(e)}")
        return 0, 0, 7
    
# Fungsi untuk menghitung pH asam lemah dengan massa dan volume
def perhitungan_pH_asam_lemah_dengan_massa_volume(massa, volume_dalam_liter, BM, konstanta_asam):
    try:
        if massa <= 0 or volume_dalam_liter <= 0 or BM <= 0 or konstanta_asam <= 0:
            raise ValueError("Semua parameter harus positif")
        konsentrasi = massa / (volume_dalam_liter * BM)
        H_plus = math.sqrt(konstanta_asam * konsentrasi)
        if H_plus <= 0:
            return 0, 7  # Nilai default jika terjadi error
        pH = -math.log10(H_plus)
        return H_plus, pH
    except ValueError as e:
        st.error(f"Error dalam perhitungan: {str(e)}")
        return 0, 7

# Fungsi untuk menghitung pH basa lemah dengan massa dan volume
def perhitungan_pH_basa_lemah_dengan_massa_volume(massa, volume_dalam_liter, BM, konstanta_basa):
    try:
        if massa <= 0 or volume_dalam_liter <= 0 or BM <= 0 or konstanta_basa <= 0:
            raise ValueError("Semua parameter harus positif")
        konsentrasi = (massa / (volume_dalam_liter * BM)) 
        OH_minus = math.sqrt(konstanta_basa * konsentrasi)
        if OH_minus <= 0:
            return 0, 0, 7  # Nilai default jika terjadi error
        pOH = -math.log10(OH_minus)
        pH = 14 - pOH
        return OH_minus, pOH, pH
    except ValueError as e:
        st.error(f"Error dalam perhitungan: {str(e)}")
        return 0, 0, 7

# Halaman utama untuk pilihan
with st.sidebar:
    selected = option_menu(
        menu_title = "Menu",
        options = ["Beranda", 
            "Konsentrasi Asam", 
            "Konsentrasi Basa",
            "Massa dan Volume Asam",
            "Massa dan Volume Basa",
            "Tentang Aplikasi"],
        icons = ["house-door", "calculator", "calculator", "calculator", "calculator", "exclamation-circle"],
        styles = {
        "icon": {"font-size": "15px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "blue"}}
    )

if selected == "Beranda":
    # Judul warna merah Roblox
    st.markdown(
        "<h1 style='text-align:center; color:#ff3131;'>SELAMAT DATANG DI KALKULATOR pH</h1>",
        unsafe_allow_html=True,
    )

    # Banner Roblox - menggunakan URL eksternal sebagai fallback
    try:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("https://via.placeholder.com/600x200?text=Kalkulator+pH", use_container_width=True)
    except Exception as e:
        st.warning("Gambar banner tidak dapat dimuat")

    st.markdown('---')
    st.markdown(
        "<div style='text-align:center;'>Kalkulator pH Larutan adalah alat online gratis "
        "yang dirancang untuk memudahkan pengguna dalam menghitung pH suatu larutan. "
        "Silakan pilih metode perhitungan yang sesuai, kemudian ikuti perintah yang ditampilkan di layar!"
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown('---')

    st.markdown("<h2 style='color:#ff3131;'>DIBUAT OLEH :</h2>", unsafe_allow_html=True)
    st.write('KELOMPOK 5 (1C)')
    st.write(
        """
1. Amar Evan Gading                (2460321)  
2. Diandra Namira Zahfa        (2460360)  
3. Lutfhia Salwani Fatonah    (2460410)  
4. Nevi Sahara                    (2460471)  
5. Taufan Aliafi                    (2460525)
"""
    )
    st.markdown('---')

# [Bagian lain dari kode tetap sama...]

elif selected == "Tentang Aplikasi":
    selected6 = option_menu(None, ["Materi pH", "Cara Penggunaan", "Contoh Soal", "Kontak"], 
    icons=["book", "list-task", "journal-text", "envelope-open-heart"], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "nav-link": {"font-size": "15px", "text-align": "center"},
        "nav-link-selected": {"background-color": "blue"}})

    if selected6 == "Materi pH":
        # [Isi materi pH tetap sama...]
        pass
        
    elif selected6 == "Cara Penggunaan":
        # [Isi cara penggunaan tetap sama...]
        pass

    elif selected6 == "Contoh Soal":
        # [Isi contoh soal tetap sama...]
        pass

    # Hapus baris yang menyebabkan SyntaxWarning
    # local_css("D:\kalkulator_ph_larutan\style.css")
