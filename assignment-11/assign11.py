# ============================================================
#  LIBRARY MANAGEMENT SYSTEM
#  Concepts: Abstraction, Method Overriding, Polymorphism,
#            Default Arguments, Static Counter
# ============================================================

from abc import ABC, abstractmethod   # ABC = Abstract Base Class


# ─────────────────────────────────────────────
# 1. ABSTRACT BASE CLASS
# ─────────────────────────────────────────────
class LibraryItem(ABC):
    """
    Abstract base class for all library items.
    Demonstrates ABSTRACTION – defines a common structure
    and forces subclasses to implement displayInfo().
    """

    # ── Class / Static Variable (shared across ALL instances) ──
    total_items = 0   # counts every LibraryItem ever created

    def __init__(self, title, year):
        self.title = title
        self.year  = year
        LibraryItem.total_items += 1       # increment class counter

    # ── Abstract Method ──
    @abstractmethod
    def displayInfo(self):
        """
        Every subclass MUST override this method.
        Abstract methods define the CONTRACT of the base class.
        """
        pass   # no implementation here

    # ── Concrete (shared) Method ──
    def getAge(self):
        return 2025 - self.year

    # ── Class Method (alternative constructor pattern) ──
    @classmethod
    def getItemCount(cls):
        return cls.total_items

    # ── String representation ──
    def __str__(self):
        return f"[{self.__class__.__name__}] {self.title} ({self.year})"


# ─────────────────────────────────────────────
# 2. SUBCLASS – Book
# ─────────────────────────────────────────────
class Book(LibraryItem):
    """
    Inherits from LibraryItem.
    Adds: author, pages
    Demonstrates: constructor with DEFAULT ARGUMENT (pages=0)
    """

    def __init__(self, title, year, author, pages=0):   # default argument
        super().__init__(title, year)   # call parent constructor
        self.author = author
        self.pages  = pages             # optional; defaults to 0

    # ── METHOD OVERRIDING ──
    def displayInfo(self):
        print("=" * 40)
        print(f"  TYPE   : Book")
        print(f"  TITLE  : {self.title}")
        print(f"  AUTHOR : {self.author}")
        print(f"  YEAR   : {self.year}  (Age: {self.getAge()} yrs)")
        print(f"  PAGES  : {self.pages if self.pages else 'N/A'}")
        print("=" * 40)


# ─────────────────────────────────────────────
# 3. SUBCLASS – DVD
# ─────────────────────────────────────────────
class DVD(LibraryItem):
    """
    Inherits from LibraryItem.
    Adds: duration (minutes), genre
    Demonstrates: constructor with DEFAULT ARGUMENT (genre="Unknown")
    """

    def __init__(self, title, year, duration, genre="Unknown"):   # default argument
        super().__init__(title, year)
        self.duration = duration
        self.genre    = genre

    # ── METHOD OVERRIDING ──
    def displayInfo(self):
        print("=" * 40)
        print(f"  TYPE     : DVD")
        print(f"  TITLE    : {self.title}")
        print(f"  GENRE    : {self.genre}")
        print(f"  YEAR     : {self.year}  (Age: {self.getAge()} yrs)")
        print(f"  DURATION : {self.duration} min")
        print("=" * 40)


# ─────────────────────────────────────────────
# 4. SUBCLASS – Magazine  (third subclass)
# ─────────────────────────────────────────────
class Magazine(LibraryItem):
    """
    Inherits from LibraryItem.
    Adds: issue_number, publisher
    """

    def __init__(self, title, year, issue_number, publisher="Unknown"):
        super().__init__(title, year)
        self.issue_number = issue_number
        self.publisher    = publisher

    # ── METHOD OVERRIDING ──
    def displayInfo(self):
        print("=" * 40)
        print(f"  TYPE      : Magazine")
        print(f"  TITLE     : {self.title}")
        print(f"  PUBLISHER : {self.publisher}")
        print(f"  ISSUE     : #{self.issue_number}")
        print(f"  YEAR      : {self.year}  (Age: {self.getAge()} yrs)")
        print("=" * 40)


# ─────────────────────────────────────────────
# 5. MAIN – Polymorphism 
# ─────────────────────────────────────────────
if __name__ == "__main__":

    # ── Create objects ──
    b1 = Book("The Alchemist",       1988, "Paulo Coelho", pages=197)
    b2 = Book("Clean Code",          2008, "Robert Martin")      # pages uses default = 0
    d1 = DVD("Inception",            2010, duration=148, genre="Sci-Fi")
    d2 = DVD("The Dark Knight",      2008, duration=152)          # genre uses default
    m1 = Magazine("National Geographic", 2023, issue_number=215, publisher="NatGeo")

    print("\n📚  LIBRARY CATALOGUE")
    print("─" * 40)

    # ── POLYMORPHISM ──
    # A single list holds objects of different types (Book, DVD, Magazine).
    # Calling displayInfo() on each invokes the correct overridden version
    # automatically – this is POLYMORPHISM in action.

    library: list[LibraryItem] = [b1, b2, d1, d2, m1]

    for item in library:
        item.displayInfo()   # same call → different behaviour per type

    # ── Static Counter ──
    print(f"\n📊  Total items created : {LibraryItem.getItemCount()}")
    print(f"    (via class/static counter on LibraryItem)\n")

    