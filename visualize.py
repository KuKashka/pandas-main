import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('GoogleApps.csv')

#df['Size'].plot(kind='hist')

#df['Category'].value_counts()plot(kind='pie')


df[df['Type']=='Paid']['Price'].plot(kind="box")
plt.show()