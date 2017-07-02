f = open("countries.txt", "r")

countries = []

for line in f:
    line = line.strip()
    print(line)
    countries.append(line)

f.close()

print(countries)

counter = 0

for country in countries:
    if country == "Zimbabwe":
        print(country)
