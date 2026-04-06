import streamlit as st
import time
import base64

# --- CONFIG ---
st.set_page_config(page_title="JOKO SEARCH", page_icon="🔍")

# Fungsi Audio Otomatis
def play_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)

# --- CSS BIAR GAK DOWNGRADE ---
st.markdown("""
    <style>
    .stApp {
        background-color: #ffffff;
    }
    .joko-header {
        text-align: center;
        font-family: 'Arial Black', sans-serif;
        font-size: 70px;
        color: #202124;
        margin-top: 50px;
        margin-bottom: 10px;
    }
    /* Kotak Input Gede */
    .stTextInput > div > div > input {
        border-radius: 24px;
        padding: 20px;
        border: 1px solid #dfe1e5;
        font-size: 18px;
    }
    /* Tombol Search Biru Gede */
    div.stButton > button {
        background-color: #1a73e8;
        color: white;
        border-radius: 8px;
        width: 200px;
        height: 50px;
        font-weight: bold;
        display: block;
        margin: 0 auto;
    }
    div.stButton > button:hover {
        background-color: #1765cc;
        color: white;
    }
    @keyframes slideFromLeft {
        0% { transform: translateX(-100%); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
    .hasil-joko {
        animation: slideFromLeft 1s ease-out;
        display: block;
        margin: 30px auto;
        max-width: 100%;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- TAMPILAN ---
st.markdown('<div class="joko-header">JOKO SEARCH</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #70757a;'>Cari apa saja, jawabannya tetap rahasia.</p>", unsafe_allow_html=True)

# Input Box (Bisa ngetik panjang)
query = st.text_input("", placeholder="Ketik pertanyaan mautmu di sini...", label_visibility="collapsed")

st.markdown("<br>", unsafe_allow_html=True)

# Tombol SEARCH (Pasti Kelihatan di Tengah)
if st.button("CARI JAWABAN"):
    if query:
        with st.spinner('Mencari di seluruh database negara...'):
            time.sleep(1.5)
        
        # Bunyi Suara
        try:
            play_audio("sound.mp3")
        except:
            st.error("File 'sound.mp3' ilang, Faldo!")

        # Muncul Gambar Geser
        try:
            with open("sticker.png", "rb") as f:
                img_data = f.read()
                img_b64 = base64.b64encode(img_data).decode()
                st.markdown(f'<img src="data:image/png;base64,{img_b64}" class="hasil-joko">', unsafe_allow_html=True)
        except:
            st.warning("### YO NDAK TAU KOK TANYA SAYA!")
            
        st.balloons()
    else:
        st.warning("Tulis dulu pertanyaannya dong!")

st.markdown("<br><br><p style='text-align: center; font-size: 12px; color: #999;'>© 2026 JOKO SEARCH - Powered by Ketidaktahuan</p>", unsafe_allow_html=True)
