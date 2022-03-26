import pandas as pd

# states = ['California', 'Texax', 'Florida', 'New York']
# population = [39464643, 45939244, 13446983, 23084895]

# dict_states = {'States': states, 'Population': population}
# df_states = pd.DataFrame.from_dict(dict_states)
# # print(df_states)
# df_states.to_csv('states.csv', index=False)

# with open('test.txt', 'w') as file:
#     file.write('Data successfuly scraped')

# Handlin Exception Errors
new_list = [2, 4, 6, 'California']

for element in new_list: 
    try: 
        print(element/2)
    except: 
        print(f'The element {element} is not a number')