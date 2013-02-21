#This converts words from letter to binary via an switch like function
from sys import argv

script, words = argv

#pass letters from word and convert with one space added
def to_morse(letter):
	return {
		'a' : ".-",
	        'b' : "-...",
		'c' : "-.-.",
		'd' : "-..",
		'e' : ".",
		'f' : "..-",
		'g' : "--.",
		'h' : "....",
		'i' : "..",
		'j' : ".---",
		'k' : "-.-",
		'l' : ".-..",
		'm' : "--",
		'n' : "-.",
		'o' : "---",
		'p' : ".--.",
		'q' : "--.-",
		'r' : ".-.",
		's' : "...",
		't' : "-",
		'u' : "..-",
		'v' : "...-",
		'w' : ".--",
		'x' : "-..-",
		'y' : "-.--",
		'z' : "--..",
		'1' : ".----",
		'2' : "..---",
		'3' : "...--",
		'4' : "....-",
		'5' : ".....",
		'6' : "-....",
		'7' : "--...",
		'8' : "---..",
		'9' : "----.",
		'0' : "-----",
		' ' : " ",
	}[letter]
	#print "%c" % letter

print "The words you entered was %s\n" % words

print "This in morse code is: "

for letter in words:
	print to_morse(letter) + " = %c " %letter

