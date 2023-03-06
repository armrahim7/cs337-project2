from navigator import navigator
import webbrowser

def main():
    url = input('Enter URL of recipe: ')
    recipe_obj = navigator(url)
    recipe = recipe_obj[0]
    ingredients_dict = recipe_obj[1]
    ingredients = []
    hard_coded=['next','back','repeat','how','help','ingredients','exit']
    for i in ingredients_dict.keys():
        ingredients.append(i + ', ' + ingredients_dict[i])
    boo = True
    curr = 0
    options = ['Options: \n',
               'Type next to go to next step.\n',
               'Type back to go to previous step.\n',
               'Type repeat to repeat current step.\n',
               'Type how to get link to a YouTube search on how to perform current step.\n',
               'Type help to show these options again. \n',
               'Type ingredients to get a list of ingredients and their measurements. \n'
               'Type exit to exit program. \n']
    o = ''.join(options)
    print(o)
    while(boo):
        step = list(recipe[curr].keys())[0]
        print(f'Step {curr+1}: ' + step)
        query = input('Please enter a command. \n')
        if query == 'next':
            if curr==(len(recipe)-1):
                print('This is the end of the recipe. Please enter another command.')
            else:
                curr+=1
        elif query == 'back':
            if curr==0:
                print('This is the beginning of the recipe. Please enter another command.')
            else:
                curr-=1
        elif query == 'repeat':
            curr += 0
        elif query == 'how':
            if(len(recipe[curr][step]['ingredients'])) and (len(recipe[curr][step]['cooking words'])):
                if(len(recipe[curr][step]['ingredients']))>1:
                    ings = recipe[curr][step]['ingredients'][0] +'+'+'with'+'+'+'+'.join(recipe[curr][step]['ingredients'][1:])
                else:
                    ings = recipe[curr][step]['ingredients'][0]
                word = recipe[curr][step]['cooking words']
                search = f'how+to+{word}+{ings}'
                webbrowser.open(f'https://www.youtube.com/results?search_query={search}')
            else:
                print('Cannot search this. Sorry. Please enter another command.')
        elif query == 'help':
            print(o)
        elif query == 'ingredients':
            print(ingredients)
        elif query not in hard_coded :
            query = query.lower()
            if 'how long' in query:
                sol=None
                doc = nlp(step)
                prev= False
                for i in doc:
                    if i.pos_ == 'NUM':
                        prev=i.text
                    if prev:
                        if 'minute' in i.text or 'hour'in i.text:
                            sol = prev + ' ' + i.text
                            prev= False
                if sol is not None:
                    print(sol)
                else:
                    print('Sorry, I am unable to help with this')
            elif 'how much' in query:
                sol= None
                for ing in recipe[curr][step]['ingredients']:
                    if ing in query and sol == None:
                        if ing in ingredients_dict.keys():
                            sol=ingredients_dict[ing]
                        else:
                            for mat in ingredients_dict.keys():
                                if ing in mat :
                                    sol=ingredients_dict[mat]               
                if sol is not None:
                    print(sol)
                else:
                    print('Sorry, I am unable to help with this')

        elif query == 'exit':
            print('Goodbye!')
            boo = False
        else:
            print('Incorrect command. Please enter a valid command.')

main()

