def contains(a, b):
    for char in b:
        if char not in a:
            return False
    return True

def generateKey(lst):
    k = [-1]*10
    # get all easy known keys first
    for string in lst:
        if (len(string)==2): #1
            k[1] = string
        elif(len(string)==4): #4
            k[4] = string
        elif(len(string)==3): #7
            k[7] = string
        elif(len(string)==7): #8
            k[8] = string
    
    #find 3
    for string in lst:
        if(len(string)==5 and contains(string, k[1])):
            k[3] = string
    #find 9
    for string in lst:
        if(len(string)==6 and contains(string, k[3])):
            k[9] = string
    #find 5
    for string in lst:
        if(len(string)==5 and contains(k[9], string) and not contains(k[3], string)):
            k[5] = string
    #find 6
    for string in lst:
        if(len(string)==6 and contains(string, k[5]) and not contains(string, k[3])):
            k[6] = string
            break
    #find 0
    for string in lst:
        if(len(string)==6 and contains(string, k[1]) and not contains(string, k[5])):
            k[0] = string
    #find 2
    for string in lst:
        if(string not in k):
            k[2] = string

    k_map = {}
    for i in range(len(k)):
        k_map[k[i]] = i
    print(len(k_map))
    return k_map
    
def isUnique(d):
    m = {}
    for each in d:
        if each not in m:
            m[each]=1
        else:
            m[each]+=1
    return all(value == 1 for value in m.values())

def isEasyDigit(d):
    if (isUnique(d)):
        if (len(d)==2): #1
            return True
        elif(len(d)==4): #4
            return True
        elif(len(d)==3): #7
            return True
        elif(len(d)==7): #8
            return True
    return False


def clean(lst):
    ret = []
    for item in lst:
        if item != '':
            ret.append(item.strip())
    return ret

def calculate(k, inp):
    num = ""
    for digit in inp:
        num+=str(k[digit])
    return int(num)

f = open("input.txt", "r")
input_digits = []
output_digits = []
for line in f.readlines():
    left = line.split("|")[0]
    right = line.split("|")[1]

    input_digits.append(clean(left.split(" ")))
    output_digits.append(clean(right.split(" ")))

counter = 0
for i in range(len(output_digits)):
    for j in range(len(output_digits[0])):
        if isEasyDigit(output_digits[i][j]):
            counter+=1
        
print("Number of easy digits is: " + str(counter))

numbers = []
for i in range(len(input_digits)):
    sortedLettersInput = ["".join(sorted(l)) for l in input_digits[i]]
    sortedLettersOutput = ["".join(sorted(l)) for l in output_digits[i]]
    key = generateKey(sortedLettersInput)
    print(key, sortedLettersOutput)
    numbers.append(calculate(key, sortedLettersOutput))
print(sum(numbers))
        

