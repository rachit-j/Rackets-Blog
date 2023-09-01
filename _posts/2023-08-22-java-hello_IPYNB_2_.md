---
toc: True
comments: True
layout: post
title: Java Hello
description: The complete Hack of the section Java. This page is also saved in a jupyter notebook.
type: hacks
courses: {'csse': {'week': 1}, 'csp': {'week': 1, 'categories': ['4.A']}, 'csa': {'week': 0}, 'labnotebook': {'week': 1}}
categories: ['C1.4']
---

### Java Notebook - Java Hello

#### Understanding Classes

<div style="text-align: center;">   
    <img src="/Rackets-Blog/images/java_class_diagram.png" alt="drawing" width="800" style="border-radius: 20%;"/>
</div>

#### My Class Code
The following code aims to create a class to record major cities, their prominent zip code, and their state. The class can be modified and data can be recieved. For the criteria of the hack, the comments and the following explanations will go through the CollegeBoard Criteria. 


```java
// Define a class
public class CityInfo {
    private String name;
    private int zip;
    private String state;

    // Constructor 1 -- No-argument constructor
    public CityInfo() {
        this.name = "";
        this.zip = 0;
        this.state = "";
    }

    // Constructor 2
    public CityInfo(String name, int zip, String state) {
        this.name = name;
        this.zip = zip;
        this.state = state;
    }

    // Setters
    public void setName(String newName) {
        this.name = newName;
    }
    public void setzip(int newzip) {
        this.zip = newzip;
    }
    public void setstate(String newstate) {
        this.state = newstate;
    }

    // Getters
    public String getName() {
        return this.name;
    }
    public int getzip() {
        return this.zip;
    }
    public String getstate() {
        return this.state;
    }

    public static void main(String[] args) {
        System.out.println("Starting the program");

        // new instance of class
        CityInfo san_diego = new CityInfo();
        san_diego.setName("San Diego");
        san_diego.setstate("California");
        san_diego.setzip(92154);

        // Using Parameterized Constructor
        CityInfo denver = new CityInfo("Denver", 80219, "Colorado");
        CityInfo phoenix = new CityInfo("Phoenix", 85001, "Arizona");
        CityInfo augusta = new CityInfo("Augusta", 04330, "Maine");
        CityInfo boston = new CityInfo("Boston", 02201, "Massachusetts");
        CityInfo jackson = new CityInfo("Jackson", 39205, "Mississippi");

        // Print Statements
        System.out.println("Key: City | Zip | State");
        System.out.println(san_diego.getName() + " | " + san_diego.getzip() + " | " + san_diego.getstate());
        System.out.println(denver.getName() + " | " + denver.getzip() + " | " + denver.getstate());
        System.out.println(phoenix.getName() + " | " + phoenix.getzip() + " | " + phoenix.getstate());
        System.out.println(augusta.getName() + " | " + augusta.getzip() + " | " + augusta.getstate());
        System.out.println(boston.getName() + " | " + boston.getzip() + " | " + boston.getstate());
        System.out.println(jackson.getName() + " | " + jackson.getzip() + " | " + jackson.getstate());
    }
}


```

### The Hack

Essentially, we do the same thing as the above but we make it simpler and easier to demonstrate


```java
CityInfo.main(null);
```

    Starting the program
    Key: City | Zip | State
    San Diego | 92154 | 
    Denver | 80219 | Colorado
    Phoenix | 85001 | Arizona
    Augusta | 2264 | Maine
    Boston | 1153 | Massachusetts
    Jackson | 39205 | Mississippi


Lets Say I wanted to dynamically change something. All I would have to do is change the value of the item!


```java
denver.setstate("California")
```


```java
denver.getstate();
```




    California


