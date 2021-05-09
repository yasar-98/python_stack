# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]
# # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# x[1][0]=15
# print(x)
# # Change the last_name of the first student from 'Jordan' to 'Bryant'
# students[0]["last_name"]="Bryant"
# print(students)
# # In the sports_directory, change 'Messi' to 'Andres'
# sports_directory["soccer"][0]="Andres"
# print(sports_directory)
# # Change the value 20 in z to 30
# z[0]["y"]=30
# print(z)

# print("#"*100)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# def iterateDictionary(students):
#     for student in students :
#         for key,value in student.items():
#             print(f"{key} - {value}" , end=", ")
#         print("")
# iterateDictionary(students)

print("#"*100)

def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)) :
        print(f"{some_list[i][key_name]}" , end="")
        print("")

iterateDictionary2("first_name",students)
print("#"*10)
iterateDictionary2("last_name",students)
# print("#"*100)

# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# def printInfo(some_dict):
#     for x in some_dict:
#         print(f"{len(some_dict[x])} {x.upper()}")
#         for y in some_dict[x]:
#             print(y)

# printInfo(dojo)
