---

---

Why would we want to do this? Answer the question in this cell.

<details>
<summary>Answer</summary>
<br>
These classes convert primitive data types (int/double) to a reference data type (object). We convert these because different data structures in java require different types of variables, some of which are only objects. By parsing the values of the primitive data to an object, we can send values to methods and structures that only take object values, like ArrayList, for example. 
</details>

#### The integer Wrapper Class
The Integer class in Java is a wrapper class for the primitive data type int. It provides several methods that can be used to perform operations on int values. The constructor looks like this:


```Java
Integer(int value)
```

An example of this running is:


```Java
Integer hungerRating = new Integer(5); // Send to an Object
int hungerRatingNum = hungerRating.intValue(); // Turn back into a primitive
```

An example of it being utilized is:


```Java
ArrayList<int> list = new ArrayList<int>();  // This will cause a compile-time error
```


    |   ArrayList<int> list = new ArrayList<int>();  // This will cause a compile-time error

    unexpected type

      required: reference

      found:    int

    

    |   ArrayList<int> list = new ArrayList<int>();  // This will cause a compile-time error

    unexpected type

      required: reference

      found:    int

    


The above code will not work because ArrayList requires on object type, while we are passing a primitive type.


```Java
ArrayList<Integer> list = new ArrayList<Integer>();
list.add(5);  // Autoboxing will automatically convert the int 5 to an Integer object
System.out.println(list)
```

    [5]


This code works because the 5 is being converted by the list.add, since the list uses integer objects. 

Challenge: In the cell below, demonstrate a function failing with an int and a function succeding with an integer. This cannot be an ArrayList. You are NOT allowed to use ChatGPT, Google AI, Llama 2, Bing AI, etc, however, you can Google for answers.


```Java

```

Moreover, we can also get other data from the integer class, which is related to how Java functions.


```Java
System.out.println("Integer Min Value: " + Integer.MIN_VALUE);
System.out.println("Integer Max Value: " + Integer.MAX_VALUE);
```

    Integer Min Value: -2147483648
    Integer Max Value: 2147483647


These numbers are the bounds of integers in java. For example, we can try going outside the range to see what happens.


```Java
Integer pleaseBreak = new Integer(2147483648)
```


    |   Integer pleaseBreak = new Integer(2147483648);

    integer number too large

    


Challenge: Can we have a primitive int that goes past that bound? Try and find out in the cell below.


```Java

```

#### Double Wrapper Classes

Double wrapper classes are basically the same thing as integer classes, however, they deal with double varaiables instead of integer variables. You write it like this:


```Java
Double(Double Value)
```

Here is an example of using Double object:


```Java
// My actual height in real life (in feet)
Double height = new Double(6.6); // Send to an Object
double primitiveHeight = height.doubleValue(); // Turn back into a primitive
```

And here is an example of when it works and when it does not.


```Java
ArrayList<double> list = new ArrayList<double>();  // This will cause a compile-time error
```


    |   ArrayList<double> list = new ArrayList<double>();  // This will cause a compile-time error

    unexpected type

      required: reference

      found:    double

    

    |   ArrayList<double> list = new ArrayList<double>();  // This will cause a compile-time error

    unexpected type

      required: reference

      found:    double

    


Again, the ArrayList needs an object type, but we are passing a primitive type.


```Java
ArrayList<Double> list = new ArrayList<Double>();
list.add(3.14);  // Autoboxing will automatically convert the double 3.14 to a Double object
```




    true



This code works because the 3.14 is being converted by the list.add, since the list uses double objects. 

#### Autoboxing
Autoboxing is when Java automatically changes a basic data type into its object form. The Java compiler does this for us. Think of it as putting the data into a box. Java can also unbox an object, which is the exact opposite of autoboxing. When an Integer object is assigned to a primitive int type, Java will automatically use the primitive int version of the number and assign it to the int variable.


```Java
// Boxing
int a = 5;
Integer b = a;
```


```Java
// Unboxing
Integer x = new Integer(10);
int y = x;
```

### 2.9 Using the Math Class

Java has a built in math class called ___? It is a part of the java.lang class.


```Java
System.out.println(Math.abs(-5)) // Absolute Value
```

    5



```Java
System.out.println(Math.pow(5, 2)) // Power: base, exponent
```

    25.0



```Java
// Two ways to calculate square roots
System.out.println(Math.pow(25, 0.5)); // Allows for different roots
System.out.println(Math.sqrt(25)) // Square Root
```

    5.0
    5.0


Finally, arguably the most important class in math: The random class! Many purposes, especially in game development. What is one purpose? 


```Java
System.out.println((int)Math.random()) // Always returns zero because the range of math.random is [0, 1)
```

    0


In the cell below, experiment and try to figure out a way to call Math.random and impliment bounds, with your bounds being integer bounds of a and b.


```Java

```
