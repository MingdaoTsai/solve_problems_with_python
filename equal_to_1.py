import itertools 

def myFunc (inputlist):
	ret=inputlist[0]/(inputlist[1]*10+inputlist[2]) + inputlist[3]/(inputlist[4]*10+inputlist[5]) + inputlist[6]/(inputlist[7]*10+inputlist[8])
	return ret

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
totallist=list(itertools.permutations([1,2,3,4,5,6,7,8,9],9))
print(len(totallist))
for i in range(len(totallist)):
	mylist=totallist[i]
	Ans=myFunc(mylist)
	if Ans==1:
		print("SEQ=")
		print(mylist)
		#如果只要一個解的話，就break
		#break
		print(mylist[0],"/",mylist[1],mylist[2],"+",mylist[3],"/",mylist[4],mylist[5],"+",mylist[6],"/",mylist[7],mylist[8])

