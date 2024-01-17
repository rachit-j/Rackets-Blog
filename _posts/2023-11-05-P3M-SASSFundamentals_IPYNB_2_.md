---
comments: True
layout: post
title: P3-M Introduction to SASS
description: Understanding the fundamental aspects of SASS
courses: {'labnotebook': {'week': 15}}
type: hacks
---

# What is SASS?

> Sass is a preprocessor language that's interpreted into CSS. A preprocessor language takes input data and converts it to an output that's used as input by another program. This means when you run Sass code, you're actually converting your code to CSS. That CSS code output is then used directly by a browser.
![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMd7eiGMX9FwRLC0uJTDewSjw_7_WvCF4ABLdwztLrCnPEXrqW0gG-pH8eT-fYPLlghjY&usqp=CAU)

#  SCSS vs. CSS 
> Understanding the differences between SCSS and CSS

## What is CSS
- CSS is the default technology that most programmers use when styling webpage. It is one of the 3 fundamental web technologies along with HTML and JavaScript. HTML manages the structure, JavaScript makes pages interactive, and CSS changes the style by taking a markup language like HTML and describes how it should be presented to the user.

- However, CSS is not very easy to work with lacking a lot features often making using CSS very confusing and difficult or hard to work with on lengthy projects. This is why there are tools like Bootstrap, Sass, and Tailwind that make styling a lot easier and more efficient. We will be using Sass in this course.  

### CSS Example
- This is an example of CSS that can be used to change body text of an HTML document
- Hack Question: Can you guess what its changing style of the text to? 

Its changing the size of the text to 16 pixels, the fonts to ariel and sans-serif. 


```python
body{
color: #0000FF;
font-family: Ariel, sans-serif;
font-size: 16px;
}
```


## What is SCSS
- SCSS is short for Sassy Cascading Style Sheets. 
- SCSS very similar to CSS but the difference comes with the fact that SCSS extends the functionality of CSS while also making it simpler. What this allows us to do is it enables us to things like nested styling, functions, mixins, variables, inheritance (more on these later) and so on. 

### Sass Code Example


```python
$blue: #0000FF;
body{
color: $blue;
font-family: Ariel, sans-serif;
font-size: 16px;
}
```


- This example is doing the same thing as the other code segment above but the difference being that here we defined the color as $blue which makes it much easier for us to recall later on. In fact, we have done this before, if you have been using the dark mode/midnight theme then go ahead and navigate your your _sass folder and check out the dark-mode.scss and you'll see something similar to the example above

### So which one is better to use?
- CSS tends to be better for really simple styling where not many complex or nested styles are required and small projects that doesn't require a lot of customization. 
- SCSS on the other hand is very good for more complex styling and working with a project with more than one page where maybe lots of customization is needed. Such as the projects we made last and first trimester.

# Modular SCSS 
> Understanding how to use modular SCSS
- Modular SCSS allows you to break multiple different files and then be able to compile them into a single CSS file 
- How do you do this? Well all you need to do is have _filenames.scss so that is compiled into its own file
- Now after adding the _ to the file name you can import it into you file without the _ and all the styles will be carried over. 
- The benefits of a partial is that it allows you to big websites and allows you to break up the code in multiple components and easily make changes instead of having to go through a huge file.
- All styles in the partial will be added and can be used into the main file as if they were defined in the main file.

## File 1 _variable.scss


```python
$primary-button-color: #009494;
$hover-color: black;
$menu-color: #f2f2f2;
```

## File 2 style.scss
- We can see the importing of the .scss file's content into the other main .scss file style.scss


```python
{@import 'variables';
@import "{{ site.theme }}";}
/* "row style" is flexible size and aligns pictures in center */
.row {
    align-items: center;
    display: flex;
  }
  
  /* "column style" is one-third of the width with padding */
  .column {
    flex: 33.33%;
    padding: 5px;
  }

.menu a {
  // float: left;
  display: block;
  color: $menu-color;
  text-align: center;
  // padding: 14px 16px;
  text-decoration: none;
}
.menu a:hover {
  background: $primary-button-color;
    color: $hover-color;
}

```

