def main():
    response = input("Input: ")
    print(shorten(response))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    empty_string = ""
    for c in word:
        if c in vowels:
            continue
        else:
            empty_string += c
    return empty_string


if __name__ == "__main__":
    main()
