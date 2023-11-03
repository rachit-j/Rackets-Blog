---
toc: True
comments: True
layout: post
title: Unit 1 Lesson
description: the lesson for the unit 1
permalink: /unit1
courses: {'csa': {'week': '7'}, 'labnotebook': {'week': 7}}
type: hacks
---

# SECTION 1.1

## Why does java matter?

one of the main reason that java is such an important language in the coding world is because it is a object-oriented-programming (OOP) language. 

it offers a structure that is easy to solve big problems. but i think that we all know that so lets skip to the real deal. 


## Basics of Java

- Block Comments- The compiler will ignore any text between /* and */

- line comments- Same as above but // ignores one line

- Class Declaration - identifies the name, the start and the end of the class. <b> the class name must match the file name. (case sensitive) </b>

- main Method- controls all of the action in the program. 

- system.out- objects that generate output to the console

- system.out.print- prints what ever you out inside the ()

- system.out.println- prints whatever is one the screen and moves to the next line to print out the next action. basically hits enter after it prints out. 



tip: add "`<classname>.main(null)`" at the end of your code to see the output in your jupyter notebook. 


```Java
/* this is a
   code block */


// code: printing out hello world. 

public class greeting {
    public static void main (String [] args) {

        System.out.println("Hello, World!");
        System.out.print("Hello,");
        System.out.print(" World!"); 
    }
}

greeting.main(null)
```

    Hello, World!
    Hello, World!

## What is a string literal?

- any sequence of letters, numbers, or symbols that is put between quotes. 
- java will put out anything in the quotes, no restrictions. 

Examples: 


```Java
public class stingLiterals {
    public static void main (String [] args) {

        System.out.println("This is a string literal.");
        System.out.println("and so are these");
        System.out.println("1234567890"); 
        System.out.println("&^&*%^$&%$#^%W#*^$%&(*^)"); 
    }
}

stingLiterals.main(null)
```

    This is a string literal.
    and so are these
    1234567890
    &^&*%^$&%$#^%W#*^$%&(*^)


## ERRORS!!!!!!
### Syntax/compiler error:

- messed up syntax
- compiler is not happy >:(


```Java

public class syntaxError {
    public static void main (String [] args) {

        System.out.println("This is a syntax error.")
        //missing semicolon
    }
}

syntaxError.main(null)
```


    |           System.out.println("This is a syntax error.")

    ';' expected

    


### Logic Error

- compiler is happy
- messed up in the string literals
- code works perfectly


```Java
public class logicError {
    public static void main (String [] args) {

        System.out.println("This is a leogic error.");

    }
}

logicError.main(null)
```

    This is a leogic error.


### exception error: 
- a number is divided by zero. 


```Java
public class exceptionError {
    public static void main(String[] args) {
        try {

            int result = 2 / 0;
            System.out.println("Result: " + result);
        } catch (ArithmeticException e) {  //this just makes the error more verbose
            e.printStackTrace();
        }
    }
}
exceptionError.main(null)

```

    java.lang.ArithmeticException: / by zero
    	at REPL.$JShell$20$exceptionError.main($JShell$20.java:19)
    	at REPL.$JShell$21.do_it$($JShell$21.java:16)
    	at java.base/jdk.internal.reflect.DirectMethodHandleAccessor.invoke(DirectMethodHandleAccessor.java:104)
    	at java.base/java.lang.reflect.Method.invoke(Method.java:578)
    	at io.github.spencerpark.ijava.execution.IJavaExecutionControl.lambda$execute$1(IJavaExecutionControl.java:95)
    	at java.base/java.util.concurrent.FutureTask.run(FutureTask.java:317)
    	at java.base/java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1144)
    	at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:642)
    	at java.base/java.lang.Thread.run(Thread.java:1623)


______

# SECTION 1.2
## Variable and Data Types.  

## Primitive Data
- determines the size and type of data can we can worth with in a java program. 
- focus on three different types that can we can represent data. 


#### Smallest to biggest:

Boolean, takes up 1 bit. 
- true or false


Int, take up 32 bit
- whole number values.
- add, subtract, multiply, etc. 

Doubles, AKA Floating point numbers. 64 bit
- same as integers

String
- "Hello World!"



Reference Purposes

