"""
Given two strings s and t, find the shortest substring 
of s that contains all characters of t.

Exemplo:

Input:

s = "ADCFEBECEABEBADFCDFCBFCBEAD"
t = "ABCA"

Output: "CEABEBA"
"""

def contains_all(freq1, freq2):
    for char in freq2:
        if freq1[char] < freq2[char]:
            return False
    return True

# 1st solution
from collections import Counter

def min_window(s, t):
    n, m = len(s), len(t)
    if m > n or m == 0:
        return ""
    freqt = Counter(t)
    shortest = " "*(n+1)
    for length in range(1, n+1):
        for i in range(n - length+1):
            sub = s[i:i+length]
            freqs = Counter(sub)
            if contains_all(freqs, freqt) and length < len(shortest):
                shortest = sub
    return shortest if len(shortest) <= n else ""

print(min_window("ADCFEBECEABEBADFCDFCBFCBEAD","ABCA"))

"""
Optimizing substring extraction:

Instead of extracting and storing the substring itself,
we just work with it's start and end indexes.

The trick is to not always build the counter again.

Optimizing checking if a substring is valid:

The trick is to keep track of how many conditions are
satisfied, and if for a specific substring all conditions
are satisfied, then it's a valid substring.
"""

# 2nd solution
def minimum_window(s, t):
    n, m = len(s), len(t)
    if m > n or t == "":
        return ""
    freqt = Counter(t)
    start, end = 0, n+1
    for length in range(1, n+1):
        freqs = Counter()
        satisfied = 0
        for char in s[:length]:
            freqs[char] += 1
            if char in freqt and freqs[char] == freqt[char]:
                satisfied += 1
        if satisfied == len(freqt) and length < end - start:
            start, end = 0, length
        for i in range(1, n-length+1):
            freqs[s[i+length-1]] += 1
            if s[i+length-1] in freqt and freqs[s[i+length-1]] == freqt[s[i+length-1]]:
                satisfied += 1
            if s[i-1] in freqt and freqs[s[i-1]] == freqt[s[i-1]]:
                satisfied -= 1
            freqs[s[i-1]] -= 1
            if satisfied == len(freqt) and length < end - start:
                start, end = i, i+length
    return s[start:end] if end - start <= n else ""

print(minimum_window("ADCFEBECEABEBADFCDFCBFCBEAD","ABCA"))

# 3rd solution
def window_min(s, t):
    n, m = len(s), len(t)
    if m > n or t == "":
        return ""
    freqt = Counter(t)
    start, end = 0, n
    satisfied = 0
    freqs = Counter()
    left = 0
    for right in range(n):
        freqs[s[right]] += 1
        if s[right] in freqt and freqs[s[right]] == freqt[s[right]]:
            satisfied += 1
        if satisfied == len(freqt):
            while s[left] not in freqt or freqs[s[left]] > freqt[s[left]]:
                freqs[s[left]] -= 1
                left += 1
            if right - left + 1 < end - start + 1:
                start, end = left, right
    return s[start:end+1] if end - start + 1 <= n else ""

print(window_min("ADCFEBECEABEBADFCDFCBFCBEAD","ABCA"))