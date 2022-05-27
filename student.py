from typing_extensions import Self
from unicodedata import name

from paramiko import Agent
from pytz import country_names


class Student:
    school="Akirachix"
# class attributes.
    def __init__(self,age,country,first_Name,second_Name):
        self.first_Name=first_Name
        self.second_Name=second_Name
        self.age=age
        
        self.country=country
# class methods
    def greeting(self):
        return f"hello {self.first_Name} from {self.country}. Welcome to {self.school}"
# Add these methods to class student - full_name, year_of_birth, initials. Create two instances and verify the work as expected
  
    def full_name(self):
        return f"Your full names are {self.first_Name} {self.second_Name}"
    def ages(self):
        return f"Your year of birth is {2022-self.age}"
    def initials(self):
        return f"Your initials is {self.first_Name[0]}.{self.second_Name[0]}"
    def final_statement(self):
        return f"hello {self.first_Name} {self.second_Name},you were born in {2022-self.age} in {self.country} and your initials are {self.first_Name[0]}.{self.second_Name[0]}"