import pandas as pd

# data = pd.DataFrame({'group':['a', 'a', 'a', 'b','b', 'b', 'c', 'c','c'],'ounces':[4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

# sorted_data = data.sort_values(by=['group','ounces'],ascending=True,inplace=False)

# data = pd.DataFrame({'k1':['one']*3 + ['two']*4, 'k2':[3,2,1,3,3,4,4]})
# sorted_data = data.sort_values(by='k2')
# drop_duplicate_data = data.drop_duplicates()
# print(sorted_data)

# subset_data = data.drop_duplicates(subset='k1')
# print(subset_data)

data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami','corned beef', 'Bacon', 'pastrami', 'honey ham','nova lox'],'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

# print(data.describe())


meat_to_animal = {
    'bacon': 'pig',
    'pulled pork': 'pig',
    'pastrami': 'cow',
    'corned beef': 'cow',
    'honey ham': 'pig',
    'nova lox': 'salmon'
}

def meat_2_animal(series):
    if series['food'] == 'bacon':
        return 'pig'
    elif series['food'] == 'pulled pork':
        return 'pig'
    elif series['food'] == 'pastrami':
        return 'cow'
    elif series['food'] == 'corned beef':
        return 'cow'
    elif series['food'] == 'honey ham':
        return 'pig'
    else:
        return 'salmon'

# data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
# print(data)

lower = lambda x: x.lower()
data['food'] = data['food'].apply(lower)
data['animal2'] = data.apply(meat_2_animal, axis='columns')
data.assign(new_variable = data['ounces']*10)
# data['new_variable'] = data['ounces']*10

print(data)