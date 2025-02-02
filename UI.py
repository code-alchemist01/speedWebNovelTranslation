import os
import streamlit as st

# Bölüm dosyalarını alıp sıralama
def list_chapters():
    """Bölümler klasöründeki mevcut bölüm dosyalarını listeler."""
    chapters_dir = "Bölümler"
    if not os.path.exists(chapters_dir):
        st.error("Bölümler klasörü bulunamadı!")
        return []

    # Bölüm dosyalarını al ve numaralarına göre sıralar (örneğin: bolum1.txt, bolum2.txt, ...)
    chapter_files = [f for f in os.listdir(chapters_dir) if f.endswith('.txt')]
    chapter_files.sort(key=lambda x: int(x.replace('bolum', '').replace('.txt', '')))  # Sayısal sıralama
    return chapter_files

# Bölüm içeriğini gösterme
def show_chapter_content(chapter_name):
    """Seçilen bölümün içeriğini gösterir."""
    file_path = os.path.join("Bölümler", chapter_name)
    with open(file_path, "r", encoding="utf-8") as file:
        chapter_content = file.read()

    # Bölüm başlığını şık bir şekilde gösterme
    st.markdown(f"<h2 style='text-align: center; color: #1abc9c; font-family: 'Roboto', sans-serif; font-size: 36px; text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);'>{chapter_name} İçeriği</h2>", unsafe_allow_html=True)

    # Bölüm içeriğini her paragrafı yeni bir satır ile göstermek için işleme
    content_lines = chapter_content.split('\n')

    # Her paragrafı ekleyelim
    for line in content_lines:
        if line.strip():  # Boş satırlardan kaçın
            st.markdown(f"<p style='font-size: 20px; line-height: 1.8; text-align: justify; font-family: 'Georgia', serif; color: #34495e; margin-bottom: 10px;'>{line.strip()}</p>", unsafe_allow_html=True)
        else:
            st.markdown("<br>", unsafe_allow_html=True)  # Paragraflar arasında boşluk bırakma

# Streamlit arayüzü
def main():
    st.set_page_config(page_title="Renaged Immortal Türkçe", page_icon="📖", layout="wide")

    # Genel arka plan rengi
    st.markdown("""
    <style>
    body {
        background: linear-gradient(45deg, #f3f4f9, #dbe3e5);
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .reportview-container {
        background: linear-gradient(45deg, #f3f4f9, #dbe3e5);
    }
    .sidebar .sidebar-content {
        background-color: #1abc9c;
        color: white;
        padding: 20px;
    }
    .stButton>button {
        background-color: #1abc9c;
        color: white;
        font-size: 18px;
        border-radius: 8px;
        padding: 12px 24px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background-color: #16a085;
    }
    </style>
    """, unsafe_allow_html=True)

    # Başlık
    st.markdown("<h1 style='text-align: center; color: #1abc9c; font-family: 'Roboto', sans-serif; font-size: 48px; text-shadow: 3px 3px 12px rgba(0, 0, 0, 0.2);'>Renaged Immortal Türkçe Çeviri</h1>", unsafe_allow_html=True)

    # Bölümleri listele
    chapters = list_chapters()

    if chapters:
        st.write(f"Toplam {len(chapters)} Bölüm Bulundu.")

        # Bölüm seçim butonları oluştur
        chapter_num = st.selectbox("Bir bölüm seçin:", range(1, len(chapters) + 1))

        # Seçilen bölümü getir
        if chapter_num:
            selected_chapter = chapters[chapter_num - 1]
            show_chapter_content(selected_chapter)
    else:
        st.write("Hiç bölüm bulunamadı. Bölümler klasörünü kontrol edin.")

if __name__ == "__main__":
    main()
