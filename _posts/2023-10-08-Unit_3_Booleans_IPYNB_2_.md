---
toc: True
comments: True
layout: post
title: Unit 3 Lesson
type: tangibles
courses: {'csa': {'week': 8}, 'labnotebook': {'week': 8}}
---

# Lessons

## 3.1

### Learning Objective
- Evaluate Boolean expressions that use relational operators in program code

Types of Rational Operators
- Operators
    - Primitives
    - Equal to: ==
    - Not Equal to: !=
- Arithmetic
    - Greater than: >
    - Less than: >
    - Greater than or equal to: >=
    - Less than or equal to: <=

All operators give a `true` or `False` value

<mark> Operators SHOULD NOT be used on String <mark>. String comparisons should be done using .equal or .compareTo

- This is because
    - In Java, strings should not be compared using the == operator because it checks for ____________ equality, not ____________ equality.
    - When you use == with objects (including strings), it checks if the references to the objects are the same. In other words, it checks if they point to the same ____________ in the memory.
    - String literals in Java are stored in a special memory area called the "String Pool". When you create a string literal, Java checks if a string with the same content already exists in the pool. If it does, it returns a reference to that existing string; if not, it creates a new string.


### Comparing Numbers
<html>
<head>
    <style>
        table {
            border-collapse: collapse;
            margin: 20px auto;
        }
        table, th, td {
            border: 1px solid black;
            padding: 10px;
        }
        select {
            width: 100px;
        }
    </style>
</head>
<body>
    <p>Select two numbers and check their relation:</p>
    <label for="firstNumber">First Number: </label>
    <select id="firstNumber">
        <option value="0">0</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <!-- Add more options as needed -->
    </select>
    <label for="relationOperator">Relation: </label>
    <select id="relationOperator">
        <option value="equal">=</option>
        <option value="greaterequal">>=</option>
        <option value="lessequal"><=</option>
        <option value="greater">></option>
        <option value="less"><</option>
    </select>
    <label for="secondNumber">Second Number: </label>
    <select id="secondNumber">
        <option value="0">0</option>
        <option value="1">1</option>
        <option value="2">2</option>
        <!-- Add more options as needed -->
    </select>
    <button onclick="checkRelation()">Check</button>
    <p id="result"></p>
    <script>
        function checkRelation() {
            const firstNumber = parseInt(document.getElementById('firstNumber').value);
            const secondNumber = parseInt(document.getElementById('secondNumber').value);
            const relationOperator = document.getElementById('relationOperator').value;
            let result = '';
            switch (relationOperator) {
                case 'equal':
                    result = firstNumber === secondNumber ? 'The numbers are equal.' : 'The numbers are not equal.';
                    break;
                case 'greaterequal':
                    result = firstNumber >= secondNumber ? 'The first number is greater than or equal to the second number.' : 'This is false.';
                    break;
                case 'lessequal':
                    result = firstNumber <= secondNumber ? 'The first number is less than or equal to the second number.' : 'This is false.';
                    break;
                case 'greater':
                    result = firstNumber > secondNumber ? 'The first number is greater.' : 'This is false.';
                    break;
                case 'less':
                    result = firstNumber < secondNumber ? 'The second number is greater' : 'This is false.';
                    break;
                default:
                    result = 'Invalid operator';
                    break;
            }
            document.getElementById('result').textContent = result;
        }
    </script>
</body>
</html>


```Java
public class Test {
    public static void main(){
        String a = "Hello";
        String b = new String("Hello");

        System.out.println( a == b);
    }
}
Test.main()
```

    false


## 3.2 3.3 and 3.4


### Learning Objective
- Represent branching logical processes by using conditional statements

We all know how if and else statements work

We all know how if and else statements work

#### Syntax

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Interactive Flip Cards</title>
<style>
  .flip-card {
    background-color: #f1f1f1;
    width: 700px;
    height: 250px;
    perspective: 1000px;
    border: 1px solid #ccc;
    margin: 10px;
    cursor: pointer;
  }
  .flip-card-inner {
    position: relative;
    width: 100%;
    height: 100%;
    transition: transform 0.6s;
    transform-style: preserve-3d;
  }
  .flip-card-front, .flip-card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
  }
  .flip-card-front {
    background-color: #bbb;
    color: #000;
    z-index: 2;
    text-align: left; /* Align text to the left */
    padding: 5px; /* Add some padding for better readability */
  }
  .flip-card-back {
    background-color: #555;
    color: #fff;
    transform: rotateY(180deg);
    text-align: left; /* Align text to the left */
    padding: 5px; /* Add some padding for better readability */
  }
  .flip-card:hover .flip-card-inner {
    transform: rotateY(180deg);
  }
</style>
</head>
<body>

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <h3>if-else Syntax</h3>
    </div>
    <div class="flip-card-back">
      <pre>
        if (condition) {
            // Code to execute if the condition is true
        } else {
            // Code to execute if the condition is false
        }
      </pre>
    </div>
  </div>
