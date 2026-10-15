"""หั่นขนมปัง"""

w, h, m, n = map(int, input().split())
x_cuts = list(map(int, input().split()))
y_cuts = list(map(int, input().split()))

widths = [x_cuts[0]]
for i in range(1, m):
    widths.append(x_cuts[i] - x_cuts[i - 1])
widths.append(w - x_cuts[-1])

heights = [y_cuts[0]]
for i in range(1, n):
    heights.append(y_cuts[i] - y_cuts[i - 1])
heights.append(h - y_cuts[-1])

widths.sort(reverse=True)
heights.sort(reverse=True)

max1 = widths[0] * heights[0]
max2 = max(widths[0] * heights[1], widths[1] * heights[0])

print(f"{max1} {max2}")