(the collegeboard person used bows as reference so will i.)
- there can be small bow
- a medium bow
- a red bow
- a large red bow



### What is the difference?

- primitive data are already in java, you don't have to make it. Except for string, which is created by the programmer. 
- non-primitive data can be use methods to perform actions, but primitive data cannot. 




## Primitive Activity
#### MIX&MATCH


```
Choices:
1. int
2. double
3. boolean
4. String



3 False

4 "ryan gosling"

1 1738

2 4.26
```

#### Questions:

what type of data should be used to store

- someones bank number and cvc?

- someones mother's maiden name and their name?

- the first 16 digits of pi

- if you want to transact one million $. 

Answers:
- someone's bank number and cvc?

bank number: int

cvc: int

- someone's mother's maiden name and their name?

mother's maiden name: String

their name: String

- the first 16 digits of pi?

double

- if you want to transact one million $.

double



## Variables

A name given to a memory location that is holding a specified type of value.

### how to name a variable (omg this is so hard !)

- may consists of letters, digits, or an underscore (case sensitive)

- may not start with a digit
- space are a big no no
- may not use other characters as &,@, or #
- may not used java reserved words


#### Tip!

use camel casing when naming a variables.

#### example: 

thisIsCamelCasing



### Declare variables:

The three primitiva data types in Java:
- integers (whole #): `int`
- Decimal numbers (floating-point values): `double`
- Boolean values (true/false): `boolean`


#### Format:

dataType varibleName;

#### Example

`int total;`

`boolean outcome;`

`double firstFifteenPi;`


### what if you don't want to change the variable's value after given?

add final in front of the declaration:

`final double PI;`

`final boolean WORKOUT_DECISION; `

for final variables, use all caps and underscore when naming them. 



## Practice

### Find the odd one out.


int value; 

double 4eva;

boolean private;

integer sum;

double wow!; 

boolean foundIt; 

int numberOfStudents; 

double chanceOfRain;

boolean #mortNews;

int count;

bool isFriday; 

final int DOZEN;



Odd ONES out:

double 4eva; (Variable names cannot start with a number.)

boolean private; (private is a reserved keyword in Java.)

integer sum; (The correct primitive data type for integers in Java is int, not integer.)

double wow!; (Variable names cannot contain special characters like !.)

boolean #mortNews; (Variable names cannot start with or contain special characters like #.)

bool isFriday; (The correct primitive data type for boolean values in Java is boolean, not bool.)


___

## 1.3 Main Topics
### Literal vs String Literal

### Arithmetic operators
- Additon
- Minus
- Multiply
- Divide
- Mod

### Arthemtic expressions
- Int
- Double
    
### Assigment Operator
- = vs ==

# Demo 1


```Java
public class demo {
    public static void main(String[] args) {
        // Whats is the outputs between these two pieces of code
        //
        //
        //
        
        /* 
        System.out.println("3" + "3");
        System.out.println(3 / 2);
        System.out.println(2.0 * 1.5);
        */
    }
}

demo.main(null);
```

# Cheat Sheet

## Literal
- The source code representation of a fixed value

## String Literal
- Something enclosed in double qoutes


## Assigment Operator
- = is an assigment operator
- == is repesents just normal =
- Assigment Operators moves right to left
- X = Y = Z = 2;
- Why is 7 = x; a non valid peice of code
- 

## PEMDAS
- Java uses PEMDAS still but a tiny bit different

### Order
1. ()
2. ^
3. *, /, %
4. +, -

## Primative Data Types
[table](http://orion.towson.edu/~izimand/237/LectureNotes/L3-PrimitiveDataTypes.JPG)

## Operation vs Result
- The bigger data type will always be the resulting output
- If you were to add a double and a int what would be the result?
- 

# Demo 2


```Java
public class demo2 {
    public static void main(String[] args) {
        // Print a math equation that goes through these steps
        // Adds 19 + 134
        // Multiplies that value by 5
        // Then takes the mod of that value by 2
        // It should print 1

        System.out.println( (19 + 134) * 5 % 2);
    }
}

demo2.main(null);
```

# Odd Even


```Java
public class OddEven {

    // Without changing any varibles
    // Print only odd numbers

    public static void main(String[] args) {
        int num = 2;
        int i = 0;
        while (i <= 10) {
            if (i % num == 0) {
                System.out.println(i + " is even");
            }
            i++;
        }
    }
}

OddEven.main(null);
```

# 1.4

# Compound Assignment Operators

look at storing items in variables with assignment statemt.

also look at compound assignment operators (+=, -= etc) to modify values stored in variables in one step

+= adds value to existing variable value

x += 7 is equivalent to x = x + 7;
x -= 5 is equivalent to x = x - 5;

same for all compound assignment operators.

# also learn how to trace through code (check comments of codeblock below)


```Java
public class CompoundDemo {
    public static void main(String[] args) {
        int x = 6;
        x += 7; // 6 + 7 = 13
        x -= 3; // 13 - 3 = 10
        System.out.println(x);
        x *= 10; // 10 * 10
        x /= 5; // 100 / 5 = 20
        System.out.println(x);
        x %= 3; // remainder of 100/3 = 2
        System.out.println(x);
}
}
CompoundDemo.main(null);

// NOTE: going through these compound assignments with comments is called tracing,
// when we do what the compiler does, and go through the code step by step. Should be
//done on the AP test to avoid human error.
```

# increment and decrement operator

IMPORTANT: THE USE OF INCREMENT AND DECREMENT OPERATORS IN THE PREFIX FORM (++X) AND INSIDE OTHER EXPRESSIONS (ARR[X++]) IS OUTSIDE THE SCOPE OF THE COURSE AND THE AP EXAM


```Java
public class incdecDemo {
    public static void main(String[] args) {
    int x = 1; 
    int y = 1;
    x++; // x = x + 1, x = 2;
    y--; // y = y - 1, y = 1 - 1 = 1;
    System.out.println(x);
    System.out.println(y);
}
}
incdecDemo.main(null);

// NOTE: going through these compound assignments in order is important to
// ensure you get the correct output at the end
```

# learn how to describe code 

the following code segment has comments that describe the line of code the comment is on. Look at how the code is described.


```Java
public class behaviorDemo {
    public static void main(String[] args) {
    int x = 20; // define an int variable x and set its initial value to 23
    x *= 2; // take the current value of x, multiply it by 2, assign the result back to x
    x %= 10; // take the current value of x, find x modulus 10 (remainder x divided by 10), 
    //assign result back to x
    System.out.println(x); // display the current value of x
}
}
behaviorDemoDemo.main(null); 
```

# practice important concepts


```Java
public class numbers {
    public static void main(String[] args) {
        int x = 777;

        // For output 100
        x -= 677;
        x /= 1;
        System.out.println(x);  // Outputs 100

        x = 777;  // Resetting x for the next challenge
        // For output 779
        x++;
        x++;
        System.out.println(x);  // Outputs 779

        x = 777;  // Resetting x for the next challenge
        // For output 2
        x++;
        x /= 389;
        System.out.println(x);  // Outputs 2
    }
}
CompoundDemo.main(null);
```


```Java
// PRACTICE TRACING THROUGH THE FOLLOWING CODE (someone could come up and do it on a whiteboard if we have time for fun)

public class Demo {
    public static void main(String[] args) {
        int x = 758;          // x is initialized with the value 758
        x += 423;            // x is incremented by 423, so x becomes 1181
        x -= 137;            // x is decremented by 137, so x becomes 1044
        x *= 99;             // x is multiplied by 99, so x becomes 103356
        x /= 33;             // x is divided by 33, so x becomes 3132
        x %= 111;            // x is taken modulo 111, so x becomes 88
        System.out.println(x); // Outputs 88
    }
}
CompoundDemo.main(null);

```


```Java
// DESCRIBE EACH LINE OF CODE
int x = 5;          // Declare an integer variable 'x' and initialize it with the value 5.
x++;                // Increment the value of 'x' by 1. After this operation, 'x' becomes 6.
x /= 2;             // Divide the value of 'x' by 2 and assign the result back to 'x'. After this operation, 'x' becomes 3.
System.out.println(x); // Print the current value of 'x' to the console. It will output '3'.
```

# what you must know 

compound operators perform an operation on a variable and assign the result to the variable

ex: x /= 25; would take x and divide it by 25, then assign the result to x.

if x = 100, then the result of x/= 25; would be 4.

increment and decrement operators take x and either increment it or decrement it by 1, then assign the value to x.

x++; would take x and add 1 to it, then assign the value to x.

x--; takes x and subtracts 1 from x, then assigns the value to x.

### your frq will likely see if you know how to use compound operators in actual code.

# mini hacks:

1. write some java code that uses compound operators and then trace through it similarly to the examples shown in this lesson. Use conditional statements as well, don't just execute some compound operators on an x value in order and call it a day. You might have to do tracing on the AP test so this is for your own good.

# example below


```Java
public class CompoundAssignment {

    public static void main(String[] args) {
      
      int sum = 0; 
      for (int i = 0; i < 2; i++) {  // i = i + 1 each iteration, 1st iteration i = 0
        for (int j = 0; j < 2; j++) { // j = j + 1 each iteration, 1st iteration j = 0
          System.out.println("i: " + i);
          System.out.println("j: " + j);
          sum += i + j; //  sum = sum + (i + j) each iteration, 1st iteration sum = 0 + (0 + 0)
          System.out.println(sum);

        }
      }
      
      System.out.println("Sum: " + sum);
  
  } }
CompoundAssignment.main(null);
```

# 1.5

<html>
<head>
<style>
    @import url('https://fonts.googleapis.com/css?family=Arima+Madurai:300');
    *,
    *::before,
    *::after {
        box-sizing: border-box;
    }
    .bird {
        background-image: url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/174479/bird-cells-new.svg);
        background-size: auto 100%;
        width: 88px;
        height: 125px;
        will-change: background-position;
        animation-name: fly-cycle;
        animation-timing-function: steps(10);
        animation-iteration-count: infinite;
        &--one {
            animation-duration: 1s;
            animation-delay: -0.5s;		
        }
        &--two {
            animation-duration: 0.9s;
            animation-delay: -0.75s;
        }
        &--three {
            animation-duration: 1.25s;
            animation-delay: -0.25s;
        }
        &--four {
            animation-duration: 1.1s;
            animation-delay: -0.5s;
        }
    }
    .bird-container {
        top: 20%;
        left: -10%;
        transform: scale(0) translateX(-10vw);
        will-change: transform;
        animation-name: fly-right-one;
        animation-timing-function: linear;
        animation-iteration-count: infinite;
        &--one {
            animation-duration: 15s;
            animation-delay: 0;
        }
        &--two {
            animation-duration: 16s;
            animation-delay: 1s;
        }      
        &--three {
            animation-duration: 14.6s;
            animation-delay: 9.5s;
        }
        &--four {
            animation-duration: 16s;
            animation-delay: 10.25s;
        }
    }
    @keyframes fly-cycle {
        100% {
            background-position: -900px 0;
        } 
    }
    @keyframes fly-right-one {
        0% {
            transform: scale(0.3) translateX(-10vw);
        }
        10% {
            transform: translateY(2vh) translateX(10vw) scale(0.4);
        }
        20% {
            transform: translateY(0vh) translateX(30vw) scale(0.5);
        }        
        30% {
            transform: translateY(4vh) translateX(50vw) scale(0.6);
        }        
        40% {
            transform: translateY(2vh) translateX(70vw) scale(0.6);
        }       
        50% {
            transform: translateY(0vh) translateX(90vw) scale(0.6);
        }        
        60% {
            transform: translateY(0vh) translateX(110vw) scale(0.6);
        }        
        100% {
            transform: translateY(0vh) translateX(110vw) scale(0.6);
        }       
    }
    @keyframes fly-right-two {  
        0% {
            transform: translateY(-2vh) translateX(-10vw) scale(0.5);
        }        
        10% {
            transform: translateY(0vh) translateX(10vw) scale(0.4);
        }       
        20% {
            transform: translateY(-4vh) translateX(30vw) scale(0.6);
        }        
        30% {
            transform: translateY(1vh) translateX(50vw) scale(0.45);
        }        
        40% {
            transform: translateY(-2.5vh) translateX(70vw) scale(0.5);
        }        
        50% {
            transform: translateY(0vh) translateX(90vw) scale(0.45);
        }     
        51% {
            transform: translateY(0vh) translateX(110vw) scale(0.45);
        }     
        100% {
            transform: translateY(0vh) translateX(110vw) scale(0.45);
        }     
    }

</style>
</head>
	<div class="bird-container bird-container--one">
		<div class="bird bird--one"></div>
	</div>
	<div class="bird-container bird-container--two">
		<div class="bird bird--two"></div>
	</div>
	<div class="bird-container bird-container--three">
		<div class="bird bird--three"></div>
	</div>
	<div class="bird-container bird-container--four">
		<div class="bird bird--four"></div>
	</div>

</html>


## Casting Variable 
<style>
.flip-card-container {
  width: 800px;
  height: 200px;
  perspective: 1000px;
}
.flip-card {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform 1s;
  transform-style: preserve-3d;
}
.flip-card-container:hover .flip-card {
  transform: rotateY(180deg); /* <=>  rotateY(.5turn) */
}
/* Position the front and back side */
.flip-card-front, .flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden; /* Safari */
  backface-visibility: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
  /* border-radius: 0.5rem; */
}
.flip-card-front {
  background-color:#DC78BB;
  color: #fff;
}
.flip-card-back {
  background-color: #517fa4;
  color: #fff;
  transform: rotateY(180deg);
}
.flip-card-front p {
  text-align: center;
  margin: 1rem;
  font-size: 1.4rem;
  line-height: 1.5rem;
}
.flip-card-back p {
  text-align: center;
  margin: 1rem;
  font-size: 1.4rem;
  line-height: 1.5rem;
}
.flip-card-back p span {
  display: block;
  font-size: 1rem;
  font-style: italic;
  font-weight: bold;
  margin-top: 1.25rem;
}
</style>
  <div class="flip-card-container">
    <div class="flip-card">
      <div class="flip-card-front">
        <p>CASTING</p>
      </div>
      <div class="flip-card-back">
        <p>
          "Change the data type of variable from one type to another."
        </p>
      </div>
    </div>
  </div>

