# Update Values in Dictionaries and Lists
x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
students[0]['last_name'] = 'Bryant'

sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'

z = [{'x': 10, 'y': 20}]

z[0]['y'] = 30

# Iterate Through a List of Dictionaries


def iterateDictionary(some_list):
    for item in some_list:
        output = ""
        for key, value in item.items():
            output += f"{key} - {value}, "
        print(output[:-2])

# Get Values From a List of Dictionaries


def iterateDictionary2(key_name, some_list):
    for item in some_list:
        print(item[key_name])

# Iterate Through a Dictionary with List Values


def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f"{len(value)} {key.upper()}")
        for item in value:
            print(item)
