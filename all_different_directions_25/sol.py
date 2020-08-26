from sys import stdin
import math

if __name__ == '__main__':
    l = int(input().strip())
    while l != 0:
        destinations = []
        for _ in range(int(l)):
            l_angle = 0
            l = input().strip().split()
            x, y = map(float, l[:2])
            l = l[2:]
            for idx in range(int(len(l) / 2)):
                instr = l[2 * idx]
                numb = float(l[2 * idx + 1])
                if instr == 'start':
                    l_angle = numb
                elif instr == 'walk':
                    x += math.cos(math.radians(l_angle)) * numb
                    y += math.sin(math.radians(l_angle)) * numb
                else:
                    l_angle += numb
            destinations.append([x, y])
        # average calculations and max distance
        avg_x = sum([x[0] for x in destinations]) / len(destinations)
        avg_y = sum([x[1] for x in destinations]) / len(destinations)
        distances = [math.sqrt((x[0] - avg_x)**2 + (x[1] - avg_y)**2) for x in destinations]
        print("{} {} {}".format(avg_x, avg_y, max(distances)))
        l = int(input().strip())

