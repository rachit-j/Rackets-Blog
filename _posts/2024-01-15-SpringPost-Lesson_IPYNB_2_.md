---
comments: True
layout: notebook
title: Spring Post and DB Lesson
description: Spring Post and DB Lesson P3
type: hacks
toc: True
courses: {'labnotebook': {'week': 19}}
---

## Background - Live Demo
- Request to user
- User database


```python
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Account Login</title>
<style>
    /* Use a gradient background for the body */
    body {
        font-family: Arial, sans-serif;
        background: linear-gradient(to right, #74ebd5, #acb6e5);
        margin: 0;
        display: flex;
        justify-content: center;
    }
    /* Use a white container with rounded corners and a drop shadow for the login form */
    .container {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
        padding: 40px;
        text-align: center;
    }
    /* Use a large and bold font for the title */
    .post-title {
        font-size: 3em;
        font-weight: bold;
        margin: 0;
        padding: 0;
    }
    /* Use a smaller font for the subtitle */
    .subtitle {
        font-size: 1.2em;
        margin: 10px 0;
    }
    /* Use a light blue button with a hover effect for the sign up button */
    #signUpButton {
        display: block;
        margin: 20px auto;
        padding: 10px 20px;
        background-color: #7ed6df;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    #signUpButton:hover {
        background-color: #22a6b3;
    }
    /* Use a flexbox layout for the login form */
    #logind {
        display: flex;
        justify-content: center;
        width: 60%;
        margin-left: 20%;
    }
    /* Use a dark mode and a light mode for the input fields and buttons */
    .normal, .lightmode {
        padding: 10px;
        border: none;
        border-radius: 5px;
        margin: 5px;
    }
    .normal input, .normal button {
        width: 100%;
        padding: 10px;
        border-radius: 5px;
    }
    .normal {
        background-color: #121212;
        color: white;
    }
    .normal input {
        border: 1px solid white;
    }
    .normal button {
        background-color: #121212;
        color: white;
        cursor: pointer;
    }
    .normal button:hover {
        background-color: #333;
    }
    .lightmode {
        background-color: #F6FFF5;
        color: black;
    }
</style>
</head>
<body>
    <div class="container">
        <!-- Login Screen -->
        <div id="loginScreen">
            <form action="javascript:login_user()">
                <p id="email" class="normal">
                    <label>Email:
                        <input class="normal" type="text" name="uid" id="uid" required>
                    </label>
                </p>
                <p id="passwordd" class="normal">
                    <label>Password:
                        <input class="normal" type="password" name="password" id="password" required>
                    </label>
                </p>
                <p id="logind" class="normal">
                    <button>Login</button>
                </p>
            </form>
        </div>
        <!-- Account Details Screen (Initially Hidden) -->
        <div id="accountDetails" style="display: none;">
            <!-- Account details will go here -->
            <p>Welcome to your account!</p>
        </div>
    </div>
    <button id="signUpButton" class="button" onclick="signUpSwitch()">Sign Up</button>
</body>
<script>
        document.addEventListener("DOMContentLoaded", function () {
            // Check if the user is logged in (You need to define your own logic for this)
            if (localStorage.getItem("loggedIn") === "true") {
                showAccountDetails();
            } else {
                showLoginScreen();
            }
        });
        function showAccountDetails() {
            document.getElementById("loginScreen").style.display = "none";
            document.getElementById("signUpButton").style.display = "none";
            document.getElementById("accountDetails").style.display = "block";
            // Create and append the email and stock elements
            const emailDiv = document.createElement("div");
            emailDiv.innerHTML = "Email: " + localStorage.getItem("localEmail");
            document.getElementById("accountDetails").appendChild(emailDiv);
            const stockDiv = document.createElement("div");
            document.getElementById("accountDetails").appendChild(stockDiv);
            // Create a button element
            const button = document.createElement('button');
            button.innerText = 'LOG OUT';
            button.addEventListener('click', () => {
                // Remove the loggedIn flag from localStorage
                localStorage.removeItem("localEmail");
                localStorage.removeItem("localPassword");
                localStorage.removeItem("loggedIn");
                // Show the login screen
                showLoginScreen();
            });
            // Append the logout button to the account details section
            document.getElementById("accountDetails").appendChild(button);
        }
        function showLoginScreen() {
            document.getElementById("loginScreen").style.display = "block";
            document.getElementById("signUpButton").style.display = "block";
            document.getElementById("accountDetails").style.display = "none";
        }
        function signUpSwitch() {
            window.location.href = "/sturdy-fiesta/signup";
        }
        function login_user() {
            // You can make a POST request here to your authentication endpoint
            var url = "http://localhost:8765";
            // Comment out next line for local testing
            //  url = "https://no-papels.stu.nighthawkcodingsociety.com"; 
            const login_url = url + '/authenticate';
            const body = {
                email: document.getElementById("uid").value,
                password: document.getElementById("password").value,
            };
            console.log(JSON.stringify(body));
            const requestOptions = {
                method: 'POST',
                mode: 'cors',
                cache: 'no-cache',
                credentials: 'include',
                body: JSON.stringify(body),
                headers: {
                    "content-type": "application/json",
                    "Access-Control-Allow-Credentials": "true",
                    "Access-Control-Allow-Origin": "*",
                },
            };
            // Fetch JWT
            fetch(login_url, requestOptions)
                .then(response => {
                    if (!response.ok) {
                        const errorMsg = 'Login error: ' + response.status;
                        console.log(errorMsg);
                        return;
                    }
                    // Success!!!
                    // Redirect to Database location
                    localStorage.setItem("localEmail", document.getElementById("uid").value);
                    localStorage.setItem("localPassword", document.getElementById("password").value);
                    console.log(localStorage.getItem("localEmail"));
                    console.log(localStorage.getItem("localPassword"));
                    localStorage.setItem("loggedIn", "true");
                    showAccountDetails();
                    window.location.href = "/sturdy-fiesta/login";
                });
        }
    </script>
```

