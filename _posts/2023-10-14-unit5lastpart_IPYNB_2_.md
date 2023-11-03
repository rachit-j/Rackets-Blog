---
layout: post
title: Unit 5 Part 3
toc: True
comments: True
description: Lesson for APCSA Unit 5
courses: {'csa': {'week': 8}, 'labnotebook': {'week': 9}}
type: tangibles
---

## 5.9 this Keyword

## KEY LEARNING OBJECTIVE

Evaluate object reference expressions that use the keyword **this**.

The keyword "this" is utilized in Java to refer to the current instance of a class. In other words, it helps to clarify what variable you're referring to within the instance.


```java
public class MyClass {
    private int value;

    public void setValue(int value) {
        this.value = value; // 'this' refers to the instance variable
    }
}

```

QUESTION: **How can you use 'this' to call a constructor?**

You can call the constructor by saying this.(constructor) and then making a new instance, and then after, doing (constructorname).(function);

## 5.10 Ethical and Social Implications of Computing Systems

# KEY LEARNING OBJECTIVE

Explain the ethical and social implications of computing systems.

**Components of Ethical Implications**:

1. Legal issues and intellectual property are big concerns in program creation. Licensing open source software is a big issue, as it dictates how programmers need to comply with terms and how software can be distributed and used.


2. Data privacy is also a big issue. There are many data protection laws that programmers need to ensure that their code complies with, especially if their program works with data collection and processing.

**Components of Social Implications**:

1. There can be harmful impacts from software - malicious software can pose significant security threats.


2. Software has transformed how people communicate, access information, and interact with each other. Social media platforms, for example, have changed the way society discusses issues, while algorithms can create filter bubbles that limit exposure to diverse opinions.

**POPCORN HACKS: (0.2)**

**Write a two sentence reflection on the social and ethical implications of programming. (0.8)**

Programming holds many significant social and ethical implications, as it shapes our digital world. Programmers need to consider the consequences of their code on privacy, security, and public society, emphasizing the importance of ethics  in tech.
