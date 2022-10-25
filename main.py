from asyncore import read
from typing import List
from method import text_reader as reader

user_stories: List[str] = []
actors: List[str] = []

df = reader.requirement_txt(path="./dataset/user-stories/g02-federalspending.txt", separator=",", title=["actor", "want", "outcome"])

