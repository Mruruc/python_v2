# IO Operations in Python

## Files

## What is a file stream ?

A ``file stream`` is an ``abstraction`` that represents the flow of data between a program and a file,
enabling sequential reading from or writing to the file through a`` standardized interface``.

### There are two basic operations performed on the stream:

* ``read`` from the stream: the portions of data are retrieved from the file and placed in a memory area managed by the
  program (e.g., a variable);
* ``write`` to the stream: the portions of the data from the memory (e.g., a variable) are transferred to the file.

## What is a mode ?

In computing, the`` mode of a file`` refers to the ``specification`` of how the file is to be accessed or operated upon,
such as reading, writing or executing. It defines the permitted operations and may also indicate file permissions or
access rights.

``open mode`` : The specification that determines how a file is accessed when it is opened, such as read-only,
write-only, append, or read/write.
``close mode`` : The operation that terminates the association between a file and its stream, ensuring that all buffered
data is written and resources are released.

### There are three basic modes used to open the stream:

* ``read mode``: a stream opened in this mode allows ``**read operations only**``; trying to write to the stream will
  cause an exception (the exception is named ``UnsupportedOperation``, which inherits ``OSError`` and ``ValueError``,
  and comes from the io module);
* ``write mode``:  a stream opened in this mode allows ``**write operations only**``.
* ``update mode``: a stream opened in this mode allows ``both writes and reads ``.

### Files handles

````txt
Python assumes that every file is hidden behind an object of an adequate class.
````

## Definition

A **file handle** is an object that serves as an interface between a program and an open file.  
It provides methods and attributes to perform operations such as reading, writing, or closing.  
In Python, a file handle is created when a file is opened and destroyed when the file is closed.

---

## Class Hierarchy

Python implements file handles through a hierarchy of stream classes:

----
In general, the object comes from one of the classes shown here:

````txt
io.IOBase
   |
   +-- io.RawIOBase
   |      |
   |      +-- io.FileIO
   |
   +-- io.BufferedIOBase
   |      |
   |      +-- io.BufferedReader
   |      |
   |      +-- io.BufferedWriter
   |      |
   |      +-- io.BufferedRWPair
   |      |
   |      +-- io.BufferedRandom
   |
   +-- io.TextIOBase
          |
          +-- io.TextIOWrapper
````

- **`IOBase`** → Abstract base for all streams.
- **`RawIOBase`** → Base for **unbuffered binary I/O** (e.g., `FileIO`).
- **`BufferedIOBase`** → Base for **buffered binary I/O** (`BufferedReader`, `BufferedWriter`, `BufferedRWPair`,
  `BufferedRandom`).
- **`TextIOBase`** → Base for text I/O (`TextIOWrapper`, handling encoding/decoding).

---

## Buffered vs. Unbuffered Binary I/O

- **Unbuffered Binary I/O (`RawIOBase`)**
    - Data is transferred **directly between the program and the file**.
    - Every read or write call corresponds to an immediate system-level operation.
    - Example: `io.FileIO`.
    - ⚡ Faster response for very small, low-level operations, but inefficient for frequent access.

- **Buffered Binary I/O (`BufferedIOBase`)**
    - Data is stored temporarily in a **memory buffer** before being read or written.
    - Reduces the number of system calls by grouping I/O operations.
    - Examples: `io.BufferedReader`, `io.BufferedWriter`.
    - ✅ More efficient for large-scale or repeated reads/writes.

---

## Text Streams

- Built on top of buffered binary streams.
- Add **character encoding/decoding** (e.g., UTF-8).
- Example: `io.TextIOWrapper`.

---

# Text and Binary Streams in Python

## Stream Types

All streams are divided into **text** and **binary** streams, depending on their content:

- **Text Streams**
    - Structured in **lines** containing typographical characters (letters, digits, punctuation, etc.).
    - Read/written **character by character** or **line by line**.
    - Example: plain text files, source code.

- **Binary Streams**
    - Contain a **sequence of raw bytes** of any value.
    - Used for data such as executables, images, audio, video, or databases.
    - Read/written **byte by byte** or in **blocks of arbitrary size**.

---

## Line-Endings and Platform Differences

- **Unix/Linux** → Line ends marked by **LF (`\n`, ASCII 10)**.
- **Windows (CP/M legacy)** → Line ends marked by **CR+LF (`\r\n`, ASCII 13 and 10)**.

### Consequences

- Programs written for one system may fail on another due to mismatched line-ending conventions.
- This is called **non-portability**: traits of a program that prevent or hinder its use across different environments.
- Conversely, **portability** is the trait that allows a program to execute correctly in multiple environments.
- A program with this trait is called a **portable program**.

---

## Portability Solution in Python

To resolve line-ending differences, Python applies **automatic newline translation** in text mode:

- **Text Mode (`t`)**
    - On **Unix/Linux**: no conversion (files use `\n`).
    - On **Windows**:
        - Reading → every `\r\n` is converted to `\n`.
        - Writing → every `\n` is converted to `\r\n`.
    - ✅ Transparent to the program: code can be written as if handling Unix-style text only, but runs correctly on both
      systems.

- **Binary Mode (`b`)**
    - No conversions are applied.
    - Data is read/written **exactly as stored** (raw bytes).

--- 

## Opening the streams

````python
file = 'example.txt'  # file location
files_stream = open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
````

## modes

````txt
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
````

* `mode` : Specifies the mode in which the file is opened. Default is 'r' (read mode).
* `buffering` : Controls the buffering policy. Default is -1 (system default).
* `encoding` : Specifies the encoding for text files. Default is None (system default).
* `errors` : Specifies how encoding/decoding errors are handled. Default is None ('strict').
* `newline` : Controls how newlines are handled in text mode. Default is None (universal newlines).
* `closefd` : If False and a file descriptor is passed, the file descriptor will be kept open when the file is closed.
  Default is True.
* `opener` : A custom opener can be used by passing a callable as `opener`. Default is None.

-----

### Summary

1. A file needs to be open before it can be processed by a program, and it should be closed when the processing is
   finished.

Opening the file associates it with the stream, which is an abstract representation of the physical data stored on the
media. The way in which the stream is processed is called open mode. Three open modes exist:

read mode – only read operations are allowed;
write mode – only write operations are allowed;
update mode – both writes and reads are allowed.

2. Depending on the physical file content, different Python classes can be used to process files. In general, the
   BufferedIOBase is able to process any file, while TextIOBase is a specialized class dedicated to processing text
   files (i.e. files containing human-visible texts divided into lines using new-line markers). Thus, the streams can be
   divided into binary and text ones.


3. The following open() function syntax is used to open a file:

open(file_name, mode=open_mode, encoding=text_encoding)
The invocation creates a stream object and associates it with the file named file_name, using the specified open_mode
and setting the specified text_encoding, or it raises an exception in the case of an error.

4. Three predefined streams are already open when the program starts:

sys.stdin – standard input;
sys.stdout – standard output;
sys.stderr – standard error output.

5. The IOError exception object, created when any file operations fails (including open operations), contains a property
   named errno, which contains the completion code of the failed action. Use this value to diagnose the problem.