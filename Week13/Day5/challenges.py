input_str = input("Enter a comma separated sequence of words: ")

words = [word.strip() for word in input_str.split(',')]

sorted_words = sorted(words)

output_str = ','.join(sorted_words)

print("Sorted words:", output_str)

def longest_word(sentence):

    words = sentence.split()
 
    longest = ""
    max_length = 0

    for word in words:

        length = len(word)

        if length > max_length:
            longest = word
            max_length = length
    
    return longest

# Examples
print(longest_word("Margaret's toy is a pretty doll."))  
print(longest_word("A thing of beauty is a joy forever."))  
print(longest_word("Forgetfulness is by all means powerless!"))  