#                 Student Management System
#  Topics: Composition, @property, Inheritance, Mutable Objects
# ========================================================

# ─────────────────────────────────────────────
# PART 1 — Address Class (used via Composition)
# ─────────────────────────────────────────────
class Address:
    # Constructor: initialises street, city, zipCode
    def __init__(self, street, city, zipCode):
        self.street  = street
        self.city    = city
        self.zipCode = zipCode

    # Returns a readable string when print() is called on this object
    def __str__(self):
        return f"{self.street}, {self.city} - {self.zipCode}"


# ─────────────────────────────────────────────
# PART 2 — Student Class
#   • Composition  : holds an Address object
#   • @property    : controls access to _age
#   • Mutable list : courses list persists in-place
# ─────────────────────────────────────────────
class Student:

    def __init__(self, name, age, address):
        self.name    = name
        self.age     = age          # calls the @age.setter → validates
        self.address = address      # COMPOSITION: Student HAS-A Address
        self._courses = []          # mutable list — shared by reference

    # ── @property for age ──────────────────────────────────
    @property
    def age(self):
        """Getter — reads the protected _age attribute."""
        return self._age

    @age.setter
    def age(self, value):
        """
        Setter — validates before storing.
        Rules: must be int, must be between 1 and 120.
        Stored as _age (single underscore = protected by convention).
        """
        if not isinstance(value, int):
            raise TypeError("Age must be an integer.")
        if not (1 <= value <= 120):
            raise ValueError("Age must be between 1 and 120.")
        self._age = value           # stored as protected attribute

    # ── add_course() ───────────────────────────────────────
    def add_course(self, course):
        """
        Appends a course to the list IN-PLACE.
        Because lists are mutable, this change persists everywhere
        the same list is referenced — no re-assignment needed.
        """
        if course in self._courses:
            print(f"  '{course}' is already enrolled.")
        else:
            self._courses.append(course)   # in-place mutation
            print(f"  Course '{course}' added.")

    # ── display() ──────────────────────────────────────────
    def display(self):
        """Prints student details."""
        print("-----------------------------")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")          # goes through getter
        print(f"Address : {self.address}")      # calls Address.__str__
        print(f"Courses : {self._courses}")


# ─────────────────────────────────────────────
# PART 3 — ScholarshipStudent Class
#   • Inherits from Student
#   • Adds scholarshipAmount
#   • Overrides display() using super()
# ─────────────────────────────────────────────
class ScholarshipStudent(Student):

    def __init__(self, name, age, address, scholarshipAmount):
        # super().__init__ reuses ALL of Student's setup
        super().__init__(name, age, address)
        self.scholarshipAmount = scholarshipAmount

    # ── override display() ─────────────────────────────────
    def display(self):
        """
        Calls super().display() to reuse Student's output,
        then adds the scholarship line on top.
        """
        super().display()           # ← Student's display() runs first
        print(f"Scholarship: Rs.{self.scholarshipAmount:,}")
        print("-----------------------------")


# ─────────────────────────────────────────────
# PART 4 — Main / Test Code
# ─────────────────────────────────────────────
if __name__ == "__main__":

    # ── Test 1: Composition ───────────────────────────────
    
    addr1 = Address("12 MG Road", "Tezpur", "784001")
    s1    = Student("Ananya", 20, addr1)
    s1.display()

    # ── Test 2: add_course + mutable list ────────────────
    
    s1.add_course("Python")
    s1.add_course("DBMS")
    s1.add_course("Python")     # duplicate — should be rejected

    # Mutable proof: grab a reference BEFORE adding
    ref = s1._courses
    s1.add_course("OS")
    print(f"Via student obj : {s1._courses}")
    print(f"Via reference   : {ref}")           # same update visible here
    print(f"Same object?    : {s1._courses is ref}")   # True

    # ── Test 3: @property validation ─────────────────────
   
    try:
        s1.age = -5
    except ValueError as e:
        print(f"ValueError : {e}")

    try:
        s1.age = "twenty"
    except TypeError as e:
        print(f"TypeError  : {e}")

    s1.age = 21
    print(f"Valid update: age = {s1.age}")

    # ── Test 4: Inheritance + super() ────────────────────
    
    addr2 = Address("7 College Lane", "Guwahati", "781001")
    ss    = ScholarshipStudent("Rohan", 22, addr2, 75000)
    ss.add_course("Machine Learning")
    ss.add_course("Cloud Computing")
    ss.display()