# Nesting

> What is nesting? 
    > Answer here (hack question): 
- Nesting is a way to organize your code and make it easier to read. It also helps keep your code DRY (dont repeat yourself) . 
- Nesting is when you put one selector inside another selector. This is a great way to keep your code organized and make it easier to read. 
- When we make HTML we often nest different elements within each other and have a clear structure when we look at it.
- The problem is that in regular CSS we don't have that so we need to use SASS to help us organize our code.

- Warning: Don't nest too much as when the CSS is processed it can make overqualified selectors which can be hard to read and maintain. Which means that it would only target that specific element type and not any other elements that have the same class name.

## Sass Nesting
- Through nesting the ul, li, and a selectors within the nav selector makes your CSS better and increases its readability overall.


```python
nav {
  ul {
    margin: 0;
    padding: 0;
    list-style: none;
  }

  li { display: inline-block; }

  a {
    display: block;
    padding: 6px 12px;
    text-decoration: none;
  }
}

```

## CSS - Lack of Nesting
- We can see that through the lack of nesting the CSS is not as organized and needs extra information to be able to make it more clear exactly what is being targeted.


```python
nav ul {
  margin: 0;
  padding: 0;
  list-style: none;
}
nav li {
  display: inline-block;
}
nav a {
  display: block;
  padding: 6px 12px;
  text-decoration: none;
}
```

# Variables
> What is a variable?
- A variable is a container that stores information so for instance when you have multiple places that refer to one value you can just use the variable name instead of the value.
- This is valuable in SASS because it allows you to reuse that value in multiple places throughout your stylesheet. 
- The $ symbol is used in Sass to designate a variable. 

Pro Tip: The reason SASS variables are better than variables in regular CSS is that they are easier to read with a much simpler syntax. 

Fun Fact: Variables in SASS came before CSS and often SASS has features long before they are actually added to CSS as a whole. 

## Variable Example Syntax
- $variable-name: value;
- Once the sass is processed the variable name is replaced with the value throughout the program.


```python
$main-font: Calibri, sans-serif;
$main-color: #000;
$main-color-hover: #000;
```

# Operators
- Operators are used to perform operations on variables and other aspects of the language. Similar to python syntax, we can use operators to see if values are equal, add, divide, subtract, multiply, etc.
- SASS has a lot of operators that can be used to perform operations on variables and other aspects of the language as well. They can include
    - `== to check if two values are equal and != to check if two values are not equal`
    - `+ to add two values together` 
    - `- to subtract two values`
    - `* to multiply two values`
    - `/ to divide two values`
    - `% to find the remainder of two values`
    - `< to check if one value is less than another`
    - `> to check if one value is greater than another`
    - `<= to check if one value is less than or equal to another`
    - `>= to check if one value is greater than or equal to another`
    - `Also there is and, or, & not to be able to use boolean operations`

## Operator Example Syntax
- Operators are used in this example to perform string concatenation


```python
// Html
<p id="testing">original text and</p>

// SASS
#testing:after{
  content: " some" + " more" + " text";
}

// Output
original text and some more text
```

# Conditional Statements 
- There are conditional statements in SASS just like in Python and JavaScript they work the same way as well.
- Conditional statements are used to perform different actions based on different conditions. Such as if a certain condition is true then do this, if it is false then do that and so on.
- SASS has @if which allows for different styles based on if a boolean expression was true or false.
- SASS has @else which allows for different set of styles if the if condition was not met or false. 
- SASS has @else if which allows for an alternative conditions to be run if the first is not met. 


```python
$color: red;

button {
  @if $color == red {
    background-color: $color;
  }
}
// @else: allows you to provide an alternative set of styles to apply if the condition in the @if statement isn't met
$color: blue;

button {
  @if $color == red {
    background-color: red;
  } @else {
    background-color: $color;
  }
}
// @else if: allows you to provide multiple alternative conditions to test
$color: green;

button {
  @if $color == red {
    background-color: red;
  } @else if $color == blue {
    background-color: blue;
  } @else {
    background-color: $color;
  }
}

```

