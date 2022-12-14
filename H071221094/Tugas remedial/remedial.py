

numbers=input("Input: ")

processed_nums = [] 
for num in numbers.split("-"): 
    if num.isdigit():
        processed_nums.append(num)
    elif not num.isdigit() and '.' in num:
        processed_nums.append(str(int(float(num))))
  
print(" ".join([n for n in processed_nums]))