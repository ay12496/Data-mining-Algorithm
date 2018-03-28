class AprioriALgorithm:
	def __init__(self,data):
		self.data=data

	def candidateSet(self,prevFrequentItemSet,size):
		c={}
		if size==1:
			for row in prevFrequentItemSet:
				for item in row:
					temp=tuple(item)
					keys=list(c.keys())
					if temp not in keys:
						c[temp]=0			
		else:
			keyPrevFrequentItemSet=list(prevFrequentItemSet.keys())
			for indexItemSet1 in range(len(keyPrevFrequentItemSet)):
				key1=keyPrevFrequentItemSet[indexItemSet1];
				for indexItemSet2 in range(indexItemSet1+1,len(keyPrevFrequentItemSet)):
					key2=keyPrevFrequentItemSet[indexItemSet2];
					if size==2:
						temp=list(key1)
						temp=temp+[key2[0]]
						temp=tuple(temp)
						keys=c.keys()
						if temp not in keys:
							c[temp]= 0
					elif size>2:
						if key1[:size-2]==key2[:size-2]:
							temp=list(key1)
							temp.append(key2[size-2])
							temp=tuple(temp)
							keys=c.keys()
							if temp not in keys:
								c[temp]= 0

						removeList=[]
						keys=list(prevFrequentItemSet.keys())
						for i in range(len(keys)):
							keys[i]=list(keys[i])
							keys[i].sort()
							keys[i]=tuple(keys[i])
						for item in c:
							for i in range(len(temp)):
								temp=list(item)
								temp.remove(temp[i])
								temp.sort()
								temp=tuple(temp)
								if temp not in keys:
									print(temp)
									removeList.append(item)
									break
						for i in range(len(removeList)):
							c.pop(removeList[i])		
		return c			

	def frequentItemSet(self,candidateSet,min_support):
		l={}
		temp=self.data
		for i in candidateSet:
			# print("i",i)
			for j in temp:
				# print("j",j)
				if set(i) < set(j) or set(i)==set(j):
					candidateSet[i]=candidateSet[i]+1
			if candidateSet[i]>=min_support:
				l[i]= candidateSet[i]
		return l


	def generateFrequentItemSet(self,min_support):	
		l_size=1
		prevFrequentItemSet=data
		while len(prevFrequentItemSet)!=0:
			print("Generating Candidate ItemSet of size",l_size)
			c=self.candidateSet(prevFrequentItemSet,l_size)
			print("C:",c)
			print("Generating Frequent ItemSet of size",l_size)
			l=self.frequentItemSet(c,min_support)
			print("L:",l)
			prevFrequentItemSet=l
			l_size=l_size+1
		return	

f = open("example.csv", "r") 
data=[]
for line in f:
	line=line.rstrip('\n')
	row=line.split(',')
	data.append(row)

print("Data:",data)

ap=AprioriALgorithm(data)

min_support=int(input("Enter min_support:"))

ap.generateFrequentItemSet(min_support)