### Example
- Int variable ---->> double
- String variable ---->> Int


```Java
/*
* Purpose: Demonstrate casting using division.
*/
public class CastingNumbers {
    public static void main(String[] args) {
        System.out.println(6 / 4); // if I just do divide 6 by 4, these are both int value, so I'm going to wing up with an int result.
        System.out.println (6.0 / 4); // Since one of those value is a double value, output will be double 
        System.out.println(6 / 4.0); // (Same Reason) I wind up with the result of 1.5
    }
}
```


<style>
.navbar {
    /* background-color: #333; */
    position: relative;
    z-index: 999;
}
.navbar ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
}
.navbar li {
    display: inline-block;
}
.navbar li a {
color: gray;
display: block;
padding: 10px 20px;
background-color: black;
}
.navbar ul ul {
position: absolute;
top: 100%;
display: none;
}
.navbar ul ul li {
display: block;
}
.navbar ul ul li a:hover {
background-color: #555;
}
.navbar li:hover ul {
display: block;
}

</style>
<nav class="navbar">
<ul>
<li>
  <a href="#">What will be the answer of System.out.println((double) 6/4);</a>
    <ul>
      <li><a href="#">By using the casting operator of double in parentheses, it will still wind up with a double result of 1.5.</a></li>
    </ul>
