from sympy import factorint
from sympy import mod_inverse
from Crypto.Util.number import long_to_bytes

#enter the value of n
n = int(input("Enter the value of n: "))

factors = factorint(n)

# Printing factors 
for i, factor in enumerate(factors, start=1):
    print(f"{i}. {factor}")

#store factors in a list
primes = list(factors.keys())

#calculate phi
phi_n = 1
for p in primes:
    phi_n *= (p - 1)

e=int(input("Enter the value of e: "))

d = mod_inverse(e, phi_n)

encrypted_flag = int(input("Enter the encrypted flag : "))


# Decrypt the flag
flag = pow(encrypted_flag, d, n)
flag_bytes = long_to_bytes(flag)


#the flag
print(flag_bytes)
