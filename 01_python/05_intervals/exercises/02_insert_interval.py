"""
Tienes intervals ya ordenados y no overlapping:

Ejemplo:
[[1,3],[6,9]]

Y quieres insertar:
[2,5]

Output:
[[1,5],[6,9]]
"""


def solution(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)

    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)

    while i < n:
        result.append(intervals[i])
        i += 1

    return result


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]

result = solution(intervals, newInterval)
print(result)
