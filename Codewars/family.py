# We need a system that can learn facts about family relationships, check their consistency and answer queries about
# them.
#
# The task
#
# Create a class family with the following methods. All arguments are strings: names of persons. Upon the first use of
# a name, that name is added to the family.
#
# male(name) and female(name) returning boolean
#
# Define the gender (corresponding to the method name) of the given person. Return False when these assignments cannot
# be made because of conflicts with earlier registered information.
#
# is_male(name) and is_female(name) returning boolean
#
# Return True when the person has the said gender. When no gender was assigned, both methods should return False
#
# set_parent_of(child_name, parent_name) returning boolean
#
# Defines the child-parent relationship between two persons. Returns False when the relationship cannot be made
# because of conflicts with earlier registered information.
#
# get_parents_of(name) and get_children_of(name) returning list of string
#
# Return the names of the person's parents/children in alphabetical order
#
# Deducing information
#
# When things can be implied from given information, it should be done.
#
# For instance, a parent's gender can be determined as soon as the other parent's gender becomes known:
#
# fam = family()
# fam.set_parent_of("Vera", "George")
# fam.set_parent_of("George", "Vera") # False
# Details, rules, assumptions
#
# Although the task relates to genealogy, the rules of this kata are not claimed to be realistic. Several
# simplifications and rules apply, which may not hold in real life:
#
# Strings are case sensitive, but there are no tests playing around with "Peter", "PETER" and "PeTeR".
# People are uniquely identified by their name. For instance, there are no two different people called "Jim" in the
# same family.
# Once a person has an assigned gender, it cannot be changed.
# No gender conclusions should be made from personal names: "Bob" could well be a woman and "Susan" a man.
# People cannot have more than one mother and one father.
# The terms "parents" and "children" refer to the relatives in the immediate previous/next generations only, not to
# more remote ancestors or descendants.
# Incest may occur, so, for example, one's parent may at the same time be their grandparent.
# One cannot be their own ancestor.
# Age is not accounted for. Even if some incestuous relationships would infer that one's parent is more than 5
# generations older, it should be allowed.
# In case a name's first occurrence is in a call of one of the two gender querying methods, the return value will
# always be false, as that new person does not have a known gender.
# In case a name's first occurrence is in a call of one of the two relation querying methods, the return value will
# always be an empty array/list, as there are no relationships known yet in which that new person participates.
# For the reasons in the preceding two bullet points it should not matter whether you actually store that name in
# these cases in your data structure, or not. In the latter case you would only store it at the next occasion when that
# name is mentioned in a call of one of the three other methods, that actually add information. The described interface
# has no way to query the difference between these two possible implementations, so you can choose freely.
# Example
#
# Consider the following family graph:
#
# Dylan (m)
# Morgan (f)
# Frank (m)
# July
# Jennifer
# Joy
# It could be created step by step with the following code — the expected return value for each method call is
# indicated in comments:
#
# fam = family()
# fam.set_parent_of("Frank", "Morgan")       # True
# fam.set_parent_of("Frank", "Dylan")        # True
# fam.male("Dylan")                          # True
# fam.set_parent_of("Joy", "Frank")          # True
# fam.male("Frank")                          # True
# fam.male("Morgan")                         # False
# (Morgan is a woman because she both is Frank's parent, but not his father)
# fam.set_parent_of("July", "Morgan")        # True
# (The preceding assertion was rejected, so there is no conflict)
# fam.is_male("Joy") or fam.is_female("Joy") # False
# (We know Joy is Frank's child, but we can't derive Joy's gender)
# fam.get_children_of("Morgan")              # ["Frank", "July"]
# fam.set_parent_of("Jennifer", "Morgan")    # True
# fam.get_children_of("Morgan")              # ["Frank", "Jennifer", "July"]
# fam.get_children_of("Dylan")               # ["Frank"]
# (That is all we know for sure)
# fam.get_parents_of("Frank")                # ["Dylan", "Morgan"]
# fam.set_parent_of("Morgan", "Frank")       # False
# (It is impossible to be the parent of your parent)

class family:
    def __init__(self):
        pass
    def male(self, name):
        return True
    def is_male(self, name):
        return False
    def female(self, name):
        return True
    def is_female(self, name):
        return False
    def set_parent_of(self, child_name, parent_name):
        return True
    def get_children_of(self, name):
        return []
    def get_parents_of(self, name):
        return []