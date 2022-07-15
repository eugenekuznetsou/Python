#import numpy as np
#a = np.random.randint(0, 100, size=10)
#b = np.random.randint(0, 100, size=10)
#print(a)
#print(b)


#string = "abcd"
#revstring = string[::-1]
#print(revstring)



#import random
#password = "asdfghsjldhlsdjhlsdvlshcldshldsjhvd"
#lenght = int(input("Enter lenght of password: "))
#
#a = "".join(random.sample(password,lenght))
#
#print(f"Your password is {a}")

import cryptocode
crfile = cryptocode.encrypt("HEllo World","ad")
decrfile = cryptocode.decrypt(f"{crfile}","ad")
print(crfile)
print(decrfile)