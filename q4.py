
def change_first_letter(init_char, words):
    new_list = list()

    for word in words:
        new_list.append(init_char + word[1:])

    return new_list


def main():
    print(change_first_letter('a', ['front-end', 'back-end', 'database']))

if __name__ == '__main__':
    main()
