#!/usr/bin/env python

# Import the User class from the user module.
from user import User

# Import the random module to help us choose random knowledge.
import random

# Create a new class called 'Teacher' that inherits from the 'User' class.
class Teacher(User):
    # This special function runs when a new 'Teacher' is created.
    def __init__(self, first_name, last_name):
        # Call the special function in the 'User' class to set the names.
        super().__init__(first_name, last_name)
        # Create a list of knowledge that the teacher has.
        self.knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]
    
    # This function lets the teacher share some knowledge.
    def teach(self):
        # Pick a random number between 0 and the length of the knowledge list.
        index = random.randint(0, len(self.knowledge) - 1)
        # Return a random piece of knowledge.
        return self.knowledge[index]
