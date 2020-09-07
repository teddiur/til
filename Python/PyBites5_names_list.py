NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    names_capitalized = []
    for person in set(names):
        # if person not in names_capitalized:
        #     print(person)
        names_capitalized.append(" ".join([name.capitalize() for name in person.split()]))
    return names_capitalized
# print(dedup_and_title_case_names(NAMES))

def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    return sorted(names, key=lambda name: name.split()[1], reverse=True)
# print(sort_by_surname_desc(NAMES))

def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    lenght_name = {len(name.split()[0]): name.split()[0] for name in names}
    return lenght_name[min(lenght_name.keys())]
# print(shortest_first_name(NAMES))