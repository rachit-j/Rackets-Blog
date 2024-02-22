---
toc: True
comments: True
layout: post
title: Thymeleaf Admin Panel Lesson
description: Use Thymeleaf to make a dynamic and cool page for your Admin Panel!
courses: {'labnotebook': {'week': 20}}
type: tangibles
---

# Basics of Thymeleaf

Thymeleaf is a spring-integrated way to easily make pages that can integrate seamlessly with API calls. It allows you to easily list out what is needed from each of your SQL tables without needing to make a direct request. An extremely beneficial aspect of thymeleaf is the ability to also create an admin panel, which allows you to perform CRUD operations. 

Necessary Resources:

Notebook: `wget `
Backend: `git clone https://github.com/nVarap/BackendThymeleaf.git`

# Bare Basics of jQuery Syntax

### 1. Selecting Elements:

- To select an HTML element with a specific ID:
  ```javascript
  $("#myElementId")
  ```

- To select HTML elements with a specific class:
  ```javascript
  $(".myClassName")
  ```

- To select all elements of a particular type:
  ```javascript
  $("p") 
  ```

### 2. Event Handling:

- To handle a click event:
  ```javascript
  $("#myButton").click(function() {
      // code to be executed when the button is clicked
  });
  ```

- To handle a form submission:
  ```javascript
  $("form").submit(function() {
      // code to be executed when the form is submitted
  });
  ```

### 3. Requests:
```javascript
    $(document).ready(function() {
        $("#data").click(function() {
            $.ajax({
                type: "GET",
                url: "/read",  // Adjust the URL based on your Spring controller mapping
                success: function(data) {
                    $("#result").html(data);
                },
                error: function() {
                    $("#result").html("Error fetching data."); // catches any error, you may even consider printing out the err.
                }
            });
        });
    });
```


## Thymeleaf Syntax Guide

Here is most of the syntax that you need to know for Thymeleaf, you should know most of this already, so I'll go through this really quickly.

### Basic Expressions

There are 5 basic tyes of expressions

1. **Variable Expressions (`${}`):**
   - Used for Spring Expression Language operations on context variables.
   - Example: `${session.user.name}`.

2. **Selection Expressions (`*{}`):**
   - Operates on the previous object instead of the entire context.
   - Example: `*{title}` within a specified object.

3. **Message Expressions (`#{}`):**
   - Can access messages from external sources, often .properties files.
   - Example: `#{title}` or `#{message.entrycreated(${entryId})}`.

4. **Link (URL) Expressions (`@{}`):**
   - Creates URLs and can rewrite URLs.
   - Example: `@{/order/list}` or `@{/order/details(id=${orderId},type=${orderType})}`.

5. **Fragment Expressions (`~{}`):**
   - Represents sections of markup for replication and inclusion in other templates.
   - Example: `~{footer :: #main/text()}`.

### Conditionals

```html
<div th:if="${condition}">when the condition is true.</div>
<div th:unless="${condition}">when the condition is false.</div>
```

### Iteration

Can use th:each with status to get information about the iteration as well:
```html
<ul>
    <li th:each="book, iterStat : ${books}" th:text="${iterStat.count + '. ' + book.title}"></li>
</ul>
```

## Anatomy

An easy look at how thymeleaf anatomy works is the division between *controllers* and *templates*. Templates are in `src/main/resources/templates/`, and can even be placed in to different folders depending on if they're all on the same project (such as person).

However, the controllers can really be located anywhere, but for the sake of organization, all of the controllers used in this section are located in `/src/main/spring_portfolio/controllers/`, because that's a folder named controllers. However, you can also have controllers anywhere, and you may want to, depending on your project.

# Example: Jokes Thymeleaf Page

This page displays all of the jokes from the jokes API, but also see if they are liked or not liked by easily checking the background. This is a good example of how thymeleaf can be used. (This example is in our backend.)

