---
toc: True
comments: True
layout: post
title: Topics 5.1-5.3
---

# 5.1 Anatomy of a Class

## KEY LEARNING OBJECTIVES:

1. Designate access and visibility constraints to classes, data, constructors, and methods.

2. Designate private visibility of instance variables to encapsulate the attributes of an object.

## What is a class?

A **class** is a template for creating objects in Java. 

## Private vs Public Designation

**Private**: A private access modifier means that the instance variables, constructors, and methods cannot be accessed outside of the class.

**Public**: This allows access from classes outside the original class of declaration.

## Data Encapsulation

This is one of the key components of object oriented programming. 

It ensures data is secure and restricted by controlling which parts of a class are accessible to other classes.

In the following example, we look at encapsulation and demonstrate how to create a Student class with private instance variables for name and age, public methods for accessing and modifying these variables, and validation checks to ensure data integrity. 


```java
public class Student {
    // 1. Private variables to store student's name and age
    private String name; // Stores the student's name
    private int age;     // Stores the student's age

    // 2. Public Class: Student

    // 3. Constructor Methods
    // Constructor to create a Student object with a name and age
    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public static void main(String[] args) {
        // Let's create a new Student!
        Student student = new Student("Vishnu", 17);

        // Displaying the student's information
        System.out.println("Meet our star student:");
        System.out.println("Name: " + student.name); // Accessing the name directly
        System.out.println("Age: " + student.age);   // Accessing the age directly
    }
}

Student.main(null);

```

    Meet our star student:
    Name: Vishnu
    Age: 17


# 5.2 Constructors

## KEY LEARNING OBJECTIVES

Define instance variables for the attributes to be initialized through the constructors of a class.

Constructors are used to set the initial state of an object.


**Mutable Objects**: These are objects whose internal state can be changed after its creation. Lists are mutable objects, as are arrays.

**Constructor Parameters**: These are values passed to a class's constructor when creating an instance. This initializes the new object's state.

**Instance Variables**: These are object attributes that store the objects state. They are declared within the class and can be accessed by the object's methods.

**Alias**: Two variables point to the same object.

A good example of a Java alias:


```java
public class AliasExample {
    public static void main(String[] args) {
        // Create an array and two references (aliases) to it
        int[] array = new int[]{1, 2, 3};
        int[] alias1 = array;
        int[] alias2 = array;

        // Modify the array through one of the aliases
        alias1[0] = 100;

        // Access the modified array through the other alias
        System.out.println("Value at index 0 through alias2: " + alias2[0]);
    }
}

AliasExample.main(null);
```

    Value at index 0 through alias2: 100


In the below example, we explore encapsulation and demonstrate how to create a Person class to represent individuals with private attributes for name, age, and hobbies. The code showcases how to initialize and manipulate a Person object's state, including adding hobbies to the person's list, while ensuring the original data remains unchanged.


```java
public class Person {
    private String name;
    private int age;

    // Constructor to initialize a Person with a name and age
    public Person(String name, int age) {
        this.name = name;  // Initialize the 'name' field with the provided name
        this.age = age;    // Initialize the 'age' field with the provided age
    }

    // Method to display the person's information
    public void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}

public class PersonConstructorDemo {
    public static void main(String[] args) {
        // Create two Person objects using the constructor
        Person person1 = new Person("Anna", 17);
        Person person2 = new Person("Rohin", 13);

        // Display information about the created persons
        System.out.println("Person 1:");
        person1.displayInfo();
        
        System.out.println("Person 2:");
        person2.displayInfo();
    }
}

PersonConstructorDemo.main(null);

```

    Person 1:
    Name: Anna
    Age: 17
    Person 2:
    Name: Rohin
    Age: 13


In the Person class, the hobbies list is encapsulated to prevent unintended modifications. What is the importance of encapsulation and how does it improve the design of the class?

**

# 5.3 Documentation with Comments

## KEY LEARNING OBJECTIVE

Describe the functionality and use of program code through comments.

**Precondition**: This is a condition that has to be met prior to an execution of a certain part of the code for the method to work.

**Postcondition**: This is a condition that has to be met after the execution of a certain part of the code. 


