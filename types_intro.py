# before type checking

# def capitalize(first_name, last_name):
#     return first_name.capitalize() + " " + last_name.capitalize() # this can give error at runtime if someone will pass integer as argument

# print(capitalize("aditya","dhanraj"))



# after type checking

# def capitaze(first_name:str, last_name:str):
#     return first_name.capitalize() + " " + last_name.capitalize() # now strict checking will work and someone can now that we are expecting string as arguments

# print(capitaze("aditya","dhanraj"))



# union or say we can give more than one type to a variable or argument and also can give default value to it

def sum(a:int | None, b:int=0):
    if a == None:
        a = 0
    return a+b


print(sum(None,2))

# we can also give generic types to variables

def average(ls:list[int]) -> int | float:
    total:int = 0
    for i  in ls:
        total+=i
        
    return total / len(ls)

ls = [1,2,3,4,5]

print(average(ls))


# we can also define the types of elements present in the generic entities but not in list

newList : tuple[int,float,str,bool] = (1,1.0,"str",True) 



# we can also define our types

# class Student:
#     def __init__(self, name:str | None = None , roll:int | None = None) -> None: # i have tried to overload the constructer which is by default not supported in python, but i think it's not that feasible here
#         if name is None and roll is None:
#             self.name: str = "Aditya Dhanraj" 
#             self.roll : int | None = 35
#         else:
#             self.name : str | None = name
#             self.roll : str | None = roll
                   

# student : Student = Student()


class Person:
    def __init__(self,name:str) -> None:
        self.name = name
        
def get_person_name(one_person:Person):
    return one_person.name

person = Person("Aditya Dhanraj")
get_person_name(person) # it will only accept argument of type Person
        
    