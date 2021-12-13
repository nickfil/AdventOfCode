f = open("input.txt", "r")
commands = []
options = []
for line in f.readlines():
    option = line.split(" ")
    command = option[0]
    value = int(option[1])
    commands.append(command)
    options.append(value)

horizontalPos = 0
depth = 0
aim = 0

for i in range(len(commands)):
    if commands[i] == "forward":
        horizontalPos+=options[i]
        depth-=(aim*options[i])
    elif commands[i] == "down":
        # depth-=options[i]
        aim+=options[i]
    elif commands[i] == "up":
        # depth+=options[i]
        aim-=options[i]
    print(horizontalPos)
    print(depth)
    print(aim)
    print("-------")

print("Depth is: " + str(depth))
print("Horizontal position is: " + str(horizontalPos))
print("Product is: " + str(depth*horizontalPos))

