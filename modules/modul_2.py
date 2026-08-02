import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def render():
    st.title("Modul 2: Relasi, Fungsi, dan Pola Perilaku Ekonomi")
    st.caption("Berbasis Referensi: Alpha C. Chiang - Fundamental Methods of Mathematical Economics (Bab 2)")

    st.markdown("""
    Pada modul ini, kita melangkah dari sekadar mengelompokkan data (Teori Himpunan) menuju **pemetaan hubungan sebab-akibat** melalui **Fungsi**. 
    Fungsi adalah alat matematis utama untuk memodelkan pola perilaku para pelaku ekonomi.
    """)

    # Membagi Modul 2 menjadi 4 Tab Interaktif
    tab1, tab2, tab3, tab4 = st.tabs([
        "1. Domain, Range & Variabel", 
        "2. Lab Pola Perilaku (Polinomial)", 
        "3. Digresi Eksponen & Non-Aljabar", 
        "4. Invers Fungsi & Konvensi Marshall"
    ])

    # =========================================================================
    # TAB 1: DOMAIN, RANGE & PEMETAAN VARIABEL
    # =========================================================================
    with tab1:
        st.header("1. Pasangan Terurut, Domain, dan Range")
        st.markdown("""
        Di Modul 1, himpunan $\{a, b\}$ bersifat *unordered*. Namun dalam fungsi, kita membutuhkan **Pasangan Terurut (Ordered Pairs)** $(x, y)$ 
        di mana order/urutan sangat menentukan posisi dan makna ekonomisnya.
        """)

        col1, col2 = st.columns([1, 1])

        with col1:
            st.subheader("💡 Konsep Utama")
            st.write("**Domain ($X$):** Daerah asal $\\rightarrow$ Tempat **Variabel Eksogen** (bebas/penentu).")
            st.write("**Range ($Y$):** Daerah hasil $\\rightarrow$ Tempat **Variabel Endogen** (terikat/yang dijelaskan).")
            
            st.info("""
            **Restriksi Ekonomi vs Matematika Murni:**
            Secara matematis, $x$ bisa bernilai negatif $(-\\infty, \\infty)$. Namun dalam ekonomi, 
            kuantitas produksi ($Q$) dan harga ($P$) umumnya dibatasi pada kuadran I: **$P \\ge 0, Q \\ge 0$**.
            """)

            # Interactive Input
            st.markdown("---")
            st.subheader("🎮 Simulator Pemetaan")
            p_val = st.slider("Tentukan Harga ($P$ - Eksogen):", min_value=0, max_value=100, value=20, step=5)
            # Contoh fungsi permintaan sederhana Q = 150 - 1.5P
            q_val = max(0, 150 - 1.5 * p_val)
            st.success(f"Hasil Pemetaan: Jika $P = {p_val}$, maka Kuantitas Permintaan ($Q$ - Endogen) $= {q_val}$")
            st.caption(f"Bentuk Ordered Pair: $(P, Q) = ({p_val}, {q_val})$")

        with col2:
            st.subheader("📈 Visualisasi Ruang Ekonomi (Kuadran I)")
            fig, ax = plt.subplots(figsize=(5, 4))
            
            # Plot Kurva Permintaan
            p_arr = np.linspace(0, 100, 200)
            q_arr = np.maximum(0, 150 - 1.5 * p_arr)
            
            ax.plot(p_arr, q_arr, color='tab:blue', linewidth=2, label=r'$Q = 150 - 1.5P$')
            ax.plot(p_val, q_val, 'ro', markersize=8, label=f'Titik Terpilih ({p_val}, {q_val})')
            
            ax.axhline(0, color='black', linewidth=1)
            ax.axvline(0, color='black', linewidth=1)
            ax.set_xlim(-10, 110)
            ax.set_ylim(-10, 160)
            ax.set_xlabel("Harga ($P$) [Domain / Eksogen]")
            ax.set_ylabel("Kuantitas ($Q$) [Range / Endogen]")
            ax.set_title("Pemetaan Domain ke Range")
            ax.grid(True, linestyle='--', alpha=0.5)
            ax.legend()
            st.pyplot(fig)

    # =========================================================================
    # TAB 2: LAB POLA PERILAKU (POLINOMIAL)
    # =========================================================================
    with tab2:
        st.header("2. Bentuk Fungsi & Pola Perilaku Ekonomi")
        st.markdown("Bentuk matematis fungsi merepresentasikan **pola perilaku** sistem ekonomi yang kita amati.")

        fungsi_type = st.selectbox(
            "Pilih Jenis Perilaku Ekonomi / Bentuk Fungsi:",
            [
                "Fungsi Konstan (Statis / Otonom)",
                "Fungsi Linear (Laju Perubahan Tetap / Marginal Konstan)",
                "Fungsi Kuadratik (Titik Optimum / Parabola)",
                "Fungsi Kubik (S-Curve / Law of Diminishing Returns)"
            ]
        )

        col_param, col_graph = st.columns([1, 1.2])

        x = np.linspace(0, 10, 200)

        with col_param:
            st.subheader("⚙️ Parameter Fungsi")
            if "Konstan" in fungsi_type:
                c_val = st.slider("Nilai Konstanta ($c$):", 0, 100, 50)
                y = np.full_like(x, c_val)
                st.latex(rf"y = f(x) = {c_val}")
                st.write("**Interpretasi Ekonomi:** Menggambarkan variabel yang bersifat otonom (tidak dipengaruhi variabel lain), seperti *Investasi Otonom* ($I_0$) atau *Pajak Lump-sum* ($T_0$).")

            elif "Linear" in fungsi_type:
                a_val = st.slider("Intersep ($a$):", 0, 50, 10)
                b_val = st.slider("Kemiringan / Slope ($b$):", -10, 10, 2)
                y = a_val + b_val * x
                st.latex(rf"y = {a_val} + {b_val}x")
                st.write("**Interpretasi Ekonomi:** Menunjukkan hubungan dengan perubahan marginal yang konstan. Contoh: Fungsi Konsumsi Keynesian $C = a + bY$.")

            elif "Kuadratik" in fungsi_type:
                a_val = st.slider("Konstanta ($a$):", -50, 50, 0)
                b_val = st.slider("Koefisien $x$ ($b$):", -20, 20, 10)
                c_val = st.slider("Koefisien $x^2$ ($c$):", -5.0, 5.0, -1.0, step=0.5)
                y = a_val + b_val * x + c_val * (x**2)
                st.latex(rf"y = {a_val} + {b_val}x + ({c_val})x^2")
                st.write("**Interpretasi Ekonomi:** Memodelkan perilaku dengan titik puncak/lembah (optimum). Contoh: Kurva Total Revenue ($TR$) atau Utilitas Total.")

            elif "Kubik" in fungsi_type:
                a_val = st.slider("Intersep ($a$ - Biaya Tetap):", 0, 50, 15)
                b_val = st.slider("Koefisien $x$ ($b$):", -10.0, 10.0, -3.0, step=0.5)
                c_val = st.slider("Koefisien $x^2$ ($c$):", 0.0, 5.0, 1.5, step=0.1)
                d_val = st.slider("Koefisien $x^3$ ($d$):", 0.01, 1.0, 0.1, step=0.01)
                y = a_val + b_val * x + c_val * (x**2) + d_val * (x**3)
                st.latex(rf"y = {a_val} + ({b_val})x + {c_val}x^2 + {d_val}x^3")
                st.write("**Interpretasi Ekonomi:** Perilaku fleksibel berbentuk huruf $S$. Sangat klasik digunakan untuk pemodelan **Total Cost (TC)** jangka pendek yang mencerminkan *Hukum Hasil Lebih yang Semakin Berkurang*.")

        with col_graph:
            fig, ax = plt.subplots(figsize=(6, 4.5))
            ax.plot(x, y, color='crimson', linewidth=2.5)
            ax.set_xlabel("Variabel Eksogen ($x$)")
            ax.set_ylabel("Variabel Endogen ($y$)")
            ax.set_title(f"Grafik {fungsi_type.split('(')[0]}")
            ax.grid(True, linestyle='--', alpha=0.6)
            st.pyplot(fig)

    # =========================================================================
    # TAB 3: DIGRESI EKSPONEN & NON-ALJABAR
    # =========================================================================
    with tab3:
        st.header("3. Fungsi Non-Aljabar & Aturan Eksponen")
        st.markdown("""
        Dalam dinamika ekonomi, banyak fenomena bertumbuh secara kontinu (seperti bunga majemuk, inflasi, atau pertumbuhan penduduk). 
        Untuk ini, kita menggunakan **Fungsi Eksponensial** $y = b^x$ atau $y = A e^{rt}$.
        """)

        col_exp1, col_exp2 = st.columns([1, 1])

        with col_exp1:
            st.subheader("📈 Simulator Pertumbuhan Eksponensial")
            y0 = st.number_input("Nilai Awal ($A_0$):", value=100)
            rate = st.slider("Tingkat Pertumbuhan ($r$ in %):", 0.0, 20.0, 5.0) / 100
            t_max = st.slider("Periode Waktu ($t$):", 1, 30, 10)

            t = np.linspace(0, t_max, 100)
            y_exp = y0 * np.exp(rate * t)
            y_lin = y0 * (1 + rate * t)  # pembanding linear

            fig2, ax2 = plt.subplots(figsize=(5, 3.5))
            ax2.plot(t, y_exp, color='green', linewidth=2, label='Eksponensial Continuous')
            ax2.plot(t, y_lin, color='gray', linestyle='--', label='Linear Simple')
            ax2.set_xlabel("Waktu ($t$)")
            ax2.set_ylabel("Nilai ($Y$)")
            ax2.legend()
            ax2.grid(True, alpha=0.3)
            st.pyplot(fig2)

        with col_exp2:
            st.subheader("📚 Aturan Dasar Eksponen (Exponent Rules)")
            st.markdown("""
            Sebelum melangkah ke fungsi Cobb-Douglas ($Q = A K^\\alpha L^\\beta$), penguasaan sifat eksponen adalah wajib:
            """)
            st.latex(r"1.\quad x^a \cdot x^b = x^{a+b}")
            st.latex(r"2.\quad \frac{x^a}{x^b} = x^{a-b}")
            st.latex(r"3.\quad (x^a)^b = x^{ab}")
            st.latex(r"4.\quad x^{-a} = \frac{1}{x^a}")
            st.latex(r"5.\quad x^0 = 1 \quad (x \neq 0)")

            st.success("💡 **Aplikasi Ekonomi:** Sifat nomor 1 dan 2 sangat krusial saat menghitung *Marginal Product* ($MP_L$ dan $MP_K$) dalam teori produksi!")

    # =========================================================================
    # TAB 4: INVERS FUNGSI & KONVENSI MARSHALL
    # =========================================================================
    with tab4:
        st.header("4. Fungsi Invers & Konvensi Marshallian")
        st.markdown("""
        Salah satu keunikan dalam ilmu ekonomi adalah **Konvensi Marshall**. 
        Secara matematis, fungsi permintaan ditulis $Q = f(P)$ di mana $P$ adalah variabel bebas (sumbu horizontal). 
        Namun, Alfred Marshall menyajikan kurva dengan $P$ di sumbu vertikal, yang secara matematis merupakan **Fungsi Invers** $P = f^{-1}(Q)$.
        """)

        st.subheader("🔄 Modul Peralihan Sumbu Grafik")
        mode = st.radio(
            "Pilih Tampilan Grafik:",
            ["Perspektif Matematika Murni: Q = f(P)", "Konvensi Ekonomi (Marshallian): P = f⁻¹(Q)"]
        )

        a_m = 100
        b_m = 2

        fig3, ax3 = plt.subplots(figsize=(6, 3.5))

        if "Matematika" in mode:
            # P di sumbu X, Q di sumbu Y
            p_vals = np.linspace(0, 50, 100)
            q_vals = a_m - b_m * p_vals
            ax3.plot(p_vals, q_vals, color='purple', linewidth=2)
            ax3.set_xlabel("Harga ($P$) $\\rightarrow$ Variabel Bebas (Domain)")
            ax3.set_ylabel("Kuantitas ($Q$) $\\rightarrow$ Variabel Terikat (Range)")
            ax3.set_title("Pendekatan Matematis Standar ($Q = 100 - 2P$)")
        else:
            # Q di sumbu X, P di sumbu Y
            q_vals = np.linspace(0, 100, 100)
            p_vals = (a_m - q_vals) / b_m
            ax3.plot(q_vals, p_vals, color='darkorange', linewidth=2)
            ax3.set_xlabel("Kuantitas ($Q$) $\\rightarrow$ Sumbu Horizontal")
            ax3.set_ylabel("Harga ($P$) $\\rightarrow$ Sumbu Vertikal")
            ax3.set_title("Konvensi Ekonomi Marshallian ($P = 50 - 0.5Q$)")

        ax3.grid(True, linestyle='--', alpha=0.5)
        st.pyplot(fig3)

        st.info("""
        **Kesimpulan Reflektif:** 
        Meskipun kita menggambar $P$ di sumbu vertikal, kita harus tetap ingat bahwa dalam teori permintaan pasar, **Harga ($P$) adalah variabel eksogen** yang menentukan keputusan kuantitas pembeli ($Q$).
        """)
