# #data structure dictionary 
happy_dict={'name':'mayank','age':19,'roll.no':2628}
# print(happy_dict['name'])
#dictiories are unordered pair but list are ordered 
# print(happy_dict['age'])
 
 # traversing of dictionary
 #1.
# for i in happy_dict:
#  print (i)
 #2.
# for i in happy_dict.values():
#  print (i)
 #3.
for key,values in happy_dict.items():
  print (key,values)