---
layout: post
title: Unit 5 Part 1
toc: True
comments: True
description: Lesson for APCSA Unit 5
courses: {'csa': {'week': 9}, 'labnotebook': {'week': 9}}
type: tangibles
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

It makes sure that the list cannot be damaged and it forces the program to make a copy of the list so that the original list is not changed, but can still be referenced for duplication to make other instances of objects. 

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

