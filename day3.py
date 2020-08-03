from sys import argv

sript, input_file = argv

def len_point_calc(path):
    x = 0
    y = 0
    length = 0
    directions = {'R': (1,0), 'L': (-1,0), 'U': (0,1), 'D': (0,-1)}
    points = {}
    for i in path:
        dx, dy = directions[i[0]]
        for j in range(int(i[1:])):
            x += dx
            y += dy
            length += 1
            if (x, y) not in points:
                points[(x, y)] = length
    return points

paths = open(input_file).read().split()
path1 = paths[0].split(',')
path2 = paths[1].split(',')

wire1 = len_point_calc(path1)
wire2 = len_point_calc(path2)

intersections = [point for point in wire1 if point in wire2]

print(min(abs(x) + abs(y) for (x, y) in intersections))
print(min(wire1[point] + wire2[point] for point in intersections))
