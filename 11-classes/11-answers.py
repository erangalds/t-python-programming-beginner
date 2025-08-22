# ==============================================================================
# SOLUTIONS FOR HANDS-ON CLASSES EXERCISES
# ==============================================================================
# This document contains the Python code and a detailed thought process
# for each of the 15 story-based questions.
# The code is organized into sections that match the exercises.
# ==============================================================================

# ------------------------------------------------------------------------------
# Section 1: Defining a Class
# ------------------------------------------------------------------------------

# Question 1: Create a Gadget Class
# Thought Process: We define a class with a constructor to set an instance attribute.
class Gadget:
    def __init__(self, name):
        self.name = name

# Question 2: Create an Object
# Thought Process: We create an instance of the class and access its attribute.
spy_camera = Gadget("Spy Camera")
print(spy_camera.name)

# Question 3: Add a Method
# Thought Process: A method is a function defined inside a class, with 'self' as its first parameter.
class Gadget:
    def __init__(self, name):
        self.name = name

    def report(self):
        print(f"The {self.name} is ready.")

spy_camera = Gadget("Spy Camera")
spy_camera.report()

# Question 4: Add a Class Attribute
# Thought Process: A class attribute is defined outside any method and is shared.
class Gadget:
    status = "Operational"

    def __init__(self, name):
        self.name = name

    def report(self):
        print(f"The {self.name} is ready.")

gadget1 = Gadget("Laser Watch")
gadget2 = Gadget("Miniature Drone")
print(gadget1.status)
print(gadget2.status)

# Question 5: Create an Agent Class
# Thought Process: A new class with a constructor that takes two parameters.
class Agent:
    def __init__(self, codename, rank):
        self.codename = codename
        self.rank = rank

agent_alpha = Agent("Alpha", "Rookie")
print(agent_alpha.rank)


# ------------------------------------------------------------------------------
# Section 2: Class Methods
# ------------------------------------------------------------------------------

# Question 1: Introduce Method
# Thought Process: Add a method to the existing Agent class to print a greeting.
class Agent:
    def __init__(self, codename, rank):
        self.codename = codename
        self.rank = rank
    
    def introduce(self):
        print(f"I am Agent {self.codename}.")

agent_bravo = Agent("Bravo", "Veteran")
agent_bravo.introduce()

# Question 2: Assign Mission
# Thought Process: The method takes a parameter and assigns it to a new instance attribute.
class Agent:
    def __init__(self, codename, rank):
        self.codename = codename
        self.rank = rank

    def assign_mission(self, mission_name):
        self.mission = mission_name

agent_charlie = Agent("Charlie", "Rookie")
agent_charlie.assign_mission("Operation Phoenix")
print(f"Agent's mission: {agent_charlie.mission}")

# Question 3: Check Status
# Thought Process: The method returns a value, which is then printed by the calling code.
class Agent:
    def __init__(self, codename, rank):
        self.codename = codename
        self.rank = rank
        self.mission = "Undisclosed"

    def assign_mission(self, mission_name):
        self.mission = mission_name

    def check_status(self):
        return self.mission

agent_delta = Agent("Delta", "Veteran")
print(agent_delta.check_status())
agent_delta.assign_mission("Operation Ghost")
print(agent_delta.check_status())

# Question 4: Update Rank
# Thought Process: A method can modify an instance attribute.
class Agent:
    def __init__(self, codename, rank):
        self.codename = codename
        self.rank = rank
        
    def promote(self):
        self.rank = "Senior Agent"

agent_echo = Agent("Echo", "Rookie")
print(f"Initial Rank: {agent_echo.rank}")
agent_echo.promote()
print(f"New Rank: {agent_echo.rank}")

# Question 5: Deactivate
# Thought Process: A method can modify a class attribute, which affects all instances.
class Gadget:
    status = "Operational"

    def __init__(self, name):
        self.name = name

    def deactivate(self):
        Gadget.status = "Inactive"

gadget1 = Gadget("GPS Tracker")
gadget2 = Gadget("Voice Changer")
print(f"Initial status: {gadget1.status}")
gadget1.deactivate()
print(f"New status for gadget2: {gadget2.status}")


# ------------------------------------------------------------------------------
# Section 3: Inheritance
# ------------------------------------------------------------------------------

# Question 1: Parent and Child Classes
# Thought Process: The child class `FieldAgent` inherits from `BaseAgent`.
class BaseAgent:
    def __init__(self, name):
        self.name = name

class FieldAgent(BaseAgent):
    pass

field_agent = FieldAgent("James")
print(field_agent.name)

# Question 2: Inherited Method
# Thought Process: The child class automatically inherits the parent's methods.
class BaseAgent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello from Agent {self.name}.")

class FieldAgent(BaseAgent):
    pass

field_agent = FieldAgent("Bond")
field_agent.greet()

# Question 3: Child Class Method
# Thought Process: A child class can have its own unique methods.
class BaseAgent:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hello from Agent {self.name}.")

class FieldAgent(BaseAgent):
    def report_location(self, location):
        print(f"Agent {self.name} reporting from {location}.")

field_agent = FieldAgent("Jason")
field_agent.report_location("Paris")

# Question 4: Constructor Inheritance
# Thought Process: We must call the parent's constructor using `super().__init__()`
# to ensure the parent's attributes are set.
class BaseAgent:
    def __init__(self, name):
        self.name = name

class FieldAgent(BaseAgent):
    def __init__(self, name, specialty):
        super().__init__(name)
        self.specialty = specialty

field_agent = FieldAgent("Ethan", "Espionage")
print(field_agent.specialty)

# Question 5: Method Overriding
# Thought Process: We redefine the `greet()` method in the child class with the
# same name and signature. The child's method will be used instead of the parent's.
class BaseAgent:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hello from Agent {self.name}.")

class FieldAgent(BaseAgent):
    def __init__(self, name):
        super().__init__(name)

    def greet(self):
        print(f"This is Field Agent {self.name}, greeting you from the field.")

field_agent = FieldAgent("Jason")
field_agent.greet()
