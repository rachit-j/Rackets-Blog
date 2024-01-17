---
layout: post
title: HashMap
toc: True
comments: True
description: Lesson by Shaurya, James, and Shivansh
courses: {'labnotebook': {'week': 16}}
type: hacks
---

# Key Concepts 
**Directions: Fill in the blanks, this is a Popcorn HACK**

## Hashing
- HashMap uses a hash function to map keys to their respective buckets .
- A good hash function generates a unique hash code for each key, but collision can still occur. (same hash code)
- The hash map in Java does not maintain insertion order.

## Performance

- HashMap provides constant-time performance (O(1)) for get() and put() operations.
- Performance can degrade to O(n) in the worst case, especially if there are many hash collisions.

## Key and Value Types

- HashMap allows any non-null object as a key and any object (including null) as a value.
- For a class to be used as a key, it must implement the get and put methods.

## Iteration:

- HashMap provides methods like keySet(), values(), and entrySet() for iterating over key-value pairs.
- The entrySet() method returns a Set view of key-value pairs, allowing iteration and modification.

## Thread Safety

- HashMap is not thread-safe. For thread-safe operations, use ConcurrentHashMap.


# What is HashMap
A HashMap store items in "key/value" pairs, and you can access them by an index of another type (e.g. a String).

One object is used as a key (index) to another object (value). It can store different types: String keys and Integer values, or the same type, like: String keys and String values:


## Creating HashMap in Java



```java
import java.util.HashMap; // import the HashMap class

public class CreateHashMap{
    public static void main(String[] args){
        // Generating the HashMap
    HashMap<String, String> capitalCities = new HashMap<String, String>();
    // Adding key/value pairs tothe HashMap to store
            capitalCities.put("America", "D.C");
            capitalCities.put("Germany", "Berlin");
            capitalCities.put("United Kingdom", "London");
            capitalCities.put("India", "Delhi");
            capitalCities.put("Afghanistan", "Delhi");
            capitalCities.put("Bangladesh", "Dhaka");
            
            System.out.println("Successfully created a HashMap which stores items in key/value pairs");
    }
}

CreateHashMap.main(null);


```

    Successfully created a HashMap which stores items in key/value pairs


# Methods in HashMap


```java

import java.util.HashMap;
 
public class ExampleHashMap {
      public static void main(String[] args) {
       
      // Create a HashMap
      HashMap<String, Integer> hashMap = new HashMap<>();
       
      // Add elements to the HashMap
      hashMap.put("Shivansh", 25);
      hashMap.put("Shaurya", 30);
      hashMap.put("Patrick Mahomes", 28);
      hashMap.put("Travis Kelce", 34);
      hashMap.put("Tom Brady", 46);
       
      // HashMap put() method in Java (Access elements in the HashMap)
      System.out.println(hashMap.get("Shivansh")); 

      // HashMap remove() method in Java (Remove an element from the HashMap)
      hashMap.remove("Tom Brady");
       
      // HashMap size() method in Java (Get the size of the HashMap)
      System.out.println(hashMap.size()); 

      // HashMap entrySet() method in Java (Get the Entry Set)
      System.out.println("The set is: " + hashMap.entrySet()); 

      // HashMap containsKey() method in Java (check whether a particular key is being mapped into the HashMap or not)
      System.out.println("Is the key 'Shivansh' present? " + hashMap.containsKey("Shivansh"));
      
      
   }
}
ExampleHashMap.main(null);
```

    25
    4
    The set is: [Travis Kelce=34, Shivansh=25, Shaurya=30, Patrick Mahomes=28]
    Is the key 'Shivansh' present? true


### Popcorn Hack 1
Declare a Hashmap, and then research 5 different HashMap method which were not listed above and use them in your code just like the one above.


