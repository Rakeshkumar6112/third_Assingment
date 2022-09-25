# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)

Sample_List =(8, 2, 3, 0, 7)
def sum(Sample_List):
    total=0
    for i in Sample_List:
        total+=i
    return total
print("Total sum Value :",sum(Sample_List))
print(Sample_List)

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))