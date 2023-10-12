---
toc: True
comments: True
layout: post
title: Y2K Coders FRQ
description: Y2K Coders Part 2
type: hacks
courses: {'csse': {'week': 1}, 'csp': {'week': 1, 'categories': ['4.A']}, 'csa': {'week': 0}, 'labnotebook': {'week': 7}}
categories: ['C1.4']
---

# FRQ: The Mystic Library

In the ancient city of Codeville, there's a mystic library that holds books of power. Each book has a unique energy level represented by an int. The library has a special pedestal that can hold two books at a time. When two books are placed on it, their combined energy is evaluated, and a magical event occurs.


```java
public class MysticLibrary {
    int book1Energy = 0;
    int book2Energy = 0;

    boolean eventTriggered = false;
}

```

## PART A: Energy Evaluation

Write a method evaluateEnergy that calculates the combined energy of the two books. If the combined energy exceeds a threshold of 100, an event is triggered.


```java
public class MysticLibrary {
    int book1Energy = 0;
    int book2Energy = 0;

    boolean eventTriggered = false;

    public void evaluateEnergy() {
        int combinedEnergy = book1Energy + book2Energy;
        if (combinedEnergy > 100) {
            eventTriggered = true;
        }
    }
}

```

The evaluateEnergy method calculates the total energy when both books are placed on the pedestal. If their combined energy surpasses 100, a magical event is set in motion, indicated by the eventTriggered variable.

## PART B: Energy Transfer

Sometimes, to balance the energies, the librarian transfers energy from one book to another. Write a method transferEnergy that transfers a specified amount of energy from book1 to book2.


```java
public class MysticLibrary {
    
    int book1Energy = 0;
    int book2Energy = 0;

    boolean eventTriggered = false;

    public void evaluateEnergy() {
        int combinedEnergy = book1Energy + book2Energy;
        if (combinedEnergy > 100) {
            eventTriggered = true;
        }
    }

    public void transferEnergy(int transferAmount) {
        if (book1Energy >= transferAmount) {
            book1Energy -= transferAmount;
            book2Energy += transferAmount;
        }
    }
}

```

The transferEnergy method allows the librarian to shift energy from one book to another. This is done to maintain equilibrium in the library. The method ensures that energy is only transferred if the first book has enough energy to spare.

# Grading:

1/1 Point for correctly calculating the combined energy in Part A.

1/1 Point for triggering the event based on the energy threshold in Part A.

1/1 Point for correctly transferring energy between books in Part B.

1/1 Point for ensuring that energy is only transferred if book1 has sufficient energy in Part B.
