# Playback Speed

# Concept: Understanding string replacement and handling whitespace.


"""
1.	Pause Between Letters

Write a program pause_letters.py that prompts the user for input and outputs the input with each character separated by a hyphen (-).
Example:
Input: hello
Output: h-e-l-l-o

"""

text = input("What? ")
text_hyphen = "-".join(text)
print(text_hyphen)


"""

2.	Word Counter

Write a program word_count.py that prompts the user for a sentence and outputs the total number of words in the sentence.
Example:
Input: hello world how are you
Output: 5

"""

text2 = input("What? ")
count_text2 = len(text2.split()) # The method split allows the code to count the number of words. Without the method, the number of characters are counted.
print(count_text2)


"""

3.	Reverse Playback
Write a program reverse_playback.py that prompts the user for input and outputs the words in reverse order, separated by three periods (...).
Example:
Input: hello world
Output: world...hello

"""

text3 = input("What? ")
words = text3.split() # split the string into a list of words
reversed_words = list(reversed(words)) # reverse the list of words
result = "...".join(reversed_words) # join the reversed list of words with "..."
print(result)