#unknown numbers of arguments
def my_function1(*kids):
    print("The youngest child is " + kids[2])

my_function1("Emil", "Tobias", "Linus")

#keyword arguments
def my_function2(child3, child2, child1):
  print("The youngest child is " + child3)

my_function2(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

