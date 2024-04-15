---
title: Workshop 2 Hacks
description: Classes Workshop Hacks
toc: True
layout: post
type: hacks
comments: True
---

# Free Response Questions

## Question 1 - Pojos and Access Control:
Situation: The school librarian wants to create a program that stores all of the books within the library in a database and is used to manage their inventory of books available to the students. You decided to put your amazing code skills to work and help out the librarian!

a. Describe the key differences between the private and public access controllers and how it affects a POJO

The key differences between the private and public access controlers in Java is that Public allows for the widest possible accessability, while private restricts the accessability to the class itself. A public can be accessed from any class, even outside of the original class. Meanwhile, private objects can only be accessed from the class itself, not from outside. In a Plain Old Java Object (POJO), which is a simple Java object with private fields and public getters and setters, these access controllers play a large role. The fields of a POJO are typically declared private to encapsulate the data and prevent unauthorized access or modification. Public getters and setters are programmed to allow controlled access to these fields, following the principle of encapsulation in OOP.

b. Identify a scenario when you would use the private vs. public access controllers that isn't the one given in the scenario above

A scenario when I would use the private vs. public is banking. In a banking application, the balance of a bank account would be declared as a private field. This is because direct access to the balance should be restricted to prevent unauthorized modifications. Access to the balance is provided through public methods such as deposit() and withdraw() that enforce rules and validation.

c. Create a Book class that represents the following attributes about a book: title, author, date published, person holding the book and make sure that the objects are using a POJO, the proper getters and setters and are secure from any other modifications that the program makes later to the objects



```java
public class Book {
    private String title;
    private String author;
    private String datePublished;
    private String personHolding;

    // Constructor
    public Book(String title, String author, String datePublished) {
        this.title = title;
        this.author = author;
        this.datePublished = datePublished;
        this.personHolding = null; // Initially, no one is holding the book
    }

    // Getters
    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public String getDatePublished() {
        return datePublished;
    }

    public String getPersonHolding() {
        return personHolding;
    }

    // Setters
    public void setTitle(String title) {
        this.title = title;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public void setDatePublished(String datePublished) {
        this.datePublished = datePublished;
    }

    public void setPersonHolding(String personHolding) {
        this.personHolding = personHolding;
    }
}

// Testing
Book myBook = new Book("How to Eat Food", "Rachit Jaiswal", "March 22, 2024");
System.out.println(myBook.getAuthor()) // Output: Rachit Jaiswal
```

    Rachit Jaiswal


## Question 2 - Writing Classes:

(a) Describe the different features needed to create a class and what their purpose is.

Class Name: A unique identifier for the class, used to create objects of that class. It should start with a capital letter. cool

Attributes (Fields): Variables that hold the state of an object. They represent the properties of the object. wow

Constructor: A method used to initialize new objects. It has the same name as the class and can have parameters to set initial values for the attributes. 

Methods: Functions that define the behavior of the objects. They can be:

Accessor (Getter) Methods: Used to read the value of an attribute.
Mutator (Setter) Methods: Used to modify the value of an attribute.
Other methods: Used to perform various operations on the object's data.
Access Modifiers: Keywords like public, private, or protected that define the accessibility of the class, its constructors, attributes, and methods.

Encapsulation: The practice of keeping the attributes private and providing public getter and setter methods to access and modify the values. Look at FRQ #1. 

(b) Code:

Create a Java class BankAccount to represent a simple bank account. This class should have the following attributes:
- accountHolder (String): The name of the account holder.
balance (double): The current balance in the account.
Implement the following mutator (setter) methods for the BankAccount class:
- setAccountHolder(String name): Sets the name of the account holder.
- deposit(double amount): Deposits a given amount into the account.
- withdraw(double amount): Withdraws a given amount from the account, but only if the withdrawal amount is less than or equal to the current balance.
Ensure that the balance is never negative.


