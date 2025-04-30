from stats import get_num_words


def sort_on(dict):
    return dict["count"]


def main():
    # if len(sys.argv) < 2:
    #     print("Usage: python3 main.py <path_to_book>")
    #     sys.exit(1)

    # book_path = sys.argv[1]
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_content = f.read().lower()
        num_words = get_num_words(file_content)

        # Count the number of times each char occours
        content_dict = {}
        for char in file_content:
            if not char.isalpha():
                continue

            if char not in content_dict:
                content_dict[char] = 1
            else:
                content_dict[char] += 1

        # Sort the dictionary
        list_of_dicts = []
        for key in content_dict:
            list_of_dicts.append({"char": key, "count": content_dict[key]})

        list_of_dicts.sort(reverse=True, key=sort_on)

        # Print a summary
        print("============ BOOKBOT ============")
        # print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"{num_words} words found in the document")
        # print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for i in list_of_dicts:
            print(f"{i['char']}: {i['count']}")

        print("============= END ===============")


main()
