# 📊 Veri Yapıları: Arama ve Sıralama Algoritmaları

Bu proje, temel bilgisayar bilimi algoritmalarının Python dilinde uygulanmasını, performans analizlerini ve zaman karmaşıklığı (Big-O) incelemelerini içerir.

## 📁 Proje İçeriği
Bartın Üniversitesi Veri Yapıları dersi ödevi kapsamında hazırlanan bu repository şunları içerir:
- *Arama:* Linear Search, Binary Search
- *Sıralama:* Bubble Sort, Selection Sort, Insertion Sort, Quick Sort

---

## 🔍 Arama Algoritmaları

### 1. Linear Search (Doğrusal Arama)
* *Mantık:* Veri setinin başından başlar ve hedef elemanı bulana kadar her elemana sırayla bakar.
* *Karmaşıklık:* $O(n)$

### 2. Binary Search (İkili Arama)
* *Mantık:* Sadece sıralı listelerde çalışır. Listeyi her adımda ikiye bölerek hedefi arar.
* *Karmaşıklık:* $O(\log n)$

---

## 📊 Sıralama Algoritmaları ve Big-O Analizi

| Algoritma | En İyi Durum | Ortalama Durum | En Kötü Durum | Bellek (Space) |
| :--- | :--- | :--- | :--- | :--- |
| *Bubble Sort* | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ |
| *Selection Sort* | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ |
| *Insertion Sort* | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ |
| *Quick Sort* | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ |

---

## 🛠️ Kodların Çalıştırılması
Projeyi yerel bilgisayarınızda çalıştırmak için:
1. git clone https://github.com/iremnzrtk/veri-yapilari-odev-arama-siralama.git
2. python main.py

---
*Hazırlayan:* İrem Nisa Öztürk  
*Bölüm:* Yapay Zekâ Operatörlüğü  
*Üniversite:* Bartın Üniversitesi
