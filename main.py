def main():
    import os
    import glob
    file_contents = ""
    counter = 0
    letter_count = {
        "a":0,"b":0,"c":0,"d":0,
        "e":0,"f":0,"g":0,"h":0,
        "i":0,"j":0,"k":0,"l":0,
        "m":0,"n":0,"o":0,"p":0,
        "q":0,"r":0,"s":0,"t":0,
        "u":0,"v":0,"w":0,"x":0,
        "y":0,"z":0,
    }
    for filename in glob.glob(os.path.join("books", '*.txt')):
        with open(filename) as f:
            file_contents = f.read()
            word_count = file_contents.split()
            letters = file_contents.lower()
            for words in word_count:
                counter +=1
            for letter in letters:
                if letter in letter_count:
                    letter_count [letter] +=1
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{counter} words found in the document\n")
    sorted_letters = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
    for letter, count in sorted_letters:    
        print(f"The '{letter}' character was found {count} times")
    print("--- End report ---")
main()