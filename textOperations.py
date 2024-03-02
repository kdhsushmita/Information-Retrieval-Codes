import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string
nltk.download('wordnet')

# Sample paragraph
paragraph = "Natural language processing (NLP) is a field of artificial intelligence (AI) that focuses on the interaction between computers and humans through natural language. It involves the development of algorithms and models that enable computers to understand, interpret, and generate human language in a way that is both meaningful and useful. NLP applications range from language translation and sentiment analysis to chatbots and virtual assistants."

# Lowercasing
lowercased_paragraph = paragraph.lower()

# Tokenization
tokens = word_tokenize(lowercased_paragraph)

# Stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(token) for token in tokens]

# Punctuation removal
table = str.maketrans('', '', string.punctuation)
stripped_paragraph = lowercased_paragraph.translate(table)

# Stop words removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [token for token in tokens if token not in stop_words]

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

# Print results
print("Original Paragraph:")
print(paragraph)
print("\nLowercased Paragraph:")
print(lowercased_paragraph)
print("\nTokens:")
print(tokens)
print("\nStemmed Tokens:")
print(stemmed_tokens)
print("\nPunctuation Removed:")
print(stripped_paragraph)
print("\nFiltered Tokens (Stop Words Removed):")
print(filtered_tokens)
print("\nLemmatized Tokens:")
print(lemmatized_tokens)
