def sort_on(dict):
    return dict["count"]


def main():
    with open("./books/frankenstein.txt") as f:
        file_content = f.read().lower()
        num_words = len(file_content.split())

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
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{num_words} words found in the document \n\n")

        for i in list_of_dicts:
            print(f"The '{i["char"]}' character was found {i["count"]} times")

        print("--- END REPORT ---")


main()
