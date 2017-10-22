import pandas as pd
import numpy as np

rand_dist = np.random.binomial(2, [0.7, 0.3])
print(rand_dist)
"""
A real world example. A company drills 9 wild-cat oil exploration wells, each with an estimated probability of success of 0.1.
All nine wells fail. What is the probability of that happening?

Let’s do 20,000 trials of the model, and count the number that generate zero positive results.
"""
answer = sum(np.random.binomial(9, 0.1, 20000) == 0)/20000.
print(answer)


"""
From coursera, look at it
"""
print("Simple ones")

rand_dist = np.random.binomial(10, 0.4)
"""
10 - Doing the event 10 times
0.4 - Probability of success
rand_dist - sum of all events where the experiment was successful
"""
print(rand_dist)

print("Using third parameter")
rand_list = np.random.binomial(20,0.5, 1000)
"""
20 - Flipping the coin 20 times
0.5 - Probability of Heads
1000 - We are running experiment for 1000 times,
So, rand_list would be an array of 1000 elements
each element contains sum of successes in 20 flipping for that experiment
"""
# print(rand_list)
print("SOME CONITIONS ATTACHED TO IT")
"""
Suppose we want to find out in how many experiments we got heads
more than 11 times
So we check the rand_list for elements > 11 and sum it up
SEE the power of vectorization
You can play around with the conditions and do sum , mean etc
If you put 2nd arg as an array with n elements means you want n distribution
You'll get array with n elements representing sum in each distribution.
"""
rand_int_11 = (np.random.binomial(20,0.5,1000) > 11).sum()
print(rand_int_11)

print("BACK TO BACK TORNEDOES")
chance_of_tornado = 0.01 #On a day
tornedo_events = np.random.binomial(1, chance_of_tornado, 1000000) #We are running it over 10000 days
#Keepin mind you can't out first argument as 10000.
#It would endup giving you sum of nuber of days when it happened.
#You keep 1 day as first argument and that's repeated over 10000 times
#Should have been easier than previous one. whatever
two_days_in_a_row = 0

for i in range(1,len(tornedo_events) -1):
    if tornedo_events[i]==1 and tornedo_events[i-1]==1:
        two_days_in_a_row += 1

print("Occurance of two back to back are {} in {} years".format(two_days_in_a_row, 1000000/365))