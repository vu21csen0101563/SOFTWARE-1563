import matplotlib.pyplot as plt
import numpy as np
# hard code variables
def quadratic_model(a,b,c,time):
  temperature = a*time*time + b*time + c
  return temperature

time_values=np.linspace(0,10,100)
a=int(input("Enter value of a : "))
b=int(input("Enter value of b : "))
c=int(input("Enter value of c : "))
temperature_hardcoded = quadratic_model(a,b,c,time_values)

plt.plot(time_values,temperature_hardcoded, label='temperature with hard coded coefficients')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.title('weather modeling with quadratic equation(keyboard input)')
plt.show()