```java
import java.util.HashMap;
public class MyHashMap{
public static void main(String[] args){
    HashMap<Integer, String> my_map = new HashMap<>();
    my_map.put(1, "Rachit");
    my_map.put(2, "Paaras");
    my_map.put(3, "Tej");

    boolean empty = my_map.isEmpty();

    boolean contains = my_map.containsValue(6);

    Set<Integer> keys = my_map.keySet();

    Collection<String> values = my_map.values();

    

    System.out.println("Is the map empty? " + my_map.isEmpty());
    System.out.println("Does the map contain the value 6? " + my_map.containsValue(6));
    System.out.println("Returning all keys! "+ my_map.keySet());
    System.out.println("Returning all values! " + my_map.values());
    System.out.println("Clearing!");

    my_map.clear();

}
}
MyHashMap.main(null);
```

    Is the map empty? false
    Does the map contain the value 6? false
    Returning all keys! [1, 2, 3]
    Returning all values! [Rachit, Paaras, Tej]
    Clearing!


# Traversing through HashMap

In the code below, hash_map.entrySet() is used to return a set view of the mapped elements. Now, getValue() and getKey() functions, key-value pairs can be iterated.


```java
import java.util.HashMap;
public class TraverseHashMap{
public static void main(String[] args){
   // Week 15 NFL Quarterback Rankings
   HashMap<Integer, String> hash_map = new HashMap<>();
   hash_map.put(1, "Jalen Hurts");
   hash_map.put(2, "Dak Prescott");
   hash_map.put(3, "Josh Allen");
   hash_map.put(4, "Lamar Jackson");
   hash_map.put(5, "Brock Purdy");
    for (Map.Entry<Integer, String> set : hash_map.entrySet()) {
        System.out.println(set.getKey() + " = " + set.getValue());
    }
}
}
TraverseHashMap.main(null);


```

    1 = Jalen Hurts
    2 = Dak Prescott
    3 = Josh Allen
    4 = Lamar Jackson
    5 = Brock Purdy


### Popcorn Hack 2 (Extra Credit)
Try to find a different way to traverse a HashMap (Hint: try using a forEach function)


```java
import java.util.HashMap;
import java.util.Map;

public class HashMapTraversal {
    public static void main(String[] args) {
        // Create a HashMap with some key-value pairs
        HashMap<String, Integer> ageMap = new HashMap<>();
        ageMap.put("Alice", 25);
        ageMap.put("Bob", 30);
        ageMap.put("Charlie", 35);
        ageMap.put("David", 40);

        // Iterate over the HashMap using a for-each loop
        for (Map.Entry<String, Integer> entry : ageMap.entrySet()) {
            String name = entry.getKey();
            int age = entry.getValue();
            System.out.println(name + " is " + age + " years old.");
        }
    }
}
HashMapTraversal.main(null);
```

    Bob is 30 years old.
    Alice is 25 years old.
    Charlie is 35 years old.
    David is 40 years old.


# HashMaps in Java - Pet Registry Example 


```java
public class Pet {
    private final String name;
    private final int age;
    private final String color;

    public Pet(String name, int age, String color) {
        this.name = name;
        this.age = age;
        this.color = color;
    }

    public String getName() {
        return this.name;
    }

    public int getAge() {
        return this.age;
    }

    public String getColor() {
        return this.color;
    }
}

```


