"""
Dado:
[[1,2],[2,3],[3,4],[1,3]]

Retornar cuántos intervals hay que remover para que no haya overlaps.

Output:
1

Porque removiendo:
[1,3]
"""


def solution(intervals):
    intervals.sort(key=lambda x: x[1])
    result = 0
    prev_end = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] < prev_end:
            result += 1
        else:
            prev_end = intervals[i][1]

    return result


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
result = solution(intervals)
print(result)
