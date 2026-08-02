import streamlit as st

def render():
    st.title("📌 Modul 1: Teori Himpunan (Set Theory)")
    st.caption("Fondasi Matematika Ekonomi berdasarkan Pendekatan Alpha C. Chiang")
    
    # BANNER MOTIVASI / URGENSI
    st.info("""
    💡 **Pertanyaan Mendasar:** *Mengapa Ekonom Harus Memahami Teori Himpunan?*
    
    Teori himpunan bukan sekadar topik matematika murni, melainkan **bahasa dasar untuk membangun kerangka berpikir ekonomi**. Sebelum ekonom bisa mengukur ($quantitative$), ia harus mampu mendefinisikan dan mengelompokkan ($qualitative/logical$).
    """)
    
    # EXPANDER: KEGUNAAN PENELITIAN & DECISION MAKING
    with st.expander("🎯 **Mengapa Teori Himpunan Penting dalam Penelitian & Decision Making? (Klik untuk membuka)**", expanded=True):
        col_res, col_dec = st.columns(2)
        
        with col_res:
            st.markdown("### 🔬 1. Dalam Penelitian (*Research*)")
            st.markdown("""
            * **Mendefinisikan Ruang Analisis (*Domain*):** Menentukan batas nilai variabel yang valid (misal: investasi $I \ge 0$, konsumsi $C \ge 0$).
            * **Partisi Data Sosial-Ekonomi:** Membagi data populasi besar menjadi *subset-subset* saling lepas untuk menghitung tingkat kemiskinan, kemiskinan ekstrem, atau ketimpangan.
            * **Aksioma Teori Ekonomi:** Landasan teori preferensi konsumen dan teori permainan (*Game Theory*) sepenuhnya dibangun dari aksioma himpunan.
            """)
            
        with col_dec:
            st.markdown("### 🎯 2. Dalam Pengambilan Keputusan (*Decision Making*)")
            st.markdown("""
            * **Memetakan Batas Pilihan (*Feasible Set*):** Keputusan optimal adalah memilih elemen terbaik dari himpunan yang sanggup dijangkau ($x \in X$).
            * **Targeting Kebijakan Publik:** Menentukan kriteria keanggotaan penerima subsidi/bansos. Kesalahan targeting secara matematis adalah kekeliruan menentukan *subset* dan *komplemen*.
            * **Ruang Strategi & Risiko:** Memetakan seluruh kemungkinan aksi lawan dan variabel luar dalam pemodelan kebijakan/bisnis.
            """)

    st.markdown("---")

    # TAB UTAMA CHIANG
    tab1, tab2, tab3, tab4 = st.tabs([
        "1. Definisi & Notasi", 
        "2. Hubungan Antar Himpunan", 
        "3. Operasi Himpunan", 
        "4. Aturan / Hukum Himpunan"
    ])
    
    # ==========================================
    # TAB 1: DEFINISI & NOTASI
    # ==========================================
    with tab1:
        st.subheader("1. Penulisan Himpunan & Jenis Sifatnya")
        st.markdown("""
        Alpha Chiang menjelaskan dua cara utama menuliskan himpunan:
        1. **Cara Enumerasi / Roster Method:** Menyebutkan seluruh anggotanya satu per satu.
           * *Contoh:* S = {Rupiah, Dollar, Yen, Euro}
        2. **Cara Deskripsi / Set-Builder Method:** Menyebutkan syarat keanggotaannya.
           * *Contoh:* S = {x | x adalah mata uang utama dunia}
        """)
        
        st.markdown("---")
        st.subheader("Finite Set vs. Infinite Set")
        
        col1, col2 = st.columns(2)
        with col1:
            st.success("🔢 **Himpunan Terhingga (Finite Set)**")
            st.write("Jumlah anggotanya terbatas dan dapat dihitung pasti.")
            st.latex(r"A = \{ x \mid x \text{ adalah BUMN di Indonesia} \}")
            st.caption("Jumlah perusahaan BUMN terbatas.")
            
        with col2:
            st.warning("♾️ **Himpunan Tak Hingga (Infinite Set)**")
            st.write("Jumlah anggotanya tidak terbatas/kontinu.")
            st.latex(r"P = \{ p \mid p > 0 \}")
            st.caption("Himpunan harga p yang mungkin bernilai kontinu dari 0 hingga tak terhingga.")

    # ==========================================
    # TAB 2: HUBUNGAN ANTAR HIMPUNAN
    # ==========================================
    with tab2:
        st.subheader("2. Hubungan Antar Himpunan (Set Relations)")
        st.markdown("""
        * **Subset (A ⊆ B):** Setiap elemen A juga merupakan elemen B.
        * **Proper Subset (A ⊂ B):** A adalah subset B, dan A ≠ B.
        * **Equal Sets (A = B):** A ⊆ B dan B ⊆ A.
        * **Disjoint Sets (A ∩ B = ∅):** Dua himpunan yang tidak memiliki satu pun anggota yang sama.
        """)
        
        st.markdown("---")
        st.subheader("🧪 Uji Hubungan Ekonomi:")
        opsi_relasi = st.selectbox(
            "Pilih Contoh Hubungan Himpunan Ekonomi:",
            [
                "Himpunan Mobil Listrik vs Himpunan Otomotif (Subset)",
                "Himpunan Barang Normal vs Himpunan Barang Inferior (Disjoint)"
            ]
        )
        
        if "Subset" in opsi_relasi:
            st.info("💡 **Penjelasan:** Semua produsen mobil listrik (A) adalah produsen otomotif (B), maka A ⊂ B.")
        else:
            st.info("💡 **Penjelasan:** Suatu barang tidak bisa menjadi barang normal sekaligus inferior pada tingkat pendapatan yang sama, maka A ∩ B = ∅.")

    # ==========================================
    # TAB 3: OPERASI PADA HIMPUNAN
    # ==========================================
    with tab3:
        st.subheader("3. Operasi pada Himpunan (Set Operations)")
        st.markdown("Misalkan kita memiliki dua kelompok konsumen pasar:")
        
        set_A = {"Produsen A", "Produsen B", "Produsen C"}
        set_B = {"Produsen C", "Produsen D", "Produsen E"}
        
        st.write(f"* **Himpunan Pasar X (A):** `{set_A}`")
        st.write(f"* **Himpunan Pasar Y (B):** `{set_B}`")
        
        op = st.radio("Pilih Operasi Himpunan:", [
            "Gabungan (Union: A ∪ B)", 
            "Irisan (Intersection: A ∩ B)", 
            "Selisih (Difference: A \\ B)"
        ])
        
        if "Union" in op:
            res = set_A.union(set_B)
            st.success(f"**Hasil Gabungan (A ∪ B):** `{res}`")
            st.caption("Semua produsen yang beroperasi di Pasar X ATAU Pasar Y.")
        elif "Intersection" in op:
            res = set_A.intersection(set_B)
            st.success(f"**Hasil Irisan (A ∩ B):** `{res}`")
            st.caption("Produsen yang beroperasi di Pasar X SEKALIGUS Pasar Y.")
        else:
            res = set_A.difference(set_B)
            st.success(f"**Hasil Selisih (A \\ B):** `{res}`")
            st.caption("Produsen yang HANYA beroperasi di Pasar X tetapi tidak di Pasar Y.")

    # ==========================================
    # TAB 4: ATURAN / HUKUM HIMPUNAN
    # ==========================================
    with tab4:
        st.subheader("4. Hukum Operasi Himpunan (Laws of Set Operations)")
        st.markdown("""
        Seperti halnya aljabar biasa, aljabar himpunan mengikuti hukum-hukum berikut:

        | Nama Hukum | Operasi Gabungan (∪) | Operasi Irisan (∩) |
        | :--- | :--- | :--- |
        | **Komutatif** | A ∪ B = B ∪ A | A ∩ B = B ∩ A |
        | **Asosiatif** | (A ∪ B) ∪ C = A ∪ (B ∪ C) | (A ∩ B) ∩ C = A ∩ (B ∩ C) |
        | **Distributif** | A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C) | A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) |
        | **De Morgan** | (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ | (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ |
        """)
        
        st.markdown("---")
        st.subheader("🧠 Refleksi Sederhana")
        st.text_area("Menurut Anda, mengapa Hukum De Morgan penting saat kita ingin mengevaluasi kelompok masyarakat yang 'TIDAK menerima bantuan A maupun bantuan B'?", height=100)
