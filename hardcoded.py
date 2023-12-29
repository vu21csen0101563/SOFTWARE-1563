import matplotlib.pyplot as plt
import numpy as np
# hard code variables
def quadratic_model(time):
 1 a=2
  b=4
  c=9
  temperature = a*time*time + b*time + c
  return temperature

time_values=np.linspace(0,10,100)
temperature_hardcoded = quadratic_model(time_values)

plt.plot(time_values,temperature_hardcoded, label='temperature with hard coded coefficients')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.title('weather modeling with quadratic equation(Hard-coded coefficient)')
plt.show()
