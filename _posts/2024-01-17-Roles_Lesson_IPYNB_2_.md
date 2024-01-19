---
title: Spring Roles for User/Admin
description: Lesson on roles.
toc: True
layout: post
courses: {'labnotebook': {'week': 19}}
type: hacks
---

### Lesson Materials

Our lesson uses backend code from [this repository](). If you want to follow along in this lesson, please git clone with the line below and run Main.java to use localhost:

`git clone https://github.com/John-sCC/Roles_BE.git`

The contents of this lesson are pretty important for projects!

## Person and PersonRole Relationship

### Person Object

(See [Person.java](https://github.com/John-sCC/Roles_BE/blob/master/src/main/java/com/nighthawk/spring_portfolio/mvc/person/Person.java))

The `Person` object is a POJO, which stands for "Plain Old Java Object." Essentially, it's a Java object with no special restrictions or requirements. It contains business logic and data for modeling entities.

Of the attributes of the object `Person`, one is `roles`, which is a Collection of `PersonRole` objects. These are the roles that we go over in this lesson.


```java
// FULLY IMPLEMENTED!
@ManyToMany(fetch = EAGER)
private Collection<PersonRole> roles = new ArrayList<>();
```

As a quick recap of SQL concepts:
- `@ManyToMany` establishes that Person and PersonRole have a Many-to-Many relationship with each other (the same role can be assigned to many Person objects, and multiple Person object can be assigned to many roles).
- `fetch = EAGER` establishes that, when a Person object is fetched, its roles should be fetched immediately at the same time. If it was instead `fetch = LAZY`, the PersonRole objects would only be fetched explicity, separate from the Person object.

### PersonRole Object

(See [PersonRole.java](https://github.com/John-sCC/Roles_BE/blob/master/src/main/java/com/nighthawk/spring_portfolio/mvc/person/PersonRole.java))

The `PersonRole` object is another POJO with its own entities separate from the `Person` object. They are assigned to each other. In preparation for the lesson, we added an argument constructor and an initializer method.


```java
public class PersonRole {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;

    @Column(unique=true)
    private String name;

    public PersonRole(String name) {
        this.name = name;
    }

    public static PersonRole[] init() {
        PersonRole student = new PersonRole("ROLE_STUDENT");
        PersonRole teacher = new PersonRole("ROLE_TEACHER");
        PersonRole admin = new PersonRole("ROLE_ADMIN");
        PersonRole[] initArray = {student, teacher, admin};
        return initArray;
    }
}
```

### Initializing PersonRole

Now that we have an initializer for the `PersonRole` object, we add it to the `ModelInit.java` file as shown below. (Modified slightly to emphasize roles.)


```java
public class ModelInit {  
    // ...declarations...
    @Autowired PersonRoleJpaRepository roleRepo;

    @Bean
    CommandLineRunner run() {  // runs when the application starts
        return args -> {
            // ...jokes...

            // initializing person roles
            PersonRole[] personRoles = PersonRole.init();
            for (PersonRole role : personRoles) {
                PersonRole existingRole = roleRepo.findByName(role.getName());
                if (existingRole != null) {
                    // role already exists
                    continue;
                } else {
                    // role doesn't exist
                    roleRepo.save(role);
                }
            }

            // initializing person objects
            Person[] personArray = Person.init();
            for (Person person : personArray) {
                //findByNameContainingIgnoreCaseOrEmailContainingIgnoreCase
                List<Person> personFound = personService.list(person.getName(), person.getEmail());  // lookup
                if (personFound.size() == 0) {
                    personService.save(person);  // save
                    // ...notes...
                    // adding the student role to each initial person
                    personService.addRoleToPerson(person.getEmail(), "ROLE_STUDENT");
                }
            }
            // for lesson demonstration: giving admin role to Mortensen
            personService.addRoleToPerson(personArray[4].getEmail(), "ROLE_ADMIN");
        };
    }
}
```

The code is written so that, if the SQL database has been emptied, the roles will be recreated, but if it hasn't been, they won't be created a second time, which would cause an error (since the names would be repeats).

We gave one of the test Person objects, "John Mortensen," the "ROLE_ADMIN" role. This will be used in conjunction with roles-based security.

### Viewing Person and PersonRole in SQL

Now that the roles have been created and assigned, they can be viewed in the SQL table in two different ways that offer different information.

If you open the sqlite.db and look at the "person_role" (singular) table, you'll see something like this:

<img src="https://github.com/drewreed2005/dre2.0/blob/main/images/person_role_table.png?raw=true">

This shows each role and its corresponding ID. It works basically the same way as the "person" table.

<img src="https://github.com/drewreed2005/dre2.0/blob/main/images/person_roles_table.png?raw=true">

The second table has the title "person_roles" (plural). This type of table is called a "join table," and it represents Many-to-Many relationships by showing the corresponding IDs of objects with relationships in pairs.

All Person objects other than the one with ID 5 only have a relationship to PersonRole ID 1, which is the "ROLE_STUDENT" role given when initialized. The Person with the ID 5 was given both "ROLE_STUDENT" and "ROLE_ADMIN," so he has two different relationships shown.

## Using Roles for Security

The first step to implementing security with roles is found in the file `PersonDetailsService.java`. The method below finds a user based on username, and then stores its roles as a Collection of `SimpleGrantedAuthority` based on the role names. All user details, including email, password and authorities are returned as "userdetails".


```java
/* UserDetailsService Overrides and maps Person & Roles POJO into Spring Security */
@Override
public org.springframework.security.core.userdetails.UserDetails loadUserByUsername(String email) throws UsernameNotFoundException {
    Person person = personJpaRepository.findByEmail(email); // setting variable user equal to the method finding the username in the database
    if(person==null) {
        throw new UsernameNotFoundException("User not found with username: " + email);
    }
    Collection<SimpleGrantedAuthority> authorities = new ArrayList<>();
    person.getRoles().forEach(role -> { //loop through roles
        authorities.add(new SimpleGrantedAuthority(role.getName())); //create a SimpleGrantedAuthority by passed in role, adding it all to the authorities list, list of roles gets past in for spring security
    });
    // train spring security to User and Authorities
    return new org.springframework.security.core.userdetails.User(person.getEmail(), person.getPassword(), authorities);
}
```

Where is this method called? Why, when you make a `/authenticate` request, silly!

In `JwtApiController.java`, you can see it used when an authenticate request is called. The "userdetails" are used to create a JWT that is sent to the requester if the request is valid.


```java
@PostMapping("/authenticate")
	public ResponseEntity<?> createAuthenticationToken(@RequestBody Person authenticationRequest) throws Exception {
		authenticate(authenticationRequest.getEmail(), authenticationRequest.getPassword());
		final UserDetails userDetails = personDetailsService
				.loadUserByUsername(authenticationRequest.getEmail()); // HERE IT IS!!
		final String token = jwtTokenUtil.generateToken(userDetails);
		final ResponseCookie tokenCookie = ResponseCookie.from("jwt", token)
			.httpOnly(true)
			.secure(true)
			.path("/")
			.maxAge(3600)
			.sameSite("None; Secure")
			.build();
		return ResponseEntity.ok().header(HttpHeaders.SET_COOKIE, tokenCookie.toString()).build();
	}
```

Now that we have a cookie that tells us what the logged-in user's roles are, we can use that as authority to make certain requests. In `SecurityConfig.java`, we added `.hasAnyAuthority("ROLE_ADMIN")` to the "mvc" and "api" update and delete requests.


```java
public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
    http
        .csrf(csrf -> csrf
        	.disable()
        )
        // list the requests/endpoints need to be authenticated
        .authorizeHttpRequests(auth -> auth
        	.requestMatchers("/authenticate").permitAll()
        	.requestMatchers("/mvc/person/update/**", "/mvc/person/delete/**").hasAnyAuthority("ROLE_ADMIN") // must be admin for these
        	.requestMatchers("/api/person/post/**", "/api/person/delete/**").hasAnyAuthority("ROLE_ADMIN")
        	.requestMatchers("/**").permitAll()
    	)
}

```

As a result, only a signed-in user with Admin permissions will be able to make these requests successfully. Now, we will show it in action.

## Frontend Application

### MVC on Localhost
```java
@GetMapping("/read")
    public String person(Model model) {
        List<Person> list = repository.listAll();
        model.addAttribute("list", list);
        return "person/read";
    }
```
When calling the `/read` endpoint the backend then returns a list of people stored in the `person` database. The line `return"person/read"` indicates to Spring that the page to be displayed is the `read.html` file.

For more examples of referencing, take a look at the `PersonViewController.java` file.

### Login on Blog

```html
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
            fetch("/authenticate", {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(data)}).then((data) => {
                if (data.status == 200) {
                    window.location.replace("/mvc/person/read");
                } else {
                    document.getElementById('message').innerHTML = "Invalid email or password"
                }
            });
        }
    </script>
```

The login page calls the authenticate endpoint, and allows the user to log in and generate the JWT cookie that can be used to authenticate whether the user has the right to perform certain operations on the system (as defined in the `SecurityConfig.java`).

<img src="https://github.com/John-sCC/jcc_frontend/assets/142441804/c3dd22b8-5851-4b45-9121-b157ff6f1d24">

## Update
```html
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
```

The thymeleaf here checks if, when the user presses on the `Update` or `Delete` tags, they have appropriate roles by calling the API. It gets the user ID for each user in the table and runs the restricted endpoints `/update` and `/delete`. If the user has the appropriate role (`ROLE_ADMIN`), then the user is allowed to continue the operation. Otherwise it throws the 403 error.

<img src="https://github.com/John-sCC/jcc_frontend/assets/142441804/95d5e085-114e-49f1-b51b-46788066fac1">


## Get a JWT

For a non-admin user, try:
- Email: "toby@gmail.com"
- Password: "123Toby!"

For an admin user, try:
- Email: "jm1021@gmail.com"
- Password: "123Qwerty!"

<br>

<label for="email">Email:</label>
<input type="email" id="email" placeholder="Enter your email">

<br>

<label for="password">Password:</label>
<input type="password" id="password" placeholder="Enter your password">

<br>

<button onclick="authenticate()">Login</button>

After clicking the "Login" button, make sure to check the console to ensure the fetch worked correctly! You'll need to be running the localhost for the provided backend.

<script>
function authenticate() {
    // Get values from input fields
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;

    // Create a JSON object with email and password
    var data = {
        email: email,
        password: password
    };

    // set options for cross-origin header request
    const authOptions = {
        method: 'POST',
        mode: 'cors',
        cache: 'default',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    };

    // Make a POST request using fetch API
    fetch('http://localhost:8085/authenticate', authOptions)
        .then(response => {
            // Check if the response is successful (status code 2xx)
            if (!response.ok) {
                throw new Error('Authentication failed');
            }

            // Continue with your code here
            console.log('Authentication successful. Now, open the "Application" tab (click the two arrows to see it). Look for a cookie called "jwt".');

            return response.ok;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
</script>

## Anatomy of a JWT

The JWT token generated from the `/authenticate` endpont gives the server the cookie that determines the user's role (it's encrypted right now).

<img src="https://github.com/John-sCC/jcc_frontend/assets/142441804/b7af9114-2e3d-41e7-be3a-2fbd4c2276c1">

You can customize JWT tokens while following certain structure. A token contains a Header, Payload, and Signature in the form `header.payload.signature`. You should be able to see this in the cookie you received after making the authenticate request!

*Note: the following paramters are not the same in the Spring library we use. That library is ResponseCookie, which has separate online documentation for the specific paramters.

### Header

Includes the type of token and signing/encryption algorithm. Ex:

```json
{
    "alg": "HS256",
    "typ": "JWT"
}
```

### Payload

The payload contains the claims/description/customized properties of the token. They can be split into Registered Claims, Public Claims, and Custom Claims.

#### Registered

Predefined claims, basically mandatory for function.
Include:
- "iss" (Issuer)
- "sub" (Subject)
- "aud" (Audience)
- "exp" (Expiration Time)
- "iat" (Time the token was issued at)

#### Public

Existing, predefined claims but optional.
Include:
- "name"
- "family"
- "email"

#### Private

Custom claims such as "admin"

### Signature

Created by the encoded header, used to verify the token is consistent and sent by the same person.
Automatically generated when using the Spring library.

### Helpful Website

If you visit [this website](https://jwt.io/) and enter your encoded JWT, it will give you information about it.