## REST API Methods
<h4> 1. GET: /users </h4>
    - Description: Acquire a system's user list.

    - Request: GET /users

    - Response: Status code 200 OK and JSON array containing details of multiple users.
    
<h4>2. GET: /users(id) </h4>
    - Description: Obtain a specific user using their unique ID.

    - Request: GET /users/Mort 

    - Response: status code 200 OK and user with ID Mort.

<h4> 3. POST: /users </h4>
    - Description: Establish a new user within the system.

    - Request: Send POST request -> /users containing the user information.

    - Response: status code 200 OK and JSON object with newly created user.

<h4> 4. PUT: /users(id) </h4>
    - Description: Update an existing user with their ID.

    - Request: Send a PUT request to /users/Mort containing the updated information.

    - Response: status code 200 OK will include the user with updated details.

## HTTP Status

`400 Bad Request` Description: Cannot read the request, often due to unknown syntax or missing parameter.

Example: When a server receives a request that is either improperly formatted or missing necessary information, it returns a 400 Bad Request status code.

`404 Not Found`  Description: The requested resource (user) could not find on server

Example Usage: If a GET, PUT, or DELETE request is made for a user that doesn't exist, the server will return a 404 Not Found status code.

`200 OK` Description: Successful request, and returns the requested data.

Example : Upon successfully executing a GET, POST, PUT, or DELETE operation, the server issues a 200 OK status code.

# Understanding Database Definitions and JSONB in User Profiles

## Database Definition

- A **database** is a structured repository for storing and managing data.
- Database design involves defining entities like User Profiles, outlining the structure and organization of user data.
- User Profiles typically include information such as user IDs, personal details, and preferences.

### User Profile Database Definitions

- **User Profile** definitions encompass details like user IDs, personal information, preferences, and more.
- Materials likely contain existing database definitions for User Profiles, specifying how this information is stored.

## API and Existing Database Structures

- **APIs (Application Programming Interfaces)** act as intermediaries for applications to interact with databases.
- Many APIs already exist, indicating established interfaces for database operations.
- APIs facilitate communication between the application and the database, enabling actions like data retrieval and manipulation.

