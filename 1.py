# Program for SDV calculation

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#df = pd.read_table('CR0ZHO00.DAT', sep='\s+',usecols=[0,1,2,3,4],names=['YY','MM','DD','HH','CRINT'],header=None)
print(str(99),chr(99))


for YY in range (85,99):
	A1='CR0ZHO'
	A2=str(YY)
	A3='.DAT'
	AA=A1+A2+A3 #'CR0ZHO00.DAT'
	print(AA)
	df = pd.read_table(AA, sep='\s+',usecols=[4],names=[str(YY)],header=None)
	dn=df.to_numpy()
	ds=np.append(dn)
	
#print(len(df[str(85)]))

print(df)



window_size = 12
moving_averages=[]
i=0
while i <= len(dn)-1:
	window_average = round(np.sum(dn[i:i+window_size])/window_size,2)
	moving_averages.append(window_average)
	#print(i,dn[i])
	i += 1
#print(moving_averages)

plt.plot(moving_averages)
plt.plot(dn)
plt.show()