```java
public class BankAccount {
    private String accountHolder;
    private double balance;

    // Constructor
    public BankAccount(String accountHolder, double balance) {
        this.accountHolder = accountHolder;
        this.balance = balance;
    }

    // Getter methods
    public String getAccountHolder() {
        return accountHolder;
    }

    public double getBalance() {
        return balance;
    }

    // Setter method for accountHolder
    public void setAccountHolder(String accountHolder) {
        this.accountHolder = accountHolder;
    }

    // Method to deposit money
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    // Method to withdraw money
    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
        }
    }
}

// Testing
BankAccount account = new BankAccount("Rachit Jaiswal", 500);
// Depositing money into the account
account.deposit(100);
System.out.println("Current Balance: " + account.getBalance());
// Withdrawing money from the account
account.withdraw(200);
System.out.println("\nCurrent Balance after withdrawal: " + account.getBalance());
```

    Current Balance: 600.0
    
    Current Balance after withdrawal: 400.0


## Question 3 - Instantiation of a Class

(a) Explain how a constructor works, including when it runs and what generally is done within a constructor.

A constructor in Java is a special method that is called when an object is instantiated (created). It has the same name as the class and does not have a return type, not even void. The purpose of a constructor is to initialize the newly created object.

When a constructor runs:

- It runs automatically when a new object of the class is created using the new keyword.
- It can take parameters to initialize the object with specific values. If no parameters are provided, the default constructor is called.

Within a constructor, generally the attributes of the class are initialized with values. This can be done directly or through parameters passed to the constructor.

(b) Create an example of an overloaded constructor within a class. You must use at least three variables. Include the correct initialization of variables and correct headers for the constructor. Then, run the constructor at least twice with different variables and demonstrate that these two objects called different constructors. 


```java
public class Vehicle {
    private String make;
    private String model;
    private int year;

    // Default constructor
    public Vehicle() {
        this.make = "Unknown";
        this.model = "Unknown";
        this.year = 0;
    }

    // Overloaded constructor with two parameters
    public Vehicle(String make, String model) {
        this.make = make;
        this.model = model;
        this.year = 0; // Default value
    }

    // Overloaded constructor with three parameters
    public Vehicle(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    // Getters for demonstration purposes
    public String getMake() {
        return make;
    }

    public String getModel() {
        return model;
    }

    public int getYear() {
        return year;
    }
}

// Creating objects with different constructors
Vehicle vehicle1 = new Vehicle(); // Calls default constructor
Vehicle vehicle2 = new Vehicle("Toyota", "Camry"); // Calls constructor with two parameters
Vehicle vehicle3 = new Vehicle("Ford", "Mustang", 2020); // Calls constructor with three parameters

// Output to demonstrate different constructors were called
System.out.println("Vehicle 1: " + vehicle1.getMake() + " " + vehicle1.getModel() + " " + vehicle1.getYear());
System.out.println("Vehicle 2: " + vehicle2.getMake() + " " + vehicle2.getModel() + " " + vehicle2.getYear());
System.out.println("Vehicle 3: " + vehicle3.getMake() + " " + vehicle3.getModel() + " " + vehicle3.getYear());

```

    Vehicle 1: Unknown Unknown 0
    Vehicle 2: Toyota Camry 0
    Vehicle 3: Ford Mustang 2020


## Question 4 - Wrapper Classes:

(a) Provide a brief summary of what a wrapper class is and provide a small code block showing a basic example of a wrapper class.

A wrapper class in Java is a class that encapsulates a primitive data type (such as int, double, char, etc.) into an object. Wrapper classes are used to convert primitive types to objects, which is necessary when working with collections (like ArrayList, HashMap, etc.) that can only store objects.

(b) Create a Java wrapper class called Temperature to represent temperatures in Celsius. Your Temperature class should have the following features:

Fields:

A private double field to store the temperature value in Celsius.


Constructor:

A constructor that takes a double value representing the temperature in Celsius and initializes the field.


Methods:

getTemperature(): A method that returns the temperature value in Celsius.
setTemperature(double value): A method that sets a new temperature value in Celsius.
toFahrenheit(): A method that converts the temperature from Celsius to Fahrenheit and returns the result as a double value. 


