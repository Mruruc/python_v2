# IO Files

## Reading from a TXT File

When reading files in Python, you can use different methods depending on your needs.  
Here we compare `read()`, `readline()`, and `readlines()` with examples and proper resource management **without context
managers**.

---

### 📖 Comparison Table

| Method        | Description                                                                                            | Use Case                                                                  |                                                                                                                                                                                                                                                                                        
|---------------|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| `read()`      | Reads the **entire file content** into a single string.                                                | Use when file is small and you need all content at once.                  |                                                                                                                                                                                                                                                                                                                                      
| `readline()`  | Reads **one line** from the file at a time (including `\\n`). Returns empty string when no more lines. | Use for sequential line-by-line processing.                               | 
| `readlines()` | Reads **all lines** and returns a list where each element is one line.                                 | Use when you need all lines in memory at once (not for very large files). | 

````python
try:
    stream = open("example.txt", "r", encoding="utf-8")
    content = stream.read()
    print(content)
except FileNotFoundError:
    print("File not found")
finally:
    try:
        stream.close()
    except NameError:
        pass
````

````python
try:
    stream = open("example.txt", "r", encoding="utf-8")
    line = stream.readline()
    while line:
        print(line, end="")
        line = stream.readline()
except FileNotFoundError:
    print("File not found")
finally:
    try:
        stream.close()
    except NameError:
        pass
````

````python
try:
    stream = open("example.txt", "r", encoding="utf-8")
    lines = stream.readlines()
    print(type(lines))  # <class 'list'>
    for line in lines:
        print(line, end="")
except FileNotFoundError:
    print("File not found")
finally:
    try:
        stream.close()
    except NameError:
        pass
````

---

### 🔑 Key Notes

- Always call `close()` when not using context managers.
- Wrap `close()` inside `finally` to guarantee closure even if an exception occurs.
- `read()` loads the whole file into memory (not good for huge files).
- `readline()` allows processing one line at a time.
- `readlines()` loads all lines into a list (similar drawback as `read()`).

----

### Writing to a TXT File

When writing files in Python, you can use different methods depending on your needs.

### 📖 Comparison Table

| Method         | Description                                                                    | Use Case                                             |
|----------------|--------------------------------------------------------------------------------|------------------------------------------------------|
| `write()`      | Writes a **single string** to the file.                                        | Use when you need to write one string at a time.     |
| `writelines()` | Writes a **list of strings** to the file. Does not add newlines automatically. | Use when you have multiple strings to write at once. |              

````python
try:
    stream = open("output.txt", "w", encoding="utf-8")
    stream.write("Hello, World!\n")
    stream.write("This is a test file.\n")
except IOError as e:
    print(f"An error occurred: {e}")
finally:
    try:
        stream.close()
    except NameError:
        pass
````

````python
try:
    stream = open("output.txt", "w", encoding="utf-8")
    lines = ["Hello, World!\n", "This is a test file.\n"]
    stream.writelines(lines)  # Note: No automatic newlines added
except IOError as e:
    print(f"An error occurred: {e}")
finally:
    try:
        stream.close()
    except NameError:
        pass
````

## Binary Files

When dealing with binary files (like images, audio files, etc.), you should open the file in binary mode by adding a `b`
to the mode string (e.g., `"rb"` for reading, `"wb"` for writing).

````txt
Should be revisited for binary files
````

### Summary

1. To read a file’s contents, the following stream methods can be used:

read(number) – reads the number characters/bytes from the file and returns them as a string; is able to read the whole
file at once;
readline() – reads a single line from the text file;
readlines(number) – reads the number lines from the text file; is able to read all lines at once;
readinto(bytearray) – reads the bytes from the file and fills the bytearray with them;

2. To write new content into a file, the following stream methods can be used:

write(string) – writes a string to a text file;
write(bytearray) – writes all the bytes of bytearray to a file;

3. The open() method returns an iterable object which can be used to iterate through all the file's lines inside a for
   loop. For example:

for line in open("file", "rt"):
print(line, end='')

The code copies the file's contents to the console, line by line. Note: the stream closes itself automatically when it
reaches the end of the file

