def positive_list(myList):
    output_list=[]
    for e in myList:
        if e >= 0:
            output_list.append(e)
    return output_list

print("my main list: {}".format([-1,23,-10,90]))
print(f"my positive list : {positive_list([-1,23,-10,90])}")

mylist = [-1,23,-10,90]
lambda_expression = lambda x: [x for x in mylist if x >= 0]
print(lambda_expression(mylist))
