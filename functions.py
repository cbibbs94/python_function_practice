from ntpath import join


def max_num(num1, num2, num3):
    number_list = [ num1, num2, num3 ]
    return max(number_list)
print(max_num(8,9,1))

def mult_list(num_list):
    product = num_list[0]
   
    for i in num_list[1:]:
            product = product * i
    return product 
print(mult_list([6,7,8]))   

def rev_string(str):
    return ''.join(reversed(str))
print(rev_string('Kaizer'))

def num_within(x, num1, num2):
    return x in range(num1, num2+1)
print(num_within(7,4,20))



##This function for pascal was copied and I'm not claiming to have wrote this, I put this here to study extensively and figure out what this block of code is doing.
triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)

# def inner_func(int_param):
#     def minus_five(inner_param):
#         return inner_param - 5
#     new_val = minus_five(int_param)
#     return new_val    
# print(inner_func(10))    

