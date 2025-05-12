
with open('str/duom.txt', 'r', encoding='utf-8') as f:
    text = f.readline()
    k = []
    # print(listas2)

    dict = {
        "A": "Z",
        "B": "Y",
        "C": "X",
        "D": "W",
        "E": "V",
        "F": "U",
        "G": "T",
        "H": "S",
        "I": "R",
        "J": "Q",
        "K": "P",
        "L": "O",
        "M": "N" 
    }

    for i in text:
        if i.upper() in dict:
            new_char = dict[i.upper()]
            if i.islower():
                new_char = new_char.lower()
            k.append(new_char)
        else:
            k.append(i)

    transformed = ''.join(k)
    print(transformed)


        