```java
public class Comments {
    private int value; // Initialize a value

    public Comments(int value) {
        this.value = value; // Set a constructure for a value
        System.out.println("Constructor called with value: " + value); // State a value
    }

    public int getValue() {
        return value; // Just get the value
    }

    public static void main(String[] args) {
        Comments myObject = new Comments(42);  // New object
        int result = myObject.getValue();    // Get the value of the object and save it to the result
        System.out.println("Value: " + result); // Output the value
    }
}

Comments.main(null); // run the main function

```

    Constructor called with value: 42
    Value: 42


**ADD DESCRIPTIVE COMMENTS TO THE ABOVE CODE. Provide descriptions of functionality, identify methods used, and initialized variables if any.**

# Hacks

**POPCORN HACKS: 0.2**

**Create a simple To-Do List that utilizes the following (0.8):**

1. Private and Public Declaration

2. Constructor

3. Mutable Array containing To-Do List Items

Make sure to add descriptive comments that are describing your code!


```java
import java.util.ArrayList;

public class TodoList {
    private ArrayList<String> items;

    // Constructor to initialize a TodoList with an item
    public TodoList(String item) {
       this.items = new ArrayList<String>();
       this.items.add(item);
    }

    public void displayInfo() {
        for(String task : items) { // for all the tasks in the list of items, print it with a dash cuz that a list
            System.out.println("- " + task);
        }
    }
}

public class ToDoListDemo {
    public static void main(String[] args) {
        // Create two TodoList objects using the constructor

        TodoList task1 = new TodoList("Hhiiii"); // first task
        TodoList task2 = new TodoList("bie"); // second task
        TodoList task3 = new TodoList("Eat food"); // third task

        // Display information about the created tasks
        System.out.println("TASKS:");
        task1.displayInfo(); // display tasks
        task2.displayInfo(); // display tasks
        task3.displayInfo(); // display tasks
    }
}

ToDoListDemo.main(null);
```

    TASKS:
    - Hhiiii
    - bie
    - Eat food


# Topic 5.4: Accessor Methods

In Java, classes serve as blueprints for creating objects. These classes can encapsulate attributes (fields) and behaviors (methods). One of the cornerstones of Object-Oriented Programming is **data encapsulation**. This principle restricts direct access to some of an object's components, ensuring data integrity and security. Accessor methods, colloquially known as "getters", offer a controlled means to access these attributes.

## Accessor Methods

An **Accessor Method** permits other objects to retrieve the value of instance or static variables. They are typically non-void methods without parameters that return a value.

For instance, consider a class `Circle`:


```Java
public class Circle {
    private double radius;

    public Circle(double r) {
        this.radius = r;
    }

    // Accessor method for radius
    public double getRadius() {
        return radius;
    }
}
```

In the code above, the method `getRadius` is an accessor method. It allows external code to retrieve the value of the `radius` attribute without directly accessing the private field. This is a fundamental aspect of data encapsulation, ensuring that the internal state of an object is protected and can only be accessed or modified in controlled ways.

## Return by Value

Java employs the "return by value" approach for its methods. This implies that when a method returns a value, it's essentially returning a copy of that value. This is especially true for primitive data types.


```Java
public int getIntegerValue() {
    int value = 5;
    return value;
}
```

In the method above, the value `5` is returned, not the variable `value` itself.

## Reference Return

For objects, when a method returns an object, it's essentially returning a reference to that object, not a fresh copy. This becomes pivotal when dealing with mutable objects.


```Java
public class Box {
    private ArrayList<String> items;

    public Box() {
        items = new ArrayList<>();
    }

    public ArrayList<String> getItems() {
        return items;
    }

    public static void main(String[] args) {
        Box box = new Box();
        box.items.add("hello");
    }
}
```

If you append an item to the ArrayList returned by `getItems`, will it modify the original `items` in the `Box` object?

Answer: NO

## `toString` Method

The `toString` method offers a string representation of an object. By default, it returns the class name followed by its memory address. However, it's a common practice to override this method to provide a more descriptive representation.


```Java
public class Circle {
    private double radius;

    public Circle(double r) {
        this.radius = r;
    }

    // @Override
    public String toString() {
        return "Circle with radius: " + radius;
    }

    public static void main(String[] args) {
        Circle circle = new Circle(5.0);
        System.out.println(circle); // This will implicitly call the toString() method
    }
}

Circle.main(null);

```

    Circle with radius: 5.0


Without overriding, what would the default `toString` method return?

Answer: 5.0

