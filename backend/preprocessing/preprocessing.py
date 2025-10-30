
import re
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize

class TextCleaner:
    def __init__(self):
        pass
    
    def clean(self, text):
        text = text.lower()
        text = re.sub(r'<.*?>', '', text)            # remove HTML
        text = re.sub(r'http\S+|www\S+', '', text)   # remove URLs
        text = re.sub(r'[^a-z\s]', '', text)         # keep only letters
        text = re.sub(r'\s+', ' ', text).strip()     # remove extra spaces
        return text

    
# class TextTokenizerStopwordsRemover:
#     def __init__(self):
#         # Load spaCy English model
#         self.nlp = spacy.load("en_core_web_lg")

#     def tokenize_and_remove_stopwords(self, text):
#         doc = self.nlp(text)
#         # Keep tokens that are not stopwords or punctuation
#         tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
#         return tokens


class TextTokenizerStopwordsRemover:
    def __init__(self):
        self.stop_words = {
            'a', 'about', 'above', 'after', 'again', 'against', 'ain', 'all',
            'am', 'an', 'and', 'any', 'are', 'aren', 'as', 'at', 'be', 'been',
            'before', 'being', 'below', 'between', 'both', 'by', 'can', 'd',
            'did', 'does', 'doing', 'down', 'during', 'each', 'few', 'for',
            'from', 'further', 'had', 'having', 'he', "he'd", "he'll", "he's",
            'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how',
            'i', "i'd", "i'll", "i'm", "i've", 'in', 'into', 'is', 'it',
            "it'd", "it'll", "it's", 'its', 'itself', 'll', 'm', 'ma', 'me',
            'my', 'myself', 'needn', "needn't", 'now', 'o', 'of', 'off', 'on',
            'once', 'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out',
            'over', 'own', 're', 's', 'same', 'she', "she'd", "she'll", "she's",
            'should', "should've", 'so', 'some', 'such', 't', 'than', 'that',
            "that'll", 'the', 'their', 'theirs', 'them', 'themselves', 'then',
            'there', 'these', 'they', "they'd", "they'll", "they're", "they've",
            'this', 'those', 'through', 'to', 'under', 'until', 'up', 've',
            'was', 'we', "we'd", "we'll", "we're", "we've", 'were', 'what',
            'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will',
            'with', 'y', 'you', "you'd", "you'll", "you're", "you've", 'your',
            'yours', 'yourself', 'yourselves'
}

    def tokenize_and_remove_stopwords(self, text):
        tokens = word_tokenize(text)
        return [token for token in tokens if token not in self.stop_words]



class Lemmatization:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_lg")

    def lemmatize_tokens_spacy(self,tokens):
        doc = self.nlp(" ".join(tokens))   # join tokens back into a sentence for spaCy
        return [token.lemma_ for token in doc]

