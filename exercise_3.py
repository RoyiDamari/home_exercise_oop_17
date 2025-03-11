# question 1
"""Thread safe means that a piece of code, data structure, or function can be safely used or executed by multiple
threads at the same time without causing unexpected behavior, data corruption, or race conditions.
In a thread safe implementation, proper synchronization like locks is used to manage concurrent access to shared resources,
ensuring that the outcome is correct regardless of the order or timing of thread execution."""

# question 2
"""
This cod is not thread safe, because Without proper synchronization, 
the shared list can be modified by multiple threads simultaneously, leading to inconsistent or unexpected states.
for example a remover thread might find the list non-empty during the check, 
but before it executes pop(), another thread could remove an item, resulting in an IndexError.
To ensure complete thread safety, it's essential to apply the same lock across all functions that access the shared resource.
This means both adder and remover functions should acquire the lock before modifying the resource. 
This comprehensive locking mechanism prevents simultaneous modifications from different functions.
Also if we want removers to wait until there’s something to remove, we would need to synchronize removers and adders 
explicitly by using a condition variable (threading.Condition) to make removers wait until at least one item is present.
"""

# question 3
"""
This cod is thread safe, because the managers can create shared data structures like lists, dictionaries, and more, 
which can be safely accessed and modified by multiple processes.
By managing access through proxies, managers ensure that operations on shared objects are synchronized, preventing race conditions.
"""