```java
public class PetsRegistry {
    
    private HashMap<String, Pet> petRegistry = new HashMap<>(); // declares a private HashMap instance variable petRegistry
    // Key Type String and Value Type Pet

    public PetsRegistry() {
        // Add some pets to the registry
        petRegistry.put("Leo", new Pet("Lion", 8, "Gold"));
        petRegistry.put("Porky", new Pet("Pig", 3, "Pink"));
        petRegistry.put("Ro-Ro", new Pet("Robin", 7, "Red"));
        petRegistry.put("Midnight", new Pet("Cat", 10, "Black"));
        petRegistry.put("Hobbes", new Pet("Kitty", 1, "Calico"));
        petRegistry.put("Duke", new Pet("Dog", 14, "Brown"));
    }

    public Pet removePet(String name) {
        // Remove a pet by name
        return petRegistry.remove(name);
    }

    public void printRegistry() {
        // Iterate over the registry and print pet information
        for (String name : petRegistry.keySet()) { // for each loop
            Pet pet = petRegistry.get(name);
            System.out.println(name + " is a " + pet.getColor() + " " + pet.getName() +
                    " and is " + pet.getAge() + " years old.");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // Initialize the pet registry
        PetsRegistry petsRegistry = new PetsRegistry();
        petsRegistry.printRegistry();

        // Remove a pet
        String petNameToRemove = "Hobbes";
        Pet removedPet = petsRegistry.removePet(petNameToRemove);
        if (removedPet == null) {
            System.out.println(petNameToRemove + " not found");
        } else {
            System.out.println("Removed: " + petNameToRemove + ", " + removedPet);
        }

        // Print the updated registry
        petsRegistry.printRegistry();
    }
}
PetsRegistry.main(null)
```

    Hobbes is a Calico Kitty and is 1 years old.
    Leo is a Gold Lion and is 8 years old.
    Porky is a Pink Pig and is 3 years old.
    Ro-Ro is a Red Robin and is 7 years old.
    Duke is a Brown Dog and is 14 years old.
    Midnight is a Black Cat and is 10 years old.
    
    Removed: Hobbes, REPL.$JShell$13$Pet@41a890b3
    Leo is a Gold Lion and is 8 years old.
    Porky is a Pink Pig and is 3 years old.
    Ro-Ro is a Red Robin and is 7 years old.
    Duke is a Brown Dog and is 14 years old.
    Midnight is a Black Cat and is 10 years old.
    


# Popcorn HACK 3 (Shaurya)


```java
import java.util.HashMap;
import java.util.Map;

public class HashMapTest {
    public static void main(String[] args) {
        // Create a new HashMap with Integer keys and String values
        Map<Integer, String> myMap = new HashMap<>();

        // Add some key-value pairs to the HashMap
        myMap.put(1, "Apple");
        myMap.put(2, "Banana");
        myMap.put(3, "Cherry");

        // Fill in the blanks: Retrieve and print the value for key 2
        String valueForKey2 = myMap.get(2);
        System.out.println("Value for key 2: " + valueForKey2);

        // Fill in the blanks: Check if the HashMap contains key 4
        boolean containsKey4 = myMap.containsKey(4);
        System.out.println("Does the map contain key 4? " + containsKey4);

        // Fill in the blanks: Remove the entry with key 1 from the HashMap
        myMap.remove(1);

        // Print the updated contents of the HashMap
        System.out.println("Updated HashMap:");
        for (Map.Entry<Integer, String> entry : myMap.entrySet()) {
            System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
        }
    }
}
HashMapTest.main(null);

```

    Value for key 2: Banana
    Does the map contain key 4? false
    Updated HashMap:
    Key: 2, Value: Banana
    Key: 3, Value: Cherry


# Popcorn HACK 4 - Quiz (Shaurya)

## Multiple Choice:

### Question 1: Hashing in HashMap

What is the primary purpose of a hash function in a HashMap?

- A) To encrypt the keys
**- B) To map keys to corresponding buckets (CORRECT ANSWER)**
- C) To validate the keys
- D) To generate random numbers

### Question 2: Performance of HashMap

What is the time complexity of the get() and put() operations in a well-distributed HashMap?

- A) O(log n)
- B) O(n)
**- C) O(1) (CORRECT ANSWER)**
- D) O(n^2)

## Free Response:

### Question 3: Key and Value Types in HashMap

Describe the types of objects that can be used as keys and values in a HashMap. Additionally, explain the methods that a class should implement if used as a key.

Any object can be used as a key in a HashMap. Key objects should be immutable and implement hashCode() and equals() methods consistently. The hashCode() method is used to find the bucket location, and equals() is used to find the correct key-value pair within the bucket. HashMap can store any type of objects as values. There are no specific requirements for value objects.


### Question 4: Iteration in HashMap

Provide brief explanations for two methods in HashMap that can be used to iterate over its key-value pairs.

- entrySet(): This method returns a Set view of the mappings contained in the HashMap. It can be used to iterate over key-value pairs. Each element in this set is a Map.Entry object.
- keySet(): This method returns a Set view of the keys contained in the HashMap. It is used to iterate over keys. After getting a key, you can get its corresponding value from the HashMap.

