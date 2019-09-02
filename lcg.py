#Exercise 1
def lcg(m,a,c,s):
    return (a*s+c) % m

#Exercise 2
print ("LCG with specific numbers=")
print(lcg((2**31-1), 48271 , 0, 123))

#Exercise 3:
rand_seed=11
def lcg_rand():
    global rand_seed
    rand_seed = lcg((2 ** 31 - 1), 48271, 0, rand_seed)
    return rand_seed

##displaying 10 values generated with lcg_rand()
data = [lcg_rand() for x in range(10)]
print("lcg_rand()=")
print(data)

##test for lcg_rand()
import matplotlib.pyplot
data = [lcg_rand() for x in range(10000000)]
plt_res = matplotlib.pyplot.hist(data, bins=1000)
matplotlib.pyplot.show()

##Exercice 4
import matplotlib.pyplot as plt         ## Not the use of import ... as ... , allows us to write short code.
def lcg_randint(lb, ub, size):
    list=[]
    global rand_seed
    for x in range(size):               ##for as many numbers as needed (= size wanted)
        res=lcg_rand()                  ##generate number with lcg
        if (res > lb and res < ub):     ##check if in the bounds
            list.append(res)
        elif (res>ub):                  ##if superior, use the %division with ub so it is always lower than ub
            list.append(res%ub)
        elif (res<lb):                  ##if inferior, add lb value and recheck if superior or not
            res+=lb
            if (res>ub):
                list.append(res%ub)
            else:
                list.append(res)
    return list

##displaying 10 values generated with lcg_randint()
data = lcg_randint(0,100, size=10)
print("lcg_randint()=")
print(data)

##test for lcg_randint()
rand_seed = 42
values = lcg_randint(0, 100, size=1000000)
hist_res = plt.hist(values, 100)
matplotlib.pyplot.show()

def uniform_float():                ##we divide it by the m value of the result of lcg_rang() function (the rest of the euclidian division with m) to have a value between 0 and 1
    return lcg_rand()/(2**31-1)

##displaying 10 values generated with normal_float()
data = [uniform_float() for x in range(10)]
print("normal_float()=")
print(data)

##test for uniform_float()
rand_seed = 42
values = [uniform_float() for x in range(10000000)]
hist_res = plt.hist(values, 100)
matplotlib.pyplot.show()

import math
def rand_gaussian():
    x= lcg_rand()
    return (1/math.sqrt(2*math.pi))*math.exp((-1/2)*x**2)       ##the formula for the gaussian distribution function

##displaying 10 values generated with rand_gaussian()
data = [rand_gaussian() for x in range(10)]
print("rand_gaussian()=")
print(data)

##test for rand_gaussian()
rand_seed = 42
values = [rand_gaussian() for x in range(10000000)]
hist_res = plt.hist(values, 100)
matplotlib.pyplot.show() ## I couldn't figure out why it doesn't

import math
def rand_poisson(lam):
    x=lcg_randint(0,10,1)[0]   ##using lcg_randint() because otherwise numbers are too big
    return math.exp(-lam)*lam**x/math.factorial(x)      ##the formula for the poission distribution function

##displaying 10 values generated with rand_poisson()
data = [rand_poisson(lam=10) for x in range(10)]
print("rand_poisson()=")
print(data)

##test for rand_poisson
rand_seed = 5
values = [rand_poisson(lam = 10) for x in range(100000)]
hist_res =  plt.hist(values ,  100)
matplotlib.pyplot.show()

import scipy.special ##in order to do use the binoom() function
def rand_binomial(n, p):
    x=lcg_randint(1, 10, 1)[0]      ##using lcg_randint() because otherwise numbers are too big
    return scipy.special.binom(n, x)*(p**x)*(1-p)**(n-x)        ##the formula for the binomila distribution function

##displaying 10 values generated with rand_binomial()
data = [rand_binomial(n=5, p=0.5) for x in range(10)]
print("rand_binomial()=")
print(data)

##test for rand_binomial
rand_seed = 5
values = [rand_binomial(n=5, p=0.7) for x in range(100000)]
hist_res =  plt.hist(values ,  100)
matplotlib.pyplot.show()