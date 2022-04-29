

def sum_odd_index(arr):
    sum = 0

    for item in arr:
        if not (arr.index(item) % 2 == 0):
            sum += item
    return sum


def main():
    print(sum_odd_index([22, 28, 33, 54, 14, 2,76]))

if __name__ == '__main__':
    main()
