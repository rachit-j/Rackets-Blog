---
toc: True
comments: True
layout: post
title: Spring/Thymeleaf Lesson
description: The Divorced Coders teaching Spring/Thymeleaf for Period 3 CSA
courses: {'labnotebook': {'week': 16}}
type: hacks
authors: Aditya Nawandhar, Akshat Parikh, Krishiv Mahendru, Parav Salaniwal, Raymond Sheng, Rohin Sood
---

# Spring/Thymeleaf Lesson

## Lesson Objectives:
* Understand the role of Thymeleaf in server-side rendering.
* Learn how to integrate Thymeleaf with the Spring Framework.
* Implement a sign-in page using Thymeleaf for securing specific API endpoints.

## Introduction:
* Briefly introduce the concept of server-side rendering and its advantages.
* Discuss the role of template engines in generating dynamic HTML.
* Introduce Thymeleaf as a template engine for Java Spring.


# What is Spring?

## Unveiling the Power of the Spring Framework

### Basics of Spring:

**Spring** is a comprehensive, open-source framework for building robust and scalable Java-based applications. It provides a structured and modular approach to application development, addressing challenges in various domains such as enterprise, web, and microservices.

## Why Choose Spring for Backend Development?

Simplified Configuration: Spring reduces the complexity of configuration through XML-based or annotation-driven approaches. This simplifies application setup and promotes a more straightforward development process.

Extensive Ecosystem: Spring offers a vast ecosystem of modules that cater to different aspects of application development. Modules like Spring MVC for web development, Spring Security for authentication and authorization, and Spring Data for database access enhance productivity.

Integrated Testing Support: Spring's design encourages the use of interfaces and dependency injection, making it easier to test components in isolation. This promotes the development of unit tests and ensures the reliability of the application.

# Spring Boot's Auto-Configuration for Thymeleaf

When you add Thymeleaf to your Spring Boot project, it automatically configures the necessary beans and settings.

Key Points:

- Spring Boot detects the presence of spring-boot-starter-thymeleaf in your classpath.
- It automatically sets up a TemplateEngine, 
- TemplateResolver, and ViewResolver for Thymeleaf.

## Basic Structure of Thymeleaf Templates

Thymeleaf templates are essentially HTML5 files with additional attributes for dynamic content.

Typical Template Location:

- Thymeleaf templates are typically located in src/main resources/templates in a Spring Boot project.


## Popcorn Hack:
Summarize the key features of Thymeleaf and explain why it is preferred for server-side rendering in Spring applications.

Thymeleaf allows your SpringBoot service to autoconfigure beans and helps your HTML files have better dynamic data. Lightweight, simple, easy to use.

# Spring Boot's Auto-Configuration for Thymeleaf

When you add Thymeleaf to your Spring Boot project, it automatically configures the necessary beans and settings.

Key Points:

- Spring Boot detects the presence of spring-boot-starter-thymeleaf in your classpath.
- It automatically sets up a TemplateEngine, 
- TemplateResolver, and ViewResolver for Thymeleaf.

## Basic Structure of Thymeleaf Templates

Thymeleaf templates are essentially HTML5 files with additional attributes for dynamic content.

Typical Template Location:

- Thymeleaf templates are typically located in src/main resources/templates in a Spring Boot project.

### example:


```java

<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Title</title>
</head>
<body>
    <h1 th:text="${message}">Welcome Message</h1>
</body>
</html>

```

Thymeleaf Expression Language (EL) is used to perform operations and display data within the template.

Syntax:

Basic syntax is ${...} for variables.
You can also use *{...} for objects (known as the selection variable), #{...} for messages, @{...} for URLs, and more.

### example:


```java

<p th:text="${user.name}">Default Name</p>
<p th:text="${user.age}">Default Age</p>

```

# How You Would Implement Thymeleaf in the Backend.

- Through the use of Controller wihtin the backend it is clearly displayed that the thymeleaf works best in which is where it can be defined to get outputs fom a specific outupts from data stored within the backend

# How does Thymleaf work in the backend 

- Thymeleaf is a framework within the backend spring set through the java controllers which ultimatley, allow you to develop html with attributes from the backend making for a more uer interactive base. All in All this means that Thymleaf is a way to get CRUD functionalities with a set of commands within the HTML.


```java
// Here is a Set of Sample Backend Code you may want to run in a Spring in Jupyter Notebooks is giving you a Hard Time. 
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class UserController {

    @GetMapping("/user")
    public String getUser(Model model)  // allowed to pass data 
     {
   
        String username = "John Doe";
        int age = 30;
        String email = "johndoe@example.com";

        // Adding user data to the Model
        model.addAttribute("username", username);// the model. makes thymleaf data applicable for rendering
        model.addAttribute("age", age);
        model.addAttribute("email", email);

        // Return the name of the Thymeleaf template
        return "userProfile";
    }
}
```

# Popcorn Hacks
- What do you think the Model model means and why is it important 
Answer Here: Model creates the user database itself. This allows for the information of the user to be displated. If the record doesn't exist, it is not displayed, instead "No user data availible" is shown.

