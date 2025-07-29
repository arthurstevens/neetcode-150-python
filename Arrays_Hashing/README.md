## Contains Duplicate

**Key Concept(s):** Sets

**Notes:**
- Sets have a slightly lower overhead than dictionaries as the keys are stored without a value pair.
- Sets inherently do not include duplicates, so construction of a set from the list and comparing the lengths garnered optimal runtime from avoiding key lookups and fast set construction.

---

## Valid Anagram

**Key Concept(s):** Hash maps and hash tables

**Notes:** 
- Remember to consider constraints in solutions. I was able to utilise a small array as `s` and `t` contained only lowercase English letters.
- Simple hash tables have a small performance boost compared to the overhead and dynamic resizing of dictionaries (hash maps).
- Counter() exists.

---
