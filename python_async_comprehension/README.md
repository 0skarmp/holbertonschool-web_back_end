Generators:

A generator is a function that returns a generator object. Unlike a normal function that returns a value and completes, a generator allows its execution to be paused and resumed.  This means that you can get one value at a time, instead of generating all the values and storing them in memory. Generators are useful when you need to generate a potentially     large sequence of data and you don't want to load all the data into memory at the same time.

Usage of the yield keyword:

The yield keyword is used in a function to indicate that it is a generator. When a yield statement is encountered in a function, the function pauses and returns a value to the caller. The function can then resume from where it stopped on the next call.
