with open('atbash/str-main/str-main/duom.txt', 'r', encoding='utf-8') as f:
    text = f.readline()

lookup_table = {'a':'z', 'b':'y', 'c':'x', 'd':'w', 'e':'v', 'f':'u', 'g':'t', 'h':'s', 'i':'r', 'j':'q', 'k':'p',
    'l':'o', 'm':'n', 'z':'a', 'y':'b', 'x':'c', 'w':'d', 'v':'e', 'u':'f', 't':'g', 's':'h',
    'r':'i', 'q':'j', 'p':'k', 'o':'l', 'n':'m', '!':'!', '?':'?', '_':'_'}

def atbash(text):
	cipher = ''
	for letter in text:
		if(letter != ' '):
			cipher += lookup_table[letter]
		else:
			cipher += ' '

	return cipher

message = text
sitas=atbash(message.lower())   

with open("atbash/str-main/str-main/duomrez.txt", "w", encoding="utf-8") as file:
    file.write(sitas)


        

