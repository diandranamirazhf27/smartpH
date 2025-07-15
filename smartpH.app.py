# Jalankan aplikasi dengan perintah `streamlit run filename.py`

import streamlit as st
import math
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Kalkulator pH", page_icon=":1234:", layout="wide")

# Fungsi untuk menghitung pH asam kuat

def perhitungan_pH_asam_kuat(konsentrasi, a):
    H_plus = konsentrasi * a
    pH = -math.log10(H_plus)
    return H_plus, pH

# Fungsi untuk menghitung pH basa kuat

def perhitungan_pH_basa_kuat(konsentrasi, a):
    OH_minus = konsentrasi * a
    pOH = -math.log10(OH_minus)
    pH = 14 - pOH
    return OH_minus, pOH, pH

# Fungsi untuk menghitung pH asam lemah

def perhitungan_pH_asam_lemah(konstanta_asam, konsentrasi):
    H_plus = math.sqrt(konstanta_asam * konsentrasi)
    pH = -math.log10(H_plus)
    return H_plus, pH
    
# Fungsi untuk menghitung pH basa lemah

def perhitungan_pH_basa_lemah(konstanta_basa, konsentrasi):
    OH_minus = math.sqrt(konstanta_basa * konsentrasi)
    pOH = -math.log10(OH_minus)
    pH = 14 - pOH
    return OH_minus, pOH, pH

# Fungsi untuk menghitung pH asam kuat dengan massa dan volume

def perhitungan_pH_asam_kuat_dengan_massa_volume(massa, volume_dalam_liter, BM, a):
    konsentrasi = massa / (volume_dalam_liter * BM)
    H_plus = konsentrasi * a
    pH = -math.log10(H_plus)
    return H_plus, pH
    
# Fungsi untuk menghitung pH basa kuat dengan massa dan volume

def perhitungan_pH_basa_kuat_dengan_massa_volume(massa, volume_dalam_liter, BM, a):
    konsentrasi = massa / (volume_dalam_liter * BM)
    OH_minus = konsentrasi * a
    pOH = -math.log10(OH_minus)
    pH = 14 - pOH
    return OH_minus, pOH, pH
    
# Fungsi untuk menghitung pH asam lemah dengan massa dan volume

def perhitungan_pH_asam_lemah_dengan_massa_volume(massa, volume_dalam_liter, BM, konstanta_asam):
    konsentrasi = massa / (volume_dalam_liter * BM)
    H_plus = math.sqrt(konstanta_asam * konsentrasi)
    pH = -math.log10(H_plus)
    return H_plus, pH

# Fungsi untuk menghitung pH basa lemah dengan massa dan volume

def perhitungan_pH_basa_lemah_dengan_massa_volume(massa, volume_dalam_liter, BM, konstanta_basa):
    konsentrasi = (massa / (volume_dalam_liter * BM)) 
    OH_minus = math.sqrt(konstanta_basa * konsentrasi)
    pOH = -math.log10(OH_minus)
    pH = 14 - pOH
    return OH_minus, pOH, pH

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
    st.markdown("<h1 style='text-align: center; color: blue;'>SELAMAT DATANG</h1>", unsafe_allow_html=True)
    left, mid, right = st.columns(3)
    with mid:
        st.image("D:\kalkulator_ph_larutan\logoapp.gif")    
    st.markdown('---')
    st.markdown('<div style="text-align: center;">Kalkulator pH Larutan adalah alat online gratis yang dirancang untuk memudahkan pengguna dalam menghitung pH suatu larutan. Silakan pilih metode perhitungan yang sesuai, kemudian ikuti perintah yang ditampilkan di layar!</div>', unsafe_allow_html=True)
    st.markdown('---')
    st.markdown('<h2 style="color: blue; ">DIBUAT OLEH:</h2>', unsafe_allow_html=True)
    st.write('KELOMPOK 5 (1C)')
    st.write('''
1. Amar Evan Gading            (2460321)
2. Diandra Namira Zahfa        (2460360)
3. Lutfhia Salwani Fatonah     (2460410) 
4. Nevi Sahara                 (2460471) 
5. Taufan Aliafi               (2460525)
''')
    st.markdown('---')
    