```java
public class Temperature {
    private double celsius;

    // Constructor
    public Temperature(double celsius) {
        this.celsius = celsius;
    }

    // Getter for temperature in Celsius
    public double getTemperature() {
        return celsius;
    }

    // Setter for temperature in Celsius
    public void setTemperature(double celsius) {
        this.celsius = celsius;
    }

    // Method to convert Celsius to Fahrenheit
    public double toFahrenheit() {
        return (celsius * 9 / 5) + 32;
    }
}

// Usage
Temperature temp = new Temperature(25.0);
System.out.println("Temperature in Celsius: " + temp.getTemperature());
System.out.println("Temperature in Fahrenheit: " + temp.toFahrenheit());

temp.setTemperature(30.0);
System.out.println("New Temperature in Celsius: " + temp.getTemperature());
System.out.println("New Temperature in Fahrenheit: " + temp.toFahrenheit());
```

    Temperature in Celsius: 25.0
    Temperature in Fahrenheit: 77.0
    New Temperature in Celsius: 30.0
    New Temperature in Fahrenheit: 86.0


## Question 5 - Inheritence:

Situation: You are developing a program to manage a zoo, where various types of animals are kept in different enclosures. To streamline your code, you decide to use inheritance to model the relationships between different types of animals and their behaviors.

(a) Explain the concept of inheritance in Java. Provide an example scenario where inheritance is useful.

Inheritance in Java is where one class (the subclass or child class) to inherit the attributes and methods of another class (the superclass or parent class). This helps in code reusability and establishes a hierarchical relationship between classes. Consider FIRST Tech Challenge. In here, most teleop code has the same structure of `LinearOpMode`, and to keep that structure with all the initialization and constructors, we extend from `LinearOpMode` so that we do not have to work with the direct API for Andriod Devices running the REV Control Hub Software in every opmode. Another example of this is the `RobotHardware` class that we define in one class for setting all our motors, servos, and sensors up so that we do not have to do them in every class. 

(b) Code:

You need to implement a Java class hierarchy to represent different types of animals in the zoo. Create a superclass Animal with basic attributes and methods common to all animals, and at least three subclasses representing specific types of animals with additional attributes and methods. Include comments to explain your code, specifically how inheritance is used.



```java
// Superclass representing a general animal
class Animal {
    protected String name;
    protected int age;
    protected String habitat;

    public Animal(String name, int age, String habitat) {
        this.name = name;
        this.age = age;
        this.habitat = habitat;
    }

    // Common method to all animals
    public void eat() {
        System.out.println(name + " is eating.");
    }
}

// Subclass representing a specific type of animal - Lion
class Lion extends Animal {
    private int maneLength;

    public Lion(String name, int age, String habitat, int maneLength) {
        super(name, age, habitat); // Call to the superclass (Animal) constructor
        this.maneLength = maneLength;
    }

    // Specific method for Lion
    public void roar() {
        System.out.println(name + " is roaring.");
    }
}

// Subclass representing another specific type of animal - Elephant
class Elephant extends Animal {
    private double trunkLength;

    public Elephant(String name, int age, String habitat, double trunkLength) {
        super(name, age, habitat);
        this.trunkLength = trunkLength;
    }

    // Specific method for Elephant
    public void trumpet() {
        System.out.println(name + " is trumpeting.");
    }
}

// Subclass representing another specific type of animal - Penguin
class Penguin extends Animal {
    private boolean canSwim;

    public Penguin(String name, int age, String habitat, boolean canSwim) {
        super(name, age, habitat);
        this.canSwim = canSwim;
    }

    // Specific method for Penguin
    public void swim() {
        if (canSwim) {
            System.out.println(name + " is swimming.");
        } else {
            System.out.println(name + " cannot swim.");
        }
    }
}

// Usage
public class Zoo {
    public static void main(String[] args) {
        Lion lion = new Lion("Leo", 5, "Savannah", 10);
        Elephant elephant = new Elephant("Ella", 8, "Forest", 6.5);
        Penguin penguin = new Penguin("Penny", 3, "Arctic", false);

        lion.eat();
        lion.roar();

        elephant.eat();
        elephant.trumpet();

        penguin.eat();
        penguin.swim();
    }
}

Zoo.main(null);

```

    Leo is eating.
    Leo is roaring.
    Ella is eating.
    Ella is trumpeting.
    Penny is eating.
    Penny cannot swim.

