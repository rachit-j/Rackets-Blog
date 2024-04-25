---
title: Workshop 4 - Lesson on 2D Arrays and Traversing them
description: Unit 8 of CB
toc: True
layout: post
---

<h2>  8.1: Declaring + Initializing 2D Arrays; Determining their  </h2>

> Review: 
Arrays are a collection (list) of elements (primitive or object reference type data)  

So, a 2-Dimensional array is an array where the elements within that array are other arrays 

2D arrays can be better at storing certain types of information 

* Especially if the data represents a space, with rows and columns


Seating chart: 

| . | Column 1 | Column 2 | Column 3 | 
| - | - | - | - |
| Row 1 | Abby | Ben | Clara | Principalida | 
| Row 2 | Ethan | Frank |  | Flanklin | 
| Row 3 | Isabelle | John | Kim | Leo | 

Note that this is a non-rectangular 2D array 

* Or if the data needs to be classified under categories 

| . | Month 1 | Month 2 | Month 3 | 
| - | - | - | - |
|  Winter | December | January | February |
|  Spring | March | April | May |
|  Summer | June | July | August |
|  Fall | Summer | October | November |

This is a rectangular 2D array. Non-rectangular 2D arrays are not a part of the CSA course


<h4> Declaring a 2D array </h4>

2D Arrays can be declared like this: 

``` dataType[][] nameOfArray; ```

<h3> Initializing a 2D array </h3>

``` new dataType[r][c]; ```

r: number of rows (number of arrays)
<br>
c: number of columns (length of each array)


```Java
public class Seasons {

    private String[][] Seasons = new String[2][3];

    // Or, if you already know what the elements should be:

    private String[][] Seasons2 = {
        {"December", "January", "February"},
        {"March", "April", "May"},
        {"June", "July", "August"},
        {"September", "October", "November"}
    };

}

```


### Size of 2D Arrays

The size of the 2D array is classified by number of rows by number of columns 

Number of rows can be found like this: 

``` r = trimesterCourses.length ```

This would give the number of arrays within the 2D array, since each array is an element

For number of columns: 

``` c = trimesterCourses[0].length ```

This finds the number of elements of the first array within the 2D array.


<h3> Accessing the Elements of a 2D Array </h3>

The elements of a 2D array can be accessed using index

``` Seasons[0][2] ```


**Output: February**

the value in the first bracket is the index of the rows, or which array we are accessing. In this case, the 0th index means we are accessing the first array 

The value in the second bracket is the index within the array. So we are looking for the 2nd value within the first array.


To update the element of a 2D array, all you need to do is reference its location and change the value. 






```Java
public class Seasons {

    private String[][] seasons = new String[2][3];

    private static String[][] seasons2 = {
        {"December", "January", "February"},
        {"March", "April", "May"},
        {"June", "July", "August"},
        {"September", "October", "November"}
    };

    public static void main(String[] args) {
        System.out.println(seasons2[0][2]);
        seasons2[0][2] = "Changed Value";  
        System.out.println(seasons2[0][2]);
    }
}

Seasons.main(null);


```

    February
    Changed Value


## Notes on Common Mistakes

Here are some notes on common mistakes made in the context of the 2D arrays question. People around the country will *definitely* make all of these mistakes many times over, so let's hope that none of those people are people at our school.

### Array Errors

