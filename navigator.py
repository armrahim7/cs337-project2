import spacy
from scraper import scrape
import nltk
nlp = spacy.load('en_core_web_lg')
def navigator(recipe):
    verbs = []
    for r in recipe:
        doc = nlp(r)
        for i in doc:
            if i.pos_ == 'VERB':
                verbs.append(i)
    print(verbs)
    # for r in recipe:
    #     text = nltk.word_tokenize(r)
    #     print(nltk.pos_tag(text))

steps = scrape("https://www.allrecipes.com/recipe/223042/chicken-parmesan/")
navigator(steps)
