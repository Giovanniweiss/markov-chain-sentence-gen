# markov-chain-sentence-gen

# Markov Chain Sentence Generator.
# Include shitposting capabilities.
# Include greentext capabilities.

# Module to process a text into the database.
# Input:
    # Text of any length.
    # Database name.
    # Order.
# Output:
    # Database stored with data extracted from text.
        # Table with words;
        # Table with sentence starters;
        # Table with sentence enders;
        # Table with transitions.
        # Table with standard deviation and average.
# Procedure:
    # Remove all "-\n".
    # Replace \n with space.
    # Remove all special characters (anything that is not alphanumerical, dot or puntuation point).
    # Replace all instances of multiple spaces with single space.
    # Begin adding words to the database.
        # If they have a dot at the end, remove the dot and add the word to the sentence enders.
        # If they are the word following a sentence ender, add it to the sentence starters.
        # If they are not a sentence starter and are capitalized, classify as capital word.
        # Finally, add the word to the database, lowercase.
    # Calculate average sentence length, and standard deviation.

# Module to make a normal sentence.
# Input: 
    # Database name.
    # Number of sentences. OR
    # Number of words.
    # Order
    # Optionals:
        # Greentext format;
        # Shitpost format;
# Output:
    # Text as requested by the user.
# Functions:
    # F1 - Add the first word to the sentence.
        # Get sum of all frequencies.
        # Select a random number from 1 to the sum.
        # Select the corresponding word.
        # Add that word to the text.
    # F2 - Add the next few words to the text.
        # Add words in increasing order as the sentence grows, for the first sentence.
        # For example: I am here now.
        # I is random, am is order 1, here is order 2 and now is order 3.
        # In other words, execute F3 with increasing order.
    # F3 - Add a word.
        # Input: 
            # Order.
        # Using the previous words and the order, filter the possibilities for the next word.
        # Get sum of all frequencies of the filteres words.
        # Select a random number from 1 to the sum.
        # Select the corresponding word.
        # Add that word to the text.
        # Check if the sentence should end.
            # Compare to the average and standard deviation.
            # Roll a chance to end the sentence.
    # F4 - Create a sentence.
        # F1, capitalize word.
        # Check for word limit.
        # Until len(sentence) > order: F2.
        # Until sentence is over: F3.
        # After sentence is over, add ". "
        # Return sentence.
# Procedure:
    # Until the number of sentences is met:
        # F4.
    # Until number of words is met:
        # F4.
