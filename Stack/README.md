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
- Maintain the stack as normal, but complement it with a `min stack`
- `min stack` will track the minimum value at any given point, aligning with main stack. As such, both must be maintained appropriately


