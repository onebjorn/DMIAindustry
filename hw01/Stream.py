import random

from collections import namedtuple

Record = namedtuple('Record', 'easy medium nightmare')

def data_stream(S):
    random_generator = random.Random(42)
    easy = 0
    for _ in range(S):
        easy += random_generator.randint(0, 2) 
        medium = random_generator.randint(0, 256 - 1)
        nightmare = random_generator.randint(0, 1000000000 - 1)
        
        yield Record(
            easy=easy,
            medium=medium,
            nightmare=nightmare)

def easy_stream(S):
    for record in data_stream(S):
        yield record.easy
        
def medium_stream(S):
    for record in data_stream(S):
        yield record.medium
        
def nightmare_stream(S):
    for record in data_stream(S):
        yield record.nightmare