import spacy
from asyncore import read
from typing import List
from method import text_reader as reader
from method import data_cleaner as cleaner


nlp = spacy.load("en_core_web_lg")

user_stories: List[str] = []
actors: List[str] = []

df = reader.requirement_txt(path="./dataset/user-stories/g02-federalspending.txt", separator=",", title=["actor", "want", "outcome"])

data = cleaner.nan_removal(dataset=df, desired_column=["want", "outcome"])


want = data["want"].iloc[1]

doc = nlp("As a dataset developer, I want to deploy a dataset type independent from any app and allow apps to create and use dataset instances of that type.")

for ent in doc:
    print(ent.text)

