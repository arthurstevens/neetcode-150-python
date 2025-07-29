## Contains Duplicate

**Key Concept(s):** Sets

**Notes:**
- Sets have a slightly lower overhead than dictionaries as the keys are stored without a value pair.
- Sets inherently do not include duplicates, so construction of a set from the list and comparing the lengths garnered optimal runtime from avoiding key lookups and fast set construction.

---

## Valid Anagram

**Key Concept(s):** Hash maps

**Notes:**
- Remember to consider constraints in solutions. I was able to utilise a small array as `s` and `t` contained only lowercase English letters.
- Simple hash tables have a small performance boost compared to the overhead and dynamic resizing of dictionaries (hash maps).
- Counter() exists.

---

## Two Sum

**Key Concept(s):** Hash maps

**Notes:**
- Begun by initialising the map first, then finding indices, requiring two iterations over `nums`. I was able to optimise by expanding the map with each iteration, as previous numbers alone are sufficient for finding the solution.
- Minor, but use enumerate() in python to track both value and index on iterables for ease/readability.

---

## Group Anagrams

**Key Concept(s):** Hash maps

**Notes:**
- The idea of grouping by a common key is central. Using a hash map (dictionary) with that key allows constant-time access to groupings.
- I initially used the character frequency array approach (`[0]*26` -> tuple as key), which is O(n * m), but observed that sorting (`''.join(sorted(word)` -> string as key) was faster in practice despite being O(n * m log m). This is likely due to:
    - Python’s optimised sorting (Timsort)  
    - Lower overhead from hashing shorter strings vs 26-integer tuples (constraint: `0 <= strs[i].length <= 100`)
- `defaultdict()` from the `collection` module simplifies appending to dictionary entries by eliminating the need to check if the key exists.
- Strings, numbers, and tuples of immutable types, are the valid key types for hash maps (dictionaries)
