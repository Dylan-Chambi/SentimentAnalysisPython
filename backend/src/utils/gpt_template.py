

SENTIMENT_ANALYSIS_TEMPLATE = """
Act as a sentiment analysis model, where you receive a text as an input and return a sentiment score.
The score is a float number between -1 and 1, where -1 is the most negative sentiment and 1 is the most positive sentiment.

The score ranges are divided in 7 categories:
-1 to -0.7: Very Negative
-0.7 to -0.4: Negative
-0.4 to -0.1: Slightly Negative
-0.1 to 0.1: Neutral
0.1 to 0.4: Slightly Positive
0.4 to 0.7: Positive
0.7 to 1: Very Positive

And provide a score with at least 3 decimals.

Analyze the sentiment of the following text:
"{text_input}"

Generate the response which whathever is the text and using the {format_instructions}.
"""


POS_TAGGING_TEMPLATE = """
Act as a Part of Speech tagging model, where you receive a text as an input and return a list of tuples with the word and the POS tag.
Where the possible POS tags are: ADJ, ADP, ADV, AUX, CCONJ, DET, INTJ, NOUN, NUM, PART, PRON, PROPN, PUNCT, SCONJ, SYM, VERB, X
Only tag the words that are possible to tag, for example, if the word is a number, you can't tag it as a VERB.
If theres no POS tag, just dont add a tuple for that word.
If there is no data for the POS, then an empty array should be returned
Analyze the POS tagging of the following text:
"{text_input}"

Generate the response which whathever is the text and using the {format_instructions}.
"""

NER_TEMPLATE = """
Act as a Named Entity Recognition model, where you receive a text as an input and return a list of tuples with the word and the NER tag.
Where the possible NER tags are: CARDINAL, DATE, EVENT, FAC, GPE, LANGUAGE, LAW, LOC, MONEY, NORP, ORDINAL, ORG, PERCENT, PERSON, PRODUCT, QUANTITY, TIME, WORK_OF_ART
Only tag the words that are possible to tag. It is not necessary to tag all the words.
If theres no NER tag, just dont add a tuple for that word.
If there is no data for the NER, then an empty array should be returned
Analyze the NER of the following text:
"{text_input}"

Generate the response which whathever is the text and using the {format_instructions}.
"""