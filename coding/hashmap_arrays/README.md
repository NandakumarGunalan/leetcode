## HashMap / Array Patterns

### 1. Two Sum (LC 1)
- Trigger: find two numbers that sum to target
- Pattern: complement lookup using hash map
- Time / Space: O(n) / O(n)
- Pitfall: check complement before inserting current index

## HashMap / Array Patterns

### Valid Anagram (LC 242)
- Pattern: frequency map
- Approach: count characters in one string, decrement with the other
- Time: O(n)
- Space: O(1) for fixed alphabet
- Pitfall: must check length mismatch early

### Best Time to Buy and Sell Stock (LC 121)
- Trigger: maximize profit with one buy before one sell
- Pattern: track min-so-far + max diff
- Time / Space: O(n) / O(1)
- Pitfall: don’t overwrite profit; use max()

### Contains Duplicate (LC 217)
- Trigger: check if any element appears more than once
- Pattern: hash set for seen elements
- Time / Space: O(n) / O(n)
- Pitfall: iterating indices instead of values


