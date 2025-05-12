with open('atbash/str-main/str-main/duom2.txt', 'r', encoding='utf-8') as f:
    text = f.readline()

lookup_table = {'a':'ž', 'ą':'z', 'b':'v', 'c':'u', 'č':'ū', 'd':'ų', 'e':'t', 'ę':'š', 'ė':'s', 'f':'r', 'g':'p',
    'h':'o', 'i':'n', 'į':'m', 'j':'k', 'k':'j', 'l':'y', 'm':'į', 'n':'i', 'o':'h', 'p':'g',
    'r':'f', 's':'ė', 'š':'ę', 't':'e', 'u':'c', 'ų':'d', 'v':'b', 'z':'ą','ž':'a','!':'!','?':'?','_':'_'}

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

with open("atbash/str-main/str-main/duomrez2.txt", "w", encoding="utf-8") as file:
    file.write(sitas)