### Question 5: Thread Safety in HashMap

Explain why HashMap is not thread-safe and what issues might arise when multiple threads access the same HashMap instance concurrently. Suggest an alternative class that can be used for concurrent access and explain its benefits.

HashMap is not thread-safe because it does not synchronize the methods that modify its structure (like put() and remove()). Concurrent access by multiple threads can lead to data corruption, such as lost updates or even infinite loops in the bucket chain.
An alternative for concurrent access is ConcurrentHashMap. It allows concurrent access to different segments of the map, reducing contention and improving performance. ConcurrentHashMap uses lock striping to control access to segments of the map, making it a better choice for multi-threaded environments. (Don't make me google this stuff plz lock stripping is cool though)

# HACKS (Shaurya)

1) Finish Popcorn HACKS
2) Develop a Java application that utilizes a HashMap to manage a sports team roster. Each player on the team should have attributes like name, position, and jersey number. The program should enable functionalities such as adding new players, updating player information, and searching for players based on their jersey numbers using the HashMap implementation.
3) Reflection (4-5 sentences):

A HashMap in Java is a fast and practical way to store and manage data using key-value pairs. It allows quick data retrieval, which is great for applications needing rapid access to information. However, its performance can suffer if the hash function isn't good or if used in multi-threaded environments without proper handling. Overall, HashMap is a popular choice in Java for its speed and ease of use in many programming scenarios.


```java
import java.util.HashMap;
import java.util.Map;


public class Player {
    private String name;
    private String position;
    private int jerseyNumber;

    public Player(String name, String position, int jerseyNumber) {
        this.name = name;
        this.position = position;
        this.jerseyNumber = jerseyNumber;
    }

    // Getters and Setters
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }

    public int getJerseyNumber() {
        return jerseyNumber;
    }

    public void setJerseyNumber(int jerseyNumber) {
        this.jerseyNumber = jerseyNumber;
    }

    @Override
    public String toString() {
        return "Player{" +
                "name='" + name + '\'' +
                ", position='" + position + '\'' +
                ", jerseyNumber=" + jerseyNumber +
                '}';
    }
}
import java.util.HashMap;
import java.util.Map;

public class TeamRoster {
    private Map<Integer, Player> roster;

    public TeamRoster() {
        roster = new HashMap<>();
    }

    public void addPlayer(Player player) {
        roster.put(player.getJerseyNumber(), player);
    }

    public void updatePlayer(int jerseyNumber, Player player) {
        roster.put(jerseyNumber, player);
    }

    public Player getPlayer(int jerseyNumber) {
        return roster.get(jerseyNumber);
    }

    public void printRoster() {
        for (Player player : roster.values()) {
            System.out.println(player);
        }
    }

    // Main method for demonstration
    public static void main(String[] args) {
        TeamRoster team = new TeamRoster();

        // Adding players
        team.addPlayer(new Player("John Doe", "Forward", 9));
        team.addPlayer(new Player("Jane Smith", "Goalkeeper", 1));

        // Updating a player's information
        Player updatedPlayer = new Player("John Doe", "Midfielder", 9);
        team.updatePlayer(9, updatedPlayer);

        // Searching for a player
        Player player = team.getPlayer(9);
        System.out.println("Searched Player: " + player);

        // Printing the entire team roster
        System.out.println("Complete Team Roster:");
        team.printRoster();
    }
}
TeamRoster.main(null);
```

    Searched Player: Player{name='John Doe', position='Midfielder', jerseyNumber=9}
    Complete Team Roster:
    Player{name='Jane Smith', position='Goalkeeper', jerseyNumber=1}
    Player{name='John Doe', position='Midfielder', jerseyNumber=9}




## Lesson: Collections in Java and SQL

### Introduction to Collections in Java
In Java, the `Collection` interface is a member of the Java Collections Framework and extends the `Iterable` interface. It includes methods for basic operations (such as `add`, `remove`, `clear`), bulk operations (such as `containsAll`, `addAll`, `retainAll`, `removeAll`), and array operations (such as `toArray`).



