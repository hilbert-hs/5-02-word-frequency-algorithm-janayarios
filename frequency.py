# 5.02 Word Frequency Algorithm

# replace the sample text with your paragraph.
example_paragraph = "lorem ipsum....."

# make all letters lowercase
ex_par_lowered = example_paragraph.lower()

#remove all periods (you'll want to repeat this for any other punctuation in your paragraph)
ex_par_lower_no_punc = ex_par_lowered.replace(".", "")

# convert the paragraph into a list of individual strings
ex_word_list = ex_par_no_punc.split(" ")


