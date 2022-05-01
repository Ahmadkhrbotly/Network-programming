file = open("textFile.txt", "r")
lines = file.read().split('\n')
x = 0
y = 0
op = ""
dic = {}
mark = 0
total = 0
name = input("Enter your name: ")
for index, line in enumerate(lines):
    i = index + 1
    print(line)
    attr = line.split(' ')
    if i % 5 == 1:
        x = int(attr[1])
        y = int(attr[3])
        op = attr[2]
        dic.clear()
    else:
       dic.update({str(attr[0][0]):attr[1]})
    if i % 5 == 0:
        total += 1
        while True:
            ans = input("Enter your answer (A, B, C, D): ")
            if ans in dic:
                if op == '+':
                    correct = x + y
                    if int(dic[ans]) == correct:
                        mark = mark + 1
                if op == '*':
                    correct = x * y
                    if int(dic[ans]) == correct:
                        mark = mark + 1
                if op == '-':
                    correct = x - y
                    if int(dic[ans]) == correct:
                        mark = mark + 1
                if op == '/':
                    correct = x / y
                    if int(dic[ans]) == correct:
                        mark = mark + 1
                break
resultFile = open("result.txt", "w")
resultFile.write(name+"\n")
resultFile.write("your result is: " + str(mark)+"/"+ str(total))
resultFile.close()