</li>
</ul>
</nav>

## Ranges of variable
int: Stored by using a finite amount (4 bytes) of memory.
<img src="https://drive.google.com/uc?export=download&id=1i3lnzVrOeIaRPSWsOntErVGiKToL0Keh">

### Integer
Max: 2,147,483,647     
Min: -2,147,483,648

### Double 
up to 14 - 15 digits for storage

### Boolean 
only 2 (true and false)


```Java
/*
* Purpose: Demonstrate Integer Range
*/
public class TooBigNumber {
    public static void main(String[] args) {
        int posInt = 2147483647; 
        int negInt = -2147483648;
        System.out.println(posInt + " "); 
        System.out.println(negInt);
    }
}
TooBigNumber.main(null);
```


```Java
/*
* Purpose: Demonstrate Integer.MAX_VALUE and Integer.MIN_VALUE.
*/
public class IntMinMax {
    public static void main(String[] args) {
        int posInt = Integer.MAX_VALUE; 
        int negInt = Integer.MIN_VALUE;
        System.out.println(posInt + " "); 
        System.out.println(negInt);
    }
}
IntMinMax.main(null);
```


```Java
/*
* Purpose: Demonstrate Integer Overflow
*/
public class TooBigNumber {
    public static void main(String[] args) {
        int posInt = Integer.MAX_VALUE; 
        int negInt = Integer.MIN_VALUE;
        System.out.println(posInt + 1); 
        System.out.println(negInt - 1);
    }
}
TooBigNumber.main(null);
```