```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Creating an ArrayList
        List<String> list = new ArrayList<String>();
        // Adding elements to the list
        list.add("Apple");
        list.add("Banana");
        list.add("Cherry");
        System.out.println("List: " + list);
    }
}
```

### Definition of Collections
In the context of SQL, collections refer to a group of related data items that can be treated as a whole. Common types of collections include arrays, lists, and sets.

### Using Collections with SQL
When working with databases in Java, you can use the `java.sql`` package. This package provides classes for connecting to a database and executing SQL queries.


```java
import java.sql.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/mydatabase";
        String user = "root";
        String password = "password";

        try {
            Connection conn = DriverManager.getConnection(url, user, password);
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM mytable");

            // Creating a list to store the results
            List<String> results = new ArrayList<String>();
            while (rs.next()) {
                results.add(rs.getString("mycolumn"));
            }
            System.out.println("Results: " + results);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```

In this code, we’re connecting to a MySQL database and executing a SQL query. The results of the query are then stored in an ArrayList

### `Purpose of Collections`
Collections are useful in a database because they allow you to store multiple values in a single column. This can be beneficial in scenarios where you have a one-to-many relationship. For example, a single product could have multiple colors, sizes, or other attributes.

#### `Important terminology`
- Elements: Individual items within a collection.
- Indexes: The position of an element within a collection.
- Scalar: A single value, as opposed to a collection which can hold multiple values.

## Advanced usage in Collections

### Nested Collections
Collections can be nested, creating a collection of collections, for more freeform control, such as representing a 2D map with a 2D array.


```java
public class NestedArrays {
    public static void print2Darray(int[][] arr){
        // function for printing arrays
        for (int i=0;i<arr.length;i++){
            for (int j=0;j<arr[i].length;j++){
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }
    }
    public static void main(String[] args){
        // Direct declaration of an array containing arrays
        int[][] arr = {
            {8,1,6},
            {3,5,7},
            {4,9,2}
        };
        print2Darray(arr);
        System.out.println(arr[1][2]);//printing the value at [1][2] (7)
        arr[1][2] = 0; //assigning a new value to inside the 2D array
        System.out.println(arr[1][2]);
    }
}
NestedArrays.main(null);
```

### Popcorn hacks
Create a program that sums the columns and the rows of the given nested array (should all be 15), then create a copy of the original array by looping through the original array and assigning the values to a new array.


```java
public class NestedArraysPopcorn {
    public static void print2Darray(int[][] arr) {
        // function for printing arrays
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int[][] arr = {
            {8, 1, 6},
            {3, 5, 7},
            {4, 9, 2}
        };

        // Calculate the sums of rows and columns
        int[] rowSums = new int[arr.length];
        int[] colSums = new int[arr[0].length];

        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                rowSums[i] += arr[i][j];
                colSums[j] += arr[i][j];
            }
        }

        // Print the sums
        System.out.println("Row sums:");
        for (int sum : rowSums) {
            System.out.println(sum);
        }

        System.out.println("Column sums:");
        for (int sum : colSums) {
            System.out.println(sum);
        }

        // Create a copy of the original array
        int[][] arrCopy = new int[arr.length][arr[0].length];
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                arrCopy[i][j] = arr[i][j];
            }
        }

        // Print the copied array
        System.out.println("Copied Array:");
        print2Darray(arrCopy);
    }
}

NestedArraysPopcorn.main(null);
```

    Row sums:
    15
    15
    15
    Column sums:
    15
    15
    15
    Copied Array:
    8 1 6 
    3 5 7 
    4 9 2 


### Null values in collections
null values are placeholders that are implemented when there is not any value that is inputed, you see it when we call the main method in our programs. It is automatically created when a new reference variable (such as an Integer) is created but no values have been assigned to it yet. It can also be created directly.

Having null values in a collection will not immediately crash the program, however, it can cause a NullPointerException error if it is used carelessly. So it is important to learn how to identify and filter it.


```java
import java.util.ArrayList;
public class NullValuesInArray {
    public static void main(String[] args){
        Integer[] arr = new Integer[10];//array of Integer
        System.out.println(arr[3]);
        // if the following line of code is ran, it will return a NullPointerException error
        //System.out.println(1+arr[2]);
        for (int i=0;i<arr.length;i++){
            arr[i]=0;// sets the values in the arr to 0
        }
        System.out.println(1+arr[2]);
    }
}
NullValuesInArray.main(null);//using null values in the main method
```

### Popcorn hacks
The given array has certain values set to null, loop through to set all null values to 0, then sum every value in the array.


```java
import java.util.ArrayList;

