def even_ho_ki_naai(num):
    if num%2==0:
        return "Yeah, its an even number"
    else:
        return "Not even"
    
print(even_ho_ki_naai(10))

    
mero_list= [1,2,3,4,5,6,7,8,9,10]
even= [num for num in mero_list if num%2==0]
print(even)