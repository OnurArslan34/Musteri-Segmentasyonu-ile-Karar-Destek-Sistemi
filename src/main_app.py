import streamlit as st
import pandas as pd
import os

from data_preprocessing import preprocess_input
from model_training import train_model, predict_cluster
from recommendations import get_random_recommendations, strategies
from utils import save_new_data, combine_and_retrain

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

rf_model, label_encoders, target_encoder, interest_mapping = train_model()

st.markdown("""
    <div style="background-color:#4CAF50;padding:5px;border-radius:10px;margin-bottom:10px">
        <h3 style="color:white;text-align:center;">Reklam Stratejisi için Öbek Tabanlı Tahmin Uygulaması</h3>
    </div>
""", unsafe_allow_html=True)
st.write("""
Bu uygulama, girilen kullanıcı verilerine dayalı olarak öbek tahmini yapar, 
reklam stratejisi ve ürün önerisi sunar. 
Ayrıca yeni tahminleri veri setine ekleyerek modeli yeniden eğitmeye imkan tanır.
""")

st.markdown('<div class="section-header">Kullanıcı Verilerini Girin</div>', unsafe_allow_html=True)

cinsiyet = st.selectbox("Cinsiyet", ["Kadın", "Erkek"])
yas_grubu = st.selectbox("Yaş Grubu", ["18-30", "31-40", "41-50", "51-60", ">60"])
medeni_durum = st.selectbox("Medeni Durum", ["Evli", "Bekar"])
egitim_duzeyi = st.selectbox("Eğitim Düzeyi", ["Eğitimsiz", "İlkokul Mezunu", "Ortaokul Mezunu", "Lise Mezunu", "Yüksek Lisans Mezunu", "Doktora Ötesi","Yüksekokul Mezunu","Üniversite Mezunu"])
istihdam_durumu = st.selectbox("İstihdam Durumu", ["İşsiz veya Düzenli Bir İşi Yok", "Düzenli ve Ücretli Bir İşi Var", "Kendi İşinin Sahibi"])
yillik_gelir = st.number_input("Yıllık Ortalama Gelir (TL)", min_value=0.0, step=1000.0)
yasadigi_sehir = st.selectbox("Yaşadığı Şehir", ["Büyük Şehir", "Küçük Şehir", "Kırsal", "Köy veya Kasaba"])
yillik_satin_alim = st.number_input("Yıllık Ortalama Satın Alım Miktarı (TL)", min_value=0.0, step=100.0)
yillik_siparis_adedi = st.number_input("Yıllık Ortalama Sipariş Verilen Ürün Adedi", min_value=0.0, step=1.0)
egitime_devam_durumu = st.selectbox("Eğitime Devam Etme Durumu", ["Ediyor", "Etmiyor"])
yillik_sepete_eklenen_urun_adedi = st.number_input("Yıllık Ortalama Sepete Atılan Ürün Adedi", min_value=0.0, step=1.0)

user_input = {
    "Cinsiyet": cinsiyet,
    "Yaş Grubu": yas_grubu,
    "Medeni Durum": medeni_durum,
    "Eğitim Düzeyi": egitim_duzeyi,
    "İstihdam Durumu": istihdam_durumu,
    "Yıllık Ortalama Gelir": yillik_gelir,
    "Yaşadığı Şehir": yasadigi_sehir,
    "Yıllık Ortalama Satın Alım Miktarı": yillik_satin_alim,
    "Yıllık Ortalama Sipariş Verilen Ürün Adedi": yillik_siparis_adedi,
    "Eğitime Devam Etme Durumu": egitime_devam_durumu,
    "Yıllık Ortalama Sepete Atılan Ürün Adedi": yillik_sepete_eklenen_urun_adedi
}

if st.button("Tahmin Et"):
    processed_input = preprocess_input(user_input, label_encoders)
    input_df = pd.DataFrame([processed_input])

    predicted_cluster_label = predict_cluster(rf_model, input_df, target_encoder)
    predicted_encoded = rf_model.predict(input_df)[0]
    
    most_common_interest = interest_mapping[predicted_encoded]

    st.markdown('<div class="section-header">Tahmin Sonuçları</div>', unsafe_allow_html=True)
    st.success(f"Tahmin Edilen Öbek: {predicted_cluster_label}")

    strategy = strategies.get(predicted_cluster_label, "Öbek için bir öneri bulunamadı.")
    st.info(f"Önerilen Reklam Stratejisi: {strategy}")




    recommended_products = get_random_recommendations(predicted_cluster_label, count=3)

    if recommended_products:
        st.markdown('<div class="recommendation-section"><h3>Bu Öbeğe Özel Ürün Önerileri</h3></div>', unsafe_allow_html=True)
        cols = st.columns(len(recommended_products))
        for i, product in enumerate(recommended_products):
            with cols[i]:
                st.image(product["image_url"], use_column_width=True)
                st.markdown(f"<h4>{product['name']}</h4>", unsafe_allow_html=True)
                st.markdown(f"<p>{product.get('description', '')}</p>", unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.write("Bu öbeğe yönelik belirli bir ürün önerisi bulunamadı.")

    user_input_to_save = {
        "index": -1,
        "Cinsiyet": cinsiyet,
        "Yaş Grubu": yas_grubu,
        "Medeni Durum": medeni_durum,
        "Eğitim Düzeyi": egitim_duzeyi,
        "İstihdam Durumu": istihdam_durumu,
        "Yıllık Ortalama Gelir": yillik_gelir,
        "Yaşadığı Şehir": yasadigi_sehir,
        "En Çok İlgilendiği Ürün Grubu": most_common_interest,
        "Yıllık Ortalama Satın Alım Miktarı": yillik_satin_alim,
        "Yıllık Ortalama Sipariş Verilen Ürün Adedi": yillik_siparis_adedi,
        "Eğitime Devam Etme Durumu": egitime_devam_durumu,
        "Öbek İsmi": predicted_cluster_label,
        "Yıllık Ortalama Sepete Atılan Ürün Adedi": yillik_sepete_eklenen_urun_adedi
    }

    save_new_data(user_input_to_save)
    st.write("Yeni tahmin verisetine kaydedildi.")

st.markdown('<div class="section-header">Modeli Yeni Verilerle Yeniden Eğit</div>', unsafe_allow_html=True)
st.write("Bu butona basıldığında 'train.csv' ile 'new_data.csv' birleştirilerek model yeniden eğitilir.")

if st.button("Yeniden Eğit"):
    combine_and_retrain()
    rf_model, label_encoders, target_encoder, interest_mapping = train_model('data/combined_train.csv')
    st.write("Model yeniden eğitildi. Artık model eklenen yeni verileri de dikkate alıyor.")
