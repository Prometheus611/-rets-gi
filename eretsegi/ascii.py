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

def convert(asci):
    full=[]
    asci_split=[]
    for i in range(len(asci)):
        asci_split.append(asci[i])
    text_index=[]
    i=0
    while i<=len(asci_split)-1:
        end = 0
        while end == 0:
            if asci_split[i]=="\n":
                end = 1
            if str(asci_split[i]).isdigit():
                for f in range(int(asci_split[i])):
                    text_index.append(asci_split[i+1])
            i+=1
        for f in range(0,i,-1):
            asci_split.pop(f)
        full.append("".join(text_index))
        text_index = []
    return full

print("exercise 1:")
f = open("book.txt", "r")
book_i = f.read()
book_lines = book_i.split()
print(F"    {book_lines[0]}")
print(F"   {book_lines[1]}      {book_lines[2]}")
print(F"  {book_lines[3]}      {book_lines[4]}")
print(F" {book_lines[5]}")
print(F"{book_lines[6]}")
print("exercise 2:")
n=int(input("number of books: "))
printlotbuk(n)
print("exercise 4:")
g = open("comp_c.txt", "r")
text = g.read()
image = convert(text)
with open("comp.txt","w") as c:
    c.write("")
for i in range(0,len(image)):
    with open("comp.txt","a") as c:
        c.write(image[i])
        c.write("\n")
computer = open("comp.txt","r")
print(computer.read())
print("exercise 5:")
comp = open(str(input("name of the compressed file: ")),"r")
uncomp = open(str(input("name of the uncompressed file: ")),"r")
a=comp.read()
b=uncomp.read()
complen=0
for i in range(0,len(a)-1):
    if a[i]=="\n":
        complen-=1
    complen+=1
uncomplen=0
for i in range(0,len(b)-1):
    if b[i]=="\n":
        uncomplen-=1
    uncomplen+=1
print(F"number of characters in compressed: {complen}")
print(F"number of characters in uncompressed: {uncomplen}")
print(F"compression ration: {round(float(complen/uncomplen),2)}")
print("exercise 6:")
bookco = open("book_c.txt","r")
bookc=bookco.read()
bookstat_index = convert(bookc)
width=int()
blocks=int()
for i in range(len(bookstat_index)):
    if len(bookstat_index[i])>width:
        width=len(bookstat_index[i])
    for f in range(len(bookstat_index[i])):
        if bookstat_index[i][f] == "_":
            blocks+=1
print(F"height is: {len(bookstat_index)}")
print(F"width is: {width}")
print(F"number of blocks: {blocks}")