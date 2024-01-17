---
toc: True
comments: True
layout: post
title: UX - jQuery - CRUD Lesson
description: The Bestest Baddest Coders lesson on UX and jQuery|CRUD
courses: {'labnotebook': {'week': 15}}
type: hacks
authors: Colin Weis, Orlando Carcamo, Aniket Chakradeo, Mati Danish, Shreyas Sarurkar, Soham Kamat
---

# UX

### Intro to the lesson
- Do you remember the first operating system you used?
- What makes you remember that first interaction?
- The first operating system that I used was Windows XP, and fun fact the XP stands for experience. This shows how important User Experience is.

### What is UX?
- UX is the shortform of user experience; a standard of understanding the usability of a product and optimise it based on data recived from users.

- UX is a standard in all industries since collecting UX and improving the product based on it increases the populatiry of the product on the market, increasing profits of the company or collaboration.

# Examples of bad UX but Good UI


- apple.com
    - the website lags on lower end devices.
    - renders the website useless on lower end devices
    (demonstrate)

<img width="1912" alt="Screenshot 2023-12-06 at 8 37 54 PM" src="https://github.com/y2kcoders/skatepark.co/assets/111465192/0b959614-184b-4e04-8986-c687fe141102">



- microsoft.com
    - the website is very hard to navigate
    - very hard to find every feature
    - the first time i used it, i didn't know where to change my password and eventually gave up
    - is it trying to sell me its products or is it trying to help me?

<img width="1912" alt="Screenshot 2023-12-06 at 8 41 13 PM" src="https://github.com/hsinaDitaM/Danish_Cookies/assets/111465192/37cdaa0a-0409-4980-a1f0-77dd03f3e749">



- controversial but true, github.com
    - veru hard to navigate
    - very hard to find every feature
    - too much is going on, mental stress 😩

<img width="1912" alt="Screenshot 2023-12-06 at 8 38 52 PM" src="https://github.com/hsinaDitaM/Danish_Cookies/assets/111465192/2d8a3e01-6e54-4c7f-adb6-c9d49e9c839c">


# Examples of Good UX and Good UI

- discord.com
    - very easy to navigate
    - very easy to find every feature
    - everything is very well organized
    - the icons are very easy to understand

