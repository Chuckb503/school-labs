# d = {'key': 'value'}
#
# print(d["key"])

people = {
    'jones': {'f_name': 'Chris', 'l_name': 'Jones', 'phone': 5032779710},
    'dover': {'f_name': 'Sheri', 'l_name': 'Dover', 'phone': 5552221111}
}


def add_entry(f_name, l_name, phone):
    # Add entry to dictionary
    people[l_name.lower()] = {'f_name': f_name, 'l_name': l_name, 'phone': phone}
print(people)

print()
add_entry('Katie','Jones-Dover', 5224445656)
print(people)
print()

# Remove Code From dictionary
del people['jones-dover']
print(people)

def print_names(last_name):
    # print dictionary
    print(people[last_name.lower()]['f_name'])
    print(people[last_name.lower()]['l_name'])
    print(people[last_name.lower()]['phone'])
#
#
# nm = input('Enter the last name you are looking for: ')
# print_names(nm)
#
# # print(people)
