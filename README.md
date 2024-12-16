# Müşteri Segmentasyonu ile Karar Destek Sistemi

Bu proje, müşterilerin demografik ve ekonomik verilerini makine öğrenimi teknikleriyle analiz ederek, onları farklı segmentlere (öbeklere) ayıran bir karar destek sistemi sunmaktadır. Kullanıcıdan alınan basit giriş verileri (yaş, cinsiyet, gelir durumu vb.) kullanılarak müşterinin ait olduğu segment tahmin edilir, segmentlere özgü pazarlama stratejileri, reklam önerileri ve alışveriş kredisi teklifleri dinamik olarak üretilir. Üstelik, zaman içinde yeni müşterilerin verileri de sisteme eklenerek veri seti sürekli genişletilir ve model güncellenerek iyileştirilir.

## Proje Özeti

- **Veri Analitiği ve Segmentasyon:** 
  Projede kullanılan veri setleri müşterilerin demografik (cinsiyet, yaş, medeni durum, eğitim), coğrafi (yaşanılan şehir), ekonomik (yıllık ortalama gelir), tüketim (en çok ilgi duyulan ürün kategorisi, yıllık satın alım miktarı, sipariş sayısı) bilgilerinden oluşur. Eğitim veri seti ile farklı makine öğrenimi modelleri eğitilerek müşteriler belirli öbeklere ayrılır.

- **Makine Öğrenimi Modelleri:**
  Farklı sınıflandırma algoritmaları (Random Forest, SVM, Decision Tree, Gradient Boosting, Logistic Regression, Gaussian NB, KNN) test edilip karşılaştırılmıştır. Performans metrikleri olarak doğruluk (accuracy), hassasiyet (precision), geri çağırma (recall) ve F1 skoru kullanılmıştır. Çalışmada Random Forest modelinin diğer yöntemlere kıyasla en iyi performansı verdiği görülmüştür.

- **Kişiselleştirilmiş Pazarlama ve Reklam Önerisi:**
  Her bir segmentin kendine özgü gelir düzeyleri, ilgi alanları ve tüketim alışkanlıkları analiz edilmiştir. Bu sayede:
  - **Segment 1: "İhtiyaç Odaklı Yaşayanlar"**  
    Temel ihtiyaç ürünlerine odaklı, düşük gelirli müşteri grubu.
  - **Segment 4: "Bolluk İçinde Yaşayanlar"**  
    Yüksek gelirli, yüksek satın alma miktarına sahip, büyük şehirlerde yaşayan tüketiciler.
  - **Segment 7: "Ofis Elitleri"**  
    Eğitim seviyesi yüksek, maaşlı istikrarlı işlerde çalışan, ev & mobilya ürünlerine ilgi duyan müşteri grubu.
  
  ve diğer segmentler için de benzer stratejiler geliştirilmiştir. Her segmente özel reklam önerisi ve alışveriş kredisi teklifleri sunularak pazarlama etkinliği artırılmaktadır.

- **Sürekli Öğrenme ve Model Güncelleme:**
  Uygulamaya yeni müşteri verileri eklendikçe model yeniden eğitilir. Bu sayede model, güncel müşteri davranışlarına adapte olur ve zaman içerisinde daha isabetli segmentasyon ve öneriler üretebilir.

- **Veritabanı ve Arayüz:**
  SQLite veritabanı, verilerin düzenli ve hızlı bir şekilde sorgulanmasına imkân sağlar.  
  Streamlit tabanlı web arayüzü sayesinde kullanıcı dostu bir deneyim sunulur. CSS ile özelleştirilen arayüz, dinamik görseller, filtreler ve interaktif grafiklerle veriyi anlamayı kolaylaştırır.

## Teknik Detaylar

- **Veri Seti:**
  - **Eğitim Verisi (train.csv):** 5460 gözlem, 14 özellik
  - **Test Verisi (test_x.csv):** 2340 gözlem, 13 özellik
  - Demografik, ekonomik ve tüketim alışkanlıklarını yansıtan değişkenler.
  - Eksik ve uç değer kontrolleri, normalizasyon, kategorik verilerin encode edilmesi gibi veri ön işleme adımları gerçekleştirilmiştir.

- **Kullanılan Modeller:**
  - **Random Forest:** En başarılı sonuçları elde etmiş, aşırı uyumu azaltarak genelleme kabiliyetini artırmıştır.
  - **Destek Vektör Makineleri, Decision Tree, Gradient Boosting, Logistic Regression, Gaussian NB, KNN:** Çeşitli karşılaştırmalar yapılarak sonuçlar tablo ve grafiklerle sunulmuştur.

- **Performans Değerlendirmesi:**
  - **Metrikler:** Accuracy, Precision, Recall, F1-score, Support.
  - **Dengesiz Veri Seti:** Çok sınıflı ve dengesiz verilerle çalışıldığından, tek başına accuracy yerine F1-score gibi dengeli metrikler de değerlendirilmiştir.
  
- **Hiperparametre Optimizasyonu ve Özellik Seçimi:**
  - Grid Search ile Random Forest için en uygun hiperparametreler aranmış, ancak bazı durumlarda varsayılan ayarların daha iyi sonuç verdiği görülmüştür.
  - Feature importance grafikleri ile hangi özelliklerin segmentasyon üzerinde daha etkili olduğu tespit edilmiştir.

## Kurulum ve Çalıştırma

1. **Proje Deposunu Klonlayın:**
   ```bash
   git clone https://github.com/kullanici_adi/proje_adi.git
   cd proje_adi
