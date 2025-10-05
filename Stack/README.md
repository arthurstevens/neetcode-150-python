# Stack

## Valid Parantheses

**Key Concept(s):** Stack

**Notes:**
- Maintain a stack for containing the parantheses
    - If opening parantheses, add to stack
    - If closing parantheses: return false if top of stack is not the equivalent opening, else pop from the top of the stack
- Ensure the stack is empty when all characters have been accounted for

---

## Minimum Stack

**Key Concept(s):** Stack

**Notes:**
- **Two stack solution**:
    - Maintain a `stack` as normal, but complement it with a `min stack`
    - `min stack` will track the minimum value at any given point in the `stack`
- **One stack solution**:
    - Use one `stack` to store differences and a single `min` variable for the current minimum
    - **First push(x)**
        - Push `0`
        - Set `min = x`
    - **Push(x)**
        - Push `min - x` to the stack
        - If `x < min`, update `min`
    - **Pop()**
        - Pop `diff` from the `stack`
        - If `diff < 0`, update `min = min - diff` (restoring the previous minimum)
    - **Top()**
        - If `diff >= 0` return `min + diff`, else return `min`

