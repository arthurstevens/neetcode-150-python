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