# Topic 5.5: Mutator Methods

Mutator methods, often referred to as "setters", play a crucial role in object-oriented programming. They allow controlled modification of an object's state. While accessor methods ("getters") retrieve the state of an object, mutator methods modify it.

## Void Methods

A **void method** does not return any value. Instead, its primary purpose is to perform an action. The keyword `void` in the method's header signifies that the method won't return any value.


```Java
public class exampleVoid {
    public void displayMessage() {
        System.out.println("Hello, World!");
    }

    public static void main(String[] args) {
        exampleVoid example = new exampleVoid();
        example.displayMessage();
    }
}

exampleVoid.main(null);
```

    Hello, World!


In the example above, the `displayMessage` method doesn't return any value; it simply prints a message to the console.

## Mutator (Modifier) Methods

A **mutator method** is typically a void method that alters the values of instance or static variables. These methods ensure that the internal state of an object can be changed in a controlled manner, adhering to the principles of data encapsulation and data integrity.

Consider a class `Rectangle`:


```Java
public class Rectangle {
    private double length;
    private double width;

    // Mutator method for length
    public void setLength(double length) {
        if (length > 0) {
            this.length = length;
        } else {
            System.out.println("Invalid length provided.");
        }
    }

    // Mutator method for width
    public void setWidth(double width) {
        if (width > 0) {
            this.width = width;
        } else {
            System.out.println("Invalid width provided.");
        }
    }

    public static void main(String[] args) {
        Rectangle rect = new Rectangle();
        rect.setLength(5);
        rect.setWidth(-3);
    }
}

Rectangle.main(null);
```

    Invalid width provided.


In the `Rectangle` class, the methods `setLength` and `setWidth` are mutator methods. They allow the modification of the `length` and `width` attributes, respectively, while ensuring that only valid values are set.

Suppose you add another method to the `Rectangle` class called `setDimensions` which takes a single string parameter in the format "length,width" (e.g., "10,5"). This method should parse the string, validate the values, and then set the `length` and `width` accordingly. If the string is in an invalid format or contains negative values, it should print an error message. Can you draft this method?

# Topic 5.6: Writing Methods

Methods in Java allow us to define behaviors for objects. When these methods are non-void and have parameters, they can return a value based on the provided arguments.

## Accessing Private Data

Methods can only access the private data and methods of a parameter that is a reference to an object when the parameter is of the same type as the method's enclosing class. This ensures data encapsulation and integrity.


```Java
public class MyClass {
    private int privateData = 10;

    public int getPrivateData() {
        return privateData;
    }

    public static void main (String[] args) {
        MyClass example = new MyClass();
        int integer = example.getPrivateData();
        System.out.println(integer);
    }
}

MyClass.main(null);
```

    10


# Non-Void Methods with Parameters

These methods are designed to receive values, process them, and return a computed result.


```Java
public class AreaCalculator {
    public double calculateArea(double length, double width) {
        return length * width;
    }

    public static void main(String[] args) {
        AreaCalculator calculator = new AreaCalculator();
        double area = calculator.calculateArea(5, 10);
        System.out.println("Area: " + area);
    }
}

AreaCalculator.main(null);
```

    Area: 50.0


# Handling Mutable Objects

It's a good programming practice not to modify mutable objects passed as parameters unless it's explicitly required.

**Why?** Modifying mutable objects that are passed as parameters can lead to unintended side effects in the calling code. The calling code might not expect the object to be modified, and this can introduce bugs that are hard to trace. By avoiding the modification of passed objects, you ensure that the function or method is "pure" and doesn't produce unexpected side effects.


```Java
import java.util.ArrayList;

public class ListModifier {
    public void modifyList(ArrayList<String> list) {
        // Not recommended unless explicitly required
        list.add("New Item");
    }

    public static void main(String[] args) {
        ArrayList<String> items = new ArrayList<>();
        items.add("Original Item");
        
        ListModifier modifier = new ListModifier();
        modifier.modifyList(items);
        
        System.out.println(items);
    }
}
```

Question: What will be the output of the above code?

Answer: Original Item, New Item (list format)

# Primitive vs. Reference Parameters

When a method's parameter is a primitive type, changes to it inside the method won't affect the original value. However, for reference types, changes inside the method will reflect on the original object.