elif selected == "Konsentrasi Asam":
    st.title(":blue[Kalkulator pH Larutan]")
    st.subheader("Menghitung [H+] dan pH dari Konsentrasi Asam Kuat dan Asam Lemah")
    
    selected2 = option_menu(None, ["Asam Kuat", "Asam Lemah", "Custom"], 
    menu_icon = "cast", default_index=0, orientation="horizontal",
    styles ={
        "nav-link": {"font-size": "15px", "text-align": "center"},
        "nav-link-selected": {"background-color": "blue"},})

    if selected2 == "Asam Kuat":
        # Pilih senyawa asam kuat
        asam_kuat = {
            "Asam Klorida (HCl)": 1,
            "Asam Nitrat (HNO3)": 1,
            "Asam Sulfat (H2SO4)": 2,            
            "Asam Bromida (HBr)": 1,
            "Asam Bromit (HBrO3)": 1,
            "Asam Perbromat (HBrO4)": 1,
            "Asam Klorat (HClO3)": 1,             
            "Asam Perklorat (HClO4)": 1,
            "Asam Iodida (HI)": 1,
            "Asam Iodit (HIO3)": 1,
            "Asam Periodat (HIO4)": 1,
        }
            
        selected_asam_kuat = st.selectbox("Pilih senyawa asam kuat", list(asam_kuat.keys()))
        a = asam_kuat[selected_asam_kuat]
        st.write("a = ", a)
            
        # Masukkan konsentrasi
        konsentrasi = st.number_input("Masukkan konsentrasi (M)", format = "%.4f", step=0.0001, key = "H1")
        st.write("Konsentrasi = ", konsentrasi)
            
        # Tombol hitung
        if st.button("Hitung pH", key = "T1"):
            H_plus, pH = perhitungan_pH_asam_kuat(konsentrasi, a)
            st.write("[H+] =", round(H_plus, 4))
            st.write("pH =", round(pH, 2))            
            st.success(f'pH asam adalah {pH:.2f}')

        
    elif selected2 == "Asam Lemah":
        # Masukkan Ka
        konstanta_asam = st.number_input("Masukkan Ka", key = "K2")
        st.write("Ka = ", konstanta_asam)

        # Masukkan konsentrasi
        konsentrasi = st.number_input("Masukkan konsentrasi (M)", format = "%.4f", step=0.0001, key = "H2")
        st.write("Konsentrasi = ", konsentrasi )
            
        # Tombol hitung
        if st.button ("Hitung pH", key = "T2"):
            H_plus, pH = perhitungan_pH_asam_lemah(konsentrasi, konstanta_asam)
            st.write("[H+] =", round(H_plus, 4))
            st.write("pH =", round(pH, 2))
            st.success(f'pH asam adalah {pH:.2f}')


    elif selected2 == "Custom":
        st.subheader("Asam Kuat")
        # Masukkan konsentrasi
        konsentrasi = st.number_input("Masukkan konsentrasi (M)", format = "%.4f", step=0.0001, key = "H3")
        st.write("Konsentrasi = ", konsentrasi)

        # Masukkan valensi
        a = st.number_input("Masukkan valensi (a)", format = "%i", step=1, key = "A3")
        st.write("a = ", a)
                
        # Tombol hitung
        if st.button("Hitung pH", key = "B3"):
            H_plus, pH = perhitungan_pH_asam_kuat(konsentrasi, a)
            st.write("[H+] =", round(H_plus, 4))
            st.write("pH =", round(pH, 2))            
            st.success(f'pH asam adalah {pH:.2f}')