# Examples With Thymeleaf Syntax in the Frontend. 


```java

<!-- Define the document type and introduce the Thymeleaf namespace  ultimatley to allow thymeleaf commands-->
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <!-- Define the character encoding -->
    <meta charset="UTF-8">
    <!-- Title of the HTML page -->
    <title>User Profile</title>
</head>
<body>
    <!-- Heading for the user profile page -->
    <h1>User Profile</h1>
    <!-- Thymeleaf conditional block: Display if 'username' exists -->
    <div th:if="${username}">
        <!-- Display Username with the value of the 'username' variable -->
        <p th:text="'Username: ' + ${username}"></p>
        <!-- Display Age with the value of the 'age' variable -->
        <p th:text="'Age: ' + ${age}"></p>
        <!-- Display Email with the value of the 'email' variable -->
        <p th:text="'Email: ' + ${email}"></p>
</div>
 <!-- Thymeleaf conditional block: Display if 'username' does not exist -->
 <div th:unless="${username}">
        <!-- Display a message when 'username' doesn't exist -->
        <p>No user data available.</p>
    </div>
</body>
</html>
```

## Here Are A list of Specifics Thymeleaf applications wihtin the frontend. 

1. **th:text**: Sets the text content of an element. `<p th:text="${variable}">Default Text</p>`

2. **th:utext**: Similar to `th:text`, but does not escape HTML characters. `<p th:utext="${unescapedHTML}">Default HTML</p>`

3. **th:if, th:unless**: Conditional rendering of elements. `<div th:if="${condition}">Render if true</div> <div th:unless="${condition}">Render if false</div>`

4. **th:each**: Iterates over collections. `<ul><li th:each="item : ${items}" th:text="${item}"></li></ul>`

5. **th:object, th:field**: Binds form fields to a model object for form handling. `<form th:object="${user}" th:action="@{/save}" method="post"><input type="text" th:field="*{username}" /><button type="submit">Submit</button></form>`

6. **th:href**: Creates links within the application. `<a th:href="@{/home}">Home</a>`

7. **th:class**: Sets CSS classes conditionally. `<div th:class="${condition} ? 'active' : 'inactive'">Element</div>`


### PopCorn Hack 
- List 3 more Attributes of Thymleaf in the Frontend
1. Conditional Rendering
2. Text Replacement
3. Iteration

# Specific HTML Attributes within Thymeleaf
- text substitution, conditional rendering, and iteration.

### Text Substitution 
- The usage of text substitution is an act of replacing text or content within HTML elements based on values provided by the server-side application. In Thymeleaf, it's achieved using attributes like th:text or th:utext.


PopCorn Hack: explain what the following code is doing:


```java

<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>Text Substitution Example</title>
</head>
<body>
    <h1>Welcome, <span th:text="${username}">Guest</span>!</h1>
    <!-- If 'username' exists in the model, it will replace 'Guest' -->
</body>
</html>
```

This HTML code is a Thymeleaf template that automatically displays a username. If the username variable is provided by the server-side model, it replaces the default text "Guest" in the greeting message.

### Conditional Rendering 

- Conditional Rendering: This feature allows displaying or hiding content based on certain conditions. Thymeleaf provides attributes like th:if and th:unless to conditionally render HTML elements.

PopCorn Hack: explain what the following code below is doing:



```java

<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>Conditional Rendering Example</title>
</head>
<body>
    <div th:if="${isAdmin}">
        <p>Welcome, Admin!</p>
    </div>
    <div th:unless="${isAdmin}">
        <p>Welcome, User!</p>
    </div>
</body>
</html>

```

This HTML code, using Thymeleaf, displays content based on whether the isAdmin variable is true. If isAdmin is true, it shows "Welcome, Admin!"; otherwise, it displays "Welcome, User!".

# An example with Password and Security 


```java
<div th:if="${password.length() < 8}">
    <p>Password must be at least 8 characters long.</p>
</div>
<div th:if="${password.length() >= 8}">
    <p>Password is strong.</p>
</div>

```

### Iteration
- Iteration: It involves looping through collections or arrays of data to render dynamic content multiple times. Thymeleaf offers the th:each attribute for iterating over collections and rendering content for each item within the collection.

PopCorn Hack Explain What this is Doing:


```java
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>Iteration Example</title>
</head>
<body>
    <ul>
        <li th:each="item : ${items}" th:text="${item}">Default Item</li>
    </ul>
</body>
</html>

<!-- Thymeleaf iteration: For each element in ${items}, -->
 <!-- Thymeleaf assigns the current element to a local variable named item. -->
 <!-- It iterates through all the elements present in the ${items} collection. -->


```

This Thymeleaf template iterates over a collection named items provided by the server-side model. For each element in the collection, it creates a list item in an unordered list, displaying the content of each element.

## Hacks
- Complete Popcorn Hacks
- Create a controller that uses the model function, then in html use the methods in Thymeleaf that were taught (AT BOTTOM)
- Extra Points For Creativity.

