# An Introduction to Object-Oriented Programming (OOP)

Object-Oriented Programming is a powerful way to organize software by bundling related properties and behaviors into
individual **objects**. Think of it as creating digital building blocks to construct your program.

---

## The Class: Your Blueprint 📝

A **class** is the blueprint or template for creating objects. It defines a set of **attributes** (data or properties)
and **methods** (functions or behaviors) that all objects created from that class will have.

| Python                                                                                 | Java                                                             | JavaScript                                                      |
|----------------------------------------------------------------------------------------|------------------------------------------------------------------|-----------------------------------------------------------------|
| ````python ```` <br> `class User:` <br> &nbsp;&nbsp;&nbsp;&nbsp; `pass` <br> ```` ```` | ````java ```` <br> `public class User {` <br> `}` <br> ```` ```` | ````javascript ```` <br> `class User {` <br> `}` <br> ```` ```` |

---

## The Object: Building from the Blueprint 🏗️

An **object** (also called an **instance**) is a specific entity created from a class. If a `User` class is the
blueprint, then an individual user with a name and email would be an object. The process of creating an object is called
**instantiation**.

| Python                                               | Java                                                         | JavaScript                                                          |
|------------------------------------------------------|--------------------------------------------------------------|---------------------------------------------------------------------|
| ````python ```` <br> `user1 = User()` <br> ```` ```` | ````java ```` <br> `User user1 = new User();` <br> ```` ```` | ````javascript ```` <br> `const user1 = new User();` <br> ```` ```` |

---

## The Constructor: The Initial Setup

A **constructor** is a special method that's automatically called when an object is created. Its main job is to set up
the initial state of the object, like assigning initial values to its attributes.

| Python                                                                                                                                                             | Java                                                                                                                                               | JavaScript                                                                                                                                        |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| ````python ```` <br> `class User:` <br> &nbsp;&nbsp;&nbsp;&nbsp; `def __init__(self):` <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `pass` <br> ```` ```` | ````java ```` <br> `public class User {` <br> &nbsp;&nbsp;&nbsp;&nbsp; `public User() {` <br> &nbsp;&nbsp;&nbsp;&nbsp; `}` <br> `}` <br> ```` ```` | ````javascript ```` <br> `class User {` <br> &nbsp;&nbsp;&nbsp;&nbsp; `constructor() {` <br> &nbsp;&nbsp;&nbsp;&nbsp; `}` <br> `}` <br> ```` ```` |

> **Note on Python's `self`**: The `self` parameter in Python's `__init__` method is a reference to the current instance
> of the class. It's used to access variables that belong to that specific object. It's similar to the `this` keyword in
> Java and JavaScript.

---

## How Objects Are Born: A Look at the `new` Keyword

While the end result is similar, each language handles the exact mechanics of object creation a bit differently.

### Java

The `new` keyword is essential for creating objects. When you write `User user = new User();`:

* Memory for the `User` object is **allocated** on the heap.
* The `User()` **constructor** is called to initialize the object's fields.
* A **reference** (the memory address) to the object is returned and stored in the `user` variable.

### JavaScript

The `new` keyword orchestrates a four-step process:

* A new, empty JavaScript object `{}` is **created**.
* This new object is **linked** to the constructor function's prototype (`User.prototype`), allowing it to inherit
  properties and methods.
* The `constructor` function is **called** with `this` bound to the new object.
* The new object is **returned**, unless the constructor explicitly returns a different object.

### Python

Python is unique here as it **does not use a `new` keyword**. The process is split between two special methods:

* `__new__` is a static method that's called first to **allocate memory** and create the blank object. You rarely need
  to write your own `__new__`.
* `__init__` is then called on the newly created object to **initialize** its attributes. This is the method you'll
  define almost every time you write a class.

### Quick Comparison

| Language       | Keyword / Method       | Allocates Memory? | Initializes Attributes? |
|----------------|------------------------|-------------------|-------------------------|
| **Java**       | `new`                  | Yes (heap)        | Yes (via constructor)   |
| **JavaScript** | `new`                  | Yes (by engine)   | Yes (via constructor)   |
| **Python**     | `__new__` / `__init__` | Yes (`__new__`)   | Yes (`__init__`)        |

---

##   

# Instance Variables and Class Variables

## Instance Variables

An **Instance variable** is a property whose existence depends on the creation of an object. Every object can have a
different set of instance variables.

### Python

```python
class User:
    def __init__(self, name, age):
        self.name = name  # Public instance variable
        self.age = age  # Public instance variable
        self.__secret = "hidden"  # Private instance variable (name mangling)

    def add_dynamic_property(self):
        self.location = "New York"  # Can add instance variables dynamically


user1 = User("Alice", 25)
user1.hobby = "reading"  # Instance variables can be added freely
print(
    user1.__dict__)  # {'name': 'Alice', 'age': 25, '_User__secret': 'hidden', 'location': 'New York', 'hobby': 'reading'}
```

**Key Points:**

- Can be freely added to and removed from objects during their lifetime
- All object instance variables are stored in a dedicated dictionary named `__dict__`
- Private variables start with `__` but are still accessible using name mangling: `_ClassName__PrivatePropertyName`
- Very flexible - new instance variables can be added at runtime

### Java

```java
public class User {
    public String name;           // Public instance variable
    private int age;              // Private instance variable
    protected String email;       // Protected instance variable
    
    public User(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    // Getter and setter methods
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }
}

User user1 = new User("Alice", 25);
// user1.newProperty = "value";  // This would cause a compile error!
```

**Key Points:**

- Must be declared in the class definition
- Cannot add new instance variables at runtime
- Access controlled by visibility modifiers (`public`, `private`, `protected`)
- Strongly typed - each variable has a fixed type
- More rigid but provides compile-time safety

