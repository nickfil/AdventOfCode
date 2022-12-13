f = open("input.txt", "r")
parenthesis = []
for line in f.readlines():
    parenthesis.append(line)

opening = ['(', '[', '{', '<']
closing = {')':'(', ']':'[', '}':'{', '>':'<'}
closing_scores = {')':3, ']':57, '}':1197, '>':25137}
closing_completion_scores = {'(':1, '[':2, '{':3, '<':4}
total_corrupted = 0
incomplete_list = []
for l in parenthesis:
    stack = []
    for i in range(len(l)):
        current_bracket = l[i]
        if current_bracket in opening:
            stack.append(current_bracket)
        elif current_bracket in closing:
            if stack[-1] != closing[current_bracket]:
                total_corrupted += closing_scores[current_bracket]
                break
            else:
                stack.pop()
        
        # now for incomplete lines
        if i == len(l)-1 and stack:
            total_incomplete = 0
            while stack:
                total_incomplete*=5
                total_incomplete+=closing_completion_scores[stack[-1]]
                stack.pop()
            incomplete_list.append(total_incomplete)

print("Score is: " + str(total_corrupted))
incomplete_list.sort()
print("Middle incomplete score: " + str(incomplete_list[len(incomplete_list)/2]))