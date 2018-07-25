import sys
import random

inputDict = {'Asking feeling':["How are you?", "What's up?", "How you doing?"]};
outputDict = {"Asking feeling":["I'm good, how about you?", "I'm great, what about you?", "I'm not feeling so well, but how about you?"]};

def runPersonalAssistant():
	while True:
		response = raw_input("talk to your personal assistant:")
		if response == "":
			break
		#print (inputDict);
		foundKey = findKey(response, inputDict);

		if foundKey:
			for key in outputDict.keys():
				if key == foundKey:
					print (random.choice(outputDict[key]));
		else:
			print ("I don't understand")

def findKey(input, dict):
	for key, values in dict.items():
		for value in values:
			if input == value: 
				return key;
#		
#		if input == value:
#			print (key, value);
#			print ('found!');
#			return key;
#		else:
#			print (key,value);
runPersonalAssistant();