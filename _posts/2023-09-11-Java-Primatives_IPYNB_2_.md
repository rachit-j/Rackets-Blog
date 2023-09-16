---
toc: True
comments: True
layout: post
title: Java Output Objects
description: Java Ouptput Objects Hacks
type: hacks
courses: {'csse': {'week': 1}, 'csp': {'week': 1, 'categories': ['4.A']}, 'csa': {'week': 0}, 'labnotebook': {'week': 4}}
categories: ['C1.4']
---

### This is the hack for Java Primatives
The following is a GPA Calculator


```Java

// Define the GPACalculator class
class GPACalculator {
    private int totalSubjects;
    private double totalPoints;

    public GPACalculator() {
        totalSubjects = 0;
        totalPoints = 0.0;
    }

    public boolean addSubject(String subject, int credits, double grade) {
        // Ensure valid data types and inputs
        if (credits > 0 && grade >= 0 && grade <= 4.0) {
            totalSubjects++;
            totalPoints += credits * grade;
            return true;
        } else {
            System.out.println("Invalid input. Please provide valid inputs.");
            return false;
        }
    }

    public double calculateGPA() {
        if (totalSubjects > 0) {
            return totalPoints / totalSubjects;
        } else {
            return 0.0;
        }
    }
}

```


```Java

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Initialize the GPA calculator
        GPACalculator gpaCalculator = new GPACalculator();

        // Input subjects, credits, and grades
        while (true) {
            System.out.print("Enter subject name (or 'quit' to exit): ");
            String subjectName = scanner.nextLine();

            if (subjectName.equalsIgnoreCase("quit")) {
                break;
            }

            System.out.print("Enter credits for " + subjectName + ": ");
            int credits = scanner.nextInt();

            System.out.print("Enter grade for " + subjectName + ": ");
            double grade = scanner.nextDouble();

            // Add subject to GPA calculator
            boolean success = gpaCalculator.addSubject(subjectName, credits, grade);

            if (success) {
                System.out.println(subjectName + " added to GPA calculation.");
            }

            scanner.nextLine(); // Consume the newline character
        }

        // Calculate and display GPA
        double gpa = gpaCalculator.calculateGPA();
        System.out.println("\nYour GPA is: " + String.format("%.2f", gpa));

        scanner.close();
    }
}

```


    |   Main(null)

    cannot find symbol

      symbol:   method Main(<nulltype>)

    



```Java

```


    |   Main()

    cannot find symbol

      symbol:   method Main()

    



```Java

```
