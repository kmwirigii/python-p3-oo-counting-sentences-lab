#!/usr/bin/env python3

import re  # Import regular expressions for advanced sentence counting

class MyString:
    def __init__(self, value=""):  # Default value is an empty string
        self.value = value  # Use property setter to validate input

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):  # Ensure value is a string
            self._value = new_value
        else:
            print("The value must be a string.")
            self._value = ""  # Default to empty string if invalid

    def is_sentence(self):
        """Returns True if the value ends with a period."""
        return self.value.endswith(".")

    def is_question(self):
        """Returns True if the value ends with a question mark."""
        return self.value.endswith("?")

    def is_exclamation(self):
        """Returns True if the value ends with an exclamation mark."""
        return self.value.endswith("!")

    def count_sentences(self):
        """Counts the number of sentences in the value."""
        # Replace multiple punctuation marks with a single period
        cleaned_value = re.sub(r"[.!?]+", ".", self.value)

        # Split the string on periods and remove empty strings
        sentences = [s.strip() for s in cleaned_value.split(".") if s.strip()]

        return len(sentences)