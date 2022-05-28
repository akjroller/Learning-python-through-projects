def front_back(str):
  if len(str) == 1:
    return str
  else:
    f=str[:1]
    mid = str[1:len(str)-1]
    b = str[-1]
    return  b + mid + f


print(front_back("test"))
print(front_back('a'))
print(front_back('to'))
print(front_back('i dont know'))