## Extending Functionality with JSONB

- **JSONB** (JSON Binary) allows storage of nested and dynamic data structures within a database.
- JSONB provides a flexible way to represent complex data hierarchies compared to traditional tabular formats.

### JSONB and Nested Data Structures

- JSONB permits the storage of complex data hierarchies, enhancing the representation of information.
- Example: In the context of a Person object's stats, each person can store activity data with the formatted date as the key.
  
   ```json
   {
     "personId": 123,
     "stats": {
       "2024-01-17": {
         "activity": "Running",
         "duration": "1 hour"
       },
       "2024-01-18": {
         "activity": "Cycling",
         "duration": "45 minutes"
       }
     }
   }

- The structure allows for efficient storage and retrieval of data related to a person's activities.

# Flexibility in Data Modification
- JSONB allows modifications to the structure of JSON data in the Front End (FE) without altering the database schema.
- Developers can adapt and evolve data representation in the user interface without disrupting the backend database.
- This flexibility enables seamless adjustments to the way data is presented to users, enhancing the user experience.

# Conclusion

- Understanding database definitions and leveraging tools like JSONB provides a solid foundation for storing user information.
- JSONB's flexibility in handling nested and dynamic data structures opens up possibilities for more organized and scalable data usage.
- APIs and existing database structures play a crucial role in facilitating communication between applications and databases.
- Developers can utilize JSONB to enhance user interfaces and modify data structures seamlessly in the Front End without impacting the backend database schema.

# Lesson: Storing Hashmaps with jsonb
## What is a Hashmap?
- A hashmap, is a data structure that implements an associative array abstract data type. It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.
- Here's a basic overview of how it works:
- Hash Function: A hash function takes an input (or key) and produces a fixed-size string of characters, which is typically a hash code. The hash code is used to determine the index of the array where the corresponding value should be stored.
- Array (Buckets): The hashmap consists of an array of buckets or slots. Each bucket can hold a key-value pair or sometimes a linked list of key-value pairs.
- Indexing: The hash code generated by the hash function is used to determine the index in the array where the key-value pair should be stored or retrieved. Collisions can occur when two different keys hash to the same index.
- Collision Resolution: Different keys might produce the same hash code (collision). Various collision resolution techniques are used to handle this, such as chaining (using linked lists in each bucket) or open addressing (finding the next available slot).
- Hashmaps provide efficient average-case time complexity for common operations such as insertions, deletions, and lookups. They are widely used in computer science and programming due to their speed and versatility.
## Storing Hashmaps:
In the context of databases and data serialization, storing HashMaps with JSONB typically refers to using the JSONB data type provided by certain database systems, such as PostgreSQL.
JSONB (Binary JSON) is a data type that allows you to store JSON-like structured data in a more compact and efficient binary format. When dealing with HashMaps, which are key-value pairs, you can represent them as JSON objects and store them in a JSONB column.
Here's a simplified example in the context of PostgreSQL:
1. **Create a Table with JSONB Column:**
   ```sql
   CREATE TABLE my_table (
       id SERIAL PRIMARY KEY,
       data JSONB
   );
   ```
   In this example, `data` is a JSONB column where you can store your HashMap-like structures.
2. **Inserting Data:**
   ```sql
   INSERT INTO my_table (data) VALUES ('{"key1": "value1", "key2": "value2"}'::JSONB);
   ```
   You can insert data as a JSONB value.
3. **Querying Data:**
   ```sql
   SELECT * FROM my_table WHERE data->>'key1' = 'value1';
   ```
   You can query based on the keys and values within the JSONB data.
When using JSONB to store HashMap-like structures, it's important to note that this approach allows flexibility in terms of the data you can store. However, it also means that you might lose some of the benefits of a structured relational database, as the data is not strongly typed.
Keep in mind that the specific syntax and capabilities might vary depending on the database system you are using. Additionally, consider the trade-offs between using a JSONB column and a more traditional relational structure based on your application's requirements.
