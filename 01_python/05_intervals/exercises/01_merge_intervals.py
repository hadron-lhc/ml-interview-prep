"""
Input:
[[1,3],[2,6],[8,10],[15,18]]

Output:
[[1,6],[8,10],[15,18]]
"""


def solution(intervals):
    intervals.sort(key=lambda x: x[0])
    result = []
    current = intervals[0]

    for interval in intervals[1:]:
        if interval[0] <= current[1]:
            start = min(current[0], interval[0])
            end = max(current[1], interval[1])
            current = [start, end]
        else:
            result.append(current)
            current = interval
    result.append(current)
    return result


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
result = solution(intervals)
print(result)
