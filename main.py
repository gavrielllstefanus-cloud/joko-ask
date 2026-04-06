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
            <source src="data:audio/mp3;base64={b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)

# --- CSS TAMPILAN MODERN ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .joko-header {
        text-align: center;
        font-family: 'Arial Black', sans-serif;
        font-size: 60px;
        color: #202124;
        margin-top: 40px;
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

st.markdown('<div class="joko-header">JOKO SEARCH</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #5f6368; margin-bottom: 30px;'>Pusat Informasi Terpercaya (Katanya).</p>", unsafe_allow_html=True)

# Layout Input & Tombol Sejajar
col_space, col_input, col_btn, col_space2 = st.columns([1, 4, 0.6, 1])

with col_input:
    query = st.text_input("", placeholder="Tuliskan rahasia yang ingin Anda tahu...", label_visibility="collapsed")

with col_btn:
    search_clicked = st.button("🔍")

# --- LOGIKA SEARCH ---
if search_clicked:
    if query:
        with st.spinner('Sedang mencari jawaban...'):
            time.sleep(1.2)
        
        # Eksekusi Hasil
        try:
            play_audio("sound.mp3")
            with open("sticker.png", "rb") as f:
                img_data = f.read()
                img_b64 = base64.b64encode(img_data).decode()
                st.markdown(f'<img src="data:image/png;base64,{img_b64}" class="hasil-joko">', unsafe_allow_html=True)
        except Exception as e:
            st.error("Pastikan file sound.mp3 dan sticker.png sudah ada di GitHub!")
            
        st.balloons()
    else:
        st.info("Ketik dulu pertanyaannya, Mas!")

st.markdown("<br><br><p style='text-align: center; font-size: 11px; color: #bdc1c6;'>© 2026 JOKO SEARCH</p>", unsafe_allow_html=True)
