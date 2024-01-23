---
toc: True
comments: True
layout: notebook
title: User Profile JavaScript/HTML Lesson
description: HTML and Javascript of User Profiles
courses: {'labnotebook': {'week': 20}}
type: tangibles
---

## Update/Delete User Info
> In this section we will be explaining how data for the user would be updated and deleted in the Java Springboot backend.

First, make sure you have this repository cloned so that you can see the code working in real time: `git clone https://github.com/CSA-AI/CSA_AI_lessonBackend.git`

If your frontend local server address is different from `http://localhost:4000` or `http://127.0.0.1:4000`, make sure to change it accordingly in the `SecurityConfig.java` and `MvcConfig.java` files and HTML files provided in the lesson.

### Update Through API Requests
> This is how the user would update data specific to their profile using a PUT request which communicates to the Springboot server.

- `@PutMapping` - maps to which site extension the update will be performed
- `ResponseEntity` - this is the method signature and specifies the required parameters (email, password, name)
- `findbyEmail` - here we find the person using the JPA repository by accessing the person object that matches the email requested, creating a copy of this object
- `setPassword`, `setName` - this is a JPA set function which allows us to set the new data that is updated
- `save()` - this saves the newly created person object, overwriting the existing person object with a matching email

This is essentially copy and paste, copying the pre-existing user data and pasting the new data in it's place.


```java
// mapping request
@PutMapping("/update")
    // method signature
    public ResponseEntity<Object> putPerson(@RequestParam("email") String email, @RequestParam("password") String password, @RequestParam("name") String name ) 
    {
        // copying person object
        Person person = repository.findByEmail(email);
        // saving new data to the copied person object
        person.setPassword(password);
        person.setName(name);
        // saving the copied person object with new data over the pre-existing person object with a matching email
        repository.save(person);
        // returning response from server to frontend
        return new ResponseEntity<>(email +" is updated successfully", HttpStatus.OK);
    }
```

In this example of HTML, we use fetch to PUT the data into the backend using parameters.

- `URLSearchParams();` - this is how we add parameters into the request towards the backend, allowing for the user to edit a pre-existing person in the backend database


```java
%%html
<body>
    <h2>Password Update</h2>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" value="toby@gmail.com" readonly><br>
    <label for="password">New Password:</label>
    <input type="password" id="password" name="password" value="test@123"><br>
    <label for="name">New Name:</label>
    <input type="text" id="name" name="name" value="Test Test"><br>
    <button onclick="updatePassword()">Update</button>
    <p id="updateMessage"></p>
    <script>
        function updatePassword() {
            const url = 'http://localhost:8085/api/person/update'; // sending to the backend API (change this address if your backend is different)
            const email = document.getElementById("email").value;
            const newPassword = document.getElementById("password").value;
            const newName = document.getElementById("name").value;
            const params = new URLSearchParams(); // creating the parameters sent to the backend
            params.append('email', email);
            params.append('password', newPassword);
            params.append('name', newName);
            fetch(url, {
                method: 'PUT', // the PUT method
                body: params,
            })
                .then(response => response.json()) // receiving the response from the backend server
                .then(data => {
                    // success
                    const updateMessage = "Updating email to: " + data.email;
                    document.getElementById("updateMessage").innerHTML = updateMessage;
                })
                // error checking
                .catch(error => console.error('Error:', error));
        }
    </script>
</body>
```

<body>
    <h2>Password Update</h2>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email" value="toby@gmail.com" readonly><br>
    <label for="password">New Password:</label>
    <input type="password" id="password" name="password" value="test@123"><br>
    <label for="name">New Name:</label>
    <input type="text" id="name" name="name" value="Test Test"><br>
    <button onclick="updatePassword()">Update</button>
    <p id="updateMessage"></p>
    <script>
        function updatePassword() {
            const url = 'http://localhost:8085/api/person/update'; // sending to the backend API (change this address if your backend is different)
            const email = document.getElementById("email").value;
            const newPassword = document.getElementById("password").value;
            const newName = document.getElementById("name").value;
            const params = new URLSearchParams(); // creating the parameters sent to the backend
            params.append('email', email);
            params.append('password', newPassword);
            params.append('name', newName);
            fetch(url, {
                method: 'PUT', // the PUT method
                body: params,
            })
                .then(response => response.json()) // receiving the response from the backend server
                .then(data => {
                    // success
                    const updateMessage = "Updating email to: " + data.email;
                    document.getElementById("updateMessage").innerHTML = updateMessage;
                })
                // error checking
                .catch(error => console.error('Error:', error));
        }
    </script>
</body>

### Delete Through API Requests
> This is how a user with admin permission would be able to request to delete specific users in the database.

