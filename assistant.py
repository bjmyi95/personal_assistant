import sys
import random
import re     

afq1 = r"\wow are you\??" #How are you?
afq2 = r"\what(s |'s | is )up\??" #What's up?
afq3 = r"\wow( are | )you doing\??" #How you doing?
afq4 = r"(^[Ww]hat(s |'s | is )up\??$)|(^[Hh]ow (((are you)( doing)?)|(you doing))\??$)" 
inputDict = {'Asking feeling':[afq4]};
outputDict = {"Asking feeling":["I'm good.", "I'm great.", "I'm not feeling so well."]};

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
					if re.search(afq1, response, flags=0):
						print (random.choice(outputDict[key])+' How are you?');
					elif re.search(afq2, response, flags=0):
						print (random.choice(outputDict[key])+" What's up?");
					elif re.search(afq3, response, flags=0):
						print (random.choice(outputDict[key])+" How are you doing?");
		else:
			print ("I don't understand")

def findKey(input, dict):
	for key, values in dict.items():
		for value in values:
			if re.search(value, input, flags=0):
				return key;
			#if input == value: 
			#	return key;
#		
#		if input == value:
#			print (key, value);
#			print ('found!');
#			return key;
#		else:
#			print (key,value);
runPersonalAssistant();