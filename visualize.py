import pandas as pd 
import matplotlib.pyplot as plt 

''' My first python program for datascience'''

if __name__ == "__main__":
	file = pd.read_csv('csv.csv')
	print "Showing population growth of " +file.iloc[26]['NAME']
	x = file.iloc[26][7:13].plot(kind='line',figsize=(20,10),title="Population Growth between 2010 and 2015")
	x.set_ylabel('Number of people')
	plt.savefig('mass')
	plt.show()
	
	#print "Showing population growth of " +file.iloc[:]['NAME']
	x = file.ix[5:,7:13].transpose()
	#print x
	x2 = x.plot(kind='line',legend=True,figsize=(20,10),title="Population Growth between 2010 and 2015")
	plt.legend(file.iloc[5:]['NAME'],prop={'size':6})
	x2.set_ylabel('Number of people')
	plt.savefig('all1')
	plt.show()
	