### JavaScript

```javascript
class User {
    constructor(name, age) {
        this.name = name;        // Public instance variable
        this.age = age;          // Public instance variable
        this.#secret = "hidden"; // Private instance variable (ES2022+)
    }
    
    addDynamicProperty() {
        this.location = "New York"; // Can add instance variables dynamically
    }
}

const user1 = new User("Alice", 25);
user1.hobby = "reading";  // Instance variables can be added freely
console.log(user1);       // User { name: 'Alice', age: 25, hobby: 'reading' }
```

**Key Points:**

- Similar flexibility to Python - can add properties dynamically
- Private fields use `#` syntax (modern JavaScript)
- No built-in `__dict__` equivalent, but you can use `Object.keys(obj)` or `Object.getOwnPropertyNames(obj)`
- Properties are dynamic and can be of any type

---

## Class Variables

A **Class variable** is a property which exists in exactly one copy and doesn't need any created object to be
accessible. It's shared among all instances of the class.

### Python

```python
class User:
    total_users = 0  # Class variable
    platform = "MyApp"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable
        User.total_users += 1  # Accessing class variable

    @classmethod
    def get_total_users(cls):
        return cls.total_users


# Accessing class variables
print(User.total_users)  # 0
print(User.platform)  # "MyApp"

user1 = User("Alice")
user2 = User("Bob")
print(User.total_users)  # 2

# Class variables are stored in the class's __dict__
print(User.__dict__)  # Contains total_users, platform, etc.
```

**Key Points:**

- Shared by all instances of the class
- Can be accessed via class name or instance (though class name is preferred)
- Stored in the class's `__dict__`, not in individual instance `__dict__`
- If modified via instance, creates an instance variable that shadows the class variable

### Java

```java
public class User {
    public static int totalUsers = 0;        // Class variable (static)
    private static final String PLATFORM = "MyApp";  // Class constant
    
    private String name;  // Instance variable
    
    public User(String name) {
        this.name = name;
        totalUsers++;  // Accessing class variable
    }
    
    public static int getTotalUsers() {  // Static method
        return totalUsers;
    }
}

// Accessing class variables
System.out.println(User.totalUsers);    // 0
System.out.println(User.PLATFORM);      // "MyApp"

User user1 = new User("Alice");
User user2 = new User("Bob");
System.out.println(User.totalUsers);    // 2
```

**Key Points:**

- Called "static variables" in Java
- Must be declared with `static` keyword
- Accessed via class name (recommended) or instance
- `final` keyword makes them constants
- Shared across all instances and initialized when class is first loaded

### JavaScript

```javascript
class User {
    static totalUsers = 0;           // Class variable (ES2022+)
    static platform = "MyApp";       // Class variable
    
    constructor(name) {
        this.name = name;            // Instance variable
        User.totalUsers++;           // Accessing class variable
    }
    
    static getTotalUsers() {         // Static method
        return this.totalUsers;
    }
}

// Accessing class variables
console.log(User.totalUsers);        // 0
console.log(User.platform);          // "MyApp"

const user1 = new User("Alice");
const user2 = new User("Bob");
console.log(User.totalUsers);        // 2

// Alternative older syntax (before ES2022)
class UserOld {
    constructor(name) {
        this.name = name;
        UserOld.totalUsers = (UserOld.totalUsers || 0) + 1;
    }
}
UserOld.totalUsers = 0;  // Defined outside class
```

**Key Points:**

- Called "static properties" in JavaScript
- Use `static` keyword (modern syntax) or define outside class (older approach)
- Accessed via class name only (not through instances)
- Shared across all instances
- No built-in constants, but you can use `Object.freeze()` for immutability

---

## Quick Comparison Table

| Feature                | Python                            | Java                              | JavaScript                     |
|------------------------|-----------------------------------|-----------------------------------|--------------------------------|
| **Instance Variables** |
| Dynamic addition       | ✅ Yes, anytime                    | ❌ No                              | ✅ Yes, anytime                 |
| Privacy                | `__name` (name mangling)          | `private` modifier                | `#name` (ES2022+)              |
| Storage                | `obj.__dict__`                    | Object memory                     | Object properties              |
| Type checking          | Dynamic                           | Static (compile-time)             | Dynamic                        |
| **Class Variables**    |
| Keyword                | None (just define in class)       | `static`                          | `static`                       |
| Access method          | `ClassName.var` or `instance.var` | `ClassName.var` or `instance.var` | `ClassName.var` only           |
| Storage                | `Class.__dict__`                  | Class metadata                    | Class object                   |
| Constants              | Convention (`UPPER_CASE`)         | `static final`                    | Convention + `Object.freeze()` |

---

## Utility Functions

### Python

```python
# Check if object/class has a specific attribute
hasattr(user1, 'name')  # True
hasattr(User, 'total_users')  # True

# Get all instance variables
vars(user1)  # Same as user1.__dict__

# Get all class attributes
vars(User)  # Same as User.__dict__
```

### Java

```java
// Use Reflection API
import java.lang.reflect.*;

Field[] fields = User.class.getDeclaredFields();
for (Field field : fields) {
    System.out.println(field.getName() + " - " + 
                      (Modifier.isStatic(field.getModifiers()) ? "Class" : "Instance"));
}
```

### JavaScript

```javascript
// Check if object has property
'name' in user1;                    // true
user1.hasOwnProperty('name');       // true

// Get all instance properties
Object.keys(user1);                 // ['name']
Object.getOwnPropertyNames(user1);  // ['name']

// Get all class properties
Object.getOwnPropertyNames(User);   // ['length', 'name', 'prototype', 'totalUsers', 'platform']
```
