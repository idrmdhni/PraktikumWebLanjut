# ✨ PraktikumWebLanjut

[![HTML](https://img.shields.io/badge/language-HTML-blue)](https://www.w3.org/html/)
[![Python](https://img.shields.io/badge/language-Python-yellow)](https://www.python.org/)

## 📝 Artikel Web – Django Project

Halo! Saya Mohammad Indra Ramadhani dengan NIM 2311102441097, mahasiswa Program Studi Teknik Informatika di Universitas Muhammadiyah Kalimantan Timur (UMKT).
Repositori ini merupakan hasil dari praktikum mata kuliah Pemrograman Web Lanjut, di mana saya mengembangkan sebuah website berbasis Django.

## 🌐 Tentang Website

Website ini dikembangkan menggunakan framework Django dan dirancang untuk menyajikan artikel-artikel menarik dengan berbagai topik.
Meskipun proyek ini dibuat sebagai bagian dari kegiatan praktikum, konten artikel yang disajikan mencakup berbagai hal menarik yang relevan dan informatif.

## ✨ Fitur Utama

- **Manajemen Artikel Blog:** Memungkinkan pembuatan, pengeditan, dan penghapusan postingan blog, termasuk pengelolaan kategori dan metadata lainnya. Termasuk fitur API untuk akses data artikel.
- **Admin Panel:** Kehadiran file `admin.py` di dalam direktori `article` dan `gallery` menunjukkan adanya admin panel Django untuk pengelolaan konten.
- **Penggunaan REST API:** File `urls_api.py` menunjukkan penggunaan Django REST framework untuk menyediakan API.
- **Penggunaan Database:** Kehadiran file `migrations` dan `models.py` menunjukkan penggunaan database untuk penyimpanan data.

## 🛠️ Tumpukan Teknologi

| Kategori           | Teknologi             | Catatan                               |
| ------------------ | --------------------- | ------------------------------------- | --- |
| Bahasa Pemrograman | Python, HTML          | Backend (Python), Frontend (HTML)     |
| Framework          | Django                | Framework web untuk backend           |
| Database           | MySQL                 | Berdasarkan dependensi `mysqlclient`. |     |
| Lainnya            | Pillow                | Untuk manipulasi gambar.              |
| Lainnya            | Django REST framework | Untuk pembuatan REST API.             |

## 🏛️ Tinjauan Arsitektur

Arsitektur proyek mengikuti pola MVT (Model-View-Template) standar Django. Model mendefinisikan struktur data (tabel database), views menangani logika dan interaksi pengguna, dan template (HTML) menampilkan data kepada pengguna. Proyek ini diorganisasikan menjadi beberapa aplikasi Django (`article`, `gallery`), masing-masing menangani fitur spesifik.

## 🚀 Memulai

1. Pastikan Anda telah menginstal Python dan Node.js.
2. Kloning repositori:
   ```bash
   git clone https://github.com/idrmdhni/PraktikumWebLanjut.git
   cd PraktikumWebLanjut
   ```
3. Instal dependensi:
   ```bash
   pip install -r requirements.txt
   npm install
   ```
4. Jalankan server pengembangan:
   ```bash
   python manage.py runserver
   ```

## 📂 Struktur File

```
/
├── .gitignore
├── Procfile
├── README.md
├── article
│   ├── __init__.py
│   ├── admin.py
│   ├── api.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_blogarticle_options_alter_category_options_and_more.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-311.pyc
│   │       └── __init__.cpython-311.pyc
│   ├── models.py
│   ├── serializer.py
│   ├── templatetags
│   │   ├── __pycache__
│   │   │   ├── auth_extras.cpython-311.pyc
│   │   │   ├── custom_filter.cpython-311.pyc
│   │   │   └── custom_filters.cpython-311.pyc
│   │   ├── auth_extras.py
│   │   └── custom_filters.py
│   ├── tests.py
│   ├── urls.py
│   ├── urls_api.py
│   └── views.py
├── gallery
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── __init__.cpython-311.pyc
│   │       └── __init__.cpython-313.pyc
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
├── media
│   ├── IMG_20201126_170342_sYeDVXF.jpg
│   ├── IMG_20201126_170342_sYeDVXF_aAeu13C.jpg
│   ├── YECVT_Yamaha.jpeg
│   └── article
│       ├── IMG_20201126_170342.jpg
│       ├── IMG_20201126_170342_MsLId1p.jpg
│       ├── IMG_20201126_170342_sYeDVXF.jpg
│       ├── YECVT_Yamaha.jpeg
│       ├── YECVT_Yamaha_hpRKWRl.jpeg
│       ├── sepakbola.jpeg
│       └── wallpaperbetter.jpg
├── mysite
│   ├── __init__.py
│   ├── asgi.py
│   ├── authentication.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── nixpacks.toml
├── requirements.txt
└── static
    └── admin
        ├── css
        │   ├── autocomplete.css
        │   ├── base.css
        │   ├── changelists.css
        │   ├── dark_mode.css
        │   ├── dashboard.css
        │   ├── forms.css
        │   ├── login.css
        │   ├── nav_sidebar.css
        │   ├── responsive.css
        │   ├── responsive_rtl.css
        │   ├── rtl.css
        │   ├── vendor
        │   │   └── select2
        │   │       ├── LICENSE-SELECT2.md
        │   │       ├── select2.css
        │   │       └── select2.min.css
        │   └── widgets.css
        ├── img
        │   ├── LICENSE
        │   ├── README.txt
        │   ├── calendar-icons.svg
        │   ├── gis
        │   │   ├── move_vertex_off.svg
        │   │   └── move_vertex_on.svg
        │   ├── icon-addlink.svg
        │   ├── icon-alert.svg
        │   ├── icon-calendar.svg
        │   ├── icon-changelink.svg
        │   ├── icon-clock.svg
        │   ├── icon-deletelink.svg
        │   ├── icon-hidelink.svg
        │   ├── icon-no.svg
        │   ├── icon-unknown-alt.svg
        │   ├── icon-unknown.svg
        │   ├── icon-viewlink.svg
        │   ├── icon-yes.svg
        │   ├── inline-delete.svg
        │   ├── search.svg
        │   ├── selector-icons.svg
        │   ├── sorting-icons.svg
        │   ├── tooltag-add.svg
        │   └── tooltag-arrowright.svg
        └── js
            ├── SelectBox.js
            ├── SelectFilter2.js
            ├── actions.js
            ├── admin
            │   ├── DateTimeShortcuts.js
            │   └── RelatedObjectLookups.js
            ├── autocomplete.js
            ├── calendar.js
            ├── cancel.js
            ├── change_form.js
            ├── collapse.js
            ├── core.js
            ├── filters.js
            ├── inlines.js
            ├── jquery.init.js
            ├── nav_sidebar.js
            ├── popup_response.js
            ├── prepopulate.js
            ├── prepopulate_init.js
            ├── theme.js
            ├── urlify.js
            └── vendor
                ├── jquery
                │   ├── LICENSE.txt
                │   ├── jquery.js
                │   └── jquery.min.js
                └── select2
                    ├── LICENSE.md
                    └── i18n
                        ├── af.js
                        ├── ar.js
                        ├── az.js
                        ├── bg.js
                        ├── bn.js
                        ├── bs.js
                        ├── ca.js
                        ├── cs.js
                        ├── da.js
                        ├── de.js
                        ├── dsb.js
                        ├── el.js
                        ├── en.js
                        ├── es.js
                        ├── et.js
                        ├── eu.js
                        ├── fa.js
                        ├── fi.js
                        ├── fr.js
                        ├── gl.js
                        ├── he.js
                        ├── hi.js
                        ├── hr.js
                        ├── hsb.js
                        ├── hu.js
                        ├── hy.js
                        ├── id.js
                        ├── is.js
                        ├── it.js
                        ├── ja.js
                        ├── ka.js
                        ├── km.js
                        ├── ko.js
                        ├── lt.js
                        └── lv.js
```

- `article`: Direktori ini berisi kode untuk manajemen artikel blog.
- `gallery`: Direktori ini berisi kode untuk manajemen galeri gambar.
- `mysite`: Direktori ini berisi konfigurasi Django utama (settings, urls, dll.).
- `static`: Direktori ini berisi aset statis seperti CSS, JavaScript, dan gambar. Subdirektori `admin` mengandung aset statis untuk admin panel Django.
- `media`: Direktori ini untuk menyimpan file yang diunggah pengguna (gambar).