# Loops In Sass
- Loops are present in SASS through the @for and @while decorators, along with @each. 
- Loops are used to repeat a block of code a certain number of times or until a certain condition is met just like in any other programming language.
    - For Loops: Are used to iterate through a value like a list or a range of numbers
    - While Loops: Are used to iterate through a block of code until a certain condition is met such as a value is being equal to a certain value through an incrementing or decrementing a variable or any other condition that is met.

- When using while loops they can be necessary but it is better to use @each and @for as it will make it clear and be able to compile faster.

- Side Note: In SASS lists care a any group of values that are separated by a comma or a space there is no special brackets used in JavaScript. Lists can be searched for values however they are immutable meaning that they cannot be changed once they are created.

## Some Code Examples of Loops and Lists


```python
// A for each loop is used to interact with a group of sizes changing 
// the size of the element for each item in the list

$sizes: 40px, 50px, 80px;

@each $size in $sizes {
  .icon-#{$size} {
    font-size: $size;
    height: $size;
    width: $size;
  }
}


// @each: allows you to loop over a list of values and generate styles
$colors: red, green, blue;

@each $color in $colors {
  .color-#{$color} {
    background-color: $color;
  }
}
```


```python
@debug list.index(1px solid red, 1px); // 1
@debug list.index(1px solid red, solid); // 2
@debug list.index(1px solid red, dashed); // null
```


```python
@use "sass:math";

/// Divides `$value` by `$ratio` until it's below `$base`.
@function scale-below($value, $base, $ratio: 1.618) {
  @while $value > $base {
    $value: math.div($value, $ratio);
  }
  @return $value;
}

$normal-font-size: 16px;
sup {
  font-size: scale-below(20px, 16px);
}
```


```python
$base-color: #036;

@for $i from 1 through 3 {
  ul:nth-child(3n + #{$i}) {
    background-color: lighten($base-color, $i * 5%);
  }
}

// @for:  allows you to loop over a range of values and generate styles

@for $i from 1 through 3 {
  .item-#{$i} {
    width: 100px * $i;
  }
}
```

#  Functions in SASS
> What is a function?
- A function is a block of code that performs a specific task. This is a great method to be able to reuse code and processes in a manner that is more efficient and allows for the reuse of code. We do this all the time in programming languages such as JavaScript.

## SASS functions
- Sass Functions allow you to define complex calculations and transformations that can be used throughout your stylesheet and allow you to perform complex operations on values, manipulate data, plus you can generate content dynamically.

- There a are built in functions and ones you can make on your own like languages such as JavaScript.
  
- SASS functions can be used to perform arithmetic operations, manipulate colors, work with strings, and more.

- Functions in SASS are similar to functions in programming languages, but they can be used within SASS stylesheets to generate CSS code dynamically.

## Using Built-in Functions
- Like Python and Javascript SASS provides a variety of built-in functions for  math, color manipulation, string manipulation, and more. 


## Math Functions
- SASS has many functions that allow you to be able to perform wide range of math operations similar to the ones present in python including more complex operations. 



```python

.round(1.2);          // returns 1
.ceil(1.2);           // returns 2
.floor(1.2);          // returns 1
.abs(-1.2);           // returns 1.2
.min(1, 2, 3);        // returns 1
.max(1, 2, 3);        // returns 3
.random(1, 100);      // returns a random number between 1 and 100

```

## Color Functions
- Color is an important component of any website and SASS provides a wide range of functions that allow you to manipulate colors in a variety of ways.


```python
.lighten(#007fff, 20%);       // returns a lighter shade of blue
.darken(#007fff, 20%);        // returns a darker shade of blue
.opacify(#007fff, 0.2);       // makes the color more opaque
.transparentize(#007fff, 0.2); // makes the color more transparent
.mix(#007fff, #ff0000, 50%);  // returns a mix of two colors
```

