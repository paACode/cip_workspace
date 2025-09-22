# region Pycharm Shortcuts
"""
Execute Selection in Console: Alt+Shift+E
Execute Script : Shift + Fn +F10
Collapse All : CTRL + Shift + "-Button"
Expand All: CTRL + Shift + "+Button"
Renam Variable : Shift + F6
"""
# endregion

# %% Run isolated sections 1
print("hello")
print("you")
# %% Run isolated sections 2
print("hello")
print("world")
# %%

# region Logic Order
result = not False or True and False
print(result)
result = (not False) or (True and False)
print(result)
# endregion

#region Shorthand Statement
x=29
x = x+1 if x%2 else x
print(x)
#endregion

#region Match Case
x=10
match x:
    case 0:
        print(0)
    case 1:
        print(1)
    case 2:
        print(2)
    case _:
        print("Everything else")
#endregion

# region "is" vs "=="
a_lst = [1,2,3,4,5]
b_lst = [1,2,3,4,5]

print(f"Conten is same:{a_lst == b_lst}")
print(f"{a_lst=} | {b_lst=}")
print(f"Reference is same: {a_lst is  b_lst}")
print(f"{id(a_lst)} != {id(b_lst)}")

# endregion

# region List Reference Copy
lst1 = [1, [1, 1, 1], 1]
print(f"{lst1=}: Original")
lst2 = lst1
print(f"{lst2=}: Reference to Original")
print("lst1[0]=0,lst1[1][0]=0 : Modifications")
lst1[1][0] = 0 #Also changes in lst2 because only "shallow copy
lst1[0] = 0 #
print(f"{lst1=}: {id(lst1)=}")
print(f"{lst2=}: {id(lst2)=}")
# endregion
# region List Shallow Copy
import copy
lst1 = [1, [1, 1, 1], 1]
print(f"{lst1=}: Original")
lst2 = copy.copy(lst1)
print(f"{lst2=}: Shallow Copy")
print("lst1[0]=0,lst1[1][0]=0 : Modifications")
lst1[1][0] = 0 #Also changes in lst2 because only "shallow copy
lst1[0] = 0 #
print(f"{lst1=}")
print(f"{lst2=}: Side Effect!")
# endregion
# region List Deep Copy
import copy
lst1 = [1, [1, 1, 1], 1]
print(f"{lst1=}: Original")
lst2 = copy.deepcopy(lst1)
print(f"{lst2=}: Shallow Copy")
print("lst1[0]=0,lst1[1][0]=0 : Modifications")
lst1[1][0] = 0 #Also changes in lst2 because only "shallow copy
lst1[0] = 0 #
print(f"{lst1=}:")
print(f"{lst2=}: No Side Effect")
# endregion



# region String Immutable
str_a = "hello"
id1 = id(str_a)
str_a += "world"
id2 = id(str_a)
print(f"Strings are immutable: {id1 is not id2}")
# endregion
# region Integer Immutable
int_a = 1002
id1 = id(int_a)
int_a += 10004
id2 = id(int_a)
print(f"Integers are immutable: {id1 is not id2}")
# endregion
# region Fixed Reference Small Integers (-5 to 256)
nr_list = list(range(-10, 300))
references1 = [id(nr) for nr in nr_list]
nr_list2 = list(range(-10, 300))
references2 = [id(nr) for nr in nr_list2]

for idx in range(len(references1)):
    if references1[idx] == references2[idx]:
        print(f"Integer {nr_list[idx]=} and {nr_list[idx]=} have same reference")
# endregion

# region Check Type of an Object
if type(112) is type(int()):
    print("112 is an Integer")

if type(112) is int:
    print("112 is an Integer")

if isinstance(112, int):
    print("112 is an Integer")


# endregion

#region Lambda Functions
divisible_by_3 = lambda nr: nr%3==0 # Lambda Function definition
print(divisible_by_3(3)) # Call by Function Name
print((lambda nr: nr%3==0)(3)) # Direct Call
#endregion

#region Lambda Functions with Filter
divisible_by_3 = lambda nr: nr%3==0 # Lambda Function definition
nr_list = list(range(0,20+1,1))
nr_list_div_by_3 = list(filter(divisible_by_3, nr_list))
print(nr_list_div_by_3)
#endregion
#region Lambda Functions with Sorted: Only sort selection in list
divisible_by_3 = lambda nr: nr%3==0 # Lambda Function definition
nr_list = list(range(0,20+1,1))
nr_list_div_by_3_descending = sorted(nr_list, key=divisible_by_3, reverse=False) # Only sorts values that are div by 3
print(nr_list_div_by_3_descending)
#endregion


# region Lambda Functions with Map
keys_list = ["a","b","c","d","e"]
values_list = [1,2,4,5,6]

a_dict = dict(map(lambda key,value: (key+"_", value+10), keys_list, values_list))
print(a_dict)
# endregion


