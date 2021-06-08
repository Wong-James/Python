#1
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

print(students[0])
print(sports_directory["basketball"])
print(x[1][0])
#1.1 swap values
x[1][0] = 15
print(x)
#1.2 switch name
sports_directory["basketball"][1] = 'Bryant'
print(sports_directory['basketball'])
#1.3 switch 'Messi to 'Andres
sports_directory['soccer'][0] = "Andres"
print(sports_directory['soccer'])
#1.4 change value 20 to 30 in z
z = [{'x': 10, 'y': 30}]
print(z[0]['y'])

# 2
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


def iterateDictionary(students):
    for dic in students:
        for key in dic.keys():
            print(key, dic[key])


iterateDictionary(students)

#3 Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for dic in some_list:
        print(key_name, dic[key_name])


iterateDictionary2('first_name', students)

iterateDictionary2('last_name', students)

#4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    for key in dojo.keys():
        print(len(dojo[key]) , key.upper())
        for dic in dojo[key]:
            print(dic)


printInfo(dojo)
