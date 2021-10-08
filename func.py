from data import movies

"""l=input("enter the language- english/hindi: ")
g=input("enter the genre: ")
a=input("enter the age group: ")
result= movies[l][g][a]
print("Here are some movies for you....")
print(result)"""



def mr(l,g,a):
    result= movies[l][g][a]
    print("Here are some movies for you....")
    print(result)
    return result

