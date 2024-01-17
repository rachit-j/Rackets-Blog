---
comments: True
layout: notebook
title: SASS Login Lesson
description: A key to development in this class is the association VSCode to a GitHub pages project.  This is where students update assignments and present work.
type: hacks
courses: {'labnotebook': {'week': 19}}
authors: Krishiv Mahendru, Vinay Rajagopalan, Edwin Abraham, Parav Salaniwal, Shaurya Goel, Yuri Subramaniam
---

# Login Feature

## HTML

```
<body>
    <div>
      <text>Enter your username and password to log in</text> 
    </div>
    <div id="boxes">
        <text>Username: </text>
        <input id="username"></input>
        <br><text>Password: </text>
        <input id="password"></input>
        <br><button id="login">Login</button>
    </div>
<body>
```

- HTML code for a simple login form.
- Displays a message prompting the user to enter their username and password.
- Contains input fields for username and password.
- Includes a login button for user authentication.

## SASS

```
// Define color variables
$white: #ffffff;
$red: #f10c0c;

// Global styles
body {
  font-family: 'Arial', sans-serif;
  background-color: $white;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

// Header styles
header {
  padding: 0;
  border: 1px solid #ccc;
  border-radius: 4px;

  // Nested div inside header
  div {
    // Nested nav inside div
    nav {
      border: 1px solid #ccc;
      border-radius: 4px;
    }
  }
}

// Main content styles
main {
  // Nested div inside main
  div {
    // Nested article inside div
    article {
      // Another nested div inside article
      form {
        border: 20px solid #06a53b;
        border-radius: 10px;

        // Nested input inside div
        input {
          width: 200px;
          padding: 8px;
          margin: 6px;
          border: 1px solid #0d25fd;
          border-radius: 4px;
        }

        // Nested button inside div
        button {
          background-color: #4caf50;
          color: $white;
          padding: 10px 20px;
          border: 5px solid $red;
          border-radius: 100px;
          cursor: pointer;
          font-size: 16px;
        }
      }
    }
  }
}
```

- Defines styling for the header and body sections.
- Sets a border, border-radius, and padding for the header.
- Styles the body with a specific font, background color, and centering.
- Defines styling for input fields and a button, specifying width, padding, margin, border, and background color.

## SASS - Shaurya
```
// Your SASS styles here
// Global styles
$primary-font: 'Roboto', sans-serif;
$primary-color: #3498DB;
$box-shadow-color: rgba(0, 0, 0, 0.2);
body {
  font-family: $primary-font;
  background-color: #EAEAEA; // Light gray background
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
// Header styles
header.site-header {
  width: 100%; // Take full width
  background-color: $primary-color;
  color: white;
  padding: 10px;
  text-align: center;
}
// Section styles
section {
  background-color: #fff;
  border-radius: 12px; // Slightly larger border-radius
  box-shadow: 0 4px 8px $box-shadow-color;
  padding: 30px; // Increased padding
  margin: 30px; // Increased margin
  max-width: 600px; // Wider section
}
// Heading 2 styles
h2 {
  color: $primary-color; // Match header background color
  text-transform: uppercase;
}
// Form styles
form {
  display: grid; // Use grid layout
  grid-template-columns: repeat(2, 1fr); // 2-column layout
  gap: 15px; // Spacing between elements
}
// Input styles
input {
  padding: 12px;
  border: 1px solid $primary-color;
  border-radius: 6px;
}
// Button styles
button {
  cursor: pointer;
  padding: 12px;
  background-color: $primary-color;
  color: white;
  border: none;
  border-radius: 6px;
  transition: background-color 0.3s ease;
  &:hover {
    background-color: darken($primary-color, 10%); // Darken on hover
  }
}
// Paragraph styles
p {
  color: #E74C3C; // Change to a different red color
  font-style: italic;
}
```
1. I introduced global variables for the primary font and color.
2. Changed the body background color and used a different font for a fresh look.
3. Updated header styles for a full-width, centered, and stylized header.
4. Modified section styles with larger border-radius, increased padding, and margin, and a wider max-width.
5. Added text transformation to the h2 for uppercase styling.
6. Transformed the form layout to a 2-column grid.
7. Refined input and button styles with border and transition effects.
8. Changed the paragraph text color and added italic styling.

