def get_ones_by_pos_for_list(lst):
    ones_by_pos = {}
    for d in range(len(lst[0])):
        ones_by_pos[d] = 0
    for number in lst:
        for i in range(len(number)):
            if (number[i] == "1"):
                ones_by_pos[i]+=1

    return ones_by_pos

def get_most_common_digit(ones_by_pos, pos, total_size, tie_breaker):
    if (float(ones_by_pos[pos])/float(total_size) > .5):
        return "1"
    elif (float(ones_by_pos[pos])/float(total_size) == .5):
        return tie_breaker
    else:
        return "0"

def get_least_common_digit(ones_by_pos, pos, total_size, tie_breaker):
    print(ones_by_pos)
    print(total_size)
    if (float(ones_by_pos[pos])/float(total_size) > .5):
        return "0"
    elif (float(ones_by_pos[pos])/float(total_size) == .5):
        return tie_breaker
    else:
        return "1"

def calculate_new_list(lst, digit, pos):
    retList = []
    for item in lst:
        if(item[pos] == digit):
            retList.append(item)
    return retList

f = open("input.txt", "r")
numbers = []
for line in f.readlines():
    numbers.append(line.strip())

gamma_rate = "" #most common bit
epsilon_rate = "" #least common bit

total_entries = len(numbers)

# will be counting how many 1s there are and then divide by the
# total to find if they are majority or minority
ones_by_pos = get_ones_by_pos_for_list(numbers)

for key in sorted(ones_by_pos):
    if (float(ones_by_pos[key])/float(total_entries) > .5):
        gamma_rate+=("1")
        epsilon_rate+=("0")
    else:
        gamma_rate+=("0")
        epsilon_rate+=("1")

print("Power Consumption: " + str(int(gamma_rate,2)*int(epsilon_rate,2)))

oxygen_generator_rating = ""
co2_scrubber_rating = ""

index = 0
current_lst = numbers
while(index < len(numbers[0])):
    ones_by_pos = get_ones_by_pos_for_list(current_lst)
    most_common = get_most_common_digit(ones_by_pos, index, len(current_lst), "1")
    current_lst = calculate_new_list(current_lst, most_common, index)
    if (len(current_lst)==1):
        oxygen_generator_rating+=current_lst[0][index:]
        break

    oxygen_generator_rating+=most_common
    index+=1

index = 0
current_lst = numbers
while(index < len(numbers[0])):
    ones_by_pos = get_ones_by_pos_for_list(current_lst)
    least_common = get_least_common_digit(ones_by_pos, index, len(current_lst), "0")
    current_lst = calculate_new_list(current_lst, least_common, index)
    if (len(current_lst)==1):
        co2_scrubber_rating+=current_lst[0][index:]
        break

    co2_scrubber_rating+=least_common
    index+=1

print("Oxygen Generator Rating: " + str(oxygen_generator_rating))
print("CO2 Scruber Rating: " + str(co2_scrubber_rating))

print("Life Support Rating: " + str(int(oxygen_generator_rating,2)*int(co2_scrubber_rating,2)))