# Two Pointer

## Valid Palindrome

**Key Concept(s):** Two pointer

**Notes:**
- For a general solution, two pointers can be moved from the outer edges towards each other, making comparisons at each step.
- In this case of ignoring non-alphanumeric characters, move the pointers enough to reach the next alphanumeric character at each step. This is faster than rebuilding the string.

---

## Two Sum

**Key Concept(s):** Two pointer

**Notes:**
- A brute force method of quadratic complexity would involve comparing each element with every other element in the array.
- The key is that the array is already sorted. Pointers can be used at the outer edges, moving the left pointer increases the value and the right decreases the value. Move the pointers based on whether the current sum is too great or too little.

---

## Three Sum

**Key Concept(s):** Two pointer, two sum

**Notes:**
- Solution implements the two sum solution but required extra computation for sorting the array. For each element, perform a two pointer search on the elements to the right.
- To avoid duplicate triplets move either the left or right pointer after a target has been found. Continue to move until the pointer is not a duplicate.

---

## Container with Most Water

**Key Concept(s):** Two pointer

**Notes:**
- Start with pointers at either edge of the list. As the limiting factor is always the shorter line, move that pointer. Repeat and update the max until the pointers meet

---

## Trapping Rain Water

**Key Concept(s):** 

**Notes:**
- For each position, water can only be trapped if it's lower than the tallest bars on both sides.
- Use two pointers (left, right) to scan from both ends.
    - Maintain left_max and right_max while scanning.
    - At each step, trap water based on the shorter boundary and increment as this is the limiting factor.
- This works as the height of the water can only rise as we tend towards the center of the heights.