## Controller
This is the controller that does all the computation. Right now, all this does is upload and find the jokes. Later, this class can do even more and have even more functions. A controller must be defined with the `@Controller` annotation, in order to let Java know that it's planned to be a controller. Then anywhere in teh class you can create a GET api endpoint and return the **name** of the html file you are trying to render. This then renders the thymeleaf template


```python
package com.nighthawk.spring_portfolio.controllers;

import java.util.List;
import java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import com.nighthawk.spring_portfolio.mvc.jokes.JokesJpaRepository;
import com.nighthawk.spring_portfolio.mvc.jokes.Jokes;

@Controller
public class JokesThymeLeafController {

    @Autowired
    private JokesJpaRepository repository; // NEEDED FOR JOKES
    // Pulls from repository

    @GetMapping("/jokestl") // Link you visit
    public String jokes(Model model) { 
        // The MODEL is what can store values computed in the controller
        List<Jokes> jokes = repository.findAll();
        model.addAttribute("jokes", jokes); // adds the jokes as a list
        return "thyme"; // This corresponds to the Thymeleaf template name (src/main/resources/templates/thyme.html)
    }   
}
```

## Template

The template is the actual HTML that displays everything. This specific part demonstrates the use of a template, looping through a variable stored by the model, and then displaying certain aspects of that model. These will be explained better in the following sections, but for a start we have:

1. `th:each`: effectively the for loop for thymeleaf, note the `j:${jokes}` notation, similar to a foreach loop
2. `th:style`: the style of the section
3. Note the use of bitwise comparisons such as ?, :, and even &/| for comparison within a style
4. Accessing values using dot methods
5. Lastly, all thymeleaf functions typically start with the `th:` syntax. This is to differentiate them from the rest of regular html tags.

**Thymeleaf syntax**
- `${}` 
  - Variable Expressions (variables stored by the model, brought into TL HTML)
- `*{}` 
  - Selection Expressions (Similar to variables, but only will be executed on the previously *selected* object. Allows you to get info down a hierarchy)
- `#{}` - Message Expressions
  -  Allows you to retrieve properties from files by a certain key, which can then be displayed. Useful for dynamic pages that can change with logins.
- `@{}` - Link (URL) Expressions
  - Links, either for calling APIs or redirection
- `~{}` - Fragment Expressions
  - Allows insertion of fragments of information, such as template or header. Then you can insert these fragments using `th:insert="${frag}"` or utilize them with templates with `layout:decorate="~{layouts/base}"`, as can be seen in almost every thymeleaf template. Fragments are important do you don't code the same thing over and over again.



```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org"> 

<head>
    <meta charset="UTF-8">
    <title>Jokes!</title>
</head>

<body style="background-color: aqua;">
    <h1> Jokes! </h1>
    <div th:each="j : ${jokes}">
        <div th:style="${j.haha &gt; j.boohoo ? 'background-color: #90EE90; border: 5px solid black;' : 'background-color: #FFB3B2; border: 5px solid black;'}">
            <p th:text="${j.joke}"></p>
            <p>Upvotes: <span th:text="${j.haha}"></span>
            <p>Downvotes: <span th:text="${j.boohoo}"></span>
        </div>
    </div>
</body>

</html>
```

This is a small example of what thymeleaf can do, but here's the output. 


<img width="1439" alt="Screenshot 2023-12-17 at 11 34 42 PM" src="https://github.com/nVarap/CSABlog/assets/108639268/a673921c-0dd5-4e31-98b2-406a90a2d0f9">

That's a lot with so little! Imagine even adding CRUD functionality to this! This demonstrates the sheer power of Thymeleaf.


## Thymeleaf Formatting
- Thymeleaf provides various formatting options to display data in a more human-readable way. These options include date and number formatting. Let's explore date formatting as an example.

### Date Formatting
- Thymeleaf allows you to format dates using the `th:format` attribute. Here's an example:

