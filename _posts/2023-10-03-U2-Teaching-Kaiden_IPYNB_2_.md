---

---

```Java
String preInt = "Hello World!"; // How we usually initialize strings
System.out.println(preInt);

// Using a constructor:
String newString = new String("Hello World!");
System.out.println(newString);
```

    Hello World!
    Hello World!


#### Escape Characters
Sometimes, you want to put a quote in a string. However, you quickly find out that the opening quotation in the quote marks the "end" of the string and you can't type out your quote unless you want the program to crash. What can you do?

![Alt text](https://media.discordapp.net/attachments/1010780182476496908/1159224994707021945/image.png?ex=65303f68&is=651dca68&hm=d8ba25c57cc1d41eb20fd2f3621f2ae0472efb874dba76d7078415c0d0b34613&=&width=2268&height=622)

Challenge: Display the background of the quote while displaying the quote in one line: "Give me liberty or give me death!" - Patrick Henry.


```Java
System.out.println("This is a famous quote written by Patrick Henry in the Virginia Convention: \n\"Give me liberty or give me death!\"")
```

    This is a famous quote written by Patrick Henry in the Virginia Convention: 
    "Give me liberty or give me death!"


#### String Concatenation

When we combine two strings together, we call that string concatenation. We use the '+' operator to concatenate two strings. 


```Java
System.out.println("I am" + "hungry");
```

    I amhungry


Notice how there is no space between am and hungry. This is because the java '+' operator does not add a space, but instead, joins the strings together without adding anything in between. To fix this, we add a space in between.


```Java
System.out.println("I am" + " " + "hungry");
```

    I am hungry


However, when we want to use variables with our strings, we can also use the '+=' operator to concatenate our strings. The '+' operator still works, however.


```Java
String a1 = "Hello ";
String a2 = "World";
System.out.println(a1 + a2);
System.out.println(a1 += a2);
```

    Hello World
    Hello World


Can you guess what happens when we try to change a string object?


```Java
String s1 = "Hello"; // String literal
String s2 = "Hello"; // String literal
String s3 = s1; // same reference

//Changing the value of s1
s1 = "Java";

//Updating with concat() operation
s2.concat(" World");

//The concatenated String will be created as a new instance and an object should refer to that instance to get the concatenated value.
String newS3 = s3.concat(" Scaler");

System.out.println("s1 refers to " + s1);
System.out.println("s2 refers to " + s2);
System.out.println("s3 refers to " + s3);
System.out.println("newS3 refers to " + newS3);
```

    s1 refers to Java
    s2 refers to Hello
    s3 refers to Hello
    newS3 refers to Hello Scaler


The strings are immutable! This is because immutable strings allows Java to be safe in multithread applications (no changes that were not supposed to happen at that time in the program), and it makes the string object very efficient, as the strings are stored in a "string pool" that Java uses, which allows strings to only be created once but used over and over again if the same string object is created multiple times.

One last cool thing about strings is that primitive types change to string objects when concatenated. You have been doing this all the time, but here is the proof!


```Java
String message = "Here is the key: ";
double key = 0.5;

System.out.println(message + key)
```

    Here is the key: 0.5


### 2.7 String Methods

#### Intro to External Libraries and APIs
There is a lot you can do with the factory version of Java, however, just like Python and many other languages, there are many new things you can do with the Java external libraries and APIs (application program interfaces). 
All Java classes, libraries, and APIs come with documentation, which lists the methods of the class and also how to use the class and its methods. Here is the official Java documentation for the String class:

[Java Docs](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html)

Courtesy of Java.

#### About the String Class
__The String class is a class in the java.lang package that comes when you install Java on your computer.__
### Accessing Substrings
With strings, we can access substrings and characters in the string. A substring is a string that is included within a larger string, and a character is a substring with a length of 1. First, we need to figure out the length of a string, which is the number of characters in the string. To do this, we use the following method:


```Java
String str = "Kaiden Do";
System.out.println(str.length())
```

    9


We can also get a index for the strings. For example, if we take "Kaiden Do"...

| Index | Character |
| --- | --- |
| 0 | K |
| 1 | a |
| 2 | i |
| 3 | d |
| 4 | e |
| 5 | n |
| 6 |   |
| 7 | D |
| 8 | o |


```Java
String str = "Kaiden Do";
System.out.println(str.substring(0, 6)); // Range is [_,_)
System.out.println(str.substring(7, 9)); // Range is [_,_)
```

    Kaiden
    Do


How would we get the nth character of a string? Write a program to find it with an integer n that you can change to get the nth character in the cell below.


```Java
String str = "Pizza is yummy";
int n = 1;
System.out.println(str.substring(n - 1, n));
```

    P


Question: If we have a string, what is its lower bound index and what is its upper bound index, if the string length is equal to the variable 'str'?

Answer: 

Lower Bound Index: 0 

Upper Bound Index: str - 1

Question: What is the error for an out of bound string? Display it in the cell below.


```Java
String str = "Hello";
System.out.println(str.substring(0, 1000))
```


    ---------------------------------------------------------------------------

    java.lang.StringIndexOutOfBoundsException: Range [0, 1000) out of bounds for length 5

    	at java.base/jdk.internal.util.Preconditions$1.apply(Preconditions.java:55)

    	at java.base/jdk.internal.util.Preconditions$1.apply(Preconditions.java:52)

    	at java.base/jdk.internal.util.Preconditions$4.apply(Preconditions.java:213)

    	at java.base/jdk.internal.util.Preconditions$4.apply(Preconditions.java:210)

    	at java.base/jdk.internal.util.Preconditions.outOfBounds(Preconditions.java:98)

    	at java.base/jdk.internal.util.Preconditions.outOfBoundsCheckFromToIndex(Preconditions.java:112)

    	at java.base/jdk.internal.util.Preconditions.checkFromToIndex(Preconditions.java:349)

    	at java.base/java.lang.String.checkBoundsBeginEnd(String.java:4608)

    	at java.base/java.lang.String.substring(String.java:2720)

    	at .(#21:1)


To do a ctrl-F search through a string, we can use the following process:


```Java
String str = "He stared out the window at the snowy field. He'd been stuck in the house for close to a month and his only view of the outside world was through the window. There wasn't much to see. It was mostly just the field with an occasional bird or small animal who ventured into the field. As he continued to stare out the window, he wondered how much longer he'd be shackled to the steel bar inside the house.";
System.out.println(str.indexOf("animal"))
```

    246


As you can see, the first instance of animal starts at the index of 246.

To compare two strings to each other, we use two functions:


```Java
// To check if a string is equal to another string:
String str1 = "I am hungry";
String str2 = "I am hungry";
System.out.println("Does string 1 equal string 2? True or false: " + str1.equals(str2));
String str2 = "I am not hungry";
System.out.println("Does string 1 equal string 2? True or false: " + str1.equals(str2));
```

    Does string 1 equal string 2? True or false: true
    Does string 1 equal string 2? True or false: false



```Java
// To compare the lengths of the strings

// Case 1: String 1 is shorter than string 2
String str1 = "I am hungry";
String str2 = "I am not hungry";
System.out.println(str1.compareTo(str2)); // Returns less than 0

// Case 2: String 1 is equal string 2
String str1 = "I am hungry";
String str2 = "I am hungry";
System.out.println(str1.compareTo(str2)); // Returns 0

// Case 3: String 1 is longer than string 2
String str1 = "I am hungry";
String str2 = "Hello!";
System.out.println(str1.compareTo(str2)); // Returns greater than 0
```

    -6
    0
    1


compareTo() returns the difference of first unmatched character in the two compared strings. If no unmatch is found, and one string comes out as shorter than other one, then the length difference is returned. It also checks to see if a string comes before or after another string alphabetically.
