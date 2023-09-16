---
toc: True
comments: True
layout: post
title: Java Output Objects
description: Java Ouptput Objects Hacks
type: hacks
courses: {'csse': {'week': 1}, 'csp': {'week': 1, 'categories': ['4.A']}, 'csa': {'week': 0}, 'labnotebook': {'week': 3}}
categories: ['C1.4']
---

### Hack no 1: Explain, how console.log can help find errors in code?

console.log can help find errors in code by allowing a developer to print certain steps in their code to make sure things are working correctly. When I code, I often insert print statements in my code to make sure some variables are functioning correctly, and this works on the same principle.

### Hack no 2: Relate console output on last step to a previous hack
This is similar to python, where we use the print function in python to check our variables

### Hack no 3: Adapt this tutorial to your own work.
Okay...


```java
%%js
console.log("Hello")
```


    <IPython.core.display.Javascript object>



```java
%%js 
element.textContent = "Hello, World!";
```


    <IPython.core.display.Javascript object>



```java
%%js
element.textContent = "This is a demonstration of the tutorial";

var msg = "I am hungry";

element.textContent = msg
```


    <IPython.core.display.Javascript object>


See how the above code does not work, lets resolve that


```java
%%js
let message = ["I am hungry", "Good Morning!", "Hello!"];
element.textContent = message[0] += ", " + message[1]
```


    <IPython.core.display.Javascript object>


Now that we know how we can concatenate strings and output them, lets create something a little fun! Lets create a input output system that can log messages!


```java
%%js
let messages = ["Hello", "Hi"];
function messageLog(message) {
    messages.push(message)
}

function getMessageNo(messageNo) {
    return messages[messageNo]
}
element.textContent = getMessageNo(1)
```


    <IPython.core.display.Javascript object>


Now lets try to get input


```java
%%js
prompt("hello")
```


    <IPython.core.display.Javascript object>


Finally, we drop in data, and enable a fetching mechanism at the end


```java
%%js
let messages = ["Hello", "Hi"];
function messageLog(message) {
    messages.push(message)
}

function getMessageNo(messageNo) {
    return messages[messageNo]
}
var some_message = prompt("Enter your secret message...")
var message_no = prompt("Which message would you like to recieve?")
messageLog(some_message)
element.textcontent = getMessageNo(message_no)
```


    <IPython.core.display.Javascript object>



```java

```
