# unique.py

def main():

# input:
    inName = input("Enter the input file name: ")

# process:
    # Initialize an empty set to store unique words
    uniqueWords = set()


    # Open the file for reading
    with open(inName, 'r') as inputFile:
        # Loop through each line in the file
        for line in inputFile:
            # Split the line into words
            words = line.split()
            # Add each word to the set (set ensures uniqueness)
            for word in words:
                uniqueWords.add(word.strip().lower())  # Strip punctuation and convert to lowercase

    # Sort the words in alphabetical order
    sortedWords = sorted(uniqueWords)

# output:
    # Print each word in alphabetical order
    for word in sortedWords:
        print(word)

if __name__ == "__main__":
    main()
