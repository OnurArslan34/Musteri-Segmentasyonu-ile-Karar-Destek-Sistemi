import random
from data_access import get_products_from_db

def get_random_recommendations(obek_label, count=3):
    products = get_products_from_db(obek_label, limit=15)
    if len(products) == 0:
        return []
    if len(products) <= count:
        return products
    return random.sample(products, count)
strategies = {
    "obek_1": "İhtiyaç Odaklı Yaşayanlar",
    "obek_2": "Görünmez Emekçiler",
    "obek_3": "Finansal Denge Ustaları",
    "obek_4": "Bolluk İçinde Yaşayanlar",
    "obek_5": "Mücadeleci Ruha Sahip Olanlar",
    "obek_6": "Hayatın Tadını Çıkaranlar",
    "obek_7": "Ofis Elitleri",
    "obek_8": "Geleceğin Liderleri"
}