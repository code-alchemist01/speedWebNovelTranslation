import os
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
from urllib.parse import urljoin
import time

def chunk_text(text, chunk_size=3000):
    """Metni küçük parçalara ayır."""
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

def fetch_chapter(url, retries=3):
    """Bölüm içeriğini çek ve URL'yi döndür."""
    for attempt in range(retries):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            chapter_content = soup.find('div', {'class': 'chr-c', 'id': 'chr-content'})
            next_button = soup.find('a', {'class': 'btn btn-success', 'id': 'next_chap'})
            
            # İçeriği al
            text = chapter_content.get_text(strip=True, separator='\n') if chapter_content else None
            if not text:
                print(f"Uyarı: {url} bölüm içeriği bulunamadı.")
            
            # Sonraki bölüm URL'sini al
            next_url = next_button['href'] if next_button else None
            if next_url:
                next_url = urljoin(url, next_url)  # Eksik URL'yi tamamla
            
            return text, next_url
        
        # Yeniden denemeden önce bekleyin
        print(f"Sayfa çekilemedi, {attempt + 1}/{retries} tekrar denenecek...")
        time.sleep(5)
    
    # Tüm denemeler başarısızsa
    return None, None

def translate_text(text):
    """Metni parçalara ayırıp çevir."""
    if not text:
        print("Uyarı: Çevrilecek metin boş.")
        return ""
    
    chunks = chunk_text(text)  # Metni parçalara ayır
    translated_text = ""
    
    for chunk in chunks:
        translated_chunk = GoogleTranslator(source='auto', target='tr').translate(chunk)
        if translated_chunk:
            translated_text += translated_chunk
        else:
            print("Çeviri hatası: Boş metin döndü.")
    
    return translated_text

def save_chapter(chapter_num, text):
    """Çevrilen metni kaydet."""
    os.makedirs("Bölümler", exist_ok=True)
    file_path = os.path.join("Bölümler", f"bolum{chapter_num}.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

def main():
    url = "https://novelbin.com/b/renegade-immortal/chapter-683"  # Başlangıç URL'si
    chapter_num = 683  # Bölüm numarası
    
    while url:
        print(f"Bölüm {chapter_num} işleniyor...")
        
        # Bölümü çek ve çevir
        text, next_url = fetch_chapter(url)
        if not text:
            print("Bölüm çekilemedi, işlem sonlandırılıyor.")
            break
        
        translated_text = translate_text(text)
        save_chapter(chapter_num, translated_text)
        print(f"Bölüm {chapter_num} kaydedildi.")
        
        # Sonraki bölüme geç
        url = next_url
        chapter_num += 1
        
    print("Tüm bölümler işlendi.")

if __name__ == "__main__":
    main()
