"""

Ejemplo:
nums = [1, -1, 5, -2, 3]
k = 3

Output: 4

Porque:
        [1, -1, 5, -2] → suma 3 → longitud 4

"""


def longest_subarray(nums, k):
    first_seen = {0: -1}
    result = 0
    prefix_sum = 0

    for i, num in enumerate(nums):
        prefix_sum += num
        complement = prefix_sum - k

        if complement in first_seen:
            result = max(result, i - first_seen[complement])

        if prefix_sum not in first_seen:
            first_seen[prefix_sum] = i

    return result


def main():
    nums = [1, -1, 5, -2, 3]
    k = 3

    result = longest_subarray(nums, k)
    print(result)


if __name__ == "__main__":
    main()
