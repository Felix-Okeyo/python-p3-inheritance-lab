#!/usr/bin/env python

# Let's start by creating a basic class called 'User'.
class User:
    # This special function runs when a new 'User' is created.
    # It asks for the person's first name and last name, and remembers them.
    def __init__(self, first_name, last_name):
        # 'self' refers to the person we're creating.
        # 'first_name' and 'last_name' are the names they tell us.
        self.first_name = first_name
        self.last_name = last_name

# The 'User' class sets up a basic person with names.
# We can now build special classes like 'Teacher' and 'Student' using what 'User' gives us.
