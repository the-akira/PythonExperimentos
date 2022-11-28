"""
Given two strings s1 and s2, check if they are anagrams.
Two strings are anagrams if they are made of the same
characters with the same frequencies.
"""

def valid_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

print(valid_anagram("garden", "danger"))
print(valid_anagram("nameless", "salesmen"))