</div>

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <h3>else-if Syntax</h3>
    </div>
    <div class="flip-card-back">
      <pre>
        if (condition1) {
            // Code to be executed if condition1 is true
        } else if (condition2) {
            // Code to be executed if condition2 is true
        } else if (condition3) {
            // Code to be executed if condition3 is true
        } else {
            // Code to be executed if none of the conditions are true
        }
      </pre>
    </div>
  </div>
</div>

</body>
</html>

## 3.5

### Learning Objectives:

- Understand nested if-else statements and their role in representing branching logical processes.
- Evaluate compound boolean expressions using logical operators like ``&&`` and ``||``.
- Introduce short-circuited evaluation in compound boolean expressions.

#### Nested if-else statements
Nested if-else statements allow for __multiple__ levels of decision-making within a program.



```Java
public class Nested {
    public static void main() {
        int x = 5;
        int y = -10;

        if (x > 0) {
            if (y > 0) {
                System.out.println("Both x and y are positive.");
            } else {
                System.out.println("x is positive, but y is not.");
            }
        } else {
            System.out.println("x is not positive.");
        }
            }
}
Nested.main()
```

    x is positive, but y is not.


#### Compound Boolean Expressions:

Compound boolean expressions involve using __logical__ operators like ``&& (and)`` and ``|| (or)`` to combine multiple conditions.


```Java
public class Compound {
    public static void main(){
        int age = 25;
        boolean isStudent = true;

        if (age >= 18 && isStudent) {
            System.out.println("You are an adult student.");
        } else if (age >= 18 || isStudent) {
            System.out.println("You are either an adult or a student.");
        } else {
            System.out.println("You are neither an adult nor a student.");
        }
            }
}
Compound.main()
```

    You are an adult student.


#### Short-Circuited Evaluation:
Short-circuited evaluation is an __optimization__ technique where the second condition in a ``compound expression is only evaluated if the first condition is true (for &&) or false (for ||).``


```Java
public class Short {
    public static void main() {
        boolean condition1 = true;
        boolean condition2 = false;

        if (condition1 || condition2) {
            System.out.println("This will be printed.");
        }
    }
}

Short.main()
```

    This will be printed.


#### Coding Practice
Calculate the final grade based on the following criteria:
- If the student didn't complete homework, the grade is automatically "F."
- If the student completed homework and the average of midterm and final exam scores is >= 70, the grade is "Pass."
- Otherwise, the grade is "Fail."


