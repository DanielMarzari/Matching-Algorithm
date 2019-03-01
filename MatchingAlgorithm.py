#Python

#This matching program can take 1 list of elements that have ranked eachother (indices indicate element, elements must always rank themselves as 0)
#Seeks to pair with highest desireability for the whole system
#This may also be a solution to the stable marriage problem ** UNTESTED
import numpy as np

def createTable_1List(ElmList):

	elementCount = len(ElmList)
	
	#debuging print
	#print ElmList
	
	#Finds the total desirability of each element(np.sum) and returns the element indices in inverse order of their desirability(flip, argsort)
	DesIndx = np.flip(np.argsort(np.sum(ElmList, axis = 0)), 0)
	#Copy array for pairing later...
	IndxCpy = DesIndx[:]
	
	#debuging printout
	#print DesIndx
	
	#var for calculating highest Mutual Benifit of a pairing A.K.A. lowest pairing cost
	pairCost = 0
	
	print "\r\nMatching Algorithm\r\n"
	
	#loops over each element selecting the bet match starting with the least desireable (itterations is n/2)
	for itteration in range(elementCount/2):
		#Gets the element with the next lowest desireability
		CrntElmt = DesIndx[0]
		
		#Finds the partner who adds the least cost to the system
		pairElmt = np.argsort(ElmList[:, CrntElmt] + ElmList[CrntElmt])[1]	
		
		#We want the element that has the lowest pairing cost
		pairCost += np.sort(ElmList[:, CrntElmt] + ElmList[CrntElmt])[1]
		
		#Gets the index of the curentElement and pairElement in DesIndx to remove
		pairIndx = list(DesIndx).index(pairElmt)
		crntIndx = list(DesIndx).index(CrntElmt)
		#Print Result Pair
		print "Pairing #" + str(itteration + 1) + "	Element " + str(IndxCpy[0]) + " is paired with " + str(pairElmt)
		
		#Removes CrntElmt and the Pair 
		ElmList = np.delete(ElmList, [CrntElmt, pairElmt], axis=1)
		ElmList = np.delete(ElmList, [CrntElmt, pairElmt], axis=0)
		
		for j in range(len(DesIndx)): 
			DesIndx[j] -= (0,1)[(crntIndx > j)] + (0,1)[(pairIndx > j)]
			
		IndxCpy = np.delete(IndxCpy, [0, pairIndx])
		DesIndx = np.delete(DesIndx, [0, pairIndx])		
		
		#print DesIndx
		#print ElmList
	print "Total Sacrifice = " + str(pairCost - elementCount) 
	print "System Equilibium = " + str((100 * ((elementCount**2) - pairCost))/((elementCount**2) - elementCount)) + "%"

arr2D = [[0,1,3,2],[1,0,2,3],[2,3,0,1],[1,2,3,0]]
#arr2D = [[0,3,1,2],[1,0,2,3],[3,2,0,1],[2,1,3,0]]
createTable_1List(np.array(arr2D))
