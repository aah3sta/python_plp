#math
import math
print(math.sqrt(16))
print(math.pi)

print('square root of 36:', math.sqrt(36))
print('Sine of 90 degrees:', math.sin(math.radians(90)))
print('Power of 2 raised to 3:', math.pow(2, 3))

#random
import random
print('Random number between 1 and 10:', random.randint(1,10))
print('Random choice from a list:', random.choice(['apple', 'banana', 'cherry']))

#datetime
import datetime
today = datetime.date.today()
print('Todays date is:', today)

now = datetime.datetime.now()
print('Current time:', now.strftime('%H:%M:%S'))

#numpy
import numpy as np
my_array = np.array([1, 2, 3, 4, 5])
print('Array:', my_array)

print('Array * 2:', my_array * 2)
print('Mean:', np.mean(my_array))
print('Square roots:', np.sqrt(my_array))

new_array = np.arange(10, 51)
print(new_array)
print('The max value is:', np.max(new_array), '\nwhile the mean value is:', np.min(new_array))
print('Array * 3: ', new_array * 3)

#pandas
import pandas as pd
data = {
    'Name' : ['Alice', 'Bob', 'Charlie'],
    'Age' : [24, 30, 22],
    'Score' : [85, 90, 95]
}

df = pd.DataFrame(data)
print(df)

print('Names:', df['Name'])
print('Scores above 90:')
print(df[df['Score']>90])

#matplotlib
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()














