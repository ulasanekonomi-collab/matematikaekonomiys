import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="MathEcon - Realita dan Model", layout="wide")

# Header Modul
st.title("🌐 Modul 0.1: Realita dan Model")
st.caption("Bagaimana Matematika Ekonomi Menyaring Kerumitan Dunia Nyata")

# --- FASE 1: INTUISI ---
with st.expander("💡 1. Pertanyaan Pemantik (Klik untuk Membaca)", expanded=True):
    st.write("""
    Bayangkan Anda ingin membeli Kopi. Di dunia nyata, keputusan Anda dipengaruhi oleh **banyak sekali hal**: 
    harga kopi, isi dompet, cuaca hari ini, diskon, hingga suasana hati (*mood*).
    
    Jika semua hal itu dimasukkan ke dalam rumus sekaligus, matematikanya akan menjadi sangat rumit. 
    **Model Ekonomi** hadir bukan untuk mencatat seluruh dunia nyata, melainkan untuk **menyaring pola utamanya**.
    """)

st.divider()

# --- FASE 2: SIMULATOR INTERAKTIF ---
st.subheader("🛠️ 2. Simulator: Dari Data Acak Realita ke Garis Model")

col_control, col_chart = st.columns([1, 2])

with col_control:
    st.markdown("### Control Panel")
    
    # Toggle Mode Realita vs Model
    mode = st.radio(
        "Pilih Mode Tampilan:",
        ["Dunia Nyata (Banyak Variabel)", "Model Ekonomi (Ceteris Paribus)"]
    )
    
    st.markdown("---")
    st.markdown("**Pengaturan Parameter Model ($Q_d = a - bP$):**")
    
    # Slider Parameter
    a_param = st.slider("Faktor Otonom / Non-Harga (a)", min_value=50, max_value=200, value=100, step=10,
                        help="Menampung semua faktor dunia nyata selain harga (Pendapatan, Selera, dll)")
    b_param = st.slider("Sensitivitas Harga (b)", min_value=0.5, max_value=5.0, value=2.0, step=0.5,
                        help="Kemiringan kurva permintaan")

with col_chart:
    # Generate Data Simulasi
    np.random.seed(42)
    prices = np.linspace(5, 40, 30)
    
    # Data Ideal (Model)
    q_model = a_param - (b_param * prices)
    q_model = np.maximum(q_model, 0) # Pastikan tidak negatif
    
    # Data Acak (Realita - dipengaruhi cuaca, mood, dll)
    noise = np.random.normal(0, 15, size=len(prices))
    q_real = q_model + noise
    q_real = np.maximum(q_real, 0)

    fig = go.Figure()

    if mode == "Dunia Nyata (Banyak Variabel)":
        # Plot titik-titik data acak realita
        fig.add_trace(go.Scatter(
            x=prices, y=q_real,
            mode='markers',
            name='Data Riil Pasar (Noise)',
            marker=dict(size=10, color='crimson', opacity=0.7)
        ))
        fig.update_layout(
            title="Dunia Nyata: Titik Data Kompleks & Acak",
            xaxis_title="Harga Kopi (P)",
            yaxis_title="Jumlah Terbeli (Q)",
            template="plotly_white"
        )
    else:
        # Plot Garis Model Mulus
        fig.add_trace(go.Scatter(
            x=prices, y=q_model,
            mode='lines',
            name=f'Model: Qd = {a_param} - {b_param}P',
            line=dict(color='royalblue', width=4)
        ))
        # Tampilkan juga bayangan data riil dengan transparansi
        fig.add_trace(go.Scatter(
            x=prices, y=q_real,
            mode='markers',
            name='Data Asal',
            marker=dict(size=6, color='gray', opacity=0.3)
        ))
        fig.update_layout(
            title=f"Model Ekonomi: Sederhana & Terpola (Ceteris Paribus)",
            xaxis_title="Harga Kopi (P)",
            yaxis_title="Jumlah Terbeli (Qd)",
            template="plotly_white"
        )

    st.plotly_chart(fig, use_container_width=True)

# --- FASE 3: FORMALISASI MATEMATIKA ---
st.divider()
st.subheader("📐 3. Formalisasi Matematika (Gaya Alpha Chiang)")

col_math1, col_math2 = st.columns(2)

with col_math1:
    st.markdown("#### A. Dari Fungsi Umum ke Fungsi Spesifik")
    st.latex(r"1.\ \text{Fungsi Umum (Kompleks): } Q_d = f(P, Y, P_r, T)")
    st.latex(r"2.\ \text{Asumsi Ceteris Paribus: Bekukan } Y, P_r, T \rightarrow \bar{Y}, \bar{P_r}, \bar{T}")
    st.latex(r"3.\ \text{Model Linear Spesifik: } Q_d = a - bP")

with col_math2:
    st.markdown("#### B. Anatomi Parameter Model")
    st.write(f"""
    * **$Q_d$ (Variabel Endogen)**: Kuantitas permintaan yang dihitung di dalam model.
    * **$P$ (Variabel Eksogen)**: Harga barang yang menjadi pemicu utama.
    * **$a = {a_param}$ (Konstanta Otonom)**: Menggabungkan efek semua variabel di luar harga ($\bar{{Y}}, \bar{{T}}, \dots$). Geser slider **a** di atas untuk melihat garis bergeser!
    * **$b = {b_param}$ (Parameter Sensitivitas)**: Tingkat kecuraman hubungan harga dan permintaan.
    """)

# --- FASE 4: TANTANGAN & REFLEKSI ---
st.divider()
st.subheader("🎯 4. Kuis Refleksi Singkat")

q_ans = st.radio(
    "Jika iklan kopi secara masif membuat selera masyarakat meningkat tajam (Faktor Selera T naik), perubahan apa yang terjadi pada model matematika kita?",
    [
        "Nilai b membesar (kurva makin curam)",
        "Nilai a membesar (seluruh garis bergeser ke kanan atas)",
        "Harga P otomatis turun"
    ]
)

if st.button("Cek Jawaban"):
    if q_ans == "Nilai a membesar (seluruh garis bergeser ke kanan atas)":
        st.success("🎉 Tepat sekali! Selera (T) adalah variabel non-harga yang ditampung di dalam konstanta otonom 'a'. Ketika T naik, nilai 'a' membesar dan seluruh garis permintaan bergeser ke kanan.")
    else:
        st.error("Kurang tepat. Ingat, perubahan selera adalah faktor non-harga. Faktor ini ditampung dalam konstanta otonom 'a'. Coba geser slider 'a' di simulator untuk membuktikannya!")
