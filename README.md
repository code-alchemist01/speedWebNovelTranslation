# Novel Turkish Translation

This project is an application that automatically fetches, translates, and displays chapters of any given novel through a user interface.

## Features

- Fetch chapters from the web
- Translate chapters into Turkish
- Save translated chapters to the local file system
- Display chapters using a Streamlit-based user interface

## Requirements

- Python 3.x
- Required Python libraries: requests, beautifulsoup4, deep_translator, streamlit

## Installation
1. Clone this repository to your local machine.

2. Install the required Python libraries: pip install requests beautifulsoup4 deep_translator streamlit

## Usage

1. Run the translat.py file to fetch and translate chapters. Specify the starting URL in the translat.py file:
python translat.py

2. Run the UI.py file to start the user interface:
streamlit run UI.py



# Novel Türkçe Çeviri

Bu proje, verilen herhangi bir romanın bölümlerini otomatik olarak çeken, çeviren ve bir kullanıcı arayüzü aracılığıyla görüntüleyen bir uygulamadır.

## Özellikler

- Web'den roman bölümlerini çekme
- Bölümleri Türkçeye çevirme
- Çevrilen bölümleri yerel dosya sistemine kaydetme
- Streamlit tabanlı kullanıcı arayüzü ile bölümleri görüntüleme

## Gereksinimler

- Python 3.x
- Gerekli Python kütüphaneleri: `requests`, `beautifulsoup4`, `deep_translator`, `streamlit`

## Kurulum

1. Bu depoyu yerel makinenize klonlayın.
2. Gerekli Python kütüphanelerini yükleyin:
   ```pip install requests beautifulsoup4 deep_translator streamlit ```

# Kullanım

1. translat.py dosyasını çalıştırarak bölümleri çekin ve çevirin. Başlangıç URL'sini translat.py dosyasında belirtin:
python translat.py

2. UI.py dosyasını çalıştırarak kullanıcı arayüzünü başlatın:
streamlit run UI.py
