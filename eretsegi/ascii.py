import re

def printlotbuk(n):
    row1 = "    "+book_lines[0]
    row2 = "   "+book_lines[1]+"      "+book_lines[2]
    row3 = "  "+book_lines[3]+"      "+book_lines[4]
    row4 = " "+book_lines[5]
    row5 = book_lines[6]
    rows1 = []
    rows2 = []
    rows3 = []
    rows4 = []
    rows5 = []
    for i in range(n):
        rows1.append(row1)
        rows2.append(row2)
        rows3.append(row3)
        rows4.append(row4)
        rows5.append(row5)
    if n==1:
        print(row1)
        print(row2)
        print(row3)
        print(row4)
        print(row5)
        return
    elif n>1:
        print("  | ".join(rows1))
        print(" | ".join(rows2))
        print("  | ".join(rows3))
        print("   | ".join(rows4))
        print("    | ".join(rows5))
        return



f = open("book.txt", "r")
book_i = f.read()
book_lines = book_i.split()
print(F"    {book_lines[0]}")
print(F"   {book_lines[1]}      {book_lines[2]}")
print(F"  {book_lines[3]}      {book_lines[4]}")
print(F" {book_lines[5]}")
print(F"{book_lines[6]}")
# n=int(input("szám "))
# printlotbuk(n)
g = open("book_c.txt", "r")
asci = g.read()
asci_split = re.split("\s",asci)
text_index = []
for i in range(len(asci_split)):
    asci_index = asci_split[i]
    if asci_index.isdigit():
        for i in range(int(asci_index)):
            text_index.append(" ")
    else:
        no_uno = list(asci_index)
        if no_uno[-1].isdigit():
            no_uno.pop(-1)
        for i in range(0,len(no_uno)-1):
            if no_uno[i].isdigit():
                print(int(no_uno[i]))
                for f in range(0,int(no_uno[i])):
                    text_index.append(no_uno[i+1])
    print(text_index)