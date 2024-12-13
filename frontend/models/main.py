import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer

# Data nutrisi sesuai kategori
data_nutrisi = [
    [13.3, 83.3, 18.3, 7.8],  # kategori 0
    [16.7, 100, 21.7, 9.3],   # kategori 1
    [18.3, 93.3, 21.7, 9]     # kategori 2
]

# Dataset resep
recipe_data = {
    'recipe_name': ['Chicken Soup', 'Veggie Salad', 'Beef Stew'],
    'ingredients_list': ['chicken, carrot, onion', 'lettuce, cucumber, tomato', 'beef, potato, onion'],
    'image_url': ['url1', 'url2', 'url3']
}
recipe_df = pd.DataFrame(recipe_data)

import pickle
knn = pickle.load(open('reduced_recommendation_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Inisialisasi scaler dan vectorizer
scaler = StandardScaler()
vectorizer = TfidfVectorizer()

# Fit vectorizer pada data bahan
X_ingredients = vectorizer.fit_transform(recipe_df['ingredients_list'])

# Fit scaler pada data nutrisi
X_nutrisi = np.array(data_nutrisi)
scaler.fit(X_nutrisi)

# Membuat model KNN untuk rekomendasi bahan
knn = NearestNeighbors(n_neighbors=1)
knn.fit(X_ingredients.toarray())  # Fit KNN pada data bahan

# Fungsi rekomendasi resep
def recommend_recipes(umur, gender, list_bahan):
    # Mengategorikan berdasarkan umur dan gender
    if umur < 7:
        print("Maaf, umur tidak termasuk kategori SD.")
        return
    elif umur < 10:
        kategori = 0
    elif umur < 13:
        if gender == 1:  # 1 untuk laki-laki, 0 untuk perempuan
            kategori = 1
        else:
            kategori = 2
    else:
        print("Maaf, umur tidak termasuk kategori SD.")
        return
    
    # Mengisi input feature berdasarkan kategori
    input_features = data_nutrisi[kategori]
    input_features.append(list_bahan)
    
    # Merekomendasikan resep
    input_features_scaled = scaler.transform([input_features[:4]])  # Transformasi nutrisi
    input_ingredients_transformed = vectorizer.transform([input_features[4]])  # Transformasi bahan
    input_combined = np.hstack([input_features_scaled, input_ingredients_transformed.toarray()])
    
    distances, indices = knn.kneighbors(input_combined)
    recommendations = recipe_df.iloc[indices[0]]
    
    return recommendations[['recipe_name', 'ingredients_list', 'image_url']]

# Contoh input
recommendations = recommend_recipes(10, 1, 'chicken')
print(recommendations)
