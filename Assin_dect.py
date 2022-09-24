# Write a Python program to print a dictionary whose keys should be the 
# alphabet from a-z and the value should be corresponding ASCII values

def test(keys, values):
  return dict(zip(keys, values))

l1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l2 = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]     


print("Sample Output :-",test( l1, l2))

