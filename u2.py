myfamily = {
  "parent1" : {
    "name" : "Bisengali",
    "year" : 1976
  },
  "parent2" : {
    "name" : "Shynar",
    "year" : 1980
  },
  "child1" : {
    "name" : "Ainamkoz",
    "year" : 2007
  }
}

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])

