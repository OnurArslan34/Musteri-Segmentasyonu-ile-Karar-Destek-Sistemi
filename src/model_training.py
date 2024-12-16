import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os

def train_model(csv_path='data/train.csv'):
    # Veriyi oku
    train_df = pd.read_csv(csv_path)

    # Kategorik değişkenleri encode et
    label_encoders = {}
    for column in train_df.select_dtypes(include=['object']).columns:
        if column not in ['Öbek İsmi', 'En Çok İlgilendiği Ürün Grubu']:
            le = LabelEncoder()
            train_df[column] = le.fit_transform(train_df[column])
            label_encoders[column] = le

    # Hedef değişkeni encode et
    target_encoder = LabelEncoder()
    train_df['Öbek İsmi'] = target_encoder.fit_transform(train_df['Öbek İsmi'])

    # Özellikler ve hedef değişkeni ayır
    X = train_df.drop(columns=['Öbek İsmi', 'index', 'En Çok İlgilendiği Ürün Grubu'])
    y = train_df['Öbek İsmi']

    # Eğitim ve test setine böl
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    # Modeli oluştur ve eğit
    rf_model = RandomForestClassifier(random_state=42, n_estimators=100)
    rf_model.fit(X_train, y_train)

    # Test seti üzerinde tahmin yap ve doğruluk skorunu hesapla
    y_pred = rf_model.predict(X_test)

    # Öbek İsmi ile En Çok İlgilendiği Ürün Grubu arasındaki ilişkiyi oluştur
    train_df['Öbek İsmi Encoded'] = y
    interest_mapping = train_df.groupby('Öbek İsmi Encoded')['En Çok İlgilendiği Ürün Grubu'].agg(lambda x: x.mode()[0])

    return rf_model, label_encoders, target_encoder, interest_mapping

def predict_cluster(model, input_df, target_encoder):
    predicted_cluster = model.predict(input_df)[0]
    return target_encoder.inverse_transform([predicted_cluster])[0]

if __name__ == "__main__":
    model, label_encoders, target_encoder, interest_mapping = train_model('data/train.csv')
    
   