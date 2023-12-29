import matplotlib.pyplot as plt
import numpy as np
# hard code variables
def quadratic_model(time,a,b,c):
  temperature = a*time*time + b*time + c
  return temperature
list = [(20,3,4),(4,3,1),(2,5,1)]
time_values=np.arange(0,51,1)

for i,(a,b,c) in enumerate(list):
  temperature_values = quadratic_model(time_values,a,b,c)
  label=f'Set{i+1}: a={a},b={b},c={c}'
  plt.plot(time_values,temperature_values, label=label)


plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.grid(True)
plt.title('weather modeling with quadratic equation(multiple set)')
plt.show()
