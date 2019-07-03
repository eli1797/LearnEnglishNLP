
##							 	 ##
#########    Chatper 1    #########
##								 ##


# # Import the English language class
# from spacy.lang.en import English

# # Create the nlp object
# nlp = English()

#### Section 1 ####

# # Process a text
# doc = nlp("This is a sentence.")

# # Print the document text
# print(doc.text)

#### Section 2 ####

# # Process the text
# doc = nlp("I like tree kangaroos and narwhals.")

# # Select the first token
# first_token = doc[0]

# # Print the first token's text
# print(first_token.text)

# # A slice of the Doc for "tree kangaroos"
# tree_kangaroos = doc[2:4]
# print(tree_kangaroos.text)

# # A slice of the Doc for "tree kangaroos and narwhals" (without the ".")
# tree_kangaroos_and_narwhals = doc[2:6]
# print(tree_kangaroos_and_narwhals.text)

#### Section 3

# # Process the text
# doc = nlp(
#     "In 1990, more than 60% of people in East Asia were in extreme poverty. "
#     "Now less than 4% are."
# )

# # Iterate over the tokens in the doc
# for token in doc:
#     # Check if the token resembles a number
#     if token.like_num:
#         # Get the next token in the document
#         next_token = doc[token.i + 1]
#         # Check if the next token's text equals '%'
#         if next_token.text == "%":
#             print("Percentage found:", token.text)

#### Section 4 ####

### Statistical Models and Part of Speech Tagging

# import spacy

# # Load the small English model
# nlp = spacy.load('en_core_web_sm')

# # Process a text
# doc = nlp("She ate the pizza")

# print()
# print(doc.text)

# # Iterate over the tokens
# # For part of speech tagging
# for token in doc:
#     # Print the text and the predicted part-of-speech tag
#     print(token.text, token.pos_)

# #For part of speech tagging and word relations
# for token in doc:
#     print(token.text, token.pos_, token.dep_, token.head.text)

# ### Entity Prediction

# # Process a text
# doc = nlp(u"Apple is looking at buying U.K. startup for $1 billion") #u prefix means it's a unicode string

# print()
# print(doc.text)
# # Iterate over the predicted entities
# for ent in doc.ents:
#     # Print the entity text and its label
#     print(ent.text, ent.label_)

# #what does this mean?
# gpe = spacy.explain('GPE')
# print(gpe)

# dobj = spacy.explain('dobj')
# print(dobj)

#### Section 5 ####

### Show that some entities aren't always picked up

# text = "New iPhone X release date leaked as Apple reveals pre-orders by mistake"

# # Process the text
# doc = nlp(text)

# # Iterate over the entities
# for ent in doc.ents:
#     # Print the entity text and label
#     print(ent.text, ent.label_)

# # Get the span for "iPhone X"
# iphone_x = doc[1:3]

# # Print the span text
# print("Missing entity:", iphone_x.text)

### Matcher: Custom Entitiy Patterns

# import spacy

# Import the Matcher
# from spacy.matcher import Matcher

# # Load a model and create the nlp object
# nlp = spacy.load('en_core_web_sm')

# # Initialize the matcher with the shared vocab
# matcher = Matcher(nlp.vocab)

# # Add the pattern to the matcher
# pattern = [{'TEXT': 'iPhone'}, {'TEXT': 'X'}]
# matcher.add('IPHONE_PATTERN', None, pattern)

# # Process some text
# doc = nlp("New iPhone X release date leaked")

# # Call the matcher on the doc
# matches = matcher(doc)

# # Call the matcher on the doc
# doc = nlp("New iPhone X release date leaked")
# matches = matcher(doc)

# # Iterate over the matches
# for match_id, start, end in matches:
#     # Get the matched span
#     matched_span = doc[start:end]
#     print(matched_span.text)

### My attempt to use the matcher

# # Initialize the matcher with the shared vocab
# matcher = Matcher(nlp.vocab)

# pattern = [
#     {'IS_DIGIT': True},
#     {'LOWER': 'fifa'},
#     {'LOWER': 'world'},
#     {'LOWER': 'cup'}
# ]
# matcher.add('FIFA_PATTERN', None, pattern)

# doc = nlp("2018 FIFA World Cup: France won!")

# matches = matcher(doc)

# # Iterate over the matches
# for match_id, start, end in matches:
#     # Get the matched span
#     matched_span = doc[start:end]
#     print(matched_span.text)


### More matching examples

# import spacy
# from spacy.matcher import Matcher

# nlp = spacy.load("en_core_web_sm")
# matcher = Matcher(nlp.vocab)

# doc = nlp(
#     "After making the iOS update you won't notice a radical system-wide "
#     "redesign: nothing like the aesthetic upheaval we got with iOS 7. Most of "
#     "iOS 11's furniture remains the same as in iOS 10. But you will discover "
#     "some tweaks once you delve a little deeper."
# )

# # Write a pattern for full iOS versions ("iOS 7", "iOS 11", "iOS 10")
# pattern = [{"TEXT": "iOS"}, {"IS_DIGIT": True}]

# # Add the pattern to the matcher and apply the matcher to the doc
# matcher.add("IOS_VERSION_PATTERN", None, pattern)
# matches = matcher(doc)
# print("Total matches found:", len(matches))

