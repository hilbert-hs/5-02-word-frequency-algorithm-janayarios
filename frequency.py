# 5.02 Word Frequency Algorithm

# replace the sample text with your paragraph.
# example_paragraph = "I made a severe and continuous lapse in my judgement, and I don’t expect to be forgiven. I’m simply here to apologize. What we came across that day in the woods was obviously unplanned. The reactions you saw on tape were raw; they were unfiltered. None of us knew how to react or how to feel. I should have never posted the video. I should have put the cameras down and stopped recording what we were going through. There's a lot of things I should have done differently but I didn't. And for that, from the bottom of my heart, I am sorry. I want to apologize to the internet. I want to apologize to anyone who has seen the video. I want to apologize to anyone who has been affected or touched by mental illness, or depression, or suicide. But most importantly I want to apologize to the victim and his family. For my fans who are defending my actions, please don't. I don’t deserve to be defended. The goal with my content is always to entertain; to push the boundaries, to be all-inclusive. In the world I live in, I share almost everything I do. The intent is never to be heartless, cruel, or malicious. Like I said I made a huge mistake. I don’t expect to be forgiven, I’m just here to apologize. I'm ashamed of myself. I’m disappointed in myself. And I promise to be better. I will be better. Thank you."
example_paragraph = "Yo yo yo. I like to swing my yo-yo by the swing."

# make all letters lowercase
ex_par_lowered = example_paragraph.lower()

#remove all periods (you'll want to repeat this for any other punctuation in your paragraph)
ex_par_lower_no_punc = ex_par_lowered.replace(".", "").replace(";", "").replace(",", "")

# convert the paragraph into a list of individual strings
ex_word_list = ex_par_lower_no_punc.split(" ")

wordDCT = {}

for word in ex_word_list:
    if word not in wordDCT:
        wordDCT[word] = 1
    else:
        wordDCT[word] += 1

for word in wordDCT:
    print(f">> {word} << appears {wordDCT[word]} times...")