elif selected == "Konsentrasi Basa":
    st.title(":blue[Kalkulator pH Larutan]")
    st.subheader("Menghitung [OH-], pOH, dan pH dari Konsentrasi Basa Kuat dan Basa Lemah")

    selected3 = option_menu(None, ["Basa Kuat", "Basa Lemah", "Custom"], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "nav-link": {"font-size": "15px", "text-align": "center"},
        "nav-link-selected": {"background-color": "blue"}})

    if selected3 == "Basa Kuat":
        # Pilih senyawa basa kuat
        basa_kuat = {
            "Natrium Hidroksida (NaOH)": 1,
            "Litium Hidroksida (LiOH)": 1,
            "Kalium Hidroksida (KOH)": 1,
            "Rubidium Hidroksida (RbOH)": 1,
            "Cesium Hidroksida (CsOH)": 1,
            "Kalsium Hidroksida (Ca(OH)2)": 2,
            "Barium Hidroksida (Ba(OH)2)": 2,
            "Stronsium Hidroksida (Sr(OH)2)": 2,
            "Magnesium Hidroksida (Mg(OH)2)": 2
        }
    
        selected_basa_kuat = st.selectbox(
            "Pilih senyawa basa kuat", list(basa_kuat.keys()))
        a = basa_kuat[selected_basa_kuat]
        st.write("a = ", a)
    
        # Masukkan konsentrasi
        konsentrasi = st.number_input(
            "Masukkan konsentrasi (M)", format= "%.4f", step=0.0001, key = "H5")
        st.write("Konsentrasi = ", konsentrasi)
    
        # Tombol hitung
        if st.button("Hitung pH", key = "T5"):
            OH_minus, pOH, pH = perhitungan_pH_basa_kuat(konsentrasi, a)
            st.write("[OH-] =", round(OH_minus, 4))
            st.write("pOH =", round(pOH, 2))
            st.write("pH =", round(pH, 2))
            st.success(f'pH basa adalah {pH:.2f}')

    elif selected3 == "Basa Lemah":
        # Masukkan Kb
        konstanta_basa = st.number_input("Masukkan Kb", key = "K6")
        st.write("Kb = ", konstanta_basa)
    
        # Masukkan konsentrasi
        konsentrasi = st.number_input("Masukkan konsentrasi (M)", format = "%.4f", step=0.0001, key = "H6")
        st.write("Konsentrasi = ", konsentrasi)
        
        # Tombol hitung
        if st.button("Hitung pH", key = "T6"):
            OH_minus, pOH, pH = perhitungan_pH_basa_lemah(konsentrasi, konstanta_basa)
            st.write("[OH-] =", round(OH_minus, 4))
            st.write("pOH =", round(pOH, 2))
            st.write("pH =", round(pH, 2))
            st.success(f'pH basa adalah {pH:.2f}')
            
    elif selected3 == "Custom":
        st.subheader("Basa Kuat")
        
        # Masukkan konsentrasi
        konsentrasi = st.number_input("Masukkan konsentrasi (M)", format = "%.4f", step=0.0001, key = "H7")
        st.write("Konsentrasi = ", konsentrasi)
    
        # Masukkan valensi
        a = st.number_input("Masukkan valensi (a)", format = "%i", step=1, key = "A7")
        st.write("a = ", a)
                
        # Tombol hitung
        if st.button("Hitung pH", key = "B7"):
            OH_minus, pOH, pH = perhitungan_pH_basa_kuat(konsentrasi, a)
            st.write("[OH-] =", round(OH_minus, 4))
            st.write("pOH =", round(pOH, 2))
            st.write("pH =", round(pH, 2))
            st.success(f'pH basa adalah {pH:.2f}')
            

