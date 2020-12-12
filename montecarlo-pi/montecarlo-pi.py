# Python 3

import random

N = 10000000
z = 0

for i in range(N):
   x = random.random()
   y = random.random()
   if (x**2+y**2)<1:
      z += 1

pi_est = 4*z/N

print('Estimation de pi: {}'.format(pi_est))