```Java
import java.util.Scanner;

public class Sum_forABC {
	public static void main(String args[]) {
		int a = 70;
		int b = 63;
		int c = 82;
		
		int total = a + b + c;
        
		double avg = total / 3; 
		
		System.out.println("a\tb\tc");
		System.out.println(a+"\t"+b+"\t"+c);
		System.out.println("total:" + total);
		System.out.printf("average: %.2f", avg);
	}
}
Sum_forABC.main(null);
```

<!DOCTYPE html>
<html>
<head>
    <title>Java Code Runner</title>
    <style>
    textarea {
        font-size: 19px;
        margin: 1.5rem 0px;
        border: none;
        outline: none;
        background-color: #eeeeff;
    }
    .w-btn {
        position: relative;
        border: none;
        display: inline-block;
        padding: 15px 30px;
        border-radius: 15px;
        font-family: "paybooc-Light", sans-serif;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
        text-decoration: none;
        font-weight: 600;
        transition: 0.25s;
    }
    .w-btn-gra3 {
        background: linear-gradient(
            45deg,
            #ff0000,
            #ff7300,
            #fffb00,
            #48ff00,
            #00ffd5,
            #002bff,
            #7a00ff,
            #ff00c8,
            #ff0000
        );
        color: white;
    }
    .w-btn-gra-anim {
        background-size: 400% 400%;
        animation: gradient1 5s ease infinite;
    }
    @keyframes gradient1 {
        0% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
        100% {
            background-position: 0% 50%;
        }
    }