elif selected == "Massa dan Volume Asam":
    st.title(":blue[Kalkulator pH Larutan]")
    st.subheader("Menghitung [H+] dan pH dari Massa dan Volume Asam Kuat dan Asam Lemah")

    selected4 = option_menu(None, ["Asam Kuat", "Asam Lemah", "Custom"], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "nav-link": {"font-size": "15px", "text-align": "center"},
        "nav-link-selected": {"background-color": "blue"}})

    if selected4 == "Asam Kuat":
        # Pilih senyawa asam kuat
        asam_kuat = {
            "Asam Klorida (HCl)":(36.5, 1),
            "Asam Nitrat (HNO3)":(63, 1),
            "Asam Sulfat (H2SO4)":(98, 2),
            "Asam Bromida (HBr)":(81, 1),
            "Asam Bromit (HBrO3)":(129, 1),
            "Asam Perbromat (HBrO4)":(145, 1),
            "Asam Klorat (HClO3)":(84.5, 1),
            "Asam Perklorat (HClO4)":(100.46, 1),
            "Asam Iodida (HI)":(127.91, 1),
            "Asam Iodit (HIO3)":(175.91, 1),
            "Asam Periodat (HIO4)":(191.91, 1)
        }
    
        selected_asam_kuat = st.selectbox(
            "Pilih senyawa asam kuat", list(asam_kuat.keys()))
        BM = asam_kuat[selected_asam_kuat][0]
        a = asam_kuat[selected_asam_kuat][1]
        st.write("BM = ", BM, "g/mol") 
        st.write("a = ", a) 
        
        # Masukkan massa
        massa = st.number_input("Masukkan massa (g)", format= "%.4f", step=0.0001, key = "M9")
        st.write("Massa = ", massa)
    
        # Masukkan volume
        volume = st.number_input("Masukkan volume (mL)", key = "V9")
        st.write("Volume = ", volume)
    
        # Tombol hitung
        if st.button("Hitung pH", key = "T9"):
            # Konversi volume dari mL ke L
            volume_dalam_liter = volume / 1000
            H_plus, pH = perhitungan_pH_asam_kuat_dengan_massa_volume(massa, volume_dalam_liter, BM, a)
            st.write("[H+] =", round(H_plus, 4))
            st.write("pH =", round(pH, 2))
            st.success(f'pH asam adalah {pH:.2f}')

    if selected4 == "Asam Lemah":
        # Pilih senyawa asam lemah
        asam_lemah = {
            "Asam Asetat (CH3COOH)": 60,
            "Asam Fluorida (HF)": 20,
            "Asam Sianida (HCN)": 27,
            "Asam Sulfida (H2S)": 32,
            "Asam Sulfit (H2SO3)": 82.1,
            "Asam Fosfat (H3PO4)": 98,
            "Asam Karbonat (H2CO3)": 62,
            "Asam Hipoklorit (HClO)": 52.5,
            "Asam Nitrit (HNO2)": 47 
        }
        
        selected_asam_lemah = st.selectbox("Pilih senyawa asam lemah", list(asam_lemah.keys()))
        BM = asam_lemah[selected_asam_lemah]
        st.write("BM = ", BM, "g/mol") 
    
        # Masukkan Ka
        konstanta_asam = st.number_input("Masukkan Ka", key = "K10")
        st.write("Ka = ", konstanta_asam)
        
        # Masukkan massa
        massa = st.number_input("Masukkan massa (g)", format= "%.4f", step=0.0001, key = "M10")
        st.write("Massa = ", massa)
    
        # Masukkan volume
        volume = st.number_input("Masukkan volume (mL)", key = "V10")
        st.write("Volume = ", volume)
    
        # Tombol hitung
        if st.button("Hitung pH", key = "T10"):
            # Konversi volume dari mL ke L
            volume_dalam_liter = volume / 1000
            H_plus, pH = perhitungan_pH_asam_lemah_dengan_massa_volume(massa, volume_dalam_liter, BM, konstanta_asam)
            st.write("[H+] =", round(H_plus, 4))
            st.write("pH =", round(pH, 2))
            st.success(f'pH asam adalah {pH:.2f}')

    if selected4 == "Custom":
        options = ("Asam Kuat", "Asam Lemah")
        selection = st.selectbox("Pilih jenis senyawa", options=options)
        if selection == "Asam Kuat": 
            # Masukkan massa
            massa = st.number_input("Masukkan massa (g)", format= "%.4f", step=0.0001, key = "M11")
            st.write("Massa = ", massa)
        
            # Masukkan volume
            volume = st.number_input("Masukkan volume (mL)", key = "V11")
            st.write("Volume = ", volume)

            # Masukkan BM
            BM = st.number_input("Masukkan BM (g/mol)", key = "B11")
            st.write("BM = ", BM)

            # Masukkan valensi
            a = st.number_input("Masukkan valensi", format = "%i", step=1, key = "A11")
            st.write("a = ", a)
            
            # Tombol hitung
            if st.button("Hitung pH", key = "T11"):
                # Konversi volume dari mL ke L
                volume_dalam_liter = volume / 1000
                H_plus, pH = perhitungan_pH_asam_lemah_dengan_massa_volume(massa, volume_dalam_liter, BM, a)
                st.write("[H+] =", round(H_plus, 4))
                st.write("pH =", round(pH, 2))
                st.success(f'pH asam adalah {pH:.2f}')

        elif selection == "Asam Lemah":
            # Masukkan Ka
            konstanta_asam = st.number_input("Masukkan Ka", key = "K12")
            st.write("Ka = ", konstanta_asam)
        
            # Masukkan massa
            massa = st.number_input("Masukkan massa (g)", format= "%.4f", step=0.0001, key = "M12")
            st.write("Massa = ", massa)
        
            # Masukkan volume
            volume = st.number_input("Masukkan volume (mL)", key = "V12")
            st.write("Volume = ", volume)

            # Masukkan BM
            BM = st.number_input("Masukkan BM (g/mol)", key = "B12")
            st.write("BM = ", BM)
                
            # Tombol hitung
            if st.button("Hitung pH", key = "T12"):
                # Konversi volume dari mL ke L
                volume_dalam_liter = volume / 1000
                H_plus, pH = perhitungan_pH_asam_lemah_dengan_massa_volume(massa, volume_dalam_liter, BM, konstanta_asam)
                st.write("[H+] =", round(H_plus, 4))
                st.write("pH =", round(pH, 2))
                st.success(f'pH asam adalah {pH:.2f}')
                