```html
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Thymeleaf Date Formatting</title>
</head>
<body>
    <h1>Date Formatting Example</h1>
    
    <p>Current Date: <span th:text="${#dates.format(#dates.createNow(), 'dd-MM-yyyy')}"></span></p>
</body>
</html>
```

- In this example, the `#dates.createNow()` method creates the current date, and `#dates.format` is used to format it as 'dd-MM-yyyy'. Adjust the format pattern based on your requirements.

## Thymeleaf If Statements
- Thymeleaf supports conditional rendering using if statements. You can use `th:if` to conditionally include or exclude elements from the rendered HTML.

### Basic If Statement


```python
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Thymeleaf If-Else Statement</title>
</head>
<body>
    <h1>Thymeleaf If-Else Statement Example</h1>
    
    <p th:if="${condition}">This paragraph is displayed when the condition is true.</p>
    <p th:else>This paragraph is displayed when the condition is false.</p>
</body>
</html>
```

- Replace `${condition}` with your actual condition. The `th:if` attribute includes the element when the condition is true, and `th:unless` includes it when the condition is false.

### If-Else Statement
- Thymeleaf also supports if-else statements using `th:if` and `th:else`.

# Exception Handlers



```python
@ControllerAdvice
public class ExceptionHandler {

    @ExceptionHandler(value = Exception.class)
    public String defaultErrorHandler(HttpServletRequest req, Exception e) throws Exception {
        return "error"; // Returns 'error.html' Thymeleaf template
    }
}
```

- @ControllerAdvice classes can handle exceptions across multiple controllers
- The @ExceptionHandler(value = Exception.class) method runs when an exception is thrown and the contents return an error thymeleaf template

# Redirection

Redirection allows you to redirect users to a new page. This is particularly useful which will be covered in detail later. 

This is all going to be covered more but we can in essence change "error" to redirect user's to a login page or whatever is necessary upon certain errors.

# Error management

Thymeleaf provides some easy ways to display error messages originating from a Spring-based back-end application. 

You need to have specified what each field requires for field errors.


```python
import javax.validation.constraints.*;

public class User {

    @NotEmpty(message = "Username is required.")
    @Size(min = 2, max = 30, message = "Username must be between 2 and 30 characters.")
    private String username;

    @NotEmpty(message = "Password is required.")
    @Size(min = 8, message = "Password must be at least 8 characters.")
    private String password;
}

```

Displaying errors on the frontend

> This code checks if there are any errors and if so iterates and displays them.


```python
<div th:if="${#fields.hasErrors('*')}">
    <p th:each="err : ${#fields.errors('*')}" th:text="${err}"></p>
</div>
```

Field Errors: A field error checks the contents of a field against specified conditions from the previous section. For example, this is useful to make sure user's submit a valid email.


```python
<form action="#" th:action="@{/submit}" th:object="${user}" method="post">
    <input type="text" th:field="*{username}">
    <span th:errors="*{username}" class="error"></span>
    <input type="password" th:field="*{password}">
    <span th:errors="*{password}" class="error"></span>
    <input type="submit" value="Submit">
</form>
```

Notice each contains th:errors="*{fieldName}." Some useful fieldnames built into thymeleaf are

### Login Redirection

When it comes to login redirection and Thymeleaf, the connection lies in how you structure and render your HTML templates to handle the redirection logic. Thymeleaf allows you to handle redirection by specifying URLs or endpoints in your controller methods. When a redirection occurs, Thymeleaf takes care of generating the appropriate HTML response with the redirection information.

1. **Dynamic Content with Thymeleaf:**
   Thymeleaf is a template engine that allows you to embed dynamic content directly into your HTML templates. It uses expressions and attributes to integrate with the server-side data. In the context of login redirection, Thymeleaf enables you to conditionally display content based on the state of the application, such as whether a user is authenticated or not.

   ```html
   <!-- Display username if authenticated -->
   <div th:if="${session.username}">
       <p>Welcome, <span th:text="${session.username}"></span>!</p>
   </div>
   ```

   Here, Thymeleaf checks if the `session.username` attribute exists (indicating authentication) and displays a welcome message with the username if true.