</style>
</head>
<body>
    <textarea id="code" rows = "13" cols="96">
/*
Long: 64-bit two's complement integer
*/
public class sum {
    public static void main(String args[]) {
        int x = 100000;
        int y = 200000;
                    
        long z = x * y; 
        System.out.println(z);
    }
}
</textarea>
<div id="codeResult"></div>
<button class="w-btn w-btn-gra3 w-btn-gra-anim" onclick ="codeRun()">Run Code</button>
<script>
        async function codeRun() {
            const javaCode = document.getElementById('code').value;
            const data = new URLSearchParams({
                'code': javaCode,
                'language': 'java', // Changed language to Java
                'input': '' // You can add input if needed
            });
            const url = 'https://api.codex.jaagrav.in'; // Added missing URL declaration
            const options = {
                method: 'post',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: data.toString() // Changed to data.toString()
            };
            try {
                const response = await fetch(url, options);
                const result = await response.json();
                document.getElementById('codeResult').innerHTML = `<textarea cols="96">${result.output}</textarea>`;
            } catch (error) {
                console.error(error);
            }
        }
    </script>
</body>
</html>

<html>

<head>
    <meta charset="UTF-8">
</head>

<body>
    <h1>Questions</h1>
    <p>1. what will be the output of (int) (2.5 * 3.0)</p>
    <form name="form1">
        <input type="radio" name="answer1" value="1">7.0<br>
        <input type="radio" name="answer1" value="2">7<br>
        <input type="radio" name="answer1" value="3">7.5<br>
        <input type="radio" name="answer1" value="4">7.50<br>
    </form>
    <p id="check1"></p>
    <p>2. what will be the output of (double) 25 / 4</p>
    <form name="form2">
        <input type="radio" name="answer2" value="1">6.50<br>
        <input type="radio" name="answer2" value="2">6.0<br>
        <input type="radio" name="answer2" value="3">6<br>
        <input type="radio" name="answer2" value="4">6.25<br>
    </form>
    <p id="check2"></p>
    <p>3. what will be the output of 6 / (double) 5</p>
    <form name="form3">
        <input type="radio" name="answer3" value="1">1.0<br>
        <input type="radio" name="answer3" value="2">1<br>
        <input type="radio" name="answer3" value="3">1.2<br>
        <input type="radio" name="answer3" value="4">1.125<br>
    </form>
    <p id="check3"></p>
    <p>4. what will be the output of (int) (-8.63 -  0.5)</p>
    <form name="form4">
        <input type="radio" name="answer4" value="1">-9<br>
        <input type="radio" name="answer4" value="2">-13.63<br>
        <input type="radio" name="answer4" value="3">-9.13<br>
        <input type="radio" name="answer4" value="4">-8<br>
    </form>
    <p id="check4"></p>
    <input type="button" name="select" value="check your answer" onclick="myFunction()">
    <script type="text/javascript">
        function myFunction() {
            checkAnswer(1, "answer1", "check1", 2);
            checkAnswer(2, "answer2", "check2", 4);
            checkAnswer(3, "answer3", "check3", 3);
            checkAnswer(4, "answer4", "check4", 1);
        }
        function checkAnswer(questionNumber, answerName, checkId, correctAnswer) {
            var selectedAnswer = document.querySelector('input[name="' + answerName + '"]:checked');
            if (selectedAnswer) {
                if (parseInt(selectedAnswer.value) === correctAnswer) {
                    document.getElementById(checkId).innerHTML = "correct!";
                } else {
                    document.getElementById(checkId).innerHTML = "wrong";
                }
            } else {
                document.getElementById(checkId).innerHTML = "Please select an answer for question " + questionNumber + ".";
            }
        }
    </script>