## Introduction to Spring Security
Spring Security is a robust framework designed to handle authentication, authorization, and various other security aspects in Java applications. Today, we'll focus on its role in securing API endpoints.
Securing API endpoints is crucial to safeguard sensitive resources and functionalities from unauthorized access. Spring Security provides a flexible and customizable solution for implementing security measures within your applications.

### Thymeleaf Template:

Creating a Thymeleaf template for the sign-in page is like designing the look of the entrance. Let's make it user-friendly and straightforward.


This is like the design of the sign-in form, telling users what to fill in.


```java
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Sign In</title>
</head>
<body>

    <h2>Admin Sign In</h2>

    <form th:action="@{/login}" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>

        <button type="submit">Sign In</button>
    </form>

</body>
</html>
```

## Comprehensive:


```java
<!-- This page is illustrative and contains ideas about HTML formatting -->
<!DOCTYPE HTML>
<!-- Signals to the Layout Dialect which layout should be used to decorate this View -->
<html xmlns:layout="http://www.w3.org/1999/xhtml" xmlns:th="http://www.w3.org/1999/xhtml"
      layout:decorate="~{layouts/base}" lang="en">

<head>
    <!-- Page specific head additions -->
    <title>Login</title>
</head>

<body>
<th:block layout:fragment="body" th:remove="tag">

    <div class="container py-4">
        <header class="pb-3 mb-4 border-bottom border-primary text-dark">
            <span class="fs-4">Login Page</span>
        </header>
    </div>

    <div class="container py-4 text-light bg-success">

        <div class="container bg-secondary py-4">
            <div class="p-5 mb-4 bg-light text-dark rounded-3">
                <h1>Login</h1>
                <label for="email">Username:</label><br>
                <input type="text" id="username" name="username"><br>
                <label for="password">Password:</label><br>
                <input type="text" id="password" name="password"><br><br>
                <input type="submit" value="Login" onclick="login()">
                <p id="message"></p>
            </div>
        </div>
        <script>
            function login() {
                var email = document.getElementById('username').value;
                var password = document.getElementById('password').value;
                var data = {email:email, password:password};
                fetch("/human/authenticate", {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(data)}).then((data) => { //handling authentication
                    if (data.status == 200) {
                        window.location.replace("/mvc/person/read");
                    } else {
                        document.getElementById('message').innerHTML = "Invalid email or password"
                    }
                });
            }
        </script>

    </div>

</th:block>
</body>
```

## API View Controller: 



```java

<!-- This page is illustrative and contains ideas about HTML formatting -->
<!DOCTYPE HTML>
<!-- Signals to the Layout Dialect which layout should be used to decorate this View -->
<html xmlns:layout="http://www.w3.org/1999/xhtml" xmlns:th="http://www.w3.org/1999/xhtml"
      layout:decorate="~{layouts/base}" lang="en">

<head>    <!-- Page specific head additions -->
    <title>Person List</title>
</head>

<!-- <body> -->
<body>
<th:block layout:fragment="body" th:remove="tag">
    <div class="container py-4 bg-primary">
        <!-- Page specific body additions -->
        <header class="pb-3 mb-4 border-bottom">
            <a href="#" class="d-flex align-items-center text-light text-decoration-none">
                <span class="fs-4">Database SQL Person</span>
            </a>
        </header>

        <div class="container py-4 text-light bg-success">

            <h2>Person Viewer</h2>
            <a th:href="@{/mvc/person/create/}">Create Person</a>
            <div class="row align-items-md-stretch">
                <table class="table">
                    <thead>
                    <tr>
                        <th>ID</th>
                        <th>User ID</th>
                        <th>Person</th>
                        <th>Age</th>
                        <th>Action</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr th:each="person : ${list}">
                        <td th:text="${person.id}">Person ID</td>
                        <td th:text="${person.email}">Birth Date</td>
                        <td th:text="${person.name}">Name</td>
                        <td th:if="${person.getAge() != -1}" th:text="${person.getAge()}">Age</td>
                        <td th:unless="${person.getAge() != -1}" th:text="Unknown">Unknown Age</td>
                        <td>
                            <!--- <a th:href="@{/mvc/notes/{id}(id = ${person.id})}">Notes</a> -->
                            <a th:href="@{/mvc/person/update/{id}(id = ${person.id})}">Update</a>
                            <a th:href="@{/mvc/person/delete/{id}(id = ${person.id})}">Delete</a>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </div>

        </div>
    </div>

</th:block>
</body>

</html>
```

## Hack
Create a Thymeleaf template to display when a 403 error occurs (Extra indicators for adding another error code).

# Hack Submissions
Since aws is down, its really hard to display the hacks. Therefore, I'll be providing the github links:
[403](https://github.com/rachit-j/ww3-backend/blob/master/src/main/resources/templates/error/403.html)
[405](https://github.com/rachit-j/ww3-backend/blob/master/src/main/resources/templates/error/405.html)
![Error](/Rackets-Blog/images/error.png)

Model Function Commit:
[https://github.com/rachit-j/ww3-backend/commit/387714234efdcaf46e79504da7d4ce8c53358e47](https://github.com/rachit-j/ww3-backend/commit/387714234efdcaf46e79504da7d4ce8c53358e47)
