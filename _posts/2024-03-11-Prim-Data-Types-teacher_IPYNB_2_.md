---
toc: True
comments: True
layout: post
title: Primitive Data Types
description: Primitive Data Types Lesson
courses: {'labnotebook': {'week': 26}}
type: tangibles
---

## Primitive Data Types - A list

There are 8 different primitive data types in Java:

- Boolean
- Char
- Byte
- Short
- Int
- Long
- Float
- Double

They are categorized in the following way...

![Categorized](https://images.shiksha.com/mediadata/ugcDocuments/images/wordpressImages/2022_05_image-162.jpg)

## 1. Booleans

Booleans are a datatype that can store either true or false. They can be used to check whether two values are equal or not (basically in conditional statements to return True or False). The default boolean value is false, and the system memory for this variable varies per JDK.


```java
class BooleanDataTypes
{
  public static void main(String args[]) {
      boolean var1 = true; // change this!
      if (var1 == true) //checks if the value is true or false
      {
          System.out.println("Boolean value is True");
      }
      else
      {
          System.out.println("Boolean value is False");  
      }
  }
}
BooleanDataTypes.main(null);
```

    Boolean value is True


## 2. Character Type - char
This datatype stores a single character, lowercase and uppercase. It takes a memory space of 16 bits or 2 bytes.


```java
class CharDataType {
    public static void main(String[] args) {
        char var1 = 'A';
        char var2 = 'd';
        System.out.println(var1);
        System.out.println(var2);
    }
}
CharDataType.main(null);
```

    A
    d


## Integer Type
This type has 4 integer types: byte, short, int, and long. These types, since they are integers, do not contain decimals but are whole numbers.

### Byte
A byte is an 8-bit integer. It can hold values from -128 to 127. 

`byte b = 50;`

### Short
A short is a 16-bit integer. It can hold values from -32,768 to 32,767.

`short s = 9999`

### Int
An int is a 32-bit signed integer and it can hold values from -2,147,483,648 to 2,147,483,647. This is the standard data type for most integers in Java programs.

`int i = 4294967`

### Long
A long is a 64-bit integer and it can hold values from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807. This data type ends with ‘L’ or ‘l’.

`long lng = 9223372036854775807L;`


```java
class IntegerDataTypes
{
  public static void main(String args[]) {
    int a = 10;
    short s = 2;
    byte b = 6;
    long l = 125362133223l;
 
    System.out.println("The integer variable is " + a + '\n');
    System.out.println("The short variable is " + s  + '\n');
    System.out.println("The byte variable is " + b + '\n');
    System.out.println("The long variable is " + l);
 
  }
}
IntegerDataTypes.main(null);
```

    The integer variable is 10
    
    The short variable is 2
    
    The byte variable is 6
    
    The long variable is 125362133223


## Float Type

A float type is a number with a decimal. It has two types: float and double.

### Float
Float is a floating point data type that stores the values, including the decimal precision. It is not used for precise data.
A Float value:

- is a single-precision 32-bit or 4 bytes IEEE 754 floating-point
- can have a 7-digit decimal precision
- ends with an ‘f’ or ‘F’
- default value = 0.0f
- stores fractional numbers ranging from 3.4e-038 to 3.4e+038

`float floatVariable;`

### Double
The double data type is similar to float. The difference between the two is that is double twice the float in the case of decimal precision. It is used for decimal values just like float and should not be used for precise values.

A double value:

- is a double-precision 64-bit or 8 bytes IEEE 754 floating-point
- can have a 15-digit decimal precision
- default value = 0.0d
- stores fractional numbers ranging from 1.7e-308 to 1.7e+308

`double doubleVariable;`



```java
class FloatDataTypes
{
  public static void main(String args[]) {
 
    float f = 65.20298f;
    double d = 876.765d;
 
    System.out.println("The float variable is " + f);
    System.out.println("The double variable is " + d);
  }
}
FloatDataTypes.main(null);
```

    The float variable is 65.20298
    The double variable is 876.765


## Hacks

1. Make a table of all the information of the different types of primitive data
2. Create a class that utilizes these values to make a calculator, one for integers or one for floats. Find some way to include booleans, and show how each type has its own advantages (such as using a long for a large number calculator)
