
def starts_with_char(init_char, my_str):
    if my_str.startswith(init_char):
        return True
    else:
        return False

def check_qualified_strings(init_char, words_list):
    count = 0

    for word in words_list:
        if starts_with_char(init_char, word):
            count += 1
    
    return count

def main():
    print(check_qualified_strings('a', ['front-end', 'angular', 'back-end', 'database', 'async']))

if __name__ == '__main__':
    main()