![image](https://github.com/hsinaDitaM/Danish_Cookies/assets/111465192/54c2a731-428c-4fb2-8902-7688edc59b15)


- google.com
    - it has a search bar, and that's it
    - it is very easy to use, even for a 5 year old or a 90 year old

<img width="1912" alt="Screenshot 2023-12-06 at 8 45 05 PM" src="https://github.com/hsinaDitaM/Danish_Cookies/assets/111465192/954f81ab-345e-44ee-810f-e3e191f0b0ef">

![image](https://github.com/Soham360/refactored-engine/assets/111465192/5d3131ff-d717-4acd-a473-708a7936169a)


### What is the difference between UX and UI?
- The main difference between UX and UI is that UI focuses on how the website looks rather than how it works.
- A website can have a great UI but a bad UX, but a website can't have a great UX but a bad UI
    - If the website is bad to look at, the User Experience is going to be horrible.

### When is UX Used?
- UX is used when a product, especially a new one, needs optimization or modification based on user prefrence. This helps with changing user perception of the product since the company producing it would have had no prior feedback and would have not known their user prefrences.

### How is UX data gathered?
- UX data is mainly gathered through internet forms or feedback discussion boards. Advertisments and websites such as Google forms or official company forums are some common methods. This data is used to make small or big quality kf life changes that make it more convineient anfor the user.

- An example of UX data collection is the Minecraft Forums:
![image](https://github.com/Henerystone/ws2/assets/96998793/5cf2c8cf-ce18-46e7-a45a-3a9c9c6720cb)
- An example of UX implementation is the Spotify Wrapped interface:
![image](https://github.com/Henerystone/ws2/assets/96998793/484ba60b-a16b-471e-85f1-3041ad615d22)   
- On one hand, the Minecraft Forums are a source of UX data and on the other hand, the Spotify Wrapped interface is an example of improving UX.

### Why is UX important?
- UX is vital for the quality of a product; if there is no quality control or optimisation of UX, demand for the product drops and it fades away. If the product keeps up with modern UX expectations, it grows in popularity, gains higher demand and profits.
- An example is the contrast between old and new Mario games:
![image](https://github.com/Henerystone/ws2/assets/96998793/340763a8-c3c8-4efb-9ff0-30a16c47ada8)

- Incredibly low resolution, very lackluster in terms of background and very simple design on the UI and the foreground/level.

![image](https://github.com/Henerystone/ws2/assets/96998793/f085b3d8-f56c-4b47-9bb3-6b2ad723c844)

- Incredibly detailed, amazing resolution, interesting levels and larger UI/interfaces.

- As time has gone by, the user demands for higher resolution, higher detail, better quality, more game depth has translated into games as they strive to improve their UX to keep their products on top of the list.

### What is jQuery?

**jQuery** is a lightweight, “write less, do more”, JavaScript library. The purpose of jQuery is to make it much easier to use JavaScript on your site and it simplifies many tasks that require many lines of JavaScript code to accomplish, wrapping them into methods that you can call with a single line of code.

**jQuery** also simplifies a lot of the complicated things from JavaScript, like AJAX calls and DOM manipulation.

### The implications of jQuery

The jQuery library has the following features

1. HTML/DOM manipulation
2. CSS manipulation
3. HTML event methods
4. Effects and animations
5. AJAX (Asynchronous Javascript and XML)
6. Utilities

- In addition, jQuery has plugins for almost any task out there.

If you ever want to use jQuery, you can download it [here](http://jquery.com/download/) or just use a CDN (Content Delivery Network) from Google!


```python
<!-- Downloaded jQuery -->
<head>
<script src="jquery-3.7.1.min.js"></script>
</head>
```


```python
<!-- Google CDN which is the more common method of getting the library -->
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
</head>
```

### jQuery syntax and how to use it

With jQuery you select (query) HTML elements and perform "actions" on them.

Basic syntax is: $(selector).action()

- A $ symbol to define/access jQuery
- A (selector) to "query (or find)" HTML elements
- A jQuery action() to be performed on the element(s)

Examples:

- $(this).hide() - hides the current element

- $("p").hide() - hides all <p> elements

- $(".test").hide() - hides all elements with class="test"

- $("#test").hide() - hides the element with id="test"

In the following example, write in one of the comments where the selector is (popcorn hack ~ raise hand when found)


```python
$(document).ready(function(){     // 
    $("button").click(function(){ //
      $("p").hide();              //
    });                           //
  });                             //
```

The element Selector
- $("p")
The #id Selector
- $("#test")
The .class Selector
- $(".class")

The Document Ready Event

All jQuery methods begin inside a document ready event:


```python
$(document).ready(function(){

    // jQuery methods go here...
  
  });
```

This is to prevent any jQuery code from running before the document is finished loading (is ready).

It is good practice to wait for the document to be fully loaded and ready before working with it. This also allows you to have your JavaScript code before the body of your document, in the head section.

Reason:
- Trying to hide an element that is not created yet
- Trying to get the size of an image that is not loaded yet


```python
$(function(){
    
    // An even quicker way to do it
    // jQuery methods go here...
  
  });
```

### jQuery methods and event handling 

What are Events?
- All the different visitors' actions that a web page can respond to are called events

|Mouse Events|Keyboard Events|Form Events|Document/Window Events|
|-|-|-|-|
|click|keypress|submit|load|
|dblclick|keydown|change|resize|
|mouseenter|keyup|focus|scroll|
|mouseleave||blur|unload|

Popcorn Hack: Name 3 other event HTML events

1. Hover

2. On Press

3. On Reload


```python
onclick=JavaScript
// The infamous onclick event in html
```


```python
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
  $("p").click(function(){
    $(this).hide();
  });
});
</script>
</head>
<body>

<p>If you click on me, I will disappear.</p>
<p>Click me away!</p>
<p>Click me too!</p>

</body>
</html>
```

Final example, look at it [here](https://soham360.github.io/refactored-engine/dissapear.html)


```python
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
  $("#hide").click(function(){
    $("p").hide();
  });
  $("#show").click(function(){
    $("p").show();
  });
});
</script>
</head>
<body>

<p>If you click on the "Hide" button, I will disappear.</p>

<button id="hide">Hide</button>
<button id="show">Show</button>

</body>
</html>
```

Final example, look at it [here](https://soham360.github.io/refactored-engine/show.html)


```python
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
    // Challenge! Make it so the text appears with an animation, causing it to slowly fade in and out!
});
</script>
</head>
<body>

<button id="hide">Hide</button>
<button id="show">Show</button>

<p>Points < Indicators :D</p>
<p>This is another small paragraph</p>
<p>(if you put a cool joke here you get .01 extra points)</p>
<p>"ew who wrote that?" ^^^</p>

</body>
</html>
```

Final example, look at it [here](https://soham360.github.io/refactored-engine/showtime.html)


```python
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
  $("button").click(function(){
    $("#div1").fadeIn();
    $("#div2").fadeIn("slow");
    $("#div3").fadeIn(3000);
  });
});
</script>
</head>
<body>

<p>Demonstrate fadeIn() with different parameters.</p>

<button>Click to fade in boxes</button><br><br>

<div id="div1" style="width:80px;height:80px;display:none;background-color:red;"></div><br>
<div id="div2" style="width:80px;height:80px;display:none;background-color:green;"></div><br>
<div id="div3" style="width:80px;height:80px;display:none;background-color:blue;"></div>

</body>
</html>
```

Final example, look at it [here](https://soham360.github.io/refactored-engine/box.html)

### Making requests with AJAX

**AJAX** stands for Asynchronous JavaScript and XML. It allows web pages to be updated asynchronously in a easier way and is promise based. A **Promise** in JavaScript represents the eventual completion (or failure) of an asynchronous request.

### Why use jQuery AJAX over a normal async request or AJAX request?

Against a normal async request AJAX has a lot of advantages:

1. **Easier Error Handling**: Promises are much easier to deal with than callbacks. If an error occurs in a promise, it will be passed down to the next `catch()` clause.

2. **Simpler API Chaining**: If you want to wait for one operation to finish before starting another one you can simply use `.then()`.

#### Normal async request


```python
getUserLocation(function(error, location) {
    if (error) {
        console.error('Error:', error);
    } else {
        getForecast(location, function(error, forecast) {
            if (error) {
                console.error('Error:', error);
            } else {
                console.log('Forecast:', forecast);
            }
        });
    }
});
```

#### Ajax requests without any library


```python
fetch('api/location')
.then(response => response.json())
.then(location => fetch('api/forecast/' + location))
.then(response => response.json())
.then(forecast => {
    console.log('Forecast:', forecast);
})
.catch(error => {
    console.error('Error:', error);
});
```

#### Ajax Requests with JQuery


```python
$.ajax({ url: 'api/location', method: 'GET', dataType: 'json' })
.then(function(location) {
    return $.ajax({ url: 'api/forecast/' + location, method: 'GET', dataType: 'json' });
})
.then(function(forecast) {
    console.log('Forecast:', forecast);
})
.catch(function(error) {
    console.error('Error:', error);
});
```

You can see using ajax is much easier to read than callback system. However when it comes to using jquery ajax vs javascript's version there are less differences. It is up to you which syntax you like more.

As mentioned earlier, jQuery ajax also builds on top of the old javascript version so it can support older browser versions.

## Jquery's use with PBL

Jquery's most important use is making you site dynamic and update from user input. The most important part of this for our projects is **taking the data from the backend and building html from it**.



```python
%%html
<head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <style>
        .post {
            border: 1px solid #ddd;
            margin-bottom: 20px;
            padding: 20px;
            border-radius: 5px;
        }
        .like-count {
            color: #007BFF;
        }
    </style>
</head>
<body>

<div id="posts"></div>

<script>
// Fake API function
function getAPI() {
    return [
        {id: 1, content: 'Dogs are man\'s best friend.', likes: 10},
        {id: 2, content: 'Dogs have an exceptional sense of smell.', likes: 20},
        {id: 3, content: 'There are hundreds of different dog breeds.', likes: 30}
    ];
}

$(document).ready(function(){
    var posts = getAPI();
    $.each(posts, function(i, post) {
        var postHtml = '<div class="post"><h2>Post ' + post.id + '</h2><p>' + post.content + '</p><p class="like-count">' + post.likes + ' likes</p></div>';
        $('#posts').append(postHtml);
    });
});
</script>

</body>
```


%%html
<head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <style>
        .post {
            border: 1px solid #ddd;
            margin-bottom: 20px;
            padding: 20px;
            border-radius: 5px;
        }
        .like-count {
            color: #007BFF;
        }
    </style>
</head>
<body>

<div id="posts"></div>

<script>
// Fake API function
function getAPI() {
    return [
        {id: 1, content: 'Dogs are man\'s best friend.', likes: 10},
        {id: 2, content: 'Dogs have an exceptional sense of smell.', likes: 20},
        {id: 3, content: 'There are hundreds of different dog breeds.', likes: 30}
    ];
}

$(document).ready(function(){
    var posts = getAPI();
    $.each(posts, function(i, post) {
        var postHtml = '<div class="post"><h2>Post ' + post.id + '</h2><p>' + post.content + '</p><p class="like-count">' + post.likes + ' likes</p></div>';
        $('#posts').append(postHtml);
    });
});
</script>

</body>


### Popcorn Hack: Complete the Jquery and JavaScript code

This represents a website for buying dogs. The API contains an id, name, price, and breed for each dog. Display them all as html using jQuery.


```python
%%html
<head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <style>
        .dog {
            border: 1px solid #ddd;
            margin-bottom: 20px;
            padding: 20px;
            border-radius: 5px;
        }
        .price {
            color: #007BFF;
        }
    </style>
</head>
<body>

<div id="dogs"></div>

<script>
// Fake API function
function getAPI() {
    return [
        {id: 1, name: 'Max', price: '$1000', breed: 'Golden Retriever'},
        {id: 2, name: 'Bella', price: '$800', breed: 'Labrador Retriever'},
        {id: 3, name: 'Charlie', price: '$1200', breed: 'German Shepherd'}
    ];
}

$(document).ready(function(){
    var dogs = getAPI();
    //Write code here

    var dogsContainer = $('#dogs');

    // Iterate through the dogs array and create HTML elements for each dog
    $.each(dogs, function(index, dog) {
        var dogElement = $('<div class="dog">');
        dogElement.append('<h2>' + dog.name + '</h2>');
        dogElement.append('<p class="price">' + dog.price + '</p>');
        dogElement.append('<p>Breed: ' + dog.breed + '</p>');
        dogsContainer.append(dogElement);
    });
});
</script>

</body>
```


%%html
<head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <style>
        .dog {
            border: 1px solid #ddd;
            margin-bottom: 20px;
            padding: 20px;
            border-radius: 5px;
        }
        .price {
            color: #007BFF;
        }
    </style>
</head>
<body>

<div id="dogs"></div>

<script>
// Fake API function
function getAPI() {
    return [
        {id: 1, name: 'Max', price: '$1000', breed: 'Golden Retriever'},
        {id: 2, name: 'Bella', price: '$800', breed: 'Labrador Retriever'},
        {id: 3, name: 'Charlie', price: '$1200', breed: 'German Shepherd'}
    ];
}

$(document).ready(function(){
    var dogs = getAPI();
    //Write code here

    var dogsContainer = $('#dogs');

    // Iterate through the dogs array and create HTML elements for each dog
    $.each(dogs, function(index, dog) {
        var dogElement = $('<div class="dog">');
        dogElement.append('<h2>' + dog.name + '</h2>');
        dogElement.append('<p class="price">' + dog.price + '</p>');
        dogElement.append('<p>Breed: ' + dog.breed + '</p>');
        dogsContainer.append(dogElement);
    });
});
</script>

</body>


## Animations with JQuery 
You can also create animations in JQuery. 

- styles: Specifies the CSS properties to animate. 
- speed: Optional and specifies the speed of the animation, by default it is 400 milliseconds.
- easing: Optional and Specifies the animation pattern. 
  - “swing” - moves slower at the beginning/end, but faster in the middle
  - “linear” - moves in a constant speed
- callback: Optional, a function to be executed after the animation completes.
  -  By default it is “swing”.

> Animations glitch out jupyter notebooks so this example can't be in runnable code.

```
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
  // Reset CSS properties to their original values
  $("div").css({
    left: '0px',
    opacity: '1',
    height: '100px',
    width: '100%'
  });

  $("button").click(function(){
    $("div").animate({
      left: '250px',
      opacity: '0.5',
      height: '150px',
      width: '100%'
    });
  });
});
</script>
</head>
<body>

<button>Start</button>

<div style="background:#98bf21;height:100px;width:100px;position:absolute;"></div>

</body>
</html>
```

Look at the animation [here](https://soham360.github.io/refactored-engine/animation.html)

### CRUD Principles:

**What Does CRUD Stand For?**
- Answer this as a Popcorn Hack: Create Read Update Delete

**What Does CRUD Do?**
- These four basic operations represent the fundamental actions that can be performed on data in a computer system or a database.

**How Can CRUD Be Applied to jQuery and Beyond?**
- **jQuery:** jQuery is a JavaScript library that simplifies HTML document traversal and manipulation. You can use jQuery to perform CRUD operations on the client side, interacting with the DOM. Here's a brief overview:

### Create (C):
```javascript
// Create a new element and append it to a table
$('#myTable').append('<tr><td>New Data</td></tr>');
```

### Read (R): 
```javascript
// Read data from a table
$('#myTable tr').each(function() {
  console.log($(this).text());
});
```

### Update (U):
```javascript
// Update data in a table
$('#myTable td:contains("Old Data")').text('Updated Data');
```

### Delete (D):
```javascript
// Delete a row from a table
$('#myTable td:contains("Data to Delete")').closest('tr').remove();
```

- **Beyond jQuery:** In more advanced web development scenarios, CRUD operations are often performed using server-side technologies and databases. Technologies like Node.js, Express, Django, Flask, and others are commonly used for server-side development. Databases such as MySQL, MongoDB, and PostgreSQL store and manage the data.

### Demonstration of Applying CRUD to Tables:

Assuming a simple HTML table with the ID "myTable":

```html
<table id="myTable">
  <tr>
    <th>Data</th>
  </tr>
  <tr>
    <td>Row 1</td>
  </tr>
  <tr>
    <td>Row 2</td>
  </tr>
</table>
```

#### Create (C):
```javascript
// Create a new row and append it to the table
$('#myTable').append('<tr><td>New Row</td></tr>');
```

#### Read (R):
```javascript
// Read and log data from the table
$('#myTable tr').each(function() {
    console.log($(this).text());
});
```

#### Update (U):
```javascript
// Update data in the first row of the table
$('#myTable tr:first-child td').text('Updated Row');
```

#### Delete (D):
```javascript
// Delete the second row from the table
$('#myTable tr:nth-child(2)').remove();
```

These examples demonstrate how CRUD operations can be applied using jQuery to manipulate a simple HTML table on the client side. In more complex applications, these operations are often handled on the server side with the help of backend frameworks and databases.

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>jQuery CRUD Demo</title>
    <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        table, th, td {
            border: 1px solid black;
        }
    </style>
</head>
<body>
    <h2>jQuery CRUD Demo</h2>
    <label for="nameInput">Name:</label>
    <input type="text" id="nameInput">
    <label for="reviewInput">Review:</label>
    <input type="text" id="reviewInput">
    <button id="addBtn">Add Row</button>
    <table id="myTable">
        <tr>
            <th>Name</th>
            <th>Review</th>
            <th>Action</th>
        </tr>
        <tr>
            <td>John Mortensen</td>
            <td>Great lesson! Explained UX and CRUD principles as well as usage of jQuery very nicely. +3 indicators! </td>
            <td><button class="editBtn">Edit</button> <button class="deleteBtn">Delete</button></td>
        </tr>
        <tr>
            <td>Sean Yeung</td>
            <td>Very interactive teaching! Covered all the topic but should have made more Taylor Swift references. </td>
            <td><button class="editBtn">Edit</button> <button class="deleteBtn">Delete</button></td>
        </tr>
    </table>
    <script>
        $(document).ready(function() {
            // Add Row
            $('#addBtn').on('click', function() {
                var name = $('#nameInput').val();
                var review = $('#reviewInput').val();
                $('#myTable').append('<tr><td>' + name + '</td><td>' + review + '</td><td><button class="editBtn">Edit</button> <button class="deleteBtn">Delete</button></td></tr>');
            });
            // Edit Row
            $(document).on('click', '.editBtn', function() {
                var currentRow = $(this).closest('tr');
                var name = currentRow.find('td:eq(0)').text();
                var review = currentRow.find('td:eq(1)').text();
                $('#nameInput').val(name);
                $('#reviewInput').val(review);
                currentRow.remove();
            });
            // Delete Row
            $(document).on('click', '.deleteBtn', function() {
                $(this).closest('tr').remove();
            });
        });
    </script>
</body>
</html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>jQuery CRUD Demo</title>
    <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        table, th, td {
            border: 1px solid black;
        }
    </style>
</head>
<body>
    <h2>jQuery CRUD Demo</h2>
    <label for="nameInput">Name:</label>
    <input type="text" id="nameInput">
    <label for="reviewInput">Review:</label>
    <input type="text" id="reviewInput">
    <button id="addBtn">Add Row</button>
    <table id="myTable">
        <tr>
            <th>Name</th>
            <th>Review</th>
            <th>Action</th>
        </tr>
        <tr>
            <td>John Mortensen</td>
            <td>Great lesson! Explained UX and CRUD principles as well as usage of jQuery very nicely. +3 indicators! </td>
            <td><button class="editBtn">Edit</button> <button class="deleteBtn">Delete</button></td>
        </tr>
        <tr>
            <td>Sean Yeung</td>
            <td>Very interactive teaching! Covered all the topic but should have made more Taylor Swift references. </td>
            <td><button class="editBtn">Edit</button> <button class="deleteBtn">Delete</button></td>
        </tr>
    </table>
    <script>
        $(document).ready(function() {
            // Add Row
            $('#addBtn').on('click', function() {
                var name = $('#nameInput').val();
                var review = $('#reviewInput').val();
                $('#myTable').append('<tr><td>' + name + '</td><td>' + review + '</td><td><button class="editBtn">Edit</button> <button class="deleteBtn">Delete</button></td></tr>');
            });
            // Edit Row
            $(document).on('click', '.editBtn', function() {
                var currentRow = $(this).closest('tr');
                var name = currentRow.find('td:eq(0)').text();
                var review = currentRow.find('td:eq(1)').text();
                $('#nameInput').val(name);
                $('#reviewInput').val(review);
                currentRow.remove();
            });
            // Delete Row
            $(document).on('click', '.deleteBtn', function() {
                $(this).closest('tr').remove();
            });
        });
    </script>
</body>
</html>


```python
popcorn hack
```


```python
%%html

<!-- Head contains information to Support the Document -->
<head>
    <!-- load jQuery and DataTables output style and scripts -->
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css">
    <script type="text/javascript" language="javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>var define = null;</script>
    <script type="text/javascript" language="javascript" src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
</head>

<!-- Body contains the contents of the Document -->
<body>
    <table id="xdemo" class="table">
        <thead>
            <tr>
                <th>Make</th>
                <th>Model</th>
                <th>Year</th>
                <th>Color</th>
                <th>Price</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Ford</td>
                <td>Mustang</td>
                <td>2022</td>
                <td>Red</td>
                <td>$35,000</td>
            </tr>
            <tr>
                <td>Toyota</td>
                <td>Camry</td>
                <td>2022</td>
                <td>Silver</td>
                <td>$25,000</td>
            </tr>
            <tr>
                <td>Tesla</td>
                <td>Model S</td>
                <td>2022</td>
                <td>White</td>
                <td>$80,000</td>
            </tr>
            <tr>
                <td>Cadillac</td>
                <td>Broughan</td>
                <td>1969</td>
                <td>Black</td>
                <td>$10,000</td>
            </tr>
            <tr>
                <td>Ford</td>
                <td>F-350</td>
                <td>1997</td>
                <td>Green</td>
                <td>$15,000</td>
            </tr>
            <tr>
                <td>Ford</td>
                <td>Excursion</td>
                <td>2003</td>
                <td>Green</td>
                <td>$25,000</td>
            </tr>
            <tr>
                <td>Ford</td>
                <td>Ranger</td>
                <td>2012</td>
                <td>Red</td>
                <td>$8,000</td>
            </tr>
            <tr>
                <td>Kuboto</td>
                <td>L3301 Tractor</td>
                <td>2015</td>
                <td>Orange</td>
                <td>$12,000</td>
            </tr>
            <tr>
                <td>Ford</td>
                <td>Fusion Energi</td>
                <td>2015</td>
                <td>Guard</td>
                <td>$25,000</td>
            </tr>
            <tr>
                <td>Acura</td>
                <td>XL</td>
                <td>2006</td>
                <td>Grey</td>
                <td>$10,000</td>
            </tr>
            <tr>
                <td>Ford</td>
                <td>F150 Lightning</td>
                <td>2024</td>
                <td>Guard</td>
                <td>$70,000</td>
            </tr>
        </tbody>
    </table>
</body>

<!-- Script is used to embed executable code -->
<script>
    $("#xdemo").DataTable();
</script>
```


%%html

<!-- Head contains information to Support the Document -->
<head>
    <!-- load jQuery and DataTables output style and scripts -->
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css">
    <script type="text/javascript" language="javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>var define = null;</script>
    <script type="text/javascript" language="javascript" src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
</head>

<!-- Body contains the contents of the Document -->
<body>
    <table id="xdemo" class="table">
        <thead>
            <tr>
                <th>Make</th>
                <th>Model</th>
                <th>Year</th>
                <th>Color</th>
                <th>Price</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Ford</td>
                <td>Mustang</td>
                <td>2022</td>
                <td>Red</td>
                <td>$35,000</td>
            </tr>
            <tr>
                <td>Toyota</td>
                <td>Camry</td>
                <td>2022</td>
                <td>Silver</td>
                <td>$25,000</td>
            </tr>
            <tr>
                <td>Tesla</td>
                <td>Model S</td>
                <td>2022</td>
                <td>White</td>
                <td>$80,000</td>
            </tr>
            <tr>
                <td>Cadillac</td>
                <td>Broughan</td>
                <td>1969</td>
                <td>Black</td>
                <td>$10,000</td>
            </tr>
            <tr>
                <td>Ford</td>
                <td>F-350</td>
                <td>1997</td>
                <td>Green</td>
                <td>$15,000</td>
            </tr>
            <tr>
                <td>Ford</td>
                <td>Excursion</td>
                <td>2003</td>
                <td>Green</td>
                <td>$25,000</td>
            </tr>
            <tr>
                <td>Ford</td>
                <td>Ranger</td>
                <td>2012</td>
                <td>Red</td>
                <td>$8,000</td>
            </tr>
            <tr>
                <td>Kuboto</td>
                <td>L3301 Tractor</td>
                <td>2015</td>
                <td>Orange</td>
                <td>$12,000</td>
            </tr>
            <tr>
                <td>Ford</td>
                <td>Fusion Energi</td>
                <td>2015</td>
                <td>Guard</td>
                <td>$25,000</td>
            </tr>
            <tr>
                <td>Acura</td>
                <td>XL</td>
                <td>2006</td>
                <td>Grey</td>
                <td>$10,000</td>
            </tr>
            <tr>
                <td>Ford</td>
                <td>F150 Lightning</td>
                <td>2024</td>
                <td>Guard</td>
                <td>$70,000</td>
            </tr>
        </tbody>
    </table>
</body>

<!-- Script is used to embed executable code -->
<script>
    $("#xdemo").DataTable();
</script>


# Hacks

Combine all aspects taught throughout this lesson. 
- Store data on the frontend with CRUD functionality. +0.25 
- You should create a frontend which can displays data with JQuery. Make sure to use event handling on each item stored to use the CRUD functionality. +0.25
- And make it look good using UX design techniques. + 0.2

In addition:
- Complete all popcorn hacks + 0.2
- Do something extra +0.1. Some good ideas are adding JQuery animations to your hacks, use extra JQuery events, or do anything else extra.

HACK SUBMISSION (RACHIT):
https://rachit-j.github.io/rachits-demo-blog/ - MAIN HACK
https://rachit-j.github.io/rachits-demo-blog/cars/ - EXTRA