- `@DeleteMapping` - this maps the site extension through which deleting will be performed
- `ResponseEntity<>` - the method signature requesting for the email, which is later used
- `findByEmail()` - finds the user object with a matching email to the one requested using the JPA repo
- `if (person != null)` - this just checks if the user exists
- `deleteByEmail(email)` - this is another JPA function that is used to delete the person object that has the same email as the one requested
- `ResponseEntity<>(HttpStatus.NOT_FOUND)` - returns a specific error that states that the user is not found

Overall, this find the user by the email and deletes them from the database if they exist.


```java
@Transactional // method is a database operation
@DeleteMapping("/delete") // mapping request
// method signature
public ResponseEntity<Person> deletePerson(@RequestParam("email") String email) {
    // finding person object by email
    Person person = repository.findByEmail(email);
    // checks if person object requested exists
    if (person != null) {
        repository.deleteByEmail(email);
        // returns success
        return new ResponseEntity<>(person, HttpStatus.OK);
    }
    // returns error
    return new ResponseEntity<>(HttpStatus.NOT_FOUND);
}
```

This is similar to the update HTML, except now we are using a DELETE request to the backend, again using parameters which are sent.


```java
%%html
<body>
    <h2>User Delete</h2>
    <label for="deleteEmail">Email:</label>
    <input type="email" id="deleteEmail" name="deleteEmail"><br>
    <button onclick="deleteUser()">Delete</button>
    <p id="updateMessage2"></p>
    <script>
        function deleteUser() {
            const url = 'http://localhost:8085/api/person/delete';
            const email = document.getElementById("deleteEmail").value;
            const params = new URLSearchParams(); // creating the parameters sent to the backend
            params.append('email', email);
            fetch(url, {
                method: 'DELETE',
                body: params,
            })
                .then(response => response.json())
                .then(data => {
                    const deleteMessage = "User deleted. Email: " + data.email;
                    document.getElementById("updateMessage2").innerHTML = deleteMessage;
                })
                .catch(error => console.error('Error:', error));
        }
    </script>
</body>

```

<body>
    <h2>User Delete</h2>
    <label for="deleteEmail">Email:</label>
    <input type="email" id="deleteEmail" name="deleteEmail"><br>
    <button onclick="deleteUser()">Delete</button>
    <p id="updateMessage2"></p>
    <script>
        function deleteUser() {
            const url = 'http://localhost:8085/api/person/delete';
            const email = document.getElementById("deleteEmail").value;
            const params = new URLSearchParams(); // creating the parameters sent to the backend
            params.append('email', email);
            fetch(url, {
                method: 'DELETE',
                body: params,
            })
                .then(response => response.json())
                .then(data => {
                    const deleteMessage = "User deleted. Email: " + data.email;
                    document.getElementById("updateMessage2").innerHTML = deleteMessage;
                })
                .catch(error => console.error('Error:', error));
        }
    </script>
</body>

If you would like to change which users are able to update or delete other users data or make the updating or deleting of data user-specific you can change the `SecurityConfig.java` file as shown below.


```java
.authorizeHttpRequests(auth -> auth
    .requestMatchers("/authenticate", "/mvc/person/post/**").permitAll()
    .requestMatchers("/mvc/person/update/**", "/mvc/person/delete/**").hasAnyAuthority("ROLE_ADMIN") // this would be used for editing locally within the server's frontend
    .requestMatchers("/api/person/post/**", "/api/person/delete/**").hasAnyAuthority("ROLE_ADMIN") // allowing only admin to essentially access these pages from requests
    .requestMatchers("/**").permitAll()
)
```

## Understanding Sign-Up Code in the Frontend

### HTML Structure
```html
<div id="signup-tab-content" class="tab-content">
  <h2 style="text-align: center;">Sign Up</h2>
  <form>
    <input type="text" id="new-name" name="name" placeholder="name" required>
    <br>
    <input type="text" id="new-email" name="email" placeholder="email" required>
    <br>
    <input type="password" id="new-password" name="password" placeholder="password" required>
    <br>
    <input type="date" id="new-dob" name="dob" required>
    <br>
    <button id="signUpButton" class="login-button" onclick="signUp()">Sign Up</button>
  </form>
</div>
```

### JavaScript Functions
```javascript
const signup_url = 'http://localhost:8085/api/person/post?';
const login_url = 'http://localhost:8085/authenticate';

function signUp() {
  // Extract user input values
  let email = document.getElementById("new-email").value;
  let password = document.getElementById("new-password").value;
  let name = document.getElementById("new-name").value;
  let dob = document.getElementById("new-dob").value;

  // Construct parameters for the sign-up API
  const params = {
    "email": email,
    "password": encodeURIComponent(password),
    "name": encodeURIComponent(name),
    "dob": encodeURIComponent(dob)
  };

  // Log sign-up fetch URL and make a POST request
  console.log("sign up fetch url: " + signup_url + new URLSearchParams(params));

  fetch(signup_url + new URLSearchParams(params), {
      method: 'POST',
    })
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error('Error:', error));
}

// Additional logIn() function not used in the provided HTML structure
```

