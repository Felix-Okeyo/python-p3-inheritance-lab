#!/usr/bin/env python

# Import the User class from the user module.
from user import User

# Create a new class called 'Student' that inherits from the 'User' class.
class Student(User):
    # This special function runs when a new 'Student' is created.
    def __init__(self, first_name, last_name):
        # Call the special function in the 'User' class to set the names.
        super().__init__(first_name, last_name)
        # Create an empty list to store the student's knowledge.
        self.knowledge = []
    
    # This function lets the student learn something new.
    def learn(self, knowledge):
        # Add the new knowledge to the student's list.
        self.knowledge.append(knowledge)