elif selected == "Massa dan Volume Basa":
    st.title(":blue[Kalkulator pH Larutan]")
    st.subheader(
        "Menghitung [OH-], pOH, dan pH dari Massa dan Volume Basa Kuat dan Basa Lemah")

    selected5 = option_menu(None, ["Basa Kuat", "Basa Lemah", "Custom"], 
    menu_icon=None, default_index=0, orientation="horizontal",
    styles={
        "nav-link": {"font-size": "15px", "text-align": "center"},
        "nav-link-selected": {"background-color": "blue"}})

    if selected5 == "Basa Kuat":
        # Pilih senyawa basa kuat
        basa_kuat = {
            "Natrium Hidroksida (NaOH)":(40, 1),
            "Litium Hidroksida (LiOH)":(23.95, 1),
            "Kalium Hidroksida (KOH)":(56.1, 1),
            "Rubidium Hidroksida (RbOH)":(102.48, 1),
            "Cesium Hidroksida (CsOH)":(149.91, 1),
            "Kalsium Hidroksida (Ca(OH)2)":(74, 2),
            "Barium Hidroksida (Ba(OH)2)":(171.34, 2),
            "Stronsium Hidroksida (Sr(OH)2)":(121.63, 2),
            "Magnesium Hidroksida (Mg(OH)2)":(58.32, 2)
        }
        
        selected_basa_kuat = st.selectbox(
            "Pilih senyawa basa kuat", list(basa_kuat.keys()))
        BM = basa_kuat[selected_basa_kuat][0]
        a = basa_kuat[selected_basa_kuat][1]
        st.write("BM = ", BM, "g/mol") 
        st.write("a = ", a) 
        
        # Masukkan massa
        massa = st.number_input("Masukkan massa (g)", format= "%.4f", step=0.0001, key = "M13")
        st.write("Massa = ", massa)
    
        # Masukkan volume
        volume = st.number_input("Masukkan volume (mL)", key = "V13")
        st.write("Volume = ", volume)
    
        # Tombol hitung
        if st.button("Hitung pH", key = "T13"):
            # Konversi volume dari mL ke L
            volume_dalam_liter = volume / 1000
            OH_minus, pOH, pH = perhitungan_pH_basa_kuat_dengan_massa_volume(massa, volume_dalam_liter, BM, a)
            st.write("[OH-] =", round(OH_minus, 5))
            st.write("pOH =", round(pOH, 2))
            st.write("pH =", round(pH, 2))
            st.success(f'pH basa adalah {pH:.2f}')
    
    if selected5 == "Basa Lemah":

        # Pilih senyawa basa lemah
        basa_lemah = {
            "Ammonium Hidroksida (NH4OH)": 35,
            "Perak Hidroksida (AgOH)": 125,
            "Seng Hidroksida (Zn(OH)2)": 99.42, 
            "Nikel Hidroksida (Ni(OH)2)": 91,
            "Alluminium (III) Hidroksida (Al(OH)3)": 78,  
            "Bismuth Hidroksida (Bi(OH)3)": 260,
            "Besi (II) Hidroksida (Fe(OH)2)": 89.86,
            "Besi (III) Hidroksida (Fe(OH)3)": 107,
            "Kobalt (II) Hidroksida (Co(OH)2)": 92.95,
            "Kobalt (III) Hidroksida (Co(OH)3)": 109.96, 
            "Raksa (I) Hidroksida (HgOH)": 218,
            "Raksa (II) Hidroksida (Hg(OH)2)": 252,
            "Tembaga (I) Hidroksida (CuOH)": 80.5,
            "Tembaga (II) Hidroksida (Cu(OH)2)": 44.01
        }
        
        selected_basa_lemah = st.selectbox(
            "Pilih senyawa basa lemah", list(basa_lemah.keys()))
        BM = basa_lemah[selected_basa_lemah]
        st.write("BM = ", BM, "g/mol") 
    
        # Masukkan Kb
        konstanta_basa = st.number_input('Masukkan Kb', key = "K14")
        st.write("Kb = ", konstanta_basa)
        
        # Masukkan massa
        massa = st.number_input("Masukkan massa (g)", format= "%.4f", step=0.0001, key = "M14")
        st.write("Massa = ", massa)
    
        # Masukkan volume
        volume = st.number_input("Masukkan volume (mL)", key = "V14")
        st.write("Volume = ", volume)
        
        # Tombol hitung
        if st.button("Hitung pH", key = "T14"):
            # Konversi volume dari mL ke L
            volume_dalam_liter = volume / 1000
            OH_minus, pOH, pH = perhitungan_pH_basa_lemah_dengan_massa_volume(massa, volume_dalam_liter, BM, konstanta_basa)
            st.write("[OH-] =", round(OH_minus, 5))
            st.write("pOH =", round(pOH, 2))
            st.write("pH =", round(pH, 2))
            st.success(f'pH basa adalah {pH:.2f}')

    if selected5 == "Custom":
        options = ("Basa Kuat", "Basa Lemah")
        selection = st.selectbox("Pilih jenis senyawa", options=options)

        if selection == "Basa Kuat": 

            # Masukkan massa
            massa = st.number_input("Masukkan massa (g)", format= "%.4f", step=0.0001, key = "M15")
            st.write("Massa = ", massa)
        
            # Masukkan volume
            volume = st.number_input("Masukkan volume (mL)", key = "V15")
            st.write("Volume = ", volume)

            # Masukkan BM
            BM = st.number_input("Masukkan BM (g/mol)", key = "B15")
            st.write("BM = ", BM)
            
            # Masukkan valensi
            a = st.number_input("Masukkan valensi", format = "%i", step=1, key = "A15")
            st.write("a = ", a)
                    
            # Tombol hitung
            if st.button("Hitung pH", key = "T15"):
                # Konversi volume dari mL ke L
                volume_dalam_liter = volume / 1000
                OH_minus, pOH, pH = perhitungan_pH_basa_kuat_dengan_massa_volume(massa, volume_dalam_liter, BM, a)
                st.write("[OH-] =", round(OH_minus, 5))
                st.write("pOH =", round(pOH, 2))
                st.write("pH =", round(pH, 2))
                st.success(f'pH basa adalah {pH:.2f}')
                
        elif selection == "Basa Lemah":

            # Masukkan Kb
            konstanta_basa = st.number_input("Masukkan Kb", key = "K16")
            st.write("Kb = ", konstanta_basa)
            
            # Masukkan massa
            massa = st.number_input("Masukkan massa (g)", format= "%.4f", step=0.0001, key = "M16")
            st.write("Massa = ", massa)
            
            # Masukkan volume
            volume = st.number_input("Masukkan volume (mL)", key = "V16")
            st.write("Volume = ", volume)

            # Masukkan BM
            BM = st.number_input("Masukkan BM (g/mol)", key = "B16")
            st.write("BM = ", BM)
                
            # Tombol hitung
            if st.button("Hitung pH", key = "T16"):
                # Konversi volume dari mL ke L
                volume_dalam_liter = volume / 1000
                OH_minus, pOH, pH = perhitungan_pH_basa_lemah_dengan_massa_volume(massa, volume_dalam_liter, BM, konstanta_basa)
                st.write("[OH-] =", round(OH_minus, 5))
                st.write("pOH =", round(pOH, 2))
                st.write("pH =", round(pH, 2))
                st.success(f'pH basa adalah {pH:.2f}')