### API Requests Made
1. **Sign-Up Request:**
   - Endpoint: `http://localhost:8085/api/person/post`
   - Method: POST
   - Parameters: email, password, name, dob

2. **Login Request:**
   - Endpoint: `http://localhost:8085/authenticate`
   - Method: POST
   - Parameters: email, password

## Interaction with HTML/CSS
- The JavaScript functions interact with the HTML elements using `getElementById` to extract user input.
- The `signUp` function constructs a parameter object based on user input and sends a POST request to the sign-up API endpoint.
- The `logIn` function is defined but not used in the provided HTML structure.

This code assumes a local development environment and does not consider security measures for production.

## Understanding Profile Management Frontend Code

### JavaScript Functions
```javascript
// Function to decode JWT token and retrieve user email and ID
const decode = token => decodeURIComponent(atob(token.split('.')[1].replace('-', '+').replace('_', '/')).split('').map(c => `%${('00' + c.charCodeAt(0).toString(16)).slice(-2)}`).join(''));

// Function to retrieve a cookie value by name
function getCookie(name) { /* ... */ }

// Function to update user profile data from the backend
function update() { /* ... */}

// Function to edit user statistics
function edit() { /* ... */}

// Function to post user statistics to the backend
function post() { /* ...*/ }

// Function to delete user account
function delUser() { /* ...*/ }

// Function to sign out and clear the token cookie
function signOut() { /* ...*/ }
```

### Requests Made
1. **Profile Update Request:**
   - Endpoint: `http://localhost:8085/api/person/:id`
   - Method: GET

2. **User Statistics Update Request:**
   - Endpoint: `http://localhost:8085/api/person/setStats`
   - Method: POST
   - Parameters: id, date, steps, calories


```java
%%html
function post() {
    console.log(currentDate);
    steps = document.getElementById("steps").innerHTML;
    calories = document.getElementById("calories").innerHTML;
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({
      "id": id,
      "date": currentDate,
      "steps": steps,
      "calories": calories
    });
    var requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
      redirect: 'follow'
    };
    fetch("http://localhost:8085/api/person/setStats", requestOptions)
      .then(response => response.text())
      .then(result => alert("stats updated!"))
      .catch(error => console.log('error', error));
}
```

This is the endpoint in the Springboot server to which the data is sent and managed. Here we:

- find the ID of the stat map requested using `parseLong()`
- finds the person that is going to have their stats added
- checks if the user is in the database and then creates a hashmap `attributeMap` where stats will be stored
- adds entry if it is not a date or id of the entry
- sets the map to the person with the JPA function `setStats()`
- returns a success if the operation was successful or an error if it wasn't


```java
@PostMapping(value = "/setStats", produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<Person> personStats(@RequestBody final Map<String,Object> stat_map) {
        // find ID
        long id=Long.parseLong((String)stat_map.get("id"));  
        Optional<Person> optional = repository.findById((id));
        if (optional.isPresent()) {  // Good ID
            Person person = optional.get();  // value from findByID

            // Extract Attributes from JSON
            Map<String, Object> attributeMap = new HashMap<>();
            for (Map.Entry<String,Object> entry : stat_map.entrySet())  {
                // Add all attribute other thaN "date" to the "attribute_map"
                if (!entry.getKey().equals("date") && !entry.getKey().equals("id"))
                    attributeMap.put(entry.getKey(), entry.getValue());
            }

            // Set Date and Attributes to SQL HashMap
            Map<String, Map<String, Object>> date_map = new HashMap<>();
            date_map.put( (String) stat_map.get("date"), attributeMap );
            person.setStats(date_map);  // BUG, needs to be customized to replace if existing or append if new
            repository.save(person);  // conclude by writing the stats updates

            // return Person with update Stats
            return new ResponseEntity<>(person, HttpStatus.OK);
        }
        // return Bad ID
        return new ResponseEntity<>(HttpStatus.BAD_REQUEST); 
    }
```

3. **User Deletion Request:**
   - Endpoint: `http://localhost:8085/api/person/delete?email=:email`
   - Method: DELETE

## Interaction with HTML/CSS
- JavaScript functions interact with HTML elements using `getElementById` to manipulate content dynamically.
- The `update` function fetches user statistics from the backend and updates HTML elements with the retrieved data.
- Buttons like "Refresh," "Edit," "Update," "Sign Out," and "Delete user" trigger corresponding JavaScript functions.
- CSS styles define the layout and appearance of the profile display.

This code assumes a local development environment and lacks certain security considerations for a production setting.
