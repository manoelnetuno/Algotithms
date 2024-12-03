
def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])
    return merge(left_half, right_half)


def sort_string(string):
    if not string:
        return ""
    return "".join(merge_sort(list(string.lower())))


def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return ("", "", False)

    first_sorted = sort_string(first_string)
    second_sorted = sort_string(second_string)

    if not first_string or not second_string:
        return (first_sorted, second_sorted, False)

    are_anagram = first_sorted == second_sorted

    return (first_sorted, second_sorted, are_anagram)