```Java
import java.util.Scanner;

public class GradeCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print(" Enter your midterm score (0-100): \n");
        int midtermScore = scanner.nextInt();
        System.out.print(midtermScore);

        System.out.print("\n Enter your final exam score (0-100): \n");
        int finalExamScore = scanner.nextInt();
        System.out.print(finalExamScore);

        System.out.print("\n Did you complete the homework (yes/no): \n");
        String homeworkComplete = scanner.next().toLowerCase();
        System.out.print(homeworkComplete);

        // write code here
        if () {

        } else {

        }

        System.out.println("\n Your final grade is: " + grade);

        scanner.close();
    }
}

GradeCalculator.main(null)
```


    |           if () {

    illegal start of expression

    


## 3.6

### Learning Objective
- Compare and contrast equivalent Boolean expressions

De Morgan’s Law
- Augustus De Morgan was a 19th century mathematician whose laws or rules about __boolean__ logic allow us to simplify expressions when they are negated
Given two Boolean variables a and b:

``De Morgan's Law provides a set of rules for negating complex boolean expressions. ``

Example:

Using ``&&`` operators:

![image](https://github.com/Firestorm0986/frontend-proj/assets/108041389/e02209c1-c2f5-4dab-8106-6f97824d5322)

Using ``||`` operator:

![image](https://github.com/Firestorm0986/frontend-proj/assets/108041389/beb4e917-03c2-4709-96f9-88981ee69812)



#### More:

- !(x > 0) → (x <= 0)
- Distributing a “not” with a boolean expression “flips” the relational operator to the opposite relational operator
    - !(x < 0) → (x >= 0)
    - !(x >= 0) → (x < 0)
    - !(x == 0) → (x != 0)
    - ! (x != 0) → ( x == 0) 


#### A bit more complex:
![image](https://github.com/Firestorm0986/frontend-proj/assets/108041389/1fa9c9c3-db17-443c-94cc-0be8e6e62436)

#### Proving the law using tables
![image](https://github.com/Firestorm0986/frontend-proj/assets/108041389/cd135d80-df08-442b-aa73-35e8afbef96b)


```Java
public class Example {
    public static void main(){
        boolean x = true;
        boolean y = false;

        // Original expression
        boolean originalExp = !(x && y);

        // Applying De Morgan's Law
        boolean equivalentExp = !x || !y;

        // Checking if the results are equivalent
        System.out.println("Are the expressions equivalent? " + (originalExp == equivalentExp));

    }
}
Example.main()
```

    Are the expressions equivalent? true



```Java
public class Example2 {
    public static void main(){
        boolean p = true;
        boolean q = true;

        // Original expression
        boolean originalExp2 = !(p || q);

        // Applying De Morgan's Law
        boolean equivalentExp2 = !p && !q;

        // Checking if the results are equivalent
        System.out.println("Are the expressions equivalent? " + (originalExp2 == equivalentExp2));
    }
}

Example2.main()
```

    Are the expressions equivalent? true



```Java
public class Example3 {
    public static void main(){
        boolean a = true;
        boolean b = false;
        boolean c = true;

        // Original expression
        boolean originalExp3 = !(a && b) || (c || !b);

        // Applying De Morgan's Law
        boolean equivalentExp3 = (!a || !b) || (c || b);

        // Checking if the results are equivalent
        System.out.println("Are the expressions equivalent? " + (originalExp3 == equivalentExp3));

    }
}

Example3.main()
```

    Are the expressions equivalent? true


#### De Morgan's Law Practice

Negate the following expressions:

``1. !(A || B)``

``2. !(A || B && C)``

``3. !(A && (B || C))``

1. ``!(A || B)``
  
  ``By De Morgan's Law: !A && !B``

2. ``!(A || B && C)``

   ``By De Morgan's Law: !A && (!B || !C)``

3. ``!(A && (B || C))``

   ``By De Morgan's Law: !A || (!B && !C)``


## 3.7

### Learning Objective
- Compare object reference using boolean expressions in program code

![image](https://github.com/Ishi-Singh/Fastpages/assets/82348259/40517c16-2f13-460c-89ea-f8f53a0a7a34)

An if statement using == to compare myHouse and momsHouse will be true but false for myHouse and annasHouse because the objects are not the same even though they have same parameters. This means that == will only return true if it is the same object, not a reference or copy of that object. 


```Java
String a = "Hello";
String b = "Hello";
String c = a;
String d = new String("Hello");

System.out.println(a == c);
System.out.println(d == b);
System.out.println(a == b);
System.out.println(a == d);
```

    true
    false
    true
    false


![image](https://github.com/Ishi-Singh/Fastpages/assets/82348259/998e721e-1c5e-41a7-9799-13cfdee14ee2)

When you want to compare objects you can use the .equal() method, it will return true if the objects have the same attributes even if they aren't identical.


```Java
String a = "Hello";
String b = "Hello";
String c = a;
String d = new String("Hello");

System.out.println(a.equals(c));
System.out.println(d.equals(b));
System.out.println(a.equals(b));
System.out.println(a.equals(d));
```

    true
    true
    true
    true


# Hacks 

- Complete popcorn hacks - 0.1 points
- Coding hacks - 0.8 points
    - Complexity: 0.4 points
    - Functionality: 0.4 points

## Coding Practice

Create a program that validates a user's password based on the following criteria:

1. The password must be at least 8 characters long.
2. The password must contain at least one uppercase letter.
3. The password must contain at least one lowercase letter.
4. The password must contain at least one digit (0-9).
5. The password must contain at least one special character (!, @, #, $, %, ^, &, *).

Write a Java program that prompts the user to enter a password and then checks if it meets the above criteria. If the password meets all the criteria, print "Password is valid." If not, print a message indicating which criteria the password fails to meet.



```Java
import java.util.Scanner;

public class PasswordChecker {
    private static String[] specialChar = {"!", "@", "#", "$", "%", "^", "&", "*"};
    private static boolean lengthCheck(String password) {
        String[] passArr = null;
        passArr = password.split("");
        if (passArr.length>=8){
            return true;
        }
        else {
            return false;
        }
    }
    private static boolean uppercaseCheck(String password) {
        for (int i = 0; i < password.length(); i++) {
            if (Character.isUpperCase(password.charAt(i))) {
              return true;
            }
        }
        return false;
    }
    private static boolean lowercaseCheck(String password) {
        for (int i = 0; i < password.length(); i++) {
            if (Character.isLowerCase(password.charAt(i))) {
              return true;
            }
        }
        return false;
    }
    private static boolean digitCheck(String password) {
        for (int i = 0; i < password.length(); i++) {
            if (Character.isDigit(password.charAt(i))) {
              return true;
            }
        }
        return false;
    }
    private static boolean specialCheck(String password) {
        for (int i = 0; i < password.length(); i++) {
            for (int j = 0; j < 8; j++) {
                if (String.valueOf(password.charAt(i)).equals(specialChar[j])) {
                    return true;
                }
            }
        }
        return false;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print(" Enter your password(must be 8 characters long, at least one uppercase, at least one lowercase, at least one digit, at least one special character) \n");
        String password = scanner.nextLine();
        System.out.print(password);


        String result;
        if (lengthCheck(password) && uppercaseCheck(password) && lowercaseCheck(password) && digitCheck(password) && specialCheck(password)) {
            result = "valid.";
        } else {
            result = "not valid.";
        }

        System.out.println("\n Password is " + result);

        scanner.close();
    }
}

PasswordChecker.main(null);
```

     Enter your password(must be 8 characters long, at least one uppercase, at least one lowercase, at least one digit, at least one special character) 
    Rachit12#
     Password is valid.

