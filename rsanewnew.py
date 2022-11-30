from random import randint
from sympy import isprime

#gerador de num prinmos.
def random_prime(lower_bound, upper_bound):
    while True:
        r = randint(lower_bound, upper_bound)
        if isprime(r):
            return r 
 #escolhendo p e q do gerador de num prinmos.
p = random_prime(2**128, 2**129)
q = random_prime(2**128, 2**129)
#Multiplicamos p e q para se obtermos a variável n:
N = p*q

#Calculamos a variável z, nos seguintes termos
z = (p-1)*(q-1)
#Escolher o número E, que deve ser menor que Z e primo.
e = random_prime(1, z)
#Escolher o número D, que deve estar entre p e q
d = pow(e, -1, z)


#solicita o número a ser criptografado
#enquanto o número não estiver entre dois e cinco dígitos ele ficará pedindo um novo número
while True:
    msg = int(input("digite o numero entre 2 e 5 digitos: "))   
    if msg >= 10 and msg <= 99999:
        break
m = msg

#processo de criptografia
ciphertext = pow(m, e, N)
print("Criptografado: ",ciphertext)



#processo de descriptografia
plaintext = pow(ciphertext, d, N)
print("Descriptografado: ",plaintext)