2. **Redirection Handling in Templates:**
   Thymeleaf allows you to handle redirection by specifying URLs or endpoints in your controller methods. When a redirection occurs, Thymeleaf takes care of generating the appropriate HTML response with the redirection information.

   ```java
   // Redirect to the home page after successful login
   return "redirect:/home";
   ```

   This line in the controller method instructs Thymeleaf to redirect to the `/home` endpoint. The corresponding template for the home page (`home.html`) can then be designed using Thymeleaf to display content based on the user's authentication status.

3. **Conditional Rendering in Templates:**
   Thymeleaf makes it easy to conditionally render content based on variables or expressions. For example, you might want to show different content to authenticated and non-authenticated users.

   ```html
   <!-- Conditional rendering based on authentication status -->
   <div th:if="${session.username}">
       <p>Welcome, <span th:text="${session.username}"></span>!</p>
       <!-- Other authenticated user content -->
   </div>
   <div th:unless="${session.username}">
       <p>Please log in to access the content.</p>
       <!-- Login form or login-related content -->
   </div>
   ```

   Here, Thymeleaf checks whether the `session.username` attribute exists. If it does, it displays a welcome message; otherwise, it prompts the user to log in.

4. **Error Handling and Display:**
   Thymeleaf can also be used to handle and display errors in your templates. For instance, when authentication fails, you can add an error message to the model, and Thymeleaf can render this message on the login page.

   ```java
   // Authentication failed, add an error message to the model
   model.addAttribute("error", "Invalid username or password");
   // Redirect back to the login page
   return "login";
   ```

   In the `login.html` template, you can then use Thymeleaf to conditionally display the error message.

   ```html
   <!-- Display error message if present -->
   <div th:if="${error}" style="color: red;">
       <p th:text="${error}"></p>
   </div>
   ```

   Thymeleaf's conditional rendering allows you to dynamically show or hide elements based on the existence of error messages.

  ### So now here's a full example:



```python
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import javax.servlet.http.HttpSession;

@Controller
public class LoginController {

    @PostMapping("/login")
    public String login(@RequestParam String username,
                        @RequestParam String password,
                        HttpSession session,
                        Model model) {
        // Replace this with your actual authentication logic
        if ("admin".equals(username) && "password".equals(password)) {
            // Authentication successful, create a session
            session.setAttribute("username", username);
            // Redirect to the home page after successful login
            return "redirect:/home";
        } else {
            // Authentication failed, add an error message to the model
            model.addAttribute("error", "Invalid username or password");
            // Redirect back to the login page
            return "login";
        }
    }
}
```



In this example, we are using Spring MVC annotations along with Thymeleaf. Here's how it connects to Thymeleaf:

1. **Controller Annotation:**
   ```java
   @Controller
   ```

   This annotation marks the class as a Spring MVC controller. It tells Spring to consider this class when handling web requests.

2. **RequestMapping Annotation:**
   ```java
   @PostMapping("/login")
   ```

   This annotation maps the `login` method to handle HTTP POST requests to the `/login` endpoint.

3. **Thymeleaf Redirect:**
   ```java
   return "redirect:/home";
   ```

   This line specifies a redirect using Thymeleaf. It tells Spring to redirect to the `home` endpoint. The actual redirection URL will be resolved by the Spring MVC configuration.

4. **Model Attribute for Error:**
   ```java
   model.addAttribute("error", "Invalid username or password");
   ```

   If authentication fails, an error message is added to the model. This message can be displayed on the login page to inform the user about the unsuccessful login attempt.

5. **Returning Template Names:**
   The method returns strings representing the names of Thymeleaf templates. For example, `"login"` refers to the `login.html` template.

In your Thymeleaf template (`login.html`), you can use Thymeleaf expressions to display the error message and create links or buttons for redirection.

Here's a simplified example of a Thymeleaf template (`login.html`):