```Java
import java.util.ArrayList;

public class ValueModifier {
    public void modifyValues(int num, ArrayList<String> list) {
        num = 20;
        list.add("Modified");
    }

    public static void main(String[] args) {
        int number = 10;
        ArrayList<String> items = new ArrayList<>();
        
        ValueModifier modifier = new ValueModifier();
        modifier.modifyValues(number, items);
        
        System.out.println("Number: " + number);
        System.out.println("List: " + items);
    }
}

ValueModifier.main(null);
```

    Number: 10
    List: [Modified]


When a reference is passed to a method, both the original and the parameter inside the method point to the same memory location. This is termed as aliasing.


```Java
public class AliasingExample {
    public void addToList(ArrayList<String> list) {
        list.add("Aliased Item");
    }

    public static void main(String[] args) {
        ArrayList<String> items = new ArrayList<>();
        
        AliasingExample example = new AliasingExample();
        example.addToList(items);
        
        System.out.println(items);
    }
}
```

Given the `AliasingExample` class, add a method named `removeFromList` that removes an item from the list based on its index. After adding the item "Aliased Item" using the `addToList` method, use the `removeFromList` method to remove it.

**Note**: Due to aliasing, changes made to the list inside the method will reflect on the original list.

# Topic 5.7: Static Variables and Methods

In Java, the `static` keyword plays a pivotal role in the realm of Object-Oriented Programming. It allows variables and methods to be associated with the class itself rather than instances of the class. Let's delve deeper into the world of static components.

## Static Variables

Static variables, unlike instance variables, are associated with the class itself and not with any specific instance. This means there's only one copy of a static variable, which is shared among all instances of the class.

### Key Points:

- **Single Copy**: All instances of the class share the same copy of the static variable. This means if one object modifies a static variable, it reflects in all other instances.
- **Access Modifiers**: Static variables can be either `public` or `private`, determining their visibility.
- **Usage**: They are accessed using the class name, not through an instance.


```Java
public class Student {
    private static int studentCount = 0;
    private String name;

    public Student(String name) {
        this.name = name;
        studentCount++;
    }

    public static int getStudentCount() {
        return studentCount;
    }

    public static void main(String[] args) {
        Student alice = new Student("Alice");
        Student bob = new Student("Bob");
        System.out.println("Total Students: " + Student.getStudentCount());
    }
}
Student.main(null)
```

    Total Students: 2


Question: If another student, Vardaan, enrolls, what will be the output of `Student.getStudentCount()`?

Answer: 3

## Static Methods

Static methods are methods that belong to the class, not any specific instance. This means you can call a static method without creating an object of the class.

### Key Points:
- **Association with Class**: Static methods are not tied to an instance of the class. This means they can't access instance variables or methods directly.
- **Access Restrictions**: Static methods cannot access instance variables or call non-static methods directly. They can only access static variables or call other static methods.
- **Usage**: They are called using the class name.


```Java
public class MathUtility {
    public int num;
    
    public static int square(int number) {
        return number * number;
    }

    public static void main(String[] args) {
        int result = MathUtility.square(num);
        System.out.println("Square: " + result);
    }
}
```

Question: What is the problem with the above code (do not run the cell)?

Answer: Var int is not static

## Aliasing in Static Components

Given that static variables are shared among all instances, changes in one instance reflect in others. This is a form of aliasing, where multiple references point to the same memory location.


```Java
public class SharedResource {
    // Static variable shared among all instances
    public static int sharedCount = 0;

    public void incrementCount() {
        sharedCount++;
    }

    public static void main(String[] args) {
        SharedResource obj1 = new SharedResource();
        SharedResource obj2 = new SharedResource();

        obj1.incrementCount();
        System.out.println("Shared count after incrementing in obj1: " + SharedResource.sharedCount);

        obj2.incrementCount();
        System.out.println("Shared count after incrementing in obj2: " + SharedResource.sharedCount);
    }
}

SharedResource.main(null);
```

    Shared count after incrementing in obj1: 1
    Shared count after incrementing in obj2: 2


When you run the above code, you'll notice that the `sharedCount` variable is incremented by both `obj1` and `obj2`, demonstrating that the static variable is indeed shared among all instances.

# Topic 5.8: Scope and Access

In Java, the scope of a variable determines where it can be accessed or modified. The scope is defined by where the variable is declared. Let's delve into the intricacies of variable scope and access in Java.

## Local 

