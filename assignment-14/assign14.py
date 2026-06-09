import sys
import gc

class Node:
    def __init__(self, name):
        self.name = name
        self.link = None

    def __repr__(self):
        return f"Node({self.name})"


# Enable garbage collection
gc.enable()

print("=== Creating Nodes ===")
A = Node("A")
B = Node("B")

# Create a cycle
A.link = B
B.link = A

print("\n=== Reference Counts ===")
print("A refcount:", sys.getrefcount(A))
print("B refcount:", sys.getrefcount(B))

# Keep object IDs for investigation later
a_id = id(A)
b_id = id(B)

print("\n=== Objects before deletion ===")
for obj in gc.get_objects():
    if id(obj) in (a_id, b_id):
        print("Found:", obj)

print("\n=== Deleting A and B ===")
del A
del B

print("Variables A and B are gone.")

print("\n=== Investigating Memory Before GC ===")
found = []

for obj in gc.get_objects():
    if id(obj) in (a_id, b_id):
        found.append(obj)

if found:
    print("Objects still exist because of the cycle:")
    for obj in found:
        print(obj)
else:
    print("Objects not found.")

print("\n=== Running Garbage Collector ===")
collected = gc.collect()

print("Unreachable objects collected:", collected)

print("\n=== Investigating Memory After GC ===")
found = []

for obj in gc.get_objects():
    if id(obj) in (a_id, b_id):
        found.append(obj)

if found:
    print("Objects still exist:")
    for obj in found:
        print(obj)
else:
    print("Cycle successfully removed. Objects no longer exist.")