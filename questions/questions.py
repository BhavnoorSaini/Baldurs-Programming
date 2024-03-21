def easy():
    questions = (
    "What is the syntax for declaring a variable in C++?: ",
    "Explain the difference between pass by value and pass by reference in C++.: ",
    "How do you initialize an array in C++?: ",
    "What is the purpose of the iostream library in C++?: ",
    "What is the difference between cout and cin in C++?: "
    )

    options = (

    # What is the syntax for declaring a variable in C++?
    ("A) variable_name = value;", "B) data_type variable_name;", "C) variable_name();", "D) variable_name = data_type;"),

    # Explain the difference between pass by value and pass by reference in C++.
    ("A) Pass by value makes a copy of the memory address of the actual parameter, while pass by reference directly accesses the value of the actual parameter.",
    "B) Pass by value makes a copy of the actual parameter's value, while pass by reference allows the function to directly access and modify the actual parameter.",
    "C) Pass by value allows the function to directly access and modify the actual parameter, while pass by reference makes a copy of the actual parameter's value.",
    "D) Pass by value directly accesses the value of the actual parameter, while pass by reference makes a copy of the memory address of the actual parameter."),

    # How do you initialize an array in C++?
    ("A) data_type array_name[size];",
    "B) array_name[size] = {value1, value2, ...};",
    "C) data_type array_name = size;",
    "D) array_name = data_type[size];"),

    # What is the purpose of the iostream library in C++?
    ("A) For manipulating strings.",
    "B) For performing mathematical operations.",
    "C) For input and output operations.",
    "D) For handling exceptions."),

    # What is the difference between cout and cin in C++?
    ("A) cout is used for input and cin is used for output.",
    "B) cout is used for formatting output, while cin is used for formatting input.",
    "C) cout is used for output (printing), while cin is used for input (reading).",
    "D) cout is used for error handling, while cin is used for exception handling.")
    )


    answers = ("B", "B", "B", "C", "C")


def medium():
    questions = ("Explain the concept of pointers in C++ and provide an example.",
    "What is the difference between struct and class in C++?",
    "Describe the purpose of constructors and destructors in C++.",
    "How do you dynamically allocate memory in C++?",
    "Explain the concept of inheritance in C++ with an example."
    )

    options = (
    
    # Explain the concept of pointers in C++ and provide an example.
    (" A) Pointers are variables that store multiple values. Example: int *ptr = 10;",
    "B) Pointers are variables that store memory addresses. Example: int *ptr;",
    "C) Pointers are functions that return multiple values. Example: ptr(int x, int y) {}",
    "D) Pointers are operators used for arithmetic operations. Example: int *ptr = &x;"),

    # What is the difference between struct and class in C++?`
    ("A) There is no difference between struct and class.",
    "B) Members of a struct are private by default, while members of a class are public by default.",
    "C) Members of a struct are public by default, while members of a class are private by default.",
    "D) struct is used for single inheritance, while class is used for multiple inheritance."),

    # Describe the purpose of constructors and destructors in C++.
    ("A) Constructors are used to initialize objects, while destructors are used to clean up resources.",
    "B) Constructors are used to clean up resources, while destructors are used to initialize objects.",
    "C) Constructors are used for dynamic memory allocation, while destructors are used for static memory allocation.",
    "D) Constructors are used to declare variables, while destructors are used to perform arithmetic operations."),

    # How do you dynamically allocate memory in C++?
    ("A) Using the alloc keyword.",
    "B) Using the malloc function.",
    "C) Using the allocate keyword.",
    "D) Using the new keyword."),

    # Explain the concept of inheritance in C++ with an example.
    ("A) Inheritance allows a class to inherit properties and behaviors from another class. Example: class DerivedClass : public BaseClass {}",
    "B) Inheritance allows a class to have multiple parents. Example: class DerivedClass : public BaseClass1, public BaseClass2 {}",
    "C) Inheritance allows a class to override methods of its parent class. Example: class DerivedClass : public BaseClass { void method() {} }",
    "D) Inheritance allows a class to implement multiple interfaces. Example: class DerivedClass : public Interface1, public Interface2 {}")

    )

    answers = ("B", "C", "A", "D", "A")

    


def hard():
    questions = ("What are lambda expressions in C++? Provide an example of their usage.",
    "Describe the difference between runtime polymorphism and compile-time polymorphism in C++.",
    "Explain the concept of function overloading and function overriding in C++.",
    "What is a template in C++? How do you define and use templates?",
    "Describe the process of multiple inheritance in C++ and its potential issues.",
    )

    options = (

    # What are lambda expressions in C++? Provide an example of their usage.
    ("A) Lambda expressions are variables that store memory addresses.",
    "B) Lambda expressions are functions that return multiple values.",
    "C) Lambda expressions are anonymous functions that can capture variables from their surrounding scope.",
    "D) Lambda expressions are used for exception handling."),
    

    # Describe the difference between runtime polymorphism and compile-time polymorphism in C++.
    ("A) Runtime polymorphism is achieved through function overloading, while compile-time polymorphism is achieved through inheritance.",
    "B) Runtime polymorphism is achieved through virtual functions and dynamic binding, while compile-time polymorphism is achieved through templates and function overloading.",
    "C) Runtime polymorphism is achieved through static binding, while compile-time polymorphism is achieved through dynamic binding.",
    "D) Runtime polymorphism is achieved through templates, while compile-time polymorphism is achieved through inheritance."),
    

    # Explain the concept of function overloading and function overriding in C++.
    ("A) Function overloading involves redefining a base class function in a derived class, while function overriding involves having multiple functions with the same name but different parameters.",
    "B) Function overloading involves having multiple functions with the same name but different parameters, while function overriding involves redefining a base class function in a derived class.",
    "C) Function overloading and function overriding are the same concept in C++.",
    "D) Function overloading and function overriding are not supported in C++."),
   
    # What is a template in C++? How do you define and use templates?
    ("A) Templates allow generic programming by defining functions or classes that can work with any data type.",
    "B) Templates are used for dynamic memory allocation.",
    "C) Templates are used for exception handling.",
    "D) Templates are used for arithmetic operations."),
   

    # Describe the process of multiple inheritance in C++ and its potential issues.
    ("A) Multiple inheritance allows a class to inherit from multiple base classes. Issues include ambiguity and the diamond problem.",
    "B) Multiple inheritance allows a class to have multiple parents, resolving issues with code reuse.",
    "C) Multiple inheritance is not supported in C++.",
    "D) Multiple inheritance allows a class to inherit from multiple derived classes.")

    )

    answers = ("C", "B", "B", "A", "A")