Local variables are declared within methods or constructors. Their scope is limited to the block in which they are declared, which means they can't be accessed outside of that block.

**Key Points**:

- **Declaration**: Local variables can be declared in methods or constructors.
- **Accessibility**: They can only be used within the method or constructor where they are declared.
- **Modifiers**: Local variables cannot have access modifiers like `public` or `private`.


```Java
public class LocalVariableExample {
    public void displayMessage() {
        String localVariable = "Hello, World!";
        System.out.println(localVariable);
    }

    public static void main(String[] args) {
        LocalVariableExample example = new LocalVariableExample();
        example.displayMessage();
    }
}

LocalVariableExample.main(null);
```

In the above code, `localVariable` is a local variable that can only be accessed within the `displayMessage` method.

## Shadowing

When a local variable has the same name as an instance variable, the local variable shadows or hides the instance variable. In such cases, the local variable takes precedence.


```Java
public class ShadowExample {
    private int value = 10;

    public void printValue(int value) {
        System.out.println(value);  // Refers to the local variable
        System.out.println(this.value);  // Refers to the instance variable
    }

    public static void main(String[] args) {
        ShadowExample example = new ShadowExample();
        example.printValue(5);
    }
}

ShadowExample.main(null);
```

    5
    10


Question: In the `ShadowExample` class, if we didn't use the `this` keyword, which `value` would the method refer to?

Answer: 5

## Formal Parameters

Formal parameters in methods or constructors are treated as local variables. Their scope is limited to the method or constructor in which they are defined.


```Java
public class DetailsDisplay {
    public void displayDetails(String name, int age) {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }

    public static void main(String[] args) {
        DetailsDisplay display = new DetailsDisplay();
        display.displayDetails("John", 25);
    }
}

DetailsDisplay.main(null);
```

    Name: John
    Age: 25



In the above method, `name` and `age` are formal parameters and can only be accessed within the `displayDetails` method.

### Method Decomposition

Method decomposition is a programming technique where a complex problem is broken down into smaller, more manageable subproblems. Each subproblem is solved using a separate method. This approach promotes modularity and reusability.

For instance, consider the following example for calculating the area and perimeter of a rectangle:


```Java
public class RectangleOperations {
    public double calculateArea(double length, double width) {
        return length * width;
    }

    public double calculatePerimeter(double length, double width) {
        return 2 * (length + width);
    }

    public static void main(String[] args) {
        RectangleOperations operations = new RectangleOperations();
        System.out.println("Area: " + operations.calculateArea(5, 10));
        System.out.println("Perimeter: " + operations.calculatePerimeter(5, 10));
    }
}

RectangleOperations.main(null);
```

    Area: 50.0
    Perimeter: 30.0




## 5.9 this Keyword

## KEY LEARNING OBJECTIVE

Evaluate object reference expressions that use the keyword **this**.

The keyword "this" is utilized in Java to refer to the current instance of a class. In other words, it helps to clarify what variable you're referring to within the instance.


```java
public class MyClass {
    private int value;

    public void setValue(int value) {
        this.value = value; // 'this' refers to the instance variable
    }
}

```

QUESTION: **How can you use 'this' to call a constructor?**

You can call the constructor by saying this.(constructor) and then making a new instance, and then after, doing (constructorname).(function);

## 5.10 Ethical and Social Implications of Computing Systems

# KEY LEARNING OBJECTIVE

Explain the ethical and social implications of computing systems.

**Components of Ethical Implications**:

1. Legal issues and intellectual property are big concerns in program creation. Licensing open source software is a big issue, as it dictates how programmers need to comply with terms and how software can be distributed and used.


2. Data privacy is also a big issue. There are many data protection laws that programmers need to ensure that their code complies with, especially if their program works with data collection and processing.

**Components of Social Implications**:

1. There can be harmful impacts from software - malicious software can pose significant security threats.


2. Software has transformed how people communicate, access information, and interact with each other. Social media platforms, for example, have changed the way society discusses issues, while algorithms can create filter bubbles that limit exposure to diverse opinions.

**POPCORN HACKS: (0.2)**

**Write a two sentence reflection on the social and ethical implications of programming. (0.8)**

Programming holds many significant social and ethical implications, as it shapes our digital world. Programmers need to consider the consequences of their code on privacy, security, and public society, emphasizing the importance of ethics  in tech.
