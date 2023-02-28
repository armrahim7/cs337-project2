import spacy
from scraper import scrape, cooking_words
import speech_recognition as sr
from ingredient_parser import parse_ingredient
from recipe_scrapers import scrape_me
nlp = spacy.load('en_core_web_lg')
cooking_library = cooking_words()
rec = sr.Recognizer()
recipe_dict = dict()
useless_words = ['and', 'or']
def navigator(url):
    recipe = scrape_me(url)
    instructions = recipe.instructions_list()
    ingredients = recipe.ingredients()
    separate_ingredients = []
    final_instructions = []
    parsed_ingredients = dict()
    for i in instructions:
        if '. ' in i:
            r_split = i.split('. ')
            for j in r_split:
                final_instructions.append(j)
        else:
            final_instructions.append(i)
    for i in ingredients:
        p = parse_ingredient(i)
        spl = p['name'].split()
        for j in spl:
            if j in useless_words:
                pass
            else:
                doc = nlp(j)[0]
                separate_ingredients.append(doc.lemma_)
        if p['quantity'] == '':
            parsed_ingredients[p['name']] = 'to taste'
        else:
            parsed_ingredients[p['name']] = p['quantity'] + ' ' + p['unit']
    for r in final_instructions:
        verbs = []
        ings = []
        doc = nlp(r)
        for i in doc:
            if i.lemma_.lower() in cooking_library:
                verbs.append(i)
            # if i.dep_ == 'dobj':
            #     ings.append(i)
            if i.lemma_.lower() in separate_ingredients:
                ings.append(i)
        if(len(verbs)):
            recipe_dict[r] = [verbs[0],ings]
        else:
            recipe_dict[r] = [verbs, ings]
    print(recipe_dict)
    print(parsed_ingredients)
    print(separate_ingredients)


navigator("https://www.allrecipes.com/recipe/223042/chicken-parmesan/")
