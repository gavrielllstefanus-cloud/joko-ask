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

# --- CSS BIAR LOGO DI KANAN ---
st.markdown("""
    <style>
    .stApp {
        background-color: #ffffff;
    }
    .joko-header {
        text-align: center;
        font-family: 'Arial Black', sans-serif;
        font-size: 60px;
        color: #202124;
        margin-top: 40px;
    }
    /* Gabungin Input & Tombol di satu baris */
    .search-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        margin-bottom: 20px;
    }
    /* Kotak Input */
    .stTextInput > div > div > input {
        border-radius: 24px 0 0 24px !important;
        border-right: none !important;
        padding: 25px !important;
        font-size: 16px !important;
    }
    /* Tombol Search di Kanan dengan Logo */
    div.stButton > button {
        background-color: #1a73e8 !important;
        color: white !important;
        border-radius: 0 24px 24px 0 !important;
        height: 52px !important;
        width: 60px !important;
        border: none !important;
        margin-top: 0px !important;
    }
    @keyframes slideFromLeft {
        0% { transform: translateX(-100%); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
    .hasil-joko {
        animation: slideFromLeft 0.8s ease-out;
        display: block;
        margin: 30px auto;
        max-width: 400px;
        border-radius: 12px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- TAMPILAN ---
st.markdown('<div class="joko-header">JOKO SEARCH</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #5f6368; margin-bottom: 30px;'>Pusat Informasi Terpercaya (Katanya).</p>", unsafe_allow_html=True)

# Bikin kolom buat nyatuin input & tombol
col_space, col_input, col_btn, col_space2 = st.columns([1, 4, 0.6, 1])

with col_input:
    query = st.text_input("", placeholder="Tuliskan rahasia yang ingin Anda tahu...", label_visibility="collapsed")

with col_btn:
    # Pak
