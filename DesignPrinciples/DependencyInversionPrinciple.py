# Dependency Inversion Principle

# One should depend upon abstraction and not concretion

# High level modules should not depend upon the low level modules

from enum import Enum
from abc import ABC, abstractmethod

class Relationship(Enum):

    PARENT = 0
    CHILD = 0

class Person:

    def __init__(self, name):
        self.name = name

class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name): pass

class Relationships(RelationshipBrowser): # Low Level Module

    def __init__(self):
        self.relations = []


    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name

class Research: # High Level Module
    # def __init__(self, relationships):
    #     relations = relationships.relations
    #
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child with name {r[2].name}.')

    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f'John has a child with name {p}')

parent = Person('John')
child1 = Person('Mike')
child2 = Person('Rick')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)



