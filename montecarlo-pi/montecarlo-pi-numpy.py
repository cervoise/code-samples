# Source: http://www.normalesup.org/~doulcier/teaching/python/Ex01_monte_carlo.html

import numpy as np

N = 10000000

# On tire un grand nombre de points uniformément sur [0,1]^2
x = np.random.random(size=N)
y = np.random.random(size=N)

# On créer un array de booléens indiquant si le point se trouve dans le quart de cercle.
z = (x**2+y**2)<1

# On estime pi
pi_est = 4*z.sum()/N

print('Estimation de pi: {}'.format(pi_est))