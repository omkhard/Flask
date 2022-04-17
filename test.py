from passlib.hash import bcrypt
h = "admin"
hahs  = bcrypt.hash(h)
print(hahs)
print(bcrypt.verify(h,hahs))
print(bcrypt.hash(h))
print(bcrypt.verify(h,bcrypt.hash(h)))