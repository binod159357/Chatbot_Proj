import nltk

# nltk.download('punkt')
# nltk.download('punkt_tab')
# #nltk.download('all')
# nltk.download('wordnet')
# nltk.download('stopwords')

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def clean_text(text):
# text = "Hello there! I am learning Python. NLTK makes text processing easy. NLP with Python is powerful and fun!"
# text = input("Enter your Statement : ")
# print('\n')

# # Sentence Tokenization processes........
    sentences = sent_tokenize(text)
    # print("The Sentence token is : ", sentences)
    # print('\n')


    # # Word Tokenization processes........
    tokens = word_tokenize(text)
    # print("The Word Tokens is :", tokens)
    # print('\n')

    # # Remove stopwords processes.......
    stop_words = set(stopwords.words('english'))
    # print('Stop words are : ',stop_words)
    # print('\n')

    filtered_tokens = [w for w in tokens if w.lower() not in stop_words]
    # print("Filtered stop words are :", filtered_tokens)
    # print('\n')


    # # Lemmatization Processes.........
    lemmas = [lemmatizer.lemmatize(w) for w in filtered_tokens]
    return lemmas

# text = input("Enter your Statement : ")
# print('\n')


