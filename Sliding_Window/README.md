## Best Time to Buy and Sell Stock

**Key Concept(s):** Sliding window

**Notes:**
- Use a left pointer as buy day (starting at day 1) and right as sell date (starting at day 2). Initialise a max profit variable.
- Increment the right pointer for all elements:
    - Update max profit variable if applicable (using `prices[r] - prices[l]`)
    - If the right pointer price is less than the left pointer price, move the buy day to the right pointer (ensuring the lowest purchase price is being used for subsequent days).

---

## Longest Substring Without Repeating Characters

**Key Concept(s):** Sliding window, Hash set

**Notes:**
- Create a left and right pointer to track the active substring
- Initialise a set to track which characters are in a substring alongisde a maximum length.
- Increment the right pointer for all elements:
    - If the active character is in the set, remove the character at the left pointer and shift it to the right. Continue this until the duplicate is removed from the substring.
    - Add the active character to the substring.
    - Update max length if applicable (using `r - l + 1`)
- This problem could potentially be optimised by using an array to track characters (using the unicode for index), removing the overhead of a set but introducing extra space.

---

## Longest Repeating Character Replacement

**Key Concept(s):** Sliding window

**Notes:**
- This problem was very fun for me, a number of oppurtunities to optimise the algorithm.
- **Sliding window**:
    - A window of `[l, r]` is maintained to represent a substring.
    - Increment `r` at every step
    - Increment `l` when a window becomes invalid
- **Validity condition**:
    - `windowSize - maxFreq <= k`
        - `windowSize` = `r - l + 1`
        - `maxFreq` is the max count for a single character within the window. This provides the minimal number of replacements.
- **Frequnecy counting (`chrs`)**:
    - Hash maps provide O(1) lookups. This has overhead, but provides more versatility (works for any charset)
    - Fixed array of size 26. Due to the constraint of the characters only being uppercase A-Z, we can calculate and index using `ord(c) - ord('A')`.
- **Tracking of `maxFreq`**:
    - **Option A:** Recompute by scanning all counts at each step over `chrs`
        - Runtime: O(26n) -> O(n), slower in practice.
    - **Option B:** Update incrementally with `max(current, chrs[index(c)])`
        - Runtime: O(1) per step.
        - `maxFreq` is never decreased
            - Any greater valid windows must include at least `maxFreq` occurences of a character.
            - This can cause the alogirthm to consider some windows as *valid* despite not matching this frequency. This does not break correctness as the maximum valid length was recorder when the window first achieved it, and the window will not incorrectly grow (left pointer will move, so the window slides right until a valid expansion of this window is possible)
- **Result**:
    - The resultant max length can be computed with `max(current, r - l + 1)`
