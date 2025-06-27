import re
from django import template
from django.utils.safestring import mark_safe
from bs4 import BeautifulSoup

register = template.Library()

@register.filter(name='remove_img_tags')
def remove_img_tags(html_content):
    if not html_content:
        return ""
    
    # Regex untuk menemukan tag <img>, termasuk yang self-closing
    cleaned_content = re.sub(r'<img[^>]*>', '', html_content, flags=re.IGNORECASE)
    
    # Menandai hasilnya sebagai 'safe' agar tag HTML lain tidak di-escape
    return mark_safe(cleaned_content)

@register.filter(name='add_image_classes')
def add_image_classes(html_content):
    """
    Template filter untuk mem-parsing konten HTML dan menambahkan kelas CSS
    ke semua tag <img>.
    """
    if not html_content:
        return ""

    soup = BeautifulSoup(html_content, 'html.parser')
    images = soup.find_all('img')

    classes_to_add = ['img-fluid', 'w-100']

    for img in images:
        # Mengambil kelas yang sudah ada jika ada
        existing_classes = img.get('class', [])
        
        # Menggabungkan kelas yang sudah ada dengan kelas baru, menghindari duplikat
        # Menggunakan set untuk efisiensi dan jaminan keunikan
        all_classes = set(existing_classes + classes_to_add)
        
        # Mengupdate atribut class pada tag img
        img['class'] = ' '.join(all_classes)

    # Mengembalikan HTML yang sudah dimodifikasi sebagai string yang aman (safe string)
    return mark_safe(str(soup)) 