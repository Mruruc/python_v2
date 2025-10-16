# Character Encoding Notes

- Computers store **characters as numbers**.

---

- There are multiple ways to encode characters, but only a few have become widely adopted in computing:

  - **ASCII** – Primarily used to encode the Latin alphabet and some of its derivatives.
  - **UNICODE** – Can represent virtually all characters used by humans across different languages and scripts.

---

```txt
Encoding: The process of converting characters into a specific format that computers
can store and process, usually as numbers (bytes).
```

---

- The number assigned to a particular character is called a **code point**.

---

## `chr()` and `ord()` Functions

- `chr(codepoint)` – Returns the character corresponding to a given Unicode code point.
- `ord(character)` – Returns the Unicode code point of a given character.

Example:

```python
print(chr(97))  # Output: 'a'
print(ord('a')) # Output: 97
```
