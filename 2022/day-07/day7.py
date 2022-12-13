class Node(object):
    def __init__(self, data, parent, value, type):
        self.data = data
        self.parent = parent
        self.value = value
        self.type = type
        self.children = []

    def add_child(self, obj, parent, value, type):
        self.children.append(Node(obj, parent, value, type))

    def getAllValuesSmallerThan100k(self, smallerThat100k):
        if self.data == None or self.type == 'file':
            return
         
        total = len(self.children)
         
        for i in range(total-1):
            self.children[i].getAllValuesSmallerThan100k(smallerThat100k)

        if (self.value <= 100000):
            smallerThat100k.append(self.value)
         
        self.children[total-1].getAllValuesSmallerThan100k(smallerThat100k)
        return smallerThat100k

    def getAllValuesLargerThan(self, largerThanMinSpace, minSpace):
        if self.data == None or self.type == 'file':
            return
         
        total = len(self.children)
         
        for i in range(total-1):
            self.children[i].getAllValuesLargerThan(largerThanMinSpace, minSpace)

        if (self.value >= minSpace):
            largerThanMinSpace.append(self.value)
         
        self.children[total-1].getAllValuesLargerThan(largerThanMinSpace, minSpace)
        return largerThanMinSpace

def readInput():
    f = open("input.txt", "r")
    input = []
    for line in f.readlines():
        input.append(line.strip())
    return input

def findChild(node, child):
    for each in node.children:
        if each.data == child:
            return each
    
def listToTree(lst):
    root = Node('/', None, 0, 'dir')
    currentNode = root
    for item in lst:
        item = item.split(' ')
        if (item[0] == '$'): #command
            if (item[1] == 'ls' or item[2] == '/'):
                continue
            else:
                if (item[2] == '..'):
                    currentNode = currentNode.parent
                else:
                    currentNode = findChild(currentNode, item[2]) #cd into some dir
        elif (item[0] == 'dir'): #add child
            currentNode.add_child(item[1], currentNode, 0, 'dir')
        else: # actual file
            currentNode.add_child(item[1], currentNode, int(item[0]), 'file')
    return root

def populateFileSizes(root):
    def recur(root):
        if root is None:
            return 0
    
        for child in root.children:
            root.value += recur(child)
        return root.value
    
    recur(root)
    return root
        
def part1(input):
    root = listToTree(input)
    root = populateFileSizes(root)
    all = []
    root.getAllValuesSmallerThan100k(all)
    
    print("Part 1: " + str(sum(all)))

def part2(input):
    root = listToTree(input)
    root = populateFileSizes(root)
    toFree = 30000000 - (70000000 - root.value)
    all = []
    root.getAllValuesLargerThan(all, toFree)
    
    print("Part 2: " + str(min(all)))
    

def main():
    input = readInput()
    part1(input)
    part2(input)

if __name__ == "__main__":
    main()