def duplicates_city(an_iterable):
    result_city = []
    s = set()

    for city in cities:
        l1 = len(s)
        s.add(city)
        l2 = len(s)
        if l1 == l2:
            result_city.append(city)
    return result_city

cities = ['Incheon','Seoul','Incheon','Incheon','Gwangju']
# cities = set(cities)
# cities.add('Incheon')
# cities.add('Suwon')
cities.append('Incheon')
cities.append('Suwon')
cities.append('Seoul')
print(cities)
print(set(duplicates_city(cities)))