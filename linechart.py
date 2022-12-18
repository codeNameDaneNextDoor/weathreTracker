#Purpose: Create Fahrenheit plot comparing period 1 and period 2
#Name: Dane Folk
#Date: 14 Aug 22
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv("formatdata.csv") #baseline data is period 1 (older)
df2 = pd.read_csv("formatdata2.csv") #data for period 2 (more recent)
plt.figure(); df1.Fahrenheit.plot(label = 'period '); df2.Fahrenheit.plot(label = 'period 2'); plt.legend(loc='best'); plt.suptitle('Fahrenheit')
plt.show()
