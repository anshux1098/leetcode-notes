# 001 · Two Sum · Easy

**Topic:** Arrays  
**Pattern:** HashMap (complement lookup)

---

## Approach
For each number, calculate its complement (`target - num`).
Check if that complement already exists in a hashmap.
If yes, return both indices. If no, store current number and index in the map.
One pass — no nested loops needed.

---

## Complexity
| | |
|---|---|
| Time | O(n) |
| Space | O(n) |

---

## Edge Cases
- Same element used twice — handled since we store index and check before storing
- No solution guaranteed by problem — no need to handle missing case

---

## Key Code
```python
seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```

---

## Mistake I Made
_fill this in after your attempt_

## Aha Moment
Instead of checking every pair (O(n²)), store what you're *looking for* as you go. The hashmap turns a search into an O(1) lookup.

---

## Revisit
No