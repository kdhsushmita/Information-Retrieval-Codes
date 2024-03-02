import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')

def remove_stopwords(sentence):
    # Tokenize the sentence
    words = nltk.word_tokenize(sentence)
    
    # Get the English stopwords from NLTK
    stop_words = set(stopwords.words('english'))
    
    # Remove stopwords from the sentence
    filtered_words = [word for word in words if word.lower() not in stop_words]
    
    # Join the filtered words back into a sentence
    filtered_sentence = ' '.join(filtered_words)
    
    return filtered_sentence

# Example sentence
random_sentence = "This is a random sentence with some stop words that need to be removed."

# Call the function to remove stop words
filtered_sentence = remove_stopwords(random_sentence)
print("Original Sentence:", random_sentence)
print("Filtered Sentence:", filtered_sentence)