public class NullValuesInArrayPopcorn {
    public static void main(String[] args) {
        Integer[] arr = { 4, 5, 6, null, 9, 10, null, 9, 3, 2, 5, null };

        // Replace null values with 0
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == null) {
                arr[i] = 0;
            }
        }

        // Calculate the sum of all values in the array
        int sum = 0;
        for (Integer value : arr) {
            sum += value;
        }

        // Print the updated array and the sum
        System.out.println("Updated Array:");
        for (Integer value : arr) {
            System.out.print(value + " ");
        }
        System.out.println("\nSum of all values: " + sum);
    }
}

NullValuesInArrayPopcorn.main(null);
```

    Updated Array:
    4 5 6 0 9 10 0 9 3 2 5 0 
    Sum of all values: 53


### Performance and Complexities
All of the functions used in collections takes a certain time complexity to do, and it may be sometimes better to use one value over the other.
Here are some time complexities for commonly used methods

|Method|Time Complexity|
|-|-|
|Initialization|O(n)|
|Accessing (arr[i] get(i))|O(1)|
|Assignment (arr[i]=a, set(i,a))|O(1)|
|Sorting (Array.sort(arr), sort(Comparator))|O(nlog(n))|
|Length (length, size())|O(1)|
|copy (clone(), arraycopy())|O(n)|

The space complexity of a collection is its size.

Most of the time, the array is a versatile tool that can effeciently store and process values, however, sometimes we would want a different requirement. For example, when we want a storage to always be sorted, while we could use some sort of binary search method to find the best position to insert a value, there are just data structures, such as TreeSet, that maintains sorted status upon insertion. It's important to use the data structure that best suits your need in the right context.

### Real world applications of Collections
In the context of an application or a database, a collection can allow for large amounts of values to be stored efficiently without creating large amounts of variables, storing what's usually a column of information in a single cell (I guess then, then that's also a collection of collection in of itself). It can be used for when you don't know how long that a list can be, you can modify the values in a collection easily also. However, the usage of many collections can add a lot of unnecessary weight on the database due to the extra spaces used, and it can be hard to keep track of what functions should be used for modifying certain values in a collection.

# Usage of Collections in SQL
In SQL, collections are powerful data types that allow us to store multiple values. Let's delve into declaring different types of collections.


```java
-- Syntax for declaring an array
DECLARE TYPE Array_Type IS VARRAY(5) OF VARCHAR2(50);

-- Syntax for declaring a nested table
DECLARE TYPE Nested_Table_Type IS TABLE OF NUMBER;

-- Syntax for declaring an associative array
DECLARE TYPE Assoc_Array_Type IS TABLE OF VARCHAR2(50) INDEX BY PLS_INTEGER;
```

### Explanation: 
In SQL, we can declare different types of collections to store multiple values. An array is defined with a fixed size of 5, specifically designed to accommodate VARCHAR2 values. Simultaneously, a nested table is declared to store numeric values, offering flexibility in handling numerical data. Additionally, an associative array is declared with an index of PLS_INTEGER, providing a dynamic structure to hold VARCHAR2 values based on the specified index. These declarations showcase the versatility of collections in SQL, allowing for efficient management of various data types.

## Initialization of Collections
Now, let's initialize these collections using different methods.


```java
-- Initializing an array
DECLARE
  my_array Array_Type := Array_Type('Value1', 'Value2', 'Value3');

-- Initializing a nested table
DECLARE
  my_table Nested_Table_Type := Nested_Table_Type(1, 2, 3);

