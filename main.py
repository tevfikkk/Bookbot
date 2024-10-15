def count_chars(text: str) -> dict:
    lowered_text = text.lower()

    char_dict = {}

    for char in lowered_text:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

    return char_dict

def generate_report(file_path: str, file_contents: str):
    # Count characters and words
    word_count = count_words(file_contents)
    char_counts = count_chars(file_contents)

    # Convert character dictionary to a list of dictionaries
    char_list = [{"char": char, "num": count} for char, count in char_counts.items()]

    # Sort the list of dictionaries by the number of occurrences in descending order
    char_list.sort(reverse=True, key=lambda d: d["num"])

    # Print the report
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    
    for char_data in char_list:
        print(f"The '{char_data['char']}' character was found {char_data['num']} times")
    
    print("--- End report ---")


def count_words(text: str) -> int:
    count = len(text.split())
    print(count)

def main():
    path: str = "books/frankenstein.txt"

    with open(path) as f:
        file_contents = f.read()
    
    generate_report(path, file_contents=file_contents)

if __name__ == "__main__":
    main()