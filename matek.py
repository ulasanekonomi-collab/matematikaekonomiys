import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

st.set_page_config(page_title="Modul 0.1: Realita & Model", layout="centered")

st.title("🌐 Modul 0.1: Realita dan Model")
st.caption("Matematika Ekonomi: Dari Intuisi ke Formalisasi")

st.markdown("---")

# --- 1. HOOK ---
st.subheader("💡 Pertanyaan Pembuka")
st.write(
    "Bayangkan Anda ingin berpergian di sebuah kota metropolitan. "
    "Apakah Anda membutuhkan peta yang menggambarkan *setiap detail* kota, "
    "mulai dari tinggi gedung, warna cat rumah, hingga posisi setiap pohon?"
)

ans = st.radio(
    "Mana yang lebih berguna untuk navigasi Anda?",
    ["Peta super detail (seperti dunia nyata)", "Peta garis sederhana yang hanya memuat jalur jalan"],
    index=1
)

if ans:
    st.info(
        "💡 **Pikirkan ini:** Peta yang berguna justru peta yang **membuang detail tidak penting** "
        "agar kita bisa fokus pada tujuannya (rute jalan). Inilah esensi dari sebuah **Model**!"
    )

st.markdown("---")

# --- 2. SIMULATOR ---
st.subheader("🛠️ Simulator: Tingkat Abstraksi Peta")
st.write("Coba geser slider di bawah untuk melihat bagaimana realitas yang kompleks disederhanakan menjadi model.")

level = st.slider("Pilih Tingkat Abstraksi Model:", min_value=1, max_value=3, value=1, step=1)

if level == 1:
    st.markdown("### 📸 Level 1: Realitas Asli (Foto Satelit / Kompleks)")
    # Menggunakan URL Unsplash khusus gambar lanskap kota satelit yang stabil
    st.image("https://inet.detik.com/science/d-7352338/ribuan-satelit-mengorbit-bumi-kok-tidak-tabrakan", caption="Kompleksitas Dunia Nyata: Penuh detail gedung, vegetasi, dan kontur bumi.")
    st.warning("🔍 **Karakteristik:** Sangat detail dan kaya informasi, tetapi membingungkan dan rumit jika digunakan untuk analisis cepat.")

elif level == 2:
    st.markdown("### 🗺️ Level 2: Peta Jalan (Model Sederhana)")
    # Gambar peta jalan vektor yang bersih
    st.image("https://images.unsplash.com/photo-1524661135-423995f22d0b?w=800", caption="Abstraksi Jalan Raya: Hanya memuat garis jalan utama.")
    st.success("✅ **Karakteristik:** Menghilangkan detail warna bangunan & posisi pohon. Hanya menyisa garis jalan dan nama tempat penting.")

elif level == 3:
    st.markdown("### 🚉 Level 3: Peta Jalur Transportasi / Topologi (Model Sangat Abstrak)")
    
    # Membuat Grafik Vektor Skema MRT langsung dengan Python
    fig, ax = plt.subplots(figsize=(6, 3))
    G = nx.Graph()
    G.add_edges_from([("Stasiun A", "Stasiun B"), ("Stasiun B", "Stasiun C"), ("Stasiun C", "Stasiun D"), ("Stasiun B", "Stasiun E")])
    pos = {"Stasiun A": (0, 0), "Stasiun B": (1, 0), "Stasiun C": (2, 0), "Stasiun D": (3, 0), "Stasiun E": (1, 1)}
    
    nx.draw(G, pos, ax=ax, with_labels=True, node_color='skyblue', node_size=2000, font_size=9, font_weight='bold', edge_color='red', width=3)
    ax.set_title("Diagram Skematis Rute Kereta", fontsize=11)
    
    st.pyplot(fig)
    st.info("⚡ **Karakteristik:** Bentuk geografis jalan dan jarak riil diabaikan total. Hanya mempertahankan **relasi/koneksi** antar titik stasiun.")

st.markdown("---")

# --- 3. FORMALISASI & JEMBATAN KE EKONOMI ---
st.subheader("📚 Dari Peta ke Ekonomi")
st.markdown("""
Sama seperti peta, **Model Ekonomi** bukanlah gambaran utuh dari seluruh ekonomi dunia nyata yang sangat rumit. 

1. **Realitas Ekonomi:** Jutaan orang bertransaksi tiap detik dengan ribuan alasan (cuaca, suasana hati, harga, gengsi, dll).
2. **Model Ekonomi:** Kita **menyederhanakan** realitas dengan membuang faktor yang kurang relevan dan memfokuskan perhatian pada hubungan variabel utama.
3. **Asumsi *Ceteris Paribus*:** Anggapan bahwa "faktor lain dianggap tetap/diabaikan". Sama seperti peta jalan yang 'mengabaikan' posisi pohon di pinggir jalan.
""")

# --- 4. REFLEKSI ---
st.markdown("---")
st.subheader("🧠 Refleksi")
st.write("Mengapa model ekonomi yang baik TIDAK HARUS memasukkan semua variabel dunia nyata?")
st.text_area("Tuliskan pendapat singkat Anda di sini:", placeholder="Misal: Karena tujuan model adalah mempermudah analisis...")