-- Initializing an associative array
DECLARE
  my_assoc_array Assoc_Array_Type;
BEGIN
  my_assoc_array(1) := 'Item1';
  my_assoc_array(2) := 'Item2';
END;
```

### Explanation: 

In the initialization phase, the array is populated with predefined values using its constructor, ensuring specific elements are set from the start. Meanwhile, the nested table is initialized with numeric values, establishing its initial content based on numerical data. In contrast, the associative array takes a more dynamic approach, as values are individually assigned within a BEGIN-END block, allowing for flexible and tailored initialization based on specific requirements or conditions.

## Adding, Removing, and Modifying Elements
Now, let's explore how to perform fundamental operations on collections.


```java
-- Adding elements to an array
my_array.EXTEND;
my_array(4) := 'Value4';

-- Removing elements from a nested table
my_table.DELETE(2);

-- Modifying an element in an associative array
my_assoc_array(1) := 'UpdatedItem';
```

### Explanation:

In this sequence of operations, the array undergoes extension to accommodate a new element, subsequently being assigned a specific value. Simultaneously, within the nested table, an element is removed. Additionally, in the associative array, a specific element undergoes modification, ensuring the dynamic adaptability of the collection to evolving data requirements.

## Common Operations
Explore common operations like appending, deleting, and checking for element existence.


```java
-- Appending elements to an array
my_array := my_array MULTISET UNION Array_Type('Value5', 'Value6');

-- Deleting all elements from a nested table
my_table := Nested_Table_Type();

-- Checking if an element exists in an associative array
IF my_assoc_array.EXISTS(1) THEN
  -- Do something
END IF;
```

### Explanation:

In the realm of SQL collections, various operations enhance their functionality. To enrich an array, additional elements can be seamlessly appended, ensuring dynamic and evolving data storage. For a nested table, a clean slate is achieved by effortlessly deleting all existing elements, offering a quick and efficient reset. The power of the EXISTS function comes into play with associative arrays, providing a means to verify the existence of a specific index, adding a layer of control and precision to the data management process.

## Incorporating Collections in SQL Queries
Now, let's leverage collections in SQL queries for more flexible and dynamic operations.


```java
-- Using an array in a SELECT statement
SELECT * FROM employees WHERE employee_id IN (SELECT * FROM TABLE(my_array));

-- Using a nested table in a JOIN operation
SELECT e.employee_id, e.employee_name, d.department_name
FROM employees e
JOIN TABLE(my_table) t ON e.department_id = t.COLUMN_VALUE;

-- Using an associative array in a WHERE clause
FOR i IN 1..my_assoc_array.LIMIT
LOOP
```

### Explanation:

In SQL queries, the array serves as a filtering mechanism within the SELECT statement, allowing for precise record retrieval. In JOIN operations, a nested table is harnessed to establish correlations between datasets, facilitating a more comprehensive analysis. Additionally, the versatility of associative arrays shines as they are seamlessly integrated into loops, enabling efficient iteration through their elements. This concise yet powerful utilization of collections enhances the flexibility and dynamism of SQL queries, showcasing their utility in various scenarios.

# Hacks:
Replaced with PERIOD 1:
- Using the [Person](https://github.com/Tirth-Thakkar/LessonBackend/tree/master/src/main/java/com/nighthawk/spring_portfolio/mvc/person) object as inspiration, create your own UNIQUE SQL database with at least 3 object entries that incorporates either a "many-to-many" relationship with another object (hint: Person and PersonRole) OR uses the JSONB column definition to store more complex data (such as a HashMap) as an attribute (hint: stats in Person object).
    - Show a clear screenshot of your SQLite table (using SQLite viewer) on your blog for credit.
    - Using past group project materials is valid for this homework as long as the expectations are met.

### Ideas for 1.0/1.0

- Incorporating both a "many-to-many" relationship and a JSONB column with information would be great.
- Implementing JPA repository methods (think CRUD methods, custom queries, etc.) would show interest in modifying SQL database data.
- Take extra notes on this lesson that show deeper research into Collections and SQL.


![HELP ME](/Rackets-Blog/images/goofball.png)