## String Functions
- SASS provides a variety of string functions that allow you to manipulate strings. Here are some examples:


```python
.to-upper-case("hello world");  // returns "HELLO WORLD"
.to-lower-case("HELLO WORLD");  // returns "hello world"
.str-index("hello world", "world"); // returns the index of the first occurrence of "world"
.str-insert("hello", " world", 5);  // inserts " world" into "hello" at position 5
```

## Creating Custom Functions

- In addition to using built-in functions, you can also create your own functions in SASS using the ``@function name(arguments){}``
- @return is similar to the return statement in JavaScript. It returns a value from a function.
- Functions take input values, perform calculations, and return a result. Here's an example of a simple function that calculates the area of a rectangle:


```python
@function rectangle-area($width, $height) {
  @return $width * $height;
}

// Usage:
$area: rectangle-area(10px, 20px); // Returns 200px
```

- Or you can also make a different kind of function that increases the font size to the factorial of a inputted number.  


```python
@function factorial($number){
  $calculated: 1;
  @for $_ from 1 through $number {
    $calculated: $calculated*$number;
  }
  @return $calculated;
}

#testing {
  font-size: factorial(3);
}
```


```python
//Combining functions and loops to achieve different sass effects

@function sum($numList){
  $sum: 0;
  @each $num in $numList {
    $sum: $sum+$num;
  }
  @return $num;
}

@function tri($num){
  $sum: 0;
  @for $i from 1 through $num {
    $sum: $sum+$num;
  }
  @return $sum;
}

@function max($nums){
  $i:0;
  $value:0px;
  @while $i<length($nums){
    @if $value<list.nth($nums,$i){
      $value:list.nth($nums,$i);
    }
  }
}

```

- Custom functions are very powerful, and can be used to create reusable pieces of code that can be used throughout your stylesheets.
 
- SASS functions are a powerful feature that allow you to perform complex operations on values, manipulate data, and generate content dynamically. By using built-in functions and creating your own custom functions, you can greatly extend the capabilities of your SASS stylesheets.

# Mixins
> Mixin what is a mix in what are we mixing in?
    > Answer here (hack question): 
- Mixins are a way to make groups of CSS that you want to reuse throughout your site anywhere you please.
- Mixins are a form of template and that you can use to build on top of to make different features later on this prevents you from having to write the same code over and over again.
- This is a form of encapsulation in your CSS and is a great way to make your code more organized and easier to read.
- Mixins can also take in arguments and be able to be used to apply effects on certain elements if that is a feature you want to add to your site. However unlike functions which also take arguments mixins cannot return values.
- To use a mixin declare it with @mixin and then incorporate with @include.

# Inheritance
> What is inheritance?
    > Answer here (hack question): 
- In general programming concept where the child class can ______ properties from the ______ class. These properties can be changed and modified in the ______ class. This prevents code from being repeated and makes the code more usable and flexible.
- In SASS we have a similar concept that can be used as well we can create base styles and then have other styles inherit from them and then we can change them as we please. 
- We can do that by through using @extend .name-of-class and then we can add more styles to it as we please. Simple as that 

## Mixin & Inheritance Code Example


```python
// example of @mixin
@mixin button {
  width: auto;
  height: auto;
  border-radius: 10px;
  background-color: #21807c;
  border: 3px solid black;
  font-size: 1.5em;

  display: flex;
  justify-content: center;
  align-items: center;

  grid-column: span 1;
  grid-row: span 1;

  // creates smooth animation effect
  transition: all 0.5s; 
}

// default button theme for calculator and stopwatch buttons. Both will follow the same button format
.button {
    // uses the scss from the @mixin
  @include button;
}

/* styling for the calculator clear button */
.calculator-button-clear {
    // @extend inherits .button and then changes the background color from .button
  @extend .button;
  background-color: #e68b1c;
}

/* styling for the calculator equals button */
.calculator-button-equals {
    // another @extend inherits .button and then changes the background color from .button
  @extend .button;
  background-color: #e70f0f;
}
```

