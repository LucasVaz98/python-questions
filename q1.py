def itens_above_avg(arr):
    avg = average(arr)
    count = 0

    for item in arr:
        if item > avg:
            count+=1
    return count

def average(arr):
    total = 0
    
    for number in arr:
        total += number

    return total / len(arr)

def main():
    print(itens_above_avg([22, 28, 33, 54, 14, 2, 76]))


if __name__ == '__main__':
        main()
