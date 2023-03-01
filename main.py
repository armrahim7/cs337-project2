from navigator import navigator

def main():
    url = input('Enter URL of recipe: ')
    recipe = navigator(url)
    boo = True
    curr = 0
    options = ['Options: \n',
               'Type next to go to next step.\n',
               'Type back to go to previous step.\n',
               'Type repeat to repeat current step.\n',
               'Type how to get link to Google search on how to perform current step.\n',
               'Type help to show these options again. \n',
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
                ings = '+'.join(recipe[curr][step]['ingredients'])
                word = recipe[curr][step]['cooking words']
                search = f'how+to+{word}+{ings}'
                print(f'https://www.youtube.com/results?search_query={search}')
            else:
                print('Cannot search this. Sorry. Please enter another command.')
        elif query == 'help':
            print(o)
        elif query == 'exit':
            print('Goodbye!')
            boo = False
        else:
            print('Incorrect command. Please enter a valid command.')

main()