</body>

</html>

## Essential Knowledge (2.B)
1. The casting operators (int) and (double) can be used to created temporary value converted into a different data type. 
2. Casting a double value to an int causes the digits to the right of the decimal point to be truncated. 
3. Some programming code causes int values to be automatically cast(widened) to double values.
4. Value of type double can be rounded to the nearest integer (int) (x + 0.5) + (int) (x - 0.5) for negative numbers.


## Essential Knowledge (5.B)
1. Integer values in Java are represented by values of type int, which are stored using a finite amount (4 bytes) of memory. Therefore, an int value must be in the range from
Integer.MIN_VALUE to Integer.MAX_VALUE inclusive.
2. If an expression would evaluate to an int value outside of the allowed range, an integer overflow occurs. This could result in an incorrect value within the allowed range.

## Questions
1. (int) (2.5 * 3.0)
2. (double) 25 / 4
3. 6 / (double) 5

## Mini Hacks
- Complete all uncompleted code segments
- Answer all questions in the code
- complete the activities in the lesson blogs
- will be scaled to 0.2 depending on the completion of your code

## Main Hack
- Use topics from 3 out of 4 of the Units
- It has to be a 2 part style question, A and B
- Will Be graded out of 4 points
- Write a scoring sheet for what you have done out six points
- Your real grade for the assigment will be based of two things
- How creative, unique, cool your question and code is
- Did you acheive 4/4 points for your code
- That will be scaled to 0.8 of 1 for all your hacks

## Example FRQ 0.65
### Question:
Winner of the game is represented by gameWin. Player 1 score is represented by int variable x, and Player 2 score is represented by int variable y



```Java
public class Game {
    int x = 0;
    int y = 0;

    boolean XgameWin = false;
    boolean YgameWin = false;
}
```

# PART A
write a method gameWinchange that checks who wins


```Java
public class Game {
    int x = 0;
    int y = 0;

    boolean XgameWin = false;
    boolean YgameWin = false;

    public void gameWinchange(boolean X, boolean Y) {
        //insert code here
        if (X == true) {
            UpdateScore(x,y);
            X = true;
        } else {
            UpdateScore(y,x);
            Y = true;
        }
    }
}
```

# Part B
Write a method to update score for Player 1 and Player 2, The player that wins gain a point, the player that loses minus a point
If a player hits 10 points, reset values


```Java
public class Game {
    
    //pretend previous method is above

    public int UpdateScore(int Wscore, int Lscore) {
        Wscore += 1;
        Lscore -= 1;

        if (Wscore == 10) {
            Wscore = 0;
            Lscore = 0;
        }
        if (Lscore == 10) {
            Wscore = 0;
            Lscore = 0;
        }
    }
}
```

# Grading
## 1/1 Point for correctly changing the boolean in Part A
## 1/1 Point for using Compound Assigment Operators in Part B
## 1/1 Point for Values reseting when one hits 10 points
## 1/1 Point for Passing Arguments through Part A and B