# =====================================================================
        # SEKUENS PEDAGOGIS: HIMPUNAN -> RELASI -> SIFAT -> MANFAAT EKONOMI
        # =====================================================================
        st.markdown("---")
        st.subheader("🔗 Sekuens Logis: Dari Himpunan ke Keputusan Ekonomi")
        st.markdown("""
        Bagaimana Teori Himpunan bertransformasi menjadi alat pengambilan keputusan? 
        Pilih skenario studi kasus di bawah ini untuk melihat alur pembentukannya secara rinci:
        """)

        skenario = st.selectbox(
            "Pilih Studi Kasus Implementasi:",
            [
                "Kasus A: Preferensi Konsumen & Rasionalitas (Teori Perilaku)",
                "Kasus B: Kelayakan Kredit Bank (Skoring Risiko)",
                "Kasus C: Pemetaan Pemasok & Rantai Pasok (Supply Chain)"
            ]
        )

        if "Kasus A" in skenario:
            st.markdown("### 🧪 Studi Kasus A: Preferensi Konsumen (Rasionalitas)")
            
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                st.markdown("**1. Himpunan ($S$)**")
                st.info("""
                Himpunan Bundel Barang yang tersedia di pasar:
                
                $A = (2\\text{ Kopi}, 1\\text{ Roti})$  
                $B = (1\\text{ Kopi}, 3\\text{ Roti})$  
                $C = (2\\text{ Kopi}, 2\\text{ Roti})$
                """)
            
            with c2:
                st.markdown("**2. Relasi ($\succsim$)**")
                st.info("""
                Relasi Preferensi:  
                * "Setidaknya sama disukai dengan" ($\succsim$).
                
                Memetakan pasangan terurut $(A, B)$ dalam produk kartesius $S \times S$.
                """)

            with c3:
                st.markdown("**3. Sifat Relasi**")
                st.info("""
                Aksioma Rasionalitas:
                * **Refleksif:** $A \succsim A$
                * **Transitif:** Jika $A \succsim B$ dan $B \succsim C$, maka $A \succsim C$.
                * **Lengkap (Complete):** Mampu membandingkan opsi apa pun.
                """)

            with c4:
                st.markdown("**4. Manfaat Ekonomi**")
                st.success("""
                **Fungsi Utilitas $U(x)$:**  
                Memungkinkan kita mengurutkan preferensi ke dalam skala numerik $U(A) \ge U(B)$, menjadi dasar pembentukan **Kurva Indiferen** dan pemaksimalan kepuasan konsumen.
                """)

        elif "Kasus B" in skenario:
            st.markdown("### 💳 Studi Kasus B: Evaluasi Kelayakan Kredit Bank")
            
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                st.markdown("**1. Himpunan**")
                st.info("""
                * $D$: Himpunan Debitur
                * $R$: Himpunan Tingkat Risiko $\{ \text{Rendah}, \text{Sedang}, \text{Tinggi} \}$
                """)
            
            with c2:
                st.markdown("**2. Relasi ($K$)**")
                st.info("""
                Relasi Kelayakan Kredit:  
                $(d, r) \in K$ jika debitur $d$ memiliki profil keuangan yang sesuai dengan risiko $r$.
                """)

            with c3:
                st.markdown("**3. Sifat Relasi**")
                st.info("""
                * **Fungsional (Many-to-One):** Setiap debitur $d$ **harus** dipetakan ke **tepat satu** kategori risiko $r$ (Domain unik). Tidak boleh ambigu.
                """)

            with c4:
                st.markdown("**4. Manfaat Ekonomi**")
                st.success("""
                **Manajemen Risiko & Suku Bunga:**  
                Bank dapat menentukan *Risk-Based Pricing* (suku bunga kredit yang disesuaikan dengan tingkatan risiko debitur secara otomatis dan objektif).
                """)

        elif "Kasus C" in skenario:
            st.markdown("### 🚚 Studi Kasus C: Hirarki Pemasok (Supply Chain)")
            
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                st.markdown("**1. Himpunan ($P$)**")
                st.info("""
                Himpunan Perusahaan Pemasok bahan baku dalam industri manufaktur:  
                $P = \{ P_1, P_2, P_3, P_4 \}$
                """)
            
            with c2:
                st.markdown("**2. Relasi ($\le$)**")
                st.info("""
                Relasi Efisiensi Biaya:  
                $(P_1, P_2) \in R$ jika biaya pasokan $P_1$ lebih murah atau sama dengan $P_2$.
                """)

            with c3:
                st.markdown("**3. Sifat Relasi**")
                st.info("""
                * **Anti-simetris:** Jika $P_1 \le P_2$ dan $P_2 \le P_1$, maka $P_1 = P_2$.
                * **Transitif:** Jika $P_1 \le P_2$ dan $P_2 \le P_3$, maka $P_1 \le P_3$.
                * **Poset (Partial Order Set)**.
                """)

            with c4:
                st.markdown("**4. Manfaat Ekonomi**")
                st.success("""
                **Pengadaan Optimal (Procurement):**  
                Manajer operasional dapat membuat struktur hirarki pengadaan (Diagram Hasse) untuk menentukan *Tier-1* dan *Tier-2 Supplier* demi efisiensi struktur biaya produksi.
                """)
