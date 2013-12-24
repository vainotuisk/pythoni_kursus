# Ruudu sees asub ring. Ringi raadius on 3. Leia ja v2ljasta ekraanile ruudu pindala, ruudu ymberm66t, ringi pindala, ringi ymberm66t.

# Võtame kasutusele Math mooduli  
import math

# Anname muutujatele v22rtuse
raadius = 3

# Ruudu kylg on 2 raadiust
kylg = 2 * raadius

# V2ljastame konsoolile ruudu pindala
print ("Ruudu pindala on " + str(kylg**2))

# V2ljastame konsoolile ruudu ymberm66du
print ("Ruudu ymberm66t on " + str(4 * kylg))

# # V2ljastame konsoolile ringi pindala
print ("Ringi pindala on " + str(round(math.pi * raadius **2,2)))

# V2ljastame konsoolile ringjoone pikkuse
print ("Ringi ymberm66t on " + str(round(math.pi * raadius * 2,2)))