import streamlit as st

def render():
    st.title("🌐 Modul 0.1: Realita dan Model")
    st.caption("Matematika Ekonomi: Dari Intuisi ke Formalisasi")
    st.markdown("---")

    # Layout 2 Kolom untuk Hook Pembuka agar lebih compact
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.subheader("💡 Pertanyaan Pembuka")
        st.write(
            "Bayangkan Anda ingin berpergian di sebuah kota metropolitan. "
            "Apakah Anda membutuhkan peta yang menggambarkan *setiap detail* kota, "
            "mulai dari tinggi gedung, warna cat rumah, hingga posisi setiap pohon?"
        )
        
        ans = st.radio(
            "Mana yang lebih berguna untuk navigasi Anda?",
            ["Peta super detail (seperti dunia nyata)", "Peta garis sederhana yang hanya memuat jalur jalan"],
            index=1,
            key="hook_radio"
        )

    with col2:
        st.write("##") # Spacing
        if ans:
            st.info(
                "💡 **Esensi Model:**\n\n"
                "Peta yang berguna justru peta yang **membuang detail tidak penting** "
                "agar kita bisa fokus pada tujuannya (rute jalan)."
            )

    st.markdown("---")

    # --- SIMULATOR ---
    st.subheader("🛠️ Simulator: Tingkat Abstraksi Peta")
    st.write("Coba geser slider di bawah untuk melihat bagaimana realitas disederhanakan menjadi model.")

    level = st.select_slider(
        "Pilih Tingkat Abstraksi Model:",
        options=["Level 1: Realitas", "Level 2: Peta Jalan", "Level 3: Skema Topologi"],
        value="Level 1: Realitas"
    )

    # Menggunakan layout kolom untuk menyandingkan gambar dan penjelasan
    img_col, txt_col = st.columns([3, 2])

    if level == "Level 1: Realitas":
        with img_col:
            st.image(
                "https://upload.wikimedia.org/wikipedia/commons/9/97/The_Earth_seen_from_Apollo_17.jpg", 
                use_container_width=True
            )
        with txt_col:
            st.warning("📸 **Level 1: Foto Udara/Satelit**")
            st.write("Sangat detail dan kaya informasi, tetapi rumit dan membingungkan jika hanya digunakan untuk mencari rute jalan cepat.")

    elif level == "Level 2: Peta Jalan":
        with img_col:
            st.image(
                "https://jsp.co.id/wp-content/uploads/2018/07/tempat-belajar-drone-terbaik-2.jpg", 
                use_container_width=True
            )
        with txt_col:
            st.success("🗺️ **Level 2: Peta Jalan Vektor**")
            st.write("Menghilangkan detail warna bangunan & vegetasi. Hanya menyisakan garis jalan, arah, dan nama tempat penting.")

    elif level == "Level 3: Skema Topologi":
        with img_col:
            st.image(
                "https://jogjakini.wordpress.com/wp-content/uploads/2009/03/peta-jogja2_resize_resize.jpg?w=1119&h=1397", 
                use_container_width=True
            )
        with txt_col:
            st.info("🚉 **Level 3: Skema Jalur MRT**")
            st.write("Bentuk geografis dan jarak riil diabaikan total. Hanya mempertahankan **relasi/koneksi** antar stasiun.")

    st.markdown("---")

    # --- FORMALISASI & REFLEKSI ---
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.subheader("📚 Dari Peta ke Ekonomi")
        st.markdown("""
        Sama halnya dengan peta, **model ekonomi bukanlah gambaran riil yang fotografis**, melainkan bentuk **penyederhanaan yang disengaja** (*deliberate simplification*).

        * **Realitas Ekonomi:** Kompleks dan riuh. Setiap detik ada jutaan keputusan individu, perubahan cuaca, preferensi, hingga suasana hati pembeli.
        * **Model Ekonomi:** Mengisolasi variabel kunci. Kita memilih untuk hanya menyoroti hubungan mendasar (misal: *Harga* vs *Jumlah Permintaan*).
        * **Peran *Ceteris Paribus*:** Seperti mematikan 'suara latar' di peta agar garis jalan terlihat jelas. Kita menganggap variabel lain di luar model bernilai tetap (*all else being equal*).
        """)

    with col_b:
        st.subheader("🧠 Refleksi")
        st.write("Mengapa model ekonomi yang baik TIDAK HARUS memasukkan semua variabel dunia nyata?")
        st.text_area("Tuliskan pendapat singkat Anda:", placeholder="Misal: Agar mempermudah pemahaman relasi inti...", height=100)