## JS

```
    <script>
       function person_login() {
        var myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        var raw = JSON.stringify({
            "email": document.getElementById("Emaillogin").value,
            "password": document.getElementById("PasswordLogin").value

            
        });
        console.log(raw);

        var requestOptions = {
            method: 'POST',
            headers: myHeaders,
            credentials: 'include',  // 
            body: raw,
            redirect: 'follow'
        };
    </script>
```

- Retrieves the username and password input elements from the HTML.
- Creates a data object with the email (username) and password.
- Sets up an event listener for the login button click.
- Uses the fetch function to make a POST request to "http://localhost:8085/authenticate" with JSON-formatted data.
- If the response status is 200, redirects the user to "/about/"; if it's 404, redirects to "/about/" as well.
- The fetch function is used to asynchronously send and receive data from a server, and it returns a Promise that resolves to the Response to that request. In this case, it's handling authentication and redirecting the user based on the server's response status.

# Signup Feature

## HTML

```
<body>
  <section id="signup">
    <h2>Signup</h2>
    <form id="signupForm">
      <input type="text" placeholder="Email" id="email" required>
      <input type="password" placeholder="Password" id="password" required>
      <input type="text" placeholder="Name" id="name" required>
      <input type="text" placeholder="Date of Birth (MM-dd-yyyy)" id="dob" required>
      <!-- Add more input fields for additional information if needed -->
      <button type="submit">Signup</button>
    </form>
    <p id="signupMessage"></p>
  </section>
```

- Form (id: signupForm) with input fields for email, password, name, and date of birth.
- Comment suggests the possibility of adding more input fields for additional information.
- "Signup" button triggers form submission; potential feedback displayed in a paragraph element (id: signupMessage).

## SASS

```
  <style>
    /* Your CSS styles here */
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
    
    header.site-header{
      width: 1100px;
      margin: 0;
      padding: 0;
    }

    section {
      background-color: #fff;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      padding: 20px;
      margin: 20px;
      max-width: 400px;
    }

    h2 {
      color: black;
    }

    form {
      display: flex;
      flex-direction: column;
    }

    input, button {
      margin-bottom: 10px;
      padding: 10px;
    }

    button {
      cursor: pointer;
    }

    p {
      color: red;
    }
  </style>
```

- Body styling with a background color of #f4f4f4, using flexbox to center content vertically and horizontally (height: 100vh).
- Header styling for a site header with a fixed width of 1100px, no margins or padding.
- Section styling with a white background, rounded corners (border-radius: 8px), box shadow, and padding/margin for spacing. Max width set to 400px.
- Heading 2 (h2) styling with black color.
- Form styling using flexbox for a column layout.
- Styling for input and button elements with margin-bottom and padding.
- Button styling with a cursor set to pointer.
- Paragraph (p) styling with red text color.

## JS

```
  <script>
    document.getElementById('signupForm').addEventListener('submit', function (event) {
      event.preventDefault();
      // Get values from form fields
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;
      const name = document.getElementById('name').value;
      const dob = document.getElementById('dob').value;

      // Other fields like age, roles, and stats can be calculated or set as needed

      // Fetch request to signup endpoint
      fetch('http://localhost:8085/api/person/post', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: email,
          password: password,
          name: name,
          dob: dob,
          // Include other fields as needed
        }),
      })
        .then(response => {
          if (!response.ok) {
            throw new Error('Signup failed');
          }
          return response.json();
        })
        .then(responseData => {
          document.getElementById('signupMessage').innerText = 'Signup successful';
          // Redirect to login page after successful signup
          window.location.href = 'login.html'; // Replace with the actual login page
        })
        .catch(error => {
          document.getElementById('signupMessage').innerText = error.message;
          console.error(error.message);
        });
    });
  </script>
```

- Event listener added to form ('signupForm') for form submission.
- Prevents default form submission behavior to enable custom handling.
- Retrieves form field values (email, password, name, dob) and prepares a JSON object.
- Initiates a fetch request to 'http://localhost:8085/api/person/post' with a POST method and JSON content type.
- Checks response status, displays 'Signup successful' message, and redirects to the login page on success.
- Handles errors by displaying the error message in the signup message element and logging the error to the console.
