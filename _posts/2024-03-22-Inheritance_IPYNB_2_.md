---
title: Inheritance in APCSA (Unit 9)
toc: True
comments: True
layout: post
type: hacks
courses: {'csse': {'week': 1}, 'csp': {'week': 1, 'categories': ['4.A']}, 'csa': {'week': 0}, 'labnotebook': {'week': 3}}
---

## Review on Inheritance

### Basics of Inheritance:
- Superclass and Subclass: In Java, a superclass (or base class) is the class being inherited from, while a subclass (or derived class) is the class that inherits from the superclass.
- extends Keyword: To create a subclass, you use the `extends` keyword followed by the name of the superclass.


```Java
class SuperClass {
    //methods and fields  
}

class SubClass extends SuperClass {  
    //methods and fields  
}  
```

## 2022 FRQ Question 2

The Book class is used to store information about a book. A partial Book class definition is shown.



```Java
public class Book { 

    private String title; // The title of the book
    private double price; // The price of the book

    public Book(String bookTitle, double bookPrice) { // Creates a new Book with given title and price
        // implementation not shown
    } 

    public String getTitle() { // Returns the title of the book
        return title; 
    } 
    
    public String getBookInfo() { // Returns a string containing the title and price of the Book
        return title + "-" + price; 
    } 

    // There may be instance variables, constructors, and methods that are not shown.
} 
```


You will write a class Textbook, which is a subclass of Book. A Textbook has an edition number, which is a positive integer used to identify different versions of the
book. The getBookInfo method, when called on a Textbook, returns a string that also includes the edition information, as shown in the example.


Information about the book title and price must be maintained in the Book class. Information about the edition must be maintained in the Textbook class. The Textbook class contains an additional method, canSubstituteFor, which returns true if
a Textbook is a valid substitute for another Textbook and returns false otherwise. The current Textbook is a valid substitute for the Textbook referenced by the parameter of the canSubstituteFor method if the two Textbook objects have the same title and if the edition of the current Textbook is greater than or equal to the edition of the parameter.

## Point distribution

- Correctly make Class with header and extends - 2
- Calls super as the first line with the appropriate parameters - 1
- Declares appropriate private instance variable - 1
- Declares at least one required method and all declared headers are correct - 1
- getEdition returns value of instance variable - 1 
- canSubstituteFor determines whether true or false should be returned based on - 1 comparison of book titles and editions - 1
- getBookInfo calls super.getBookInfo - 1
- Constructs information string - 1


## Points to be careful on

- Point for declaring class correctly (always a point), Point for declaring a constructor, use meaningful variable names, ensure constructor is in correct order, constructor must call super as first line. 
- Title and Price must be maintained in the book class according to problem, so super has to be used. Edition is specific to textbook, means it should be private and has to be correctly initialized outside of the constructor. Sometimes you get point if you correctly write at least one correct method header. 
- Make sure you understand super! Super is a way to access the parent classes variables without using a constructor.

## Example solution


```Java
public class Textbook extends Book
{
    //private instance variable for edition number
    private int edition;

    //full constructor must have String, double, int matches the examples given in table
    public Textbook(String t, double p, int e)
    {
        //must be first: let Book manage its variables
        super(t, p);

        //instance variable on left, parameter on right
        this.edition = e;
    }

    //basic accessor method, note: only need getEdition because Book manages the others
    public int getEdition()
    {
        return edition;
    }

    //similar to toString: all data returned nicely formatted
    public String getBookInfo()
    {
        //need to use the method from Book to get the title and price, then concatenate the edition
        return super.getBookInfo() + "-" + edition;
    }

    //similar to equals: compare the two data pieces
    public boolean canSubstituteFor(Textbook other)
    {
        //titles are equals and edition is >= to other's
        return this.getTitle().equals(other.getTitle()) &&
        this.getEdition() >= other.getEdition();
    }
}
```

## Key Components

1. **Class Header**:
   - `public class Textbook extends Book`: Declares the class header.

2. **Instance Variable**:
    - `private int edition`: This variable stores the edition number of the textbook.

3. **Constructor**:
    - `public Textbook(String t, double p, int e)`: This is the constructor method for the `Textbook` class. It takes three parameters: a `String` for the title (`t`), a `double` for the price (`p`), and an `int` for the edition (`e`)
    - It initializes the instance variables of the `Textbook` class using the `super` keyword to call the constructor of the superclass `Book`, passing the title and price
    - Then, it sets the `edition` instance variable to the value provided.

4. **Accessor Method**:
    - `public int getEdition()`: This method returns the edition number of the textbook.

5. **Other Methods**:
    - `public String getBookInfo()`: This method returns a string containing information about the textbook
    - It calls the `getBookInfo()` method of the superclass `Book` to get the title and price, and then appends the edition number to it.
    - `public boolean canSubstituteFor(Textbook other)`: This method checks if the current textbook can substitute another textbook (`other`)
      - It returns `true` if the titles are equal and if the edition of the current textbook is greater than or equal to the edition of the other textbook.
  


### ** It is not required to include a main method in the code as not required by scoring guidelines **

## Common Mistakes

1. **Misunderstanding the Problem**
- Not fully understanding the requirements given in the problem can lead to incorrect solutions or implementations.

2. **Incomplete Implementation**
- Forgetting to implement all necessary methods or attributes as per the requirements of the problem.

3. **Misinterpreting Method Overrides**
- Incorrectly overriding methods from the superclass in subclasses, leading to unexpected behavior.

4. **Ignoring Access Modifiers**
- Forgetting to consider access modifiers like public, private, and protected, which can result in errors in accessing or modifying variables and methods.
    - public: Accessible by any class.
    - protected: Accessible within the same package and subclasses.
    - private: Not inherited, not accessible.
    - default (no modifier): Accessible within the same package.

5. **Failure to Call Superclass Constructors**
- Forgetting to call constructors of the superclass in subclasses can lead to uninitialized variables or incorrect behavior of inherited attributes.

## Hacks
### Inheritance (Unit 9)

Situation: You are developing a program to manage a zoo, where various types of animals are kept in different enclosures. To streamline your code, you decide to use inheritance to model the relationships between different types of animals and their behaviors.

(a) Explain the concept of inheritance in Java. Provide an example scenario where inheritance is useful.

(b) Code:

You need to implement a Java class hierarchy to represent different types of animals in the zoo. Create a superclass `Animal` with basic attributes and methods common to all animals, and at least three subclasses representing specific types of animals with additional attributes and methods. Include comments to explain your code, specifically how inheritance is used.
