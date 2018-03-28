import pandas as pd
import numpy as np

file=open("test.csv",'r')
x=[]
y=[]

for line in file:
	line=line.rstrip('\n')
	row=line.split(',')
	x.append(int(row[0]))
	y.append(int(row[1]))


df=pd.DataFrame({
	'x':x,
	'y':y
	})

print("Datapoints")
print(df)

numOfCluster=int(input('Enter num of cluster:'))

centroids={}

for i in range(numOfCluster):
	centroids[i+1]=[x[i],y[i]]
print(centroids)

def assignment(df,centroids):
	for i in centroids.keys():
		df['distance_from_{}'.format(i)] = (
            np.sqrt(
                (df['x'] - centroids[i][0]) ** 2
                + (df['y'] - centroids[i][1]) ** 2
            )
        )
	centroids_coloumn=['distance_from_{}'.format(i) for i in centroids.keys()]    
	df['closest']=df.loc[:,centroids_coloumn].idxmin(axis=1)
	df['closest']=df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
	print("Datapoints")
	print(df)
	return df

def update(centroids):
	for i in centroids.keys():
		centroids[i][0]=np.mean(df[df['closest']==i]['x'])
		centroids[i][1]=np.mean(df[df['closest']==i]['y'])
	return centroids

df=assignment(df,centroids)
while True:
	centroids = update(centroids)
	closest_centroids = df['closest'].copy(deep=True)
	df = assignment(df, centroids)
	if closest_centroids.equals(df['closest']):
	    print("Matched:" , centroids)    
	    break


