import spacy
import speech_recognition as sr
from ingredient_parser import parse_ingredient
from recipe_scrapers import scrape_me
nlp = spacy.load('en_core_web_lg')
# cooking_words()
f = open('cook_words.txt', 'r')
cooking_library = f.read().splitlines()
rec = sr.Recognizer()
useless_words = ['and', 'or']
steps_array = []
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
        recipe_dict = dict()
        recipe_obj = dict()
        verbs = []
        ings = []
        doc = nlp(r)
        for i in doc:
            if i.lemma_.lower() in cooking_library:
                verbs.append(i)
            # if i.dep_ == 'dobj':
            #     ings.append(i)
            if (i.lemma_.lower() in separate_ingredients) and (i.lemma_.lower() not in ings):
                ings.append(i.text)
        recipe_obj['ingredients'] = ings
        if(len(verbs)):
            recipe_obj['cooking words'] = verbs[0]
        else:
            recipe_obj['cooking words'] = verbs
        recipe_dict[r] = recipe_obj
        steps_array.append(recipe_dict)
    # print(steps_array)
    # print(parsed_ingredients)
    # print(separate_ingredients)
    return [steps_array, parsed_ingredients]


# navigator("https://www.allrecipes.com/recipe/223042/chicken-parmesan/")
