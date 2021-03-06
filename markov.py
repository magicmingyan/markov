"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
	"""Take file path as string; return text as string.

	Takes a string that is a file path, opens the file, and turns
	the file's contents as one string of text.
	"""

	file_read = open(file_path, 'r')
	file_str = file_read.read()
	return file_str

	# return "Contents of your file as one long string"


def make_chains(text_string):
	"""Take input text as string; return dictionary of Markov chains.

	A chain will be a key that consists of a tuple of (word1, word2)
	and the value would be a list of the word(s) that follow those two
	words in the input text.

	For example:

		>>> chains = make_chains("hi there mary hi there juanita")

	Each bigram (except the last) will be a key in chains:

		>>> sorted(chains.keys())
		[('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

	Each item in chains is a list of all possible following words:

		>>> chains[('hi', 'there')]
		['mary', 'juanita']
		
		>>> chains[('there','juanita')]
		[None]
	"""
	chains = {}

	# your code goes here
	text_string = text_string.split()

	for i in range(len(text_string) - 2):
		bigram = (text_string[i], text_string[i + 1])
		next_word = text_string[i + 2]
		if bigram not in chains:
			chains[bigram] = []
		chains[bigram].append(next_word)

	return chains
	



def make_text(chains):
#     """Return text from chains."""

	words = []
	link = choice(list(chains.keys()))

	while link in chains:
		link_value = choice(chains[link])
		words.extend(list(link))
		words.append(link_value)

		link = (link[1],) + (link_value,)
		
	return " ".join(words)


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

#Produce random text
random_text = make_text(chains)

print(random_text)