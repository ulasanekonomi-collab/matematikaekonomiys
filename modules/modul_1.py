import streamlit as st

def render():
    st.title("📌 Modul 1: Teori Himpunan (*Set Theory*)")
    st.caption("Fondasi Matematika Ekonomi berdasarkan Pendekatan Alpha C. Chiang")
    
    st.info("""
    💡 **Landasan Konsep:** Himpunan (*Set*) adalah kumpulan objek-objek terdefinisi dengan jelas. 
    Dalam ekonomi, himpunan digunakan untuk mengelompokkan agen ekonomi, batas-batas pilihan, hingga himpunan strategi.
    """)
    
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
           * *Contoh:* $S = \{ {Rupiah, Dollar, Yen, Euro} }$
        2. **Cara Deskripsi / Set-Builder Method:** Menyebutkan syarat keanggotaannya.
           * *Contoh:* $S = \{ x \mid x \text{ adalah mata uang utama dunia} \}$
        """)
        
        st.markdown("---")
        st.subheader("Finite Set vs. Infinite Set")
        
        col1, col2 = st.columns(2)
        with col1:
            st.success("🔢 **Himpunan Terhingga (*Finite Set*)**")
            st.write("Jumlah anggotanya terbatas dan dapat dihitung pasti.")
            st.latex(r"A = \{ x \mid x \text{ adalah BUMN di Indonesia} \}")
            st.caption("Jumlah perusahaan BUMN terbatas.")
            
        with col2:
            st.warning("♾️ **Himpunan Tak Hingga (*Infinite Set*)**")
            st.write("Jumlah anggotanya tidak terbatas/kontinu.")
            st.latex(r"P = \{ p \mid p > 0 \}")
            st.caption("Himpunan harga $p$ yang mungkin bernilai kontinu dari 0 hingga tak terhingga.")

    # ==========================================
    # TAB 2: HUBUNGAN ANTAR HIMPUNAN
    # ==========================================
    with tab2:
        st.subheader("2. Hubungan Antar Himpunan (*Set Relations*)")
        st.markdown("""
        * **Subset ($A \subseteq B$):** Setiap elemen $A$ juga merupakan elemen $B$.
        * **Proper Subset ($A \subset B$):** $A$ adalah subset $B$, dan $A \neq B$.
        * **Equal Sets ($A = B$):** $A \subseteq B$ dan $B \subseteq A$.
        * **Disjoint Sets ($A \cap B = \emptyset$):** Dua himpunan yang tidak memiliki satu pun anggota yang sama.
        """)
        
        # Interaktif Sederhana
        st.markdown("---")
        st.markdown("### 🧪 Uji Hubungan Ekonomi:")
        opsi_relasi = st.selectbox(
            "Pilih Contoh Hubungan Himpunan Ekonomi:",
            [
                "Himpunan Mobil Listrik vs Himpunan Otomotif (Subset)",
                "Himpunan Barang Normal vs Himpunan Barang Inferior (Disjoint)"
            ]
        )
        
        if "Subset" in opsi_relasi:
            st.info("💡 **Penjelasan:** Semua produsen mobil listrik ($A$) adalah produsen otomotif ($B$), maka $A \subset B$.")
        else:
            st.info("💡 **Penjelasan:** Suatu barang tidak bisa menjadi barang normal sekaligus inferior pada tingkat pendapatan yang sama, maka $A \cap B = \emptyset$.")

    # ==========================================
    # TAB 3: OPERASI PADA HIMPUNAN
    # ==========================================
    with tab3:
        st.subheader("3. Operasi pada Himpunan (*Set Operations*)")
        st.markdown("Misalkan kita memiliki dua kelompok konsumen pasar:")
        
        # Interactive Set Operations
        set_A = {"Produsen A", "Produsen B", "Produsen C"}
        set_B = {"Produsen C", "Produsen D", "Produsen E"}
        
        st.write(f"* **Himpunan Pasar X (A):** `{set_A}`")
        st.write(f"* **Himpunan Pasar Y (B):** `{set_B}`")
        
        op = st.radio("Pilih Operasi Himpunan:", ["Gabungan (Union: A ∪ B)", "Irisan (Intersection: A ∩ B)", "Selisih (Difference: A - B)"])
        
        if "Union" in op:
            res = set_A.union(set_B)
            st.success(f"**Hasil Gabungan ($A \\cup B$):** `{res}`")
            st.caption("Semua produsen yang beroperasi di Pasar X ATAU Pasar Y.")
        elif "Intersection" in op:
            res = set_A.intersection(set_B)
            st.success(f"**Hasil Irisan ($A \\cap B$):** `{res}`")
            st.caption("Produsen yang beroperasi di Pasar X SEKALIGUS Pasar Y.")
        else:
            res = set_A.difference(set_B)
            st.success(f"**Hasil Selisih ($A \\setminus B$):** `{res}`")
            st.caption("Produsen yang HANYA beroperasi di Pasar X tetapi tidak di Pasar Y.")

    # ==========================================
    # TAB 4: ATURAN / HUKUM HIMPUNAN
    # ==========================================
    with tab4:
        st.subheader("4. Hukum Operasi Himpunan (*Laws of Set Operations*)")
        st.markdown("""
        Seperti halnya aljabar biasa, aljabar himpunan mengikuti hukum-hukum berikut:

        | Nama Hukum | Operasi Gabungan ($\cup$) | Operasi Irisan ($\cap$) |
        | :--- | :--- | :--- |
        | **Komutatif** | $A \cup B = B \cup A$ | $A \cap B = B \cap A$ |
        | **Asosiatif** | $(A \cup B) \cup C = A \cup (B \cup C)$ | $(A \cap B) \cap C = A \cap (A \cap C)$ |
        | **Distributif** | $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$ | $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ |
        | **De Morgan** | $(A \cup B)^c = A^c \cap B^c$ | $(A \cap B)^c = A^c \cup B^c$ |
        """)
        
        st.markdown("---")
        st.subheader("🧠 Refleksi Sederhana")
        st.text_area("Menurut Anda, mengapa Hukum De Morgan penting saat kita ingin mengevaluasi kelompok masyarakat yang 'TIDAK menerima bantuan A maupun bantuan B'?", height=100)