We just had a lesson on common Arrays errors, so rather than rephrase their work, give [these mistakes](https://men-in-brown.github.io/BrownPages/ArraysLesson#common-mistakes) another look.

There are some Array errors that are especially relevant to 2D arrays problems, however. For example...

- Off-By-One Errors

When working with a 2D array, you are working with an array full of arrays. In this structure, there is a set number of rows and columns when the structure is initialized. The length of each row and the number of rows are *often different*, so both must be identified properly before iterating using index-based loops.

Out of bounds errors will *always* lose you at least one point on the scoring guidelines, according to our research.

- For-Each loop modification

If values are intended to be modified during an iterative process, *do not* use a for-each loop. The elements accessed using this strategy are copies; accessing the array indexes directly to make modifications is the only way for them to be retained. See the example below:


```Java
import java.util.Arrays;

int[][] modifyArray = {
    {1, 4, 3},
    {3, 8, 9}
};

System.out.println("Prior to modification: " + Arrays.deepToString(modifyArray));

for (int[] row : modifyArray) {
    for (int col : row) {
        if (col == 3) {
            col = 0;
        }
    }
}

System.out.println("After to modification: " + Arrays.deepToString(modifyArray));
```

    Prior to modification: [[1, 4, 3], [3, 8, 9]]
    After to modification: [[1, 4, 3], [3, 8, 9]]


Instead, when modifying, you can use a traditional for loop (which also comes with the added benefit of having direct access to the relevant indexes):


```Java
import java.util.Arrays;

int[][] actualModifyArray = {
    {1, 4, 3},
    {3, 8, 9}
};

System.out.println("Prior to modification: " + Arrays.deepToString(actualModifyArray));

for (int r = 0; r < actualModifyArray.length; r++) {
    for (int c = 0; c < actualModifyArray[r].length; c++) {
        if (actualModifyArray[r][c] == 3) {
            actualModifyArray[r][c] = 0;
        }
    }
}

System.out.println("After to modification: " + Arrays.deepToString(actualModifyArray));
```

    Prior to modification: [[1, 4, 3], [3, 8, 9]]
    After to modification: [[1, 4, 0], [0, 8, 9]]


### FRQ Scoring Guidelines Mistakes

To succeed on the AP test, it's important to be able to identify which elements of a correct answer earn points.

- Most often, if you create a method in a previous part used to interact with a 2D array, *it is intended that you use that method again in future methods*.

Means of traversing and interacting with 2D arrays are relatively specific in the context of one College Board problem (i.e., iterate through to determine a condition about a row, find a value in a row, search columns by condition, etc.), so make sure to analyze the context to determine if a certain method may be used again to abstract what would otherwise be a more complex task in a future method. With practice, this connection should be obvious.

If there is no possible relevance between two methods, this may not necessarily be the case.

Make sure that you use the proper parameters when calling your own method! Scoring guidelines are sometimes lenient about this, but don’t tempt fate. Just format your call properly.

- If a “helper” method is provided to you in a question, *make sure to note it and use it*.

If one is provided, it is most certainly present to make the process of writing the code less complex. Scoring guidelines will always include utilizing past student-created methods and “helper” methods.

You can also use the helper method’s functionality to aid your thinking about a question. If you are confused by its content and aren’t sure how to tackle the problem instinctively, you can be sure that a provided “helper” method will be a part of the solution.

Once again, make sure that you’re using the proper parameters!

- Know how to use column-major order. (Many go into the test having only used row-major order.)

It's very possible that a question will prompt you to access a 2D array by its columns. (We found two in research for this lesson.) If you know you haven't practiced column-major order, give the code below a look. It might be a good idea to create your own code cell with a unique 2D array to practice with.


```Java
int[][] array = {
    {3, 5, 1},
    {9, 9, 7}
};

// you should always be able to use array[0].length for the number of columns
// since each row is the same length
int colNum = 1;
for (int col = 0; col < array[0].length; col++) {
    System.out.print("Column " + colNum + ":\t");
    for (int row = 0; row < array.length; row++) {
        System.out.print(array[row][col] + "\t");
    }
    System.out.println();
    colNum++;
}
```

    Column 1:	3	9	
    Column 2:	5	9	
    Column 3:	1	7	


### Popcorn Hack:



```Java
public class TrimesterGrades {

    private static int[][] trimesterGrades = {
        {85, 90, 78, 92, 99}, // tri 1
        {92, 88, 91, 97, 80}, // tri 2
        {79, 85, 83, 95, 67}  // tri 3
    };

    public static void main(int[] args) {
        System.out.println(trimesterGrades[2][4]);
        trimesterGrades[2][4] = 90;  
        System.out.println(trimesterGrades[2][4]);
    }
}

TrimesterGrades.main(null);
```

    90
    90


The 2D array keeps track of a students grade, grouped by each trimester. 
The student, currently in Trimester 3, retook a test in their 3rd period, which raised that grade to 90. 

Show how they would write code that changes the grade for the 3rd period class

Hacks:
Finish FRQ from Friday, 2015 Q1

Hack done:


```Java
/** Returns the sum of the entries in the one-dimensional array arr.
 */ 
public static int arraySum(int[] arr) 
{
    int sum = 0; 
    for (int i = 0; i < arr.length; i++)
    {
        sum += arr[i]; 
    }
    return sum; 
}

/** Returns a one-dimensional array in which the entry at index k is the sum of * the entries of row k of the two-dimensional array arr2D. */ 
public static int[] rowSums(int[][] arr2D) { 
    int [] sums=new int[arr2D.length]; 
    int rowNum=0; 
    for(int[] row : arr2D) { 
        sums[rowNum]=arraySum(row); 
        rowNum++; 
    } return sums; 
}

/** Returns true if all rows in arr2D have different row sums; * false otherwise. */ 
public static boolean isDiverse(int[][] arr2D) { 
    int [] sums=rowSums(arr2D); 
    for (int i=0; i < sums.length; i++) { 
        for (int j=i+1; j < sums.length; j++) { 
            if (sums[i]==sums[j]){ return false; 
            } 
        } 
    } return true; 
}
```
