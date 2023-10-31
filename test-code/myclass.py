# Databricks notebook source
class MyClass:
    """
    A simple class to be reused in another notebook.
    """
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display(self):
        print ("This alert's id is {0}, the score is {1}.".format(self.name, self.score))

    
