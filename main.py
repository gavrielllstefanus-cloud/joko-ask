import streamlit as st
import time
import base64
import os

# --- CONFIG ---
st.set_page_config(page_title="JOKO SEARCH", page_icon="🔍")

# Fungsi Audio Otomatis
def play_audio(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
                <audio autoplay="true">
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                """
            st.markdown(md, unsafe_allow_html=True)

# --- CSS TAMPILAN ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .joko-header {
        text-align: center;
        font-family: 'Arial Black', sans-serif;
        font-size: 45px;
        color: #202124;
        margin-bottom: 20px;
    }
    .stTextInput > div > div > input {
        border-radius: 24px 0 0 24px !important;
        padding: 25px !important;
    }
    div.stButton > button {
        background-color: #1a73e8 !important;
        color: white !important;
        border-radius: 0 24px 24px 0 !important;
        height: 52px !important;
        width: 60px !important;
        border: none !important;
        margin-top: 0px !important;
    }
    .hasil-joko {
        display: block;
        margin: 20px auto;
        max-width: 100%;
        border-radius: 10px;
        animation: slideIn 0.8s ease-out;
    }
    @keyframes slideIn {
        0% { transform: translateX(-100%); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)

# --- FOTO HEADER (BISIK.PNG) ---
if os.path.exists("bisik.png"):
    st.image("bisik.png", use_container_width=True)
else:
    st.warning("File 'bisik.png' belum ada di GitHub kamu, Faldo!")

st.markdown('<div class="joko-header">JOKO SEARCH</div>', unsafe_allow_html=True)

# --- INPUT & TOMBOL ---
c1, c2, c3, c4 = st.columns([1, 4, 0.7, 1])
with c2:
    query = st.text_input("", placeholder="Tuliskan rahasia yang ingin Anda cari...", label_visibility="collapsed")
with c3:
    search_clicked = st.button("🔍")

# --- LOGIKA SEARCH ---
if search_clicked:
    if query:
        with st.spinner('Menghubungi pusat data...'):
            time.sleep(1)
        
        # Putar Suara
        play_audio("sound.mp3")

        # Munculkan Sticker
        if os.path.exists("sticker.png"):
            with open("sticker.png", "rb") as f:
                img_data = f.read()
                img_b64 = base64.b64encode(img_data).decode()
                st.markdown(f'<img src="data:image/png;base64,{img_b64}" class="hasil-joko">', unsafe_allow_html=True)
        else:
            st.warning("### 🤫 YO NDAK TAU KOK TANYA SAYA!")
            
        st.balloons()
    else:
        st.info("Ketik sesuatu dulu, Mas!")
