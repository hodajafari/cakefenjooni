def get_list_from_user():
    user_input=input("enter your score")
    items=user_input.split(",")
    numbers=[int(item.strip()) for item in items]
    return numbers
def bigger_than_five(numbers):
    result=[]
    for number in numbers:
        if number > 5:
            result.append(number)
    return result
a=get_list_from_user()
b=bigger_than_five(a)
print("numbers of list that is bigger than five=\n" , b)