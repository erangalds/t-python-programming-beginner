# **Python Classes: The Agent's Blueprint 🛠️**

Welcome back, Junior Agent\! Today, we're diving into **classes**, the foundation of **Object-Oriented Programming (OOP)** in Python. A class is a blueprint or a template for creating objects. It defines a set of attributes (data) and methods (functions) that the created objects will have. Think of a class as the master blueprint for a spy gadget: it specifies the parts it will have (attributes like a laser, camera, and microphone) and what it can do (methods like `fire_laser()`, `take_photo()`, and `record_audio()`).

-----

## **1. Defining a Class: The Blueprint**

You define a class using the `class` keyword. By convention, class names are in **PascalCase** (e.g., `SecretAgent`). The body of the class is where you define its attributes and methods.

**Example Code:**

```python
# A simple class representing a gadget
class SpyGadget:
    # A class attribute shared by all objects
    manufacturer = "TechCorp"

    # The __init__ method is a constructor
    def __init__(self, name, function):
        # Instance attributes specific to each object
        self.name = name
        self.function = function

    # A method that defines a behavior
    def activate(self):
        print(f"The {self.name} is now active.")
        print(f"Its function is to {self.function}.")

# Create an object (an instance) from the class
my_gadget = SpyGadget("Laser Watch", "cut through steel")
my_gadget.activate()
```

  - `__init__()`: This is a special method called the **constructor**. It's automatically executed when a new object is created from the class. It's used to initialize the object's attributes. The `self` parameter is a reference to the specific object being created.
  - `self`: This parameter is a convention in Python that refers to the instance of the class. It's always the first parameter in any instance method.

-----

## **2. Instance and Class Attributes**

  - **Instance Attributes:** These are unique to each object (instance) created from the class. They are defined inside the `__init__()` method using the `self` keyword. For example, in the code above, `name` and `function` are instance attributes.
  - **Class Attributes:** These are shared by all instances of the class. They are defined directly inside the class but outside of any method. For example, `manufacturer` is a class attribute.

-----

## **3. Class Methods: Defining Behaviors**

Methods are functions defined inside a class. They describe the actions that an object can perform. They always take `self` as their first parameter.

**Example Code:**

```python
class Agent:
    def __init__(self, codename, rank):
        self.codename = codename
        self.rank = rank
    
    # A method to display agent info
    def get_info(self):
        print(f"Codename: {self.codename}, Rank: {self.rank}")

    # A method to promote an agent
    def promote(self):
        if self.rank == "Rookie":
            self.rank = "Veteran"
            print(f"Agent {self.codename} has been promoted to Veteran.")
        else:
            print(f"Agent {self.codename} is already a Veteran.")

# Create an agent object
agent_alpha = Agent("Alpha", "Rookie")
agent_alpha.get_info()
agent_alpha.promote()
agent_alpha.get_info()
```

-----

## **4. Inheritance: Creating Specialized Classes**

**Inheritance** is a fundamental OOP concept where a new class, called the **child class**, derives properties and behaviors from an existing class, the **parent class**. This allows you to reuse code and model a "is-a" relationship (e.g., a `CovertAgent` is an `Agent`).

  - The parent class is defined as usual.
  - The child class is defined with the parent class name in parentheses: `class ChildClass(ParentClass):`.
  - The child class inherits all attributes and methods of the parent. It can also add its own new methods or override parent methods.
  - `super().__init__()` is used in the child class's constructor to call the parent's constructor and ensure all parent attributes are initialized.

**Example Code:**

```python
# Parent Class
class Agent:
    def __init__(self, codename):
        self.codename = codename

    def introduce(self):
        print(f"Hello, my codename is {self.codename}.")

# Child Class inheriting from Agent
class CovertAgent(Agent):
    def __init__(self, codename, specialization):
        # Call the parent's constructor
        super().__init__(codename)
        self.specialization = specialization
    
    # A new method for the child class
    def get_specialization(self):
        print(f"My specialization is {self.specialization}.")

# Create a specialized object
covert_agent = CovertAgent("Spectre", "Stealth")
covert_agent.introduce() # Inherited from Agent
covert_agent.get_specialization() # New method
```

-----

## **Hands-On Exercises: Blueprint Puzzles 🧩**

It's time to test your class-building skills to create your own agent-themed objects.

### **1. Defining a Class (5 Exercises)**

1.  **Create a Gadget Class:** Define a class named `Gadget`. The `__init__` method should take one parameter, `name`, and set it as an instance attribute.
2.  **Create an Object:** Create an object from your `Gadget` class with the name `"Spy Camera"`. Print the `name` attribute of the object.
3.  **Add a Method:** To the `Gadget` class, add a method named `report()` that prints `f"The {self.name} is ready."`. Create an object and call this method.
4.  **Add a Class Attribute:** To the `Gadget` class, add a class attribute named `status` with the value `"Operational"`. Create two different `Gadget` objects and print their `status` attribute.
5.  **Create an Agent Class:** Define a class named `Agent`. The `__init__` method should take `codename` and `rank` as parameters. Create an object and print its `rank`.

### **2. Class Methods (5 Exercises)**

1.  **Introduce Method:** In your `Agent` class, create a method named `introduce()` that prints `f"I am Agent {self.codename}."`. Create an object and call the method.
2.  **Assign Mission:** In your `Agent` class, add a method `assign_mission(mission_name)` that takes a parameter and sets it as a new instance attribute `self.mission`. Create an object and call this method with `"Operation Phoenix"`.
3.  **Check Status:** In your `Agent` class, add a method `check_status()` that returns the value of the `self.mission` attribute. Call the method and print the returned value.
4.  **Update Rank:** In your `Agent` class, add a method `promote()` that changes the agent's `rank` to `"Senior Agent"`. Create an agent with the rank `"Rookie"` and call the method. Then print the new rank.
5.  **Deactivate:** To your `Gadget` class, add a method `deactivate()` that changes the class attribute `status` to `"Inactive"`. Create a gadget object and call this method. Then print the `status` of another gadget object to see the change.

### **3. Inheritance (5 Exercises)**

1.  **Parent and Child Classes:** Define a parent class `BaseAgent` with an `__init__` that takes a `name` parameter. Define a child class `FieldAgent` that inherits from `BaseAgent`. Create a `FieldAgent` object and print its `name`.
2.  **Inherited Method:** In the `BaseAgent` class, add a method `greet()` that prints `f"Hello from Agent {self.name}."`. Create a `FieldAgent` object and call the `greet()` method.
3.  **Child Class Method:** In the `FieldAgent` class, add a new method `report_location(location)` that prints `f"Agent {self.name} reporting from {location}."`. Create an object and call this method.
4.  **Constructor Inheritance:** In the `FieldAgent` class, add a new `__init__` that takes `name` and `specialty`. Call the parent constructor using `super().__init__(name)` and then set the `specialty` attribute for the child class. Create an object and print its `specialty`.
5.  **Method Overriding:** In the `FieldAgent` class, override the `greet()` method from the parent class to instead print `f"This is Field Agent {self.name}, greeting you from the field."`. Create a `FieldAgent` object and call the `greet()` method to see the new message.


