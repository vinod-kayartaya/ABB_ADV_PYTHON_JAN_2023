## Ask yourself these and see if you can answer this to your friend:

1. What is a class in Python?
2. What is an object in Python?
3. How do you create a class in Python?
4. How do you create an object in Python?
5. What is the difference between a class and an object?
6. What are class variables and instance variables?
7. What is the purpose of a constructor in a class?
8. What is the self keyword in Python?
9. How do you define a method in a class?
10. How do you inherit from one class to another in Python?
11. What is encapsulation in OOP?
12. What are the magic methods in Python and what are they used for?
13. How do you override a built-in method in Python?
14. Give an example of how you would use OOP to model a real-world problem.

## Explore more by R&D:

1. What is multiple inheritance in Python?
2. How do you achieve multiple inheritance in Python?
3. What is the method resolution order (MRO) in Python?
4. How does Python handle conflicts when multiple inheritance is used?
5. How does the diamond problem in multiple inheritance impact the MRO in Python?
6. How can you use the super() function in a multiple inheritance scenario?
7. How does Mixin class concept work in Python?
8. Give an example of how you would use multiple inheritance to model a real-world problem.
9. How does multiple inheritance impact the encapsulation in OOP?
10. What are the advantages and disadvantages of using multiple inheritance?

## Here are some reference links related to the topics we discussed:

1. Python Classes and Objects: [https://www.w3schools.com/python/python_classes.asp](https://www.w3schools.com/python/python_classes.asp)
2. Python Constructors: [https://www.w3schools.com/python/python_constructors.asp](https://www.w3schools.com/python/python_constructors.asp)
3. Python Inheritance: [https://www.w3schools.com/python/python_inheritance.asp](https://www.w3schools.com/python/python_inheritance.asp)
4. Python Method Overriding: [https://www.w3schools.com/python/python_method_overriding.asp](https://www.w3schools.com/python/python_method_overriding.asp)
5. Python Magic Methods: [https://www.geeksforgeeks.org/magic-methods-python/](https://www.geeksforgeeks.org/magic-methods-python/)
6. Python Multiple Inheritance: [https://www.geeksforgeeks.org/multiple-inheritance-python/](https://www.geeksforgeeks.org/multiple-inheritance-python/)
7. Mixins in Python: [https://en.wikipedia.org/wiki/Mixin](https://en.wikipedia.org/wiki/Mixin)
8. Method Resolution Order (MRO) in Python: [https://www.python.org/download/releases/2.3/mro/](https://www.python.org/download/releases/2.3/mro/)
9. Python super() function: [https://www.geeksforgeeks.org/super-in-python/](https://www.geeksforgeeks.org/super-in-python/)

# Decorators in Python

-   Decorators in Python are a way to modify or extend the behavior of a function or class without modifying its source code.
-   They are typically implemented as a wrapper function that takes the original function or class as an input, performs some operation on it, and then returns the modified function or class.
-   Decorators are applied to functions or methods using the "@" symbol followed by the decorator function name, immediately preceding the definition of the function or method to be decorated.
-   They can take arguments to customize the behavior of the decorated function or method.
-   Some examples of built-in decorators in Python include `@property`, `@classmethod`, `@staticmethod`, `@abstractmethod`.
-   They can be used for adding functionality such as logging, authentication, timing, etc. to functions or methods without cluttering the code.

```mermaid
sequenceDiagram
    participant Original Function/Method
    participant Decorator Function
    participant Wrapper Function
    participant Modified Function/Method

    Original Function/Method->Decorator Function: Pass as argument
    Decorator Function->Wrapper Function: Defines a new function
    Wrapper Function->Decorator Function: Perform operations
    Decorator Function->Modified Function/Method: Returns modified function


```

-   The original function or method is defined and passed as an argument to the decorator function.
-   The decorator function defines a new wrapper function that takes the same arguments as the original function or method.
-   The wrapper function performs some operation on the original function or method, such as logging, authentication, timing, etc.
-   The modified function or method is returned by the decorator function.
-   The modified function or method can be called like the original function or method, but now it also includes the added functionality provided by the decorator.

# Multithreading

-   It is a technique in computer science to execute multiple lines (threads) of execution concurrently
-   A `thread` is a light weight, independent unit of execution
-   Multiple threads can be part of the same process
-   There are a lot of things (for example, memory) that shared by a thread with other threads, and hence they are light weight

## Advantages:

-   Improved performance
-   Increased responsiveness
-   Better utilization of resources
-   Easy to implement

## Differences between multithreading and multiprocessing

-   Concurrent execution
-   Resource sharing
-   Communication
-   Overhead

# Assignments for Day 2

## Assignment 1

Create a CLI application in Python that allows the user to perform CRUD operations on a database. The application should have the following functionality:

1. Connect to a database and create a table named "employees" with the following columns: "id" (integer), "name" (text), "age" (integer), and "salary" (real).

    - The students should use the sqlite3 library to connect to a database.
    - The students should use the appropriate SQL commands to create the "employees" table with the specified columns.

2. Allow the user to insert, update, and delete data in the "employees" table.

    - The students should provide a menu-based interface for the user to choose between the different CRUD operations.
    - The students should use appropriate SQL commands for each CRUD operation (INSERT, UPDATE, DELETE).

3. Allow the user to retrieve data from the "employees" table and display it in the console.

    - The students should provide a menu-based interface for the user to choose between different retrieval options.
    - The students should use the SELECT SQL command to retrieve data from the table and display it in the console.

4. Close the database connection when the application exits.

    - The students should properly close the database connection when the user chooses to exit the application.

Some additional requirements for the students to complete the project:

-   Students should validate the user inputs and handle the possible errors that may occur.
-   Students should write the necessary comments for the code
-   Provide the students with a sample database to work with and also include necessary instructions on how to connect to the database.

## Assignment 2

Create a Python program that utilizes multithreading to perform the following tasks:

1. Read a large text file concurrently. The program should split the file into smaller chunks and each chunk should be read by a separate thread.
2. Process the text concurrently. Each thread should process the text it read, to count the number of occurrences of a specific word.
3. Write the processed data concurrently to a database. Each thread should write the number of occurrences of the specific word for the chunk of text it read, to the database.
4. Implement a progress bar that updates in real-time to show the progress of the reading, processing, and writing tasks.

Additional requirements:

-   The students should use the threading library to create and manage threads.
-   The students should handle exceptions and ensure that the program can gracefully handle any errors that may occur during the execution.
-   The students should use a database such as MySQL or PostgreSQL to store the data
-   The students should write the necessary comments for the code

# Web services

What is a web service?

-   A service offered on the web
-   A method of communication between two electronic devices over a web network
-   Uses the web protocol (HTTP)
-   Allows communication between applications written in different languages/platforms
    -   For example, a Java app can communicate with a PHP application

Types:

1. SOAP (Big) web services
2. RESTful web services
    - Based on the work by Roy Fielding (who is the co-creator of HTTP protocol)
    - 6 constraints
        1. Uniform interface
            - http://example.com/api/products --> GET, POST
            - http://example.com/api/products/23 --> GET, PUT, DELETE
        1. Client/Server
        1. Stateless
        1. Cacheable
        1. Layered system
        1. Code on demand (Optional)
    - Can be easily implemented by using frameworks
        - Java --> Springboot, JAX-RS, Resteasy, Restlets, Apache Axis
        - Python --> Flask, Bottle, DJango
        - .Net --> Web api