```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>

    <!-- Display error message if present -->
    <div th:if="${error}" style="color: red;">
        <p th:text="${error}"></p>
    </div>

    <!-- Conditional rendering based on authentication status -->
    <div th:if="${session.username}">
        <p>Welcome, <span th:text="${session.username}"></span>!</p>
        <!-- Other authenticated user content -->
        <a href="/logout">Logout</a>
    </div>
    <div th:unless="${session.username}">
        <form action="/login" method="post">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            <br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            <br>
            <button type="submit">Login</button>
        </form>
    </div>

</body>
</html>
```

In this example:

- The controller method sets the `error` attribute in the model if authentication fails.
- The Thymeleaf template checks for the presence of the `error` attribute and displays an error message if it exists.
- The template also uses Thymeleaf expressions to conditionally render content based on the existence of `session.username`. If the user is authenticated, it displays a welcome message and a logout link; otherwise, it shows the login form.

Please note that the actual URLs (`/home`, `/login`, `/logout`) and styling will vary based on your specific requirements and application structure. 

## Thymeleaf & CRUD Operations:
> The code shown will be in context to our own website, Linkr, and will accomplish CRUD operations in our idea database.


```python
public class Idea {
    private Long id;
    private String ideaName;
    private String description;
    private String username;
}
```


```python
// IdeaController.java
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@Controller
@RequestMapping("/ideas")
public class IdeaController {

    private List<Idea> ideas = new ArrayList<>();
    private Long idCounter = 1L;

    @GetMapping
    public String listIdeas(Model model) {
        model.addAttribute("ideas", ideas);
        return "ideas/list";
    }

    @GetMapping("/create")
    public String createIdeaForm(Model model) {
        model.addAttribute("idea", new Idea());
        return "ideas/create";
    }

    @PostMapping("/create")
    public String createIdea(@ModelAttribute Idea idea) {
        idea.setId(idCounter++);
        ideas.add(idea);
        return "redirect:/ideas";
    }

    @GetMapping("/edit/{id}")
    public String editIdeaForm(@PathVariable Long id, Model model) {
        Idea idea = findById(id);
        model.addAttribute("idea", idea);
        return "ideas/edit";
    }

    @PostMapping("/edit/{id}")
    public String editIdea(@PathVariable Long id, @ModelAttribute Idea idea) {
        idea.setId(id);
        updateIdea(idea);
        return "redirect:/ideas";
    }

    @GetMapping("/delete/{id}")
    public String deleteIdea(@PathVariable Long id) {
        ideas.removeIf(idea -> idea.getId().equals(id));
        return "redirect:/ideas";
    }

    private Idea findById(Long id) {
        return ideas.stream().filter(idea -> idea.getId().equals(id)).findFirst().orElse(null);
    }

    private void updateIdea(Idea updatedIdea) {
        int index = ideas.indexOf(findById(updatedIdea.getId()));
        if (index != -1) {
            ideas.set(index, updatedIdea);
        }
    }
}
```


```python
```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>Idea List</title>
</head>
<body>

<h2>Idea List</h2>

<table>
    <thead>
    <tr>
        <th>ID</th>
        <th>Idea Name</th>
        <th>Description</th>
        <th>Username</th>
        <th>Actions</th>
    </tr>
    </thead>
    <tbody>
    <tr th:each="idea : ${ideas}">
        <td th:text="${idea.id}"></td>
        <td th:text="${idea.ideaName}"></td>
        <td th:text="${idea.description}"></td>
        <td th:text="${idea.username}"></td>
        <td>
            <a th:href="@{/ideas/edit/{id}(id=${idea.id})}">Edit</a>
            |
            <a th:href="@{/ideas/delete/{id}(id=${idea.id})}">Delete</a>
        </td>
    </tr>
    </tbody>
</table>

<br/>

<a th:href="@{/ideas/create}">Create New Idea</a>

</body>
</html>
```
```