#region Dict Comprehension with Zip
car = ["BMW", "Audi", "Porsche", "Tesla"]
car_type = ["SUV", "Combi", "Sport", "SUV"]
car_dict = {key:value for key,value in zip(car, car_type)}
#endregion
#region List comprehension
nr_list = [1,2,3,4,5,6,7,8,9,10,11,12]
only_even_nr = [nr for nr in nr_list if (nr%2 == 0)]
print(only_even_nr)
#endregion

#region Mixed Dict and List Comprehension | "Random Value [IDs where RandomValue occurs]"
import random
mylist = [random.randint(1, 100) for _ in range(100)]

counter_dict = {
    unique_value: [id for id,value in enumerate(mylist) if value ==unique_value]
    for unique_value in set(mylist)}
print(counter_dict)
#endregion
#region Mixed Dict and List Comprehension | "LineNr: Count of Whitespaces"
file_path = 'C:\\Users\\acker\\Documents\\Python_Workspace\\PyKnowdlegeBase\\a_file_to_read.txt'
with open(file=file_path, mode="r") as file:
    lines = [line.rstrip() for line in file]

spaces = " "
counter = {
    nr : line.count(spaces)
    for nr,line in enumerate(lines) if line.count(spaces)
}

print(counter)
#endregion ":

# region Open a file
file_path = 'C:\\Users\\acker\\Documents\\Python_Workspace\\PyKnowdlegeBase\\a_file_to_read.txt'
with open(file=file_path, mode="r") as file:
    lines = [line.rstrip() for line in file]
    print(lines)
# endregion

# region OOP class method

class Employee:
    __company_name = "No Name"
    counter =0
    def __init__(self, name, salary):
        self.increment_counter()
        #Employee.increment_counter()
        self._name = name
        self._salary = salary
        self._company_name = Employee.company_name

    @classmethod # Set a company we currently want to edit
    def set_company_name(cls, name):
        cls.company_name = name

    @classmethod
    def increment_counter(cls):
        cls.counter +=1
        #Employee.counter +=1

Employee.set_company_name("ABB") # Can call Classmethod without an instance of Employee
hans_muster = Employee(name="Hans Muster", salary= "78k")
print(f"{Employee.counter=}")
peter_hans = Employee(name="Peter Hans", salary= "64k")
print(f"{Employee.counter=}")

Employee.set_company_name("Siemems")
beat_schlatter = Employee(name="Beat Schlatter", salary= "12k")
print(f"{Employee.counter=}")

beat_schlatter.set_company_name("SBB") # This is the same as if we would call Employee.set_company_name("")
peter_lokomotivo = Employee(name="Peter Lokomotivo", salary= "12k")


print(f"{hans_muster._company_name=}, {hans_muster._salary}")
print(f"{peter_hans._company_name=}, {peter_hans._salary}")
print(f"{beat_schlatter._company_name=}, {beat_schlatter._salary}")
print(f"{peter_lokomotivo._company_name=}, {peter_lokomotivo._salary}")
# endregion
#region OOP Inheritance and Super
class Mother:
        print("Money money money, must be funny, in a rich mens world")

class Daughter(Mother):
    def sing(self):
        print("To the left to the left!")
    pass

class Grandson(Daughter, Mother):
    def __init__(self, name, eye_color, size, favourite_band):
        super().__init__(name, eye_color, size) # We need super if we want to extend the constructor
        self._favourite_band = favourite_band

    def introduce(self):
        super().introduce()
        print(f"And my favourite band is {self._favourite_band}")


layla = Daughter(name="Layla", eye_color="blue", size="168")
#If there is no constructor __init() it takes the one from mother

layla.sing()

peter = Grandson(name="Peter", eye_color="blue", size="186", favourite_band="Metallica")
peter.introduce() #Peter also want to say what his favourite band is
peter.sing() #As Grandson has no sing() method it first checks in class Daughter if there is a sing function
# If not it goes to Mother

#endregion

#region *args and **kwars

def print_all_args_and_kwargs(*args, **kwargs):
    print(f"{args=}, {type(args)}")
    for element in args:
        print(element)
    print(f"{kwargs=}, {type(kwargs)}")
    for key,value in kwargs.items():
        print(f"{key=}, {value=}")

print_all_args_and_kwargs(2,3,4,5,6,7,8,12,pos1=12,pos2=25, pos5=6)

kwargs_example = {"a":1,"b":2, "c":3}
args_example = [11,12,13,14,15]

print_all_args_and_kwargs(*args_example, **kwargs_example)


#endregion

#region Iterate over Dictionary
my_dict = {"a":12, "b": 13, "c": 14, "d":15}

for key,value in my_dict.items():
    print(f"{key=}, {value=}")

#endregion
#region Iterate over List with enumerate
my_list = ["ferrari", "alpha", "tesla", "bmw"]

for key,value in enumerate(my_list):
    print(f"{key=}, {value=}")

#endregion