"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

switched = True
while switched:
    switched = False
    for i in range(0, len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            temp = numbers[i+1]
            numbers[i+1] = numbers[i]
            numbers[i] = temp
            switched = True

if len(numbers)%2 != 0: 
    print(f"The median of this list is {numbers[(len(numbers)//2)]}")
else:
    a = float(len(numbers))/2
    average = (numbers[int(a-0.5)]+numbers[int(a+0.5)])/2
    print(f"The median of this list is {average}")
    
