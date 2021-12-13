def pretty_print(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def calculate_diagonal(x1,y1,x2,y2):
    ret=[]
    s = min(x1, x2)
    e = max(x1, x2)

    ymin=0
    ymax=0
    if (x1==s): 
        yfirst = y1
        ysecond = y2
    else:
        yfirst = y2
        ysecond = y1
    if (yfirst < ysecond):
        index=0
        for i in range(s, e+1):
            ret.append({'x': i, 'y': yfirst+index})
            index+=1
    else:
        index=0
        for i in range(s, e+1):
            ret.append({'x': i, 'y': yfirst-index})
            index+=1
    return ret

def generate_all_points(x1, y1, x2, y2, andDiagonal):
    retList = []

    if (x1 == x2):
        s = min(y1, y2)
        e = max(y1, y2)
        for i in range(s, e+1):
            retList.append({'x': x1, 'y': i})
    elif (y1 == y2):
        s = min(x1, x2)
        e = max(x1, x2)
        for i in range(s, e+1):
            retList.append({'x': i, 'y': y1})
    elif andDiagonal:
        retList = calculate_diagonal(x1,y1,x2,y2)
    return retList

def is_horizontal_or_vertical_line(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2

f = open("input.txt", "r")

start_coordinates = []
end_coordinates = []

all_start_coordinates = []
all_end_coordinates = []
for line in f.readlines():
    start_x = int(line.split('->')[0].split(',')[0])
    start_y = int(line.split('->')[0].split(',')[1])
    
    end_x = int(line.split('->')[1].split(',')[0])
    end_y = int(line.split('->')[1].split(',')[1])

    if (is_horizontal_or_vertical_line(start_x, start_y, end_x, end_y)):
        start_coordinates.append({'x': start_x, 'y': start_y})
        end_coordinates.append({'x': end_x, 'y': end_y})
    
    all_start_coordinates.append({'x': start_x, 'y': start_y})
    all_end_coordinates.append({'x': end_x, 'y': end_y})

all_points = []
all_points_and_diagonal = []
for i in range(len(start_coordinates)):
    all_points.append(generate_all_points(start_coordinates[i]['x'], start_coordinates[i]['y'], end_coordinates[i]['x'], end_coordinates[i]['y'], False))
for i in range(len(all_start_coordinates)):
    all_points_and_diagonal.append(generate_all_points(all_start_coordinates[i]['x'], all_start_coordinates[i]['y'], all_end_coordinates[i]['x'], all_end_coordinates[i]['y'], True))
all_points_flat = [item for sublist in all_points for item in sublist]
all_points_and_diagonal_flat = [item for sublist in all_points_and_diagonal for item in sublist]

max_value = 1000
m = [ [ '.' for i in range(max_value) ] for j in range(max_value) ]
m_diag = [ [ '.' for i in range(max_value) ] for j in range(max_value) ]

for point in all_points_flat:
    if(m[point['y']][point['x']] == '.'):
        m[point['y']][point['x']] = 1
    else:
        m[point['y']][point['x']] += 1

for point in all_points_and_diagonal_flat:
    if(m_diag[point['y']][point['x']] == '.'):
        m_diag[point['y']][point['x']] = 1
    else:
        m_diag[point['y']][point['x']] += 1

counter = 0
for i in range(max_value):
    for j in range(max_value):
        if(m[i][j]!='.' and m[i][j]>1):
            counter+=1
print(counter)

counter = 0
for i in range(max_value):
    for j in range(max_value):
        if(m_diag[i][j]!='.' and m_diag[i][j]>1):
            counter+=1
print(counter)