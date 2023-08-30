---
toc: True
comments: True
layout: post
title: College Board Pseudo Code
description: The College Board testing language is Pseudo Code.  Pseudo mean kind-of language that we will compare to Python.
courses: {'csp': {'week': 0}}
type: hacks
---

## Learning College Board Pseudo Code
> College Board uses a kind-of programming language in its Multiple Choice exam. There are thousands of different programming languages have been created, and more are being created every year.  College Board has designed a pseudo code, a non operational programming language, to highlight concepts that it wants every student to learn.

College Board is trying to remain neutral and build Computer Science Principles off of any language, thus the Teacher is left to pick the language(s) according to application and curriculum. 

College Board Pseudo Code [Exam Reference Sheet](https://apcentral.collegeboard.org/media/pdf/ap-computer-science-principles-exam-reference-sheet.pdf)


### Comparison of CB Pseudo Code to Python with descriptions

Command Vocabulary | Pseudo code         | Python                 | Purpose
Output       | DISPLAY(expression) | print(expression, end=" ") | Displays the value of expression, followed by a space. Python defaults to newline, thus the end=" "
Input        | a ← INPUT()         | a = input(prompt)      | Accepts a value from the user and returns it to the variable a.
Assignment   |	a ← expression	   | a = expression         | Evaluates expression and assigns the result to the variable a.
Selection    | IF (expression)     | if expression:         | Run commands in the code block associated with the selection
Iteration n times     |	REPEAT n TIMES      | for i in range(n): | Repeat commands in the code block associated withe the iteration n times
Iteration expression  | REPEAT UNTIL (expression) |	while expression: |  Repeat commands in the code block associated withe the iteration while expression is true
List Assignment | list ← [expression1, expression2, expression3] | list = [expression1, expression2, expression3] | Assigns 3 values to list, value can be literal or expressions
First index in List     |	list[1] | list[0] | Access the 1st element in the list[].  FYI, most programming languages start a zero.
Last index in List    | list[LENGTH(list)] | list[len(list) - 1] | Access the last element in the list[].  If you start at zero, last element is length - 1.
Define Procedure      | PROCEDURE name (parameter) | def name(parameter): |  Create a procedure containing a sequence of programming instructions.
Expression equals     |	a = b	| a == b  | Evaluate if assigned value of a equals assigned value of b
Expression not equals |	a ≠ b	| a != b  | Evaluate if assigned value of a is NOT equal to assigned value of b

### Pseudo code IF Code Block
```
a ← 1
b ← 1

IF (a = b) {
   DISPLAY("A equals B")
}
```


```python
# Python code if block to match Pseudo Code
a = 1
b = 1
if (a == b):
    # Python uses indent to establish code block, Teacher use tab key
    print("A equals B")
```

## Hacks
> Key Learnings.  It is very important that you become fluent in " Vocabulary" and researching problems.

- Code a JavaScript cell, this must start with %%js%% in first line of cell. Match the IF condition example in this blog.

- Code a REPEAT n TIMES as described in comparison sheet in Pseudo code, Python, and JavaScript.  Be sure to comment your code.
    -  REPEAT 100 TIMES
    -  Sum all the numpers
    -  PRINT the result

- Reflect on our PSEUDO code and how it helped with your problem solving in these hacks.  

- Maked efinition for: code block, sequence, selections, iteration.  Consider a strategy to remember Pseudo Code, Python and JavaScript for these definitions.