# # Iterate over the matches and print the span text
# for match_id, start, end in matches:
#     print("Match found:", doc[start:end].text)


##							 	 ##
#########    Chatper 2    #########
##								 ##


#### Section 1: Data Structures ####

### Vocab

# import spacy

# nlp = spacy.load("en_core_web_sm")

# doc = nlp("I love coffee")

# #vocab exposed by nlp
# print('hash value:', nlp.vocab.strings['coffee'])
# print('string value:', nlp.vocab.strings[3197928453018144401])

# #vocab exposed by doc
# doc = nlp("I love coffee")
# print('hash value:', doc.vocab.strings['coffee'])

# doc = nlp("I love coffee")
# lexeme = nlp.vocab['coffee']

# # Lexemes expose attributes, just like tokens.
# # They hold context-independent information about a word, like the text, or whether the the word consists of alphanumeric characters.

# # Print the lexical attributes
# print(lexeme.text, lexeme.orth, lexeme.is_alpha)

### Doc

# # Create an nlp object
# from spacy.lang.en import English
# nlp = English()

# # Import the Doc class
# from spacy.tokens import Doc

# # The words and spaces to create the doc from
# words = ['Hello', 'world', '!']
# # true if a space follows the word
# spaces = [True, False, False]

# # Create a doc manually
# doc = Doc(nlp.vocab, words=words, spaces=spaces)

### Doc and Span

# # Import the Doc and Span classes
# from spacy.tokens import Doc, Span

# # The words and spaces to create the doc from
# words = ['Hello', 'world', '!']
# spaces = [True, False, False]

# # Create a doc manually
# doc = Doc(nlp.vocab, words=words, spaces=spaces)

# # Create a span manually
# span = Span(doc, 0, 2)

# # Create a span with a label
# span_with_label = Span(doc, 0, 2, label="GREETING")

# # Add span to the doc.ents
# doc.ents = [span_with_label]

# for ent in doc.ents:
#     # Print the entity text and its label
#     print(ent.text, ent.label_)

### Data Struct Example

# #look for verbs following proper nouns
# import spacy

# nlp = spacy.load("en_core_web_sm")
# doc = nlp("Berlin is a nice city")

# # Iterate over the tokens
# for token in doc:
#     # Check if the current token is a proper noun
#     if token.pos_ == "PROPN":
#         # Check if the next token is a verb
#         # next_token = doc[token.i + 1].text
#         if doc[token.i + 1].pos_ == "VERB":
#             print("Found proper noun before a verb:", token.text)
#             # print("Verb:", next_token)


#### Section 2: Word Vectors and Semantic Similiarities ####

### Semantic Similiarity

# import spacy

# # Load a larger model with vectors
# nlp = spacy.load('en_core_web_md')

# # Compare two documents
# doc1 = nlp("I like fast food")
# doc2 = nlp("I like pizza")
# print(doc1.similarity(doc2))

# # Compare two tokens
# doc = nlp("I like pizza and pasta")
# token1 = doc[2]
# token2 = doc[4]
# print(token1.similarity(token2))

# #the definition of similiarity might be what you want
# #these are highly similiar according to spacy, probably because they both express sentiment towards cats
# #if you thought they're opposites you're right, but not under this definition of similiarity
# doc1 = nlp("I like cats")
# doc2 = nlp("I hate cats")

# print(doc1.similarity(doc2))

#### Section 3: Combining Models and Rules ####

### Examples

import spacy

# # Load a larger model with vectors
nlp = spacy.load('en_core_web_sm')

# # Initialize with the shared vocab
# from spacy.matcher import Matcher
# # matcher = Matcher(nlp.vocab)

# # # Patterns are lists of dictionaries describing the tokens
# # pattern = [{'LEMMA': 'love', 'POS': 'VERB'}, {'LOWER': 'cats'}]
# # matcher.add('LOVE_CATS', None, pattern)

# # # Operators can specify how often a token should be matched
# # pattern = [{'TEXT': 'very', 'OP': '+'}, {'TEXT': 'happy'}]

# # # Calling matcher on doc returns list of (match_id, start, end) tuples
# # doc = nlp("I love cats and I'm very very happy")
# # matches = matcher(doc)

# matcher = Matcher(nlp.vocab)
# matcher.add('DOG', None, [{'LOWER': 'golden'}, {'LOWER': 'retriever'}])
# doc = nlp("I have a Golden Retriever")

# print(doc.text)
# for match_id, start, end in matcher(doc):
#     span = doc[start:end]
#     print('Matched span:', span.text)
#     # Get the span's root token and root head token
#     print('Root token:', span.root.text)
#     print('Root head token:', span.root.head.text)
#     # Get the previous token and its POS tag
#     print('Previous token:', doc[start - 1].text, doc[start - 1].pos_)


### Phrase Matcher

from spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)

pattern = nlp("Golden Retriever")
matcher.add('DOG', None, pattern)
doc = nlp("I have a Golden Retriever")

# Iterate over the matches
for match_id, start, end in matcher(doc):
    # Get the matched span
    span = doc[start:end]
    print('Matched span:', span.text)


#I think you use Matcher for small entities and Phrase Matcher for multi word entities


##							 	 ##
#########    Chatper 3    #########
##								 ##
