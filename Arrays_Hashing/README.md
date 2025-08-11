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

---

## Top K Frequent Elements

**Key Concept(s):** Bucket sort, Hash maps

**Notes:**
- The core idea is to bucket elements by frequency, taking advantage of the fact that no element can occur more than n times (where n = len(nums)), making bucket sort viable in O(n) time.
- A frequency map is built using Counter(nums) (or a manual dictionary) to count occurrences in O(n). Counter is faster due to its C-level implementation.
- A list of size n+1 is used as buckets (buckets[freq] holds all elements that occur freq times).
    - Two ways to initialise:
        1. [[] for _ in range(n+1)]: creates all lists up front — simple, readable.
        2. [None] * (n+1): lazily creates lists only when needed — less memory overhead, marginally faster.
- Iterating backward from the highest frequency (n) down to 1 allows early termination when enough top-k elements are gathered. This avoids unnecessary processing.
- A slicing operation return top_k[:k] ensures only the top-k results are returned if a frequency bucket contains more than one element.
- This method avoids full sorting of elements (O(n log n)), offering linear-time performance in the average case and performing well under LeetCode constraints.

---

## Encode and Decode Strings

**Key Concept(s):** String serialisation/deserialisation, Delimiters, Run-Length Encoding (RLE), Unicode Shifting

**Notes:**
- My solution to this problem involved some creativity, straying from the general goal by adding some obfuscation.
- The main challenge was creating a reversible transformation from a list of strings -> single string -> back to the same list, preserving edge cases such as:
    1. Empty arrays
    2. Empty strings inside arrays (["", ""])
    3. Special characters (colons, pipes, newlines, Unicode symbols)
- Used a delimiter (<length>:<word>) to separate encoded entries, combined with escaping to ensure delimiters inside strings don’t break decoding.
- Applied Unicode shift to obfuscate characters on either side of an RLE compression to attempt reducing size for repeated characters.
- Decode reverses the process.
- This obfuscation was silly, but for fun!

---

## Product of Array Except Self

**Key Concept(s):** Prefix sum (product)

**Notes:**

- The brute force O(n^2) approach is to iterate over the array, taking the product of all other numbers each time, and then inserting those into the resultant array.
- A prefix and postfix array can be built to reduce time complexity to O(n), at the expense of additional memory.
    - The result for any index can then be found by taking `prefix[i-1] * postfix[i+1]` (defaulting to 1 when operating at array edges).
- To improve this, we can operate directly in the output array. This works on a similar basis as before, an index being equal to `prefix[i-1] * postfix[i+1]`
    1. Initialise an array of integers of length equalling the input array
    2. Fill out the array with the prefix products (`prefix[i-1]`)
    3. Reverse back through the array, multiplying each value by postfix products (`postfix[i+1]`)
- This optimisation results in O(n) time complexity and O(1) extra space.