elif selected == "Tentang Aplikasi":
    selected6 = option_menu(None, ["Materi pH", "Cara Penggunaan", "Contoh Soal", "Kontak"], 
    icons=["book", "list-task", "journal-text", "envelope-open-heart"], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "nav-link": {"font-size": "15px", "text-align": "center"},
        "nav-link-selected": {"background-color": "blue"}})

    if selected6 == "Materi pH":
        #Apa itu pH
        st.header(":blue[Apa itu pH?]")
        st.markdown('<div style="text-align: justify;">pH (Potential of Hydrogen) adalah ukuran keasaman atau kebasaan suatu larutan kimia. pH adalah nilai numerik yang menyatakan seberapa asam atau basa suatu larutan cair.</div>', unsafe_allow_html=True)
       
        #Skala pH
        st.header(":blue[Skala pH]")
        st.write('Skala pH adalah skala logaritmik yang digunakan untuk menentukan keasaman atau kebasaan (alkalinitas) suatu larutan berair. Skalanya berkisar dari 0 hingga 14.')
        st.write('''
    - Larutan asam memiliki pH kurang dari 7. Semakin rendah pH, ​​semakin asam larutan tersebut. 
    - Larutan basa atau basa memiliki pH lebih besar dari 7. Semakin tinggi pH, semakin basa larutan tersebut. 
    - PH 7 dianggap netral, artinya tidak bersifat asam atau basa. Air murni biasanya dianggap netral, dengan pH 7. 
    ''')
        st.write('Asam meningkatkan konsentrasi ion hidrogen (H+) dalam larutan, sedangkan basa menurunkannya dengan menghasilkan ion hidroksida (OH−) yang bergabung dengan ion hidrogen menghasilkan air.')
        
        from PIL import Image
        st.image(
                "SKALAPH.jpg", width=500
                )
        
        #Rumus pH
        st.header(":blue[Rumus pH]")
        st.image(
                "RUMUSPH.jpg", width=500
                )
        
        #Cara Penggunaan
    elif selected6 == "Cara Penggunaan":
        st.header(":blue[Cara Menggunakan Kalkulator pH Larutan]")
        st.write('''Dari konsentrasi asam kuat:
1. Anda diberikan daftar beberapa senyawa asam kuat umum. Silakan pilih salah satunya.
2. Selanjutnya, masukkan konsentrasi dalam satuan molar (M).
3. Klik Hitung pH, alat ini akan segera menentukan [H+] dan pH dari ion Hidrogen.
4. Jika Anda tidak dapat menemukan senyawa asam kuat yang Anda inginkan dalam daftar opsi, pilih Custom. 
5. Sekarang, Anda harus memasukkan nilai valensi (a) beserta konsentrasinya. Alat akan menghitung nilai [H+] dan pH berdasarkan informasi yang diberikan.

Dari konsentrasi asam lemah:
1. Anda diminta untuk memasukkan nilai konstanta asam (Ka).
2. Selanjutnya, masukkan konsentrasi dalam satuan molar (M).
3. Klik Hitung pH, alat ini akan segera menentukan [H+] dan pH dari ion Hidrogen.

Dari konsentrasi basa kuat:
1. Anda diberikan daftar beberapa senyawa basa kuat umum. Silakan pilih salah satunya.
2. Selanjutnya, masukkan konsentrasi dalam satuan molar (M).
3. Klik Hitung pH, alat ini akan segera menentukan [OH-], pOH, dan pH dari ion Hidroksida.
4. Jika Anda tidak dapat menemukan senyawa basa kuat yang Anda inginkan dalam daftar opsi, pilih Custom. 
5. Sekarang, Anda harus memasukkan nilai valensi (a) beserta konsentrasinya. Alat akan menghitung nilai [OH-], pOH, dan pH berdasarkan informasi yang diberikan.

Dari konsentrasi basa lemah:
1. Anda diminta untuk memasukkan nilai konstanta basa (Kb).
2. Selanjutnya, masukkan konsentrasi dalam satuan molar (M).
3. Klik Hitung pH, alat ini akan segera menentukan [OH-], pOH, dan pH dari ion Hidrogen.

Dari massa dan volume asam kuat:
1. Anda diberikan daftar beberapa senyawa asam kuat umum. Silakan pilih salah satunya.
2. Selanjutnya, masukkan massa dalam satuan gram (g) dan masukkan volume dalam satuan mililiter (mL).
3. Klik Hitung pH, alat ini akan segera menentukan [H+] dan pH dari ion Hidrogen.
4. Jika Anda tidak dapat menemukan senyawa asam kuat yang Anda inginkan dalam daftar opsi, pilih Custom. 
5. Sekarang, Anda harus memasukkan nilai massa, volume, BM, dan valensi. Alat akan menghitung nilai [H+] dan pH berdasarkan informasi yang diberikan.

Dari massa dan volume asam lemah:
1. Anda diberikan daftar beberapa senyawa asam lemah umum. Silakan pilih salah satunya.
2. Selanjutnya, masukkan nilai konstanta asam (Ka), masukkan massa dalam satuan gram (g) dan masukkan volume dalam satuan mililiter (mL).
3. Klik Hitung pH, alat ini akan segera menentukan [H+] dan pH dari ion Hidrogen.
4. Jika Anda tidak dapat menemukan senyawa asam lemah yang Anda inginkan dalam daftar opsi, pilih Custom. 
5. Sekarang, Anda harus memasukkan nilai massa, volume, BM, dan konstanta asam. Alat akan menghitung nilai [H+] dan pH berdasarkan informasi yang diberikan.

Dari massa dan volume basa kuat:
1. Anda diberikan daftar beberapa senyawa basa kuat umum. Silakan pilih salah satunya.
2. Selanjutnya, masukkan massa dalam satuan gram (g) dan masukkan volume dalam satuan mililiter (mL).
3. Klik Hitung pH, alat ini akan segera menentukan [OH-], pOH, dan pH dari ion Hidrogen.
4. Jika Anda tidak dapat menemukan senyawa basa kuat yang Anda inginkan dalam daftar opsi, pilih Custom. 
5. Sekarang, Anda harus memasukkan nilai massa, volume, BM, dan valensi. Alat akan menghitung nilai [OH-], pOH, dan pH berdasarkan informasi yang diberikan.

Dari massa dan volume basa lemah:
1. Anda diberikan daftar beberapa senyawa basa lemah umum. Silakan pilih salah satunya.
2. Selanjutnya, masukkan nilai konstanta basa (Kb), masukkan massa dalam satuan gram (g) dan masukkan volume dalam satuan mililiter (mL).
3. Klik Hitung pH, alat ini akan segera menentukan [OH-], pOH, dan pH dari ion Hidrogen.
4. Jika Anda tidak dapat menemukan senyawa basa lemah yang Anda inginkan dalam daftar opsi, pilih Custom. 
5. Sekarang, Anda harus memasukkan nilai massa, volume, BM, dan konstanta basa. Alat akan menghitung nilai [OH-], pOH, dan pH berdasarkan informasi yang diberikan.
        ''')

    #Contoh Soal
    elif selected6 == "Contoh Soal":
        st.header(":blue[Contoh Soal 1]")
        st.write('''Suatu senyawa HNO3 memiliki konsentrasi sebesar 2x10^-3 M. Berapa pH larutan tersebut?
              
    Diketahui:
    Konsentrasi HNO3 = 2x10^-3 M
    Valensi ion H+ = 1

    Jawab:
    [H+] = M x a
    [H+] = 2x10^-3 M x 1
    [H+] = 2x10^-3

    pH = -log[H+]
    pH =-log 2x10^-3
    pH = 3-log 2
    pH = 2,70 
    ''')
        
        st.header(":blue[Contoh Soal 2]")
        st.write('''Larutan NaOH 0,05 M memiliki pH sebesar?
        
    Diketahui: 
    Konsentrasi NaOH = 0,05 M
    Valensi ion OH- = 1
        
    Jawab:
    [OH-] = M x a
    [OH-] = 0,05 M x 1
    [OH-] = 5x10^-2
        
    pOH = -log [OH-]
    pOH = -log (5x10^-2)
    pOH = 2-log 5
    pOH = 1,30

    pH = 14-pOH
    pH = 14-1,30
    pH = 12,7
    ''')
        
        st.markdown('---')
        st.write('Soal lainnya dapat diakses dengan mengklik tautan dibawah ini.')
        st.write("[Tautan](https://drive.google.com/drive/folders/1_NOPmnEaZKHsPQHVr6ITyha8-J7rQYrF?usp=sharing)")
        
    #Kontak
    elif selected6 == "Kontak":
        st.header(":blue[Hubungi Kami]")
        st.write("Silahkan tinggalkan pesan Anda pada kolom yang tersedia.")
        contact_from = """
        <form action="https://formsubmit.co/riskamaulidya818@gmail.com" method="POST">
            <input type="email" name="email" placeholder="Email Anda" required>
            <textarea name="message" placeholder="Pesan Anda"></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_from, unsafe_allow_html=True)
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
                
        local_css("D:\kalkulator_ph_larutan\style.css")