# Compiling SASS to CSS
SASS can't be directly input to an HTML file, it first must be compiled to CSS. The easiest way to do this is in your terminal. Change the name of your input and output file to whatever you would like to run the conversion a single time. 
```console
sass input.scss output.css
```

If you want to automatically change your CSS file whenever you update the SASS file, you can instead run:

```console
sass --watch input.scss output.css
```

This will update whenever you save a change in your SASS file. If you're actively working on a project and changing the SASS this is probably the better option for you.

<!-- # Hacks & [Hack Helper - Calculator](https://nighthawkcoders.github.io/teacher_portfolio/c7.0/2023/08/23/javascript-calculator.html)  -->
## Hacks
- Hacks are due by Friday 12/08/2023 at 11:59 p.m. PST. Any late submission will have a deduction of 0.1 Indicators from their total grade. 

## Hack Questions .1 Indicators
- Answer the hack questions throughout the lesson.

## Sass Demo 0.5+ Indicators
- Using at least 3 sass features (variables, nesting, mixins, etc.) create a UI demo that may be used for future or current projects. Extra Indicators will be awarded based on creativity and extra addition of features from SASS.

## Reflection .3 Indicators
- Reflect on each feature you decided to use for your UI demo. Explain how this feature was utilized and why it was more effective than accomplishing the same task without SASS

Live SASS Demo: https://rachit-j.github.io/rachits-demo-blog/sassdemo/

Stylesheet:
```
// Variables
$custom-blue: #3498db;
$base-font-family: 'Helvetica Neue', sans-serif;

// Function to generate shades
@function shade-of-color($color, $percentage) {
  @return mix(white, $color, $percentage);
}

// Complex Container
.complex-container {
  font-family: $base-font-family;
  padding: 20px;
  background-color: shade-of-color($custom-blue, 20%);
  border: 1px solid shade-of-color($custom-blue, 40%);
  border-radius: 10px;

  // Loop to create multiple boxes with varying shades
  @for $i from 1 through 5 {
    .box-#{$i} {
      background-color: shade-of-color($custom-blue, $i * 15%);
      padding: 15px;
      margin-bottom: 5px;
      transition: transform 0.3s ease;

      &:hover {
        transform: scale(1.1);
      }

      // Nested Pseudo-Classes
      &:nth-child(odd) {
        border: 2px dotted shade-of-color($custom-blue, $i * 10%);
      }

      // Nested Media Query
      @media (min-width: 600px) {
        width: calc(100% / 3 - 10px);
        display: inline-block;
        margin-right: 10px;

        &:nth-last-child(-n+3) {
          margin-bottom: 0;
        }
      }
    }
  }
}

```

Reflection: 

Features:
Variables: SASS allows us to define reusable variables, such as colors and font families. These variables make it easy to maintain a consistent design by centralizing values that may change throughout the stylesheet.

Nesting: SASS allows nesting of selectors, matching the HTML structure. This improves code readability and reduces redundancy, as we don't need to repeat parent selectors in each rule.

Loops: SASS's loops simplify the creation of repetitive code patterns. In the example, a loop is used to generate five boxes with varying styles. Without SASS, this would require duplicating code for each box, leading to bloated and less maintainable code.

Mixins and Functions: SASS enables the reuse of common code patterns using mixins and functions. This promotes code reusability and maintainability. For instance, we can define transitions and media queries once and use them across the stylesheet.

Modularization: SASS promotes modularization and encapsulation of styles within selectors. This makes it easier to manage and apply styles to specific elements without affecting unrelated parts of the layout.

Efficient Color Manipulation: SASS simplifies color manipulation and calculations. In this example, it's used to generate shades of a base color, creating a visually appealing and consistent design.

Overall, SASS streamlines the styling process, making it more organized, maintainable, and efficient. It eliminates redundancy, encourages code reuse, and facilitates the creation of dynamic and visually pleasing interfaces. Without SASS, achieving the same level of modularity and code efficiency would be more challenging and error-prone.
