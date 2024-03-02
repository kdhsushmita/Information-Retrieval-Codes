import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

music_features_text = [
   "Pop Rock Jazz",      
   "Pop Country Rock",               
   "Pop R&B Soul",           
   "Metal Heavy Metal Rock",      
   "Hip Hop Rap",                    
   "Jazz Fusion",                        
   "R&B Pop Soul",                       
   "Rock Hard Rock Classic Rock",
   "Pop Soul Blues",                        
   "Rock Hard Rock Punk",
   "Bollywood Hindi Indian",
   "Nepali Pop Folk",
   "K-pop Korean Pop",
]

user_profile_text = "Bollywood Hindi Indian Nepali"

def recommend_music(user_profile, music_features, num_recommendations=3):
   # Convert text data to TF-IDF vectors
   vectorizer = TfidfVectorizer()
   music_features_tfidf = vectorizer.fit_transform(music_features)
   user_profile_tfidf = vectorizer.transform([user_profile])
  
   # Calculate cosine similarity between the user profile and all music items
   similarities = cosine_similarity(user_profile_tfidf, music_features_tfidf)[0]
  
   similar_items = np.argsort(similarities)[::-1]
  
   # Recommend top 'num_recommendations' music items
   recommended_items = similar_items[:num_recommendations]
   return recommended_items

def main():
   recommended_items = recommend_music(user_profile_text, music_features_text, num_recommendations=3)
  
   print("Recommended music items:")
   for item_idx in recommended_items:
       print(f"Music Item {item_idx + 1}: {music_features_text[item_idx]}")

if __name__ == "__main__":
   main()
