---
toc: True
comments: True
layout: post
title: Unit 10 Lesson
description: the lesson for the unit 0
permalink: /lesson10
courses: {'csa': {'week': '11'}, 'labnotebook': {'week': 11}}
type: tangibles
---

```java
// void recursive method
public static void simpleRecur(int n)
{
    System.out.println(n);
    if (n > 2) // the if statement cuases the recursion to end when n <. 2 since the recursive call 
    // since the recursive call only occurs when n > 2 
        simpleRecur(n-1); 
    System.out.println(n);

}
```

lets trace the call simpleRecur(4)

<table>
  <tr>
    <th>Call Stack</th>
    <th>Variable trace for call</th>
    <th>Output</th>
  </tr>
  <tr>
    <td>simpleRecur(4)</td>
    <td>n=4, 4>2, T</td>
    <td>4 3 2 2 3 4</td>
  </tr>
  <tr>
    <td>simpleRecur(3)</td>
    <td>n=3, 3>2, T</td>
    <td>3 2 2 3</td>
  </tr>
  <tr>
    <td>simpleRecur(2)</td>
    <td>n=2, 2>2, F</td>
    <td>2 2</td>
  </tr>
</table>


### pop corn hack!!!!!!
#### Note: 0.01 extra credit for each correct answer, we have limit Paraas to 3 answers.

What would be the output of the code above? (0.01 extra credit)

here is a modified code from above, what would be the output of the code above? and what would be the base case? (0.01 extra credit)
In this modified code, there is no base case to end the recursion, and the value of n is increased with each recursive call. This code will result in an infinite loop, as there is no condition that prevents the recursive calls from continuing indefinitely. There is no specific base case in this modified code.



```java
// infinite 
public static void simpleRecur(int n)
{
    system.out.println(n);
    if (n > 2)
        simpleRecur(n+3); 
    system.out.println(n);

}
```

| Call Stack  | Variable trace for call  |
|---|---|
| simpleRecur(4)  | n=4    4>2, T  |
| simpleRecur(7)  | n=7   7>2, T  |
| simpleRecur(10)  | n=10    10>2, T  |

n is getting larger infinitely. java will eventually run out of memory and cause a ```CallStackOverflowException```.


```java
// non-void recursive method
public static void simpleRecur(int n)
{
    system.out.println(n);
    if (n == 0)
        return 0;
    return n + system.out.println(n);

}
```

| Call Stack  | Variable trace for call  |
|---|---|
| simpleRecur(8)=8 + simpleRecur(4) | n=8    8==0 F |
| simpleRecur(4)=4 + simpleRecur(2) | n=4    4==0 F |
| simpleRecur(2)=2 + simpleRecur(1) | n=2    2==0 F |
| simpleRecur(1)=1 + simpleRecur(0) | n=1    1==0 F |
| simpleRecur(0)=0 | n=    0==0 T |


### but where does it return 0 to?


<body>
    <div id="content">
        <p>Enter the password to answer:</p>
        <input type="password" id="password">
        <button onclick="revealText()">Reveal Text</button>
        <div id="hiddenText" style="display: none;">
            <p>where it was called!!!!<br/>

in this case, 0 was recalled in simpleRecur(0), the 0 replaces it so 1+ 0 = 1 and 1 tries to do the same as zero</p>
        </div>
    </div>
    <script>
        function revealText() {
            const password = document.getElementById("password").value;
            const hiddenText = document.getElementById("hiddenText");
            if (password === "mort") {
                hiddenText.style.display = "block";
            } else {
                alert("Incorrect password. Try again.");
            }
        }
    </script>
</body>

### what would be the return of simpleRecur(8)?
<body>
    <div id="content">
        <p>Enter the password answer:</p>
        <input type="password" id="password">
        <button onclick="revealText()">Reveal Text</button>
        <div id="hiddenText" style="display: none;">
            <p>8</p>
        </div>
    </div>
    <script>
        function revealText() {
            const password = document.getElementById("password").value;
            const hiddenText = document.getElementById("hiddenText");
            if (password === "vardaan") {
                hiddenText.style.display = "block";
            } else {
                alert("Incorrect password. Try again.");
            }
        }
    </script>
</body>




### most of this might have flew over your head, but don't fret. 
## real world examples of recursion:
### Russian dolls
- Russian dolls are a set of wooden dolls of decreasing size placed one inside another.
- The dolls are made in such a way that each doll can be opened in half to reveal a smaller doll inside.
- Lets set the smallest as the base case
- The dolls are a recursive structure because each doll is a smaller version of the previous doll.

![Russian dolls](https://nestingdolls.co/cdn/shop/products/product-image-782189840.jpg?v=1571724422)

mr. finn here is gonna talk about how to visualize recursion better. 

## 10.2
- James and Justin

# linear search 

int Array- |0|2|4|6|8|10|12|14|16|18|20|22|

target 12

with linear search, we just iterate through each value, starting at the start of the list. here, we need 7 iterations to find 4.

# iterative binary search


```java
//iterative approach to binary search
// This is a method for performing a binary search on a sorted integer array.
// It returns the index of the target element if found, or -1 if the element is not in the array.
public static int binarySearch(int[] intArray, int lowPosition, int highPosition, int target) {
    int midPosition;

    // Use a while loop to repeatedly divide the search range in half.
    while (lowPosition <= highPosition) {
        // Calculate the middle position of the current search range.
        midPosition = (highPosition + lowPosition) / 2;

        // If the element at the middle position is less than the target,
        // we narrow our search to the right half of the current range.
        if (intArray[midPosition] < target) {
            lowPosition = midPosition + 1;
        }
        // If the element at the middle position is greater than the target,
        // we narrow our search to the left half of the current range.
        else if (intArray[midPosition] > target) {
            highPosition = midPosition - 1;
        }
        // If the element at the middle position is equal to the target,
        // we have found our target, and we return its index.
        else {
            return midPosition;
        }
    }
    
    // If the while loop completes without finding the target, we return -1 to indicate it's not in the array.
    return -1;
}

```

# recursive binary search


```java
public static int recBinarySearch(int[] intArray, int lowPosition, int highPosition, int target) {
    int midPosition;

    // Check if the lower index is greater than the higher index, indicating an empty search range.
    if (lowPosition > highPosition) {
        // If the low index is greater than the high index, the target element is not found.
        return -1;
    } else {
        // Calculate the middle index of the current search range.
        midPosition = (lowPosition + highPosition) / 2;

        // If the element at the middle index is less than the target, search in the right half of the array.
        if (intArray[midPosition] < target) {
            // Recursively call the function with an updated search range (right half).
            return recBinarySearch(intArray, midPosition + 1, highPosition, target);
        }

        // If the element at the middle index is greater than the target, search in the left half of the array.
        if (intArray[midPosition] > target) {
            // Recursively call the function with an updated search range (left half).
            return recBinarySearch(intArray, lowPosition, midPosition - 1, target);
        }

        // If the element at the middle index is equal to the target, we found the target element.
        // Return the index where the target element is found (midPosition).
        return midPosition;
    }
}

```

# tracing through a runthrough

int Array: |0|2|4|6|8|10|12|14|16|18|20|22|
Target: 12

recBinarySearch(intArray, 0, 10, 12);

Call 1:
Midpoint calculated as (0 + 10) / 2 = 5
The target value 12 is greater than the midpoint value at index 5 (10).
So, we narrow our search to values greater than the midpoint.

Call 2: recBinarySearch(intArray, mid1, high, target)
Midpoint 1 calculated as (mid + high) / 2 = 7

The midpoint value at index 7 is 14, which is greater than 12, so the next call is between low and mid.

Call 3: Another recursive call finds the midpoint value at index 6, as it's between low and mid, which is our target number.

If the target does not exist, we would print -1 as the value is not found.

# popcorn hack

edit the following code so that running the cell will sort through an array of your creation.


```java
public class BinarySearchExample {

    public static int recBinarySearch(int[] intArray, int lowPosition, int highPosition, int target) {
        int midPosition;

        if (lowPosition > highPosition) {
            return -1;
        } else {
            midPosition = (lowPosition + highPosition) / 2;

            if (intArray[midPosition] < target) {
                return recBinarySearch(intArray, midPosition + 1, highPosition, target);
            }

            if (intArray[midPosition] > target) {
                return recBinarySearch(intArray, lowPosition, midPosition - 1, target);
            }

            return midPosition;
        }
    }

    public static void main(String[] args) {
        // Create an array of integers (you can replace this with your own array).
        int[] intArray = { 1, 2, 9, 1, 5, 6, 8, 3, 7, 4 };

        // Define the target element you want to search for.
        int target = 5;

        // Sort the array in ascending order (if needed).
        // You can use a sorting algorithm to sort the array, or use Arrays.sort(intArray).

        // Perform a binary search on the sorted array.
        int result = recBinarySearch(intArray, 0, intArray.length - 1, target);

        if (result != -1) {
            System.out.println("Element " + target + " found at index " + result);
        } else {
            System.out.println("Element " + target + " not found in the array.");
        }
    }
}
BinarySearchExample.main(null);
```

    Element 5 found at index 4


# takeaways

Data must be in sorted order for binary search to work.

The binary search algorithm starts in the middle of the sorted array or arraylist and and eliminates half of the array or arraylist in each iteration until
the desired value is found or all elements have been eliminated

Binary search can be more effective than linear search

binary search algorithm can be written linearly or recursively

# topic 2 recursive sorting and searching

APPLY RECURSIVE LOGIC TO sort arrays for elements



```java
mergeSort(myList) {
    mergeSort(left)
    mergeSort(right)
}

// left, right merge
```

# example trace (look at the whiteboard, I will draw it out maybe)

Original List:
|5|25|8|-9|14|0|-2|2|

The first recursive call begins by splitting the list into the left and right sides: (5, 25, 8, -9).

Another recursive call is made on the left side, which further splits into (5, 25).

The left and right sides are split into individual elements, and the two elements (5 and 25) are merged, resulting in (5, 25).

The current list becomes (5, 25, -9, 8).

The current list is sorted, resulting in (-9, 5, 8, 25).

Current List:

|-9|5|8|25|14|0|-2|2|

The final left side is sorted, and a recursive call is made for the right side: (14, 0, -2, 2).

The right side is further split into (14, 0).

These two elements (14 and 0) are merged into (0, 14).

The remaining elements (-2 and 2) are merged into (-2, 2).

The right side is now (0, 14, -2, 2).

Current List:
|-9|5|8|25|0|14|-2|2|

The left and right sides are finally merged together:

Left: -9, 5, 8, 25

Right: 0, 14, -2, 2

The two merged sides are sorted, resulting in the final sorted list:
|-9|0|2|5|8|14|25|

The merge sort process is complete, and the original list is sorted:
Sorted List: |-9|0|2|5|8|14|25|




```java
Merge Method ---The **merge** method 
```


```java
// work from left to right in each virtual myArray
// compare elements to return them to the original array in order
int[] myArray = {3, 4, 6, 8, 1, 2, 5, 7}
// think of the temporary array as two virtual arrays
int[] myArray1 = {3, 4, 6, 8};
int[] myArray2 = {1, 2, 5, 7};
// have to throw an exception for the last one to end the code
// if any elements remain in the lower half of the temporary array, return them to the original array
```

1. 1 < 3, 1 goes to the first place
2. 2 < 3, 2 goes to the second place
3. 3 < 5, 3 goes to the third place

<p>4. 4 < 5, 4 goes to the fourth place</p> 
<p>5. 5 < 6, 5 goes to the fifth place</p>      
<p>6. 6 < 7, 6 goes to the sixth place</p> 
<p>7. 7 < 8, 7 goes tot the seventh place</p> 
<p>8. 8 goes to the last place</p>



```java

public class sort {
    public static int[] output;   
    public static void __mergeSort(int[] myArray, int left, int right) {
      if(left < right) {
        int i;
        int center = (left + right) / 2;
        int p = 0;
        int j = 0;
        int k = left;
  
        __mergeSort(myArray, left, center);    // sort front part     
        __mergeSort(myArray, center + 1, right);     // sort back part
  
        for(i = left; i <= center; i++) {
          output[p++] = myArray[i];
  
        }
        // comparing the elements and put in myArray
        while (i <= right && j < p) {
          if (output[j] <= myArray[i]) {
              myArray[k] = output[j]; 
              j++; 
          } else {
              myArray[k] = myArray[i]; 
              i++; 
          }
          k++; 
        }
        // put the remain in myArray
        while (j < p) {
            myArray[k++] = output[j++];
        }
      }
    }
  
    public static void mergeSort(int[] myArray) {
  
      output = new int[myArray.length];          
  
      __mergeSort(myArray, 0, myArray.length - 1);   
      output = null;               
    }
    public static void printArray(int[] array) {
        for(int data: array) {
            System.out.print(data + " ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        int[] array = {3, 4, 6, 8, 1, 2, 5, 9};
        System.out.println("before");
        printArray(array);
        mergeSort(array);
        System.out.println("after");
        printArray(array);
    }
  }
  sort.main(null);

```

# TAKEAWAYS

Mergesort is a recursive sorting algorithm that can be used to sort elements in an array or ArrayList

for the AP test, you must remember how it works. remember the left-right merge rule.

# hack

Question: what are the usage cases of merge sort? what about usage cases of recursive binary sort? try and come up with a real life scenario for each usage case.

Merge Sort is great for sorting large amounts of data, like financial transactions or library catalogs. It helps keep everything in order efficiently. Recursive Binary Search, on the other hand, is like a super-fast detective for finding things in a sorted list. It's good for quickly locating a name in a phone directory, speeding up database searches, or pinpointing data in scientific research.

# Recursion Visualized
- Finn Carpenter
- XCHART Library

## Important Note
- If you hit the X button to close the window it breaks the kernel
- Two Options
    - Have a bunch of those windows, when done the close
    - Keep refreshing kernel by switching to python and then back to java

## Basic X Chart Code



```java
%maven org.knowm.xchart:xchart:3.5.2

import org.knowm.xchart.*;

public class Example0 {
 
    public static void main(String[] args) throws Exception {
        
        // these vars hold your X and Y values
        double[] xData = new double[] { 0.0, 1.0, 2.0 };
        double[] yData = new double[] { 2.0, 1.0, 0.0 };
   
        // Create Chart
        XYChart chart = QuickChart.getChart("Sample Chart", "X", "Y", "y(x)", xData, yData);
        
        // Show it
        new SwingWrapper(chart).displayChart();
    }
  }

  Example0.main(null);
```

## X Chart Graphs with recursion
- What is the shape of the graph going to look like when the recursive function is done
- The equation would be **a parabola**


```java
private static void graph(double[] xData, double[] yData, int index, double x, int maxIndex, double stepSize) {
    if (index > maxIndex) {
        return;
    }

    xData[index] = x;
    yData[index] = x * x;

    graph(xData, yData, index + 1, x + stepSize, maxIndex, stepSize);
}
```


```java
%maven org.knowm.xchart:xchart:3.5.2


import org.knowm.xchart.*;

public class recursiveGraph {

    public static void main(String[] args) throws Exception {
        int numPoints = 100;
        double[] xData = new double[numPoints];
        double[] yData = new double[numPoints];

        plotParabola(xData, yData, 0, -5.0, numPoints - 1, 0.1);

        // Create Chart
        XYChart chart = QuickChart.getChart("Parabola", "X", "Y", "y(x)", xData, yData);

        // Show it
        new SwingWrapper(chart).displayChart();
    }

    private static void plotParabola(double[] xData, double[] yData, int index, double x, int maxIndex, double stepSize) {
        if (index > maxIndex) {
            return;
        }

        xData[index] = x;
        yData[index] = x * x;

        plotParabola(xData, yData, index + 1, x + stepSize, maxIndex, stepSize);
    }
}


recursiveGraph.main(null);
```

## XChart 2
- What is the shape of the graph going to look like when the recursive function is done
- The equation would be **an exponential function**


```java
private static void plot(double[] xData, double[] yData, int index, double x, int maxIndex, double stepSize, double base) {
    if (index > maxIndex) {
        return;
    }

    xData[index] = x;
    yData[index] = Math.pow(base, x);

    plot(xData, yData, index + 1, x + stepSize, maxIndex, stepSize, base);
}
```


```java
%maven org.knowm.xchart:xchart:3.5.2

import org.knowm.xchart.*;

public class recursiveGraph2 {

    public static void main(String[] args) throws Exception {
        int numPoints = 100;
        double[] xData = new double[numPoints];
        double[] yData = new double[numPoints];

        plotExponential(xData, yData, 0, -5.0, numPoints - 1, 0.1, 2.0); // You can adjust the base as needed (e.g., 2.0 for 2^x)

        // Create Chart
        XYChart chart = QuickChart.getChart("Mati Yapping Graph", "Seconds of Mati Yapping", "My Anger", "y(x)", xData, yData);

        // Show it
        new SwingWrapper(chart).displayChart();
    }

    private static void plotExponential(double[] xData, double[] yData, int index, double x, int maxIndex, double stepSize, double base) {
        if (index > maxIndex) {
            return;
        }

        xData[index] = x;
        yData[index] = Math.pow(base, x);

        plotExponential(xData, yData, index + 1, x + stepSize, maxIndex, stepSize, base);
    }
}

recursiveGraph2.main(null);
```

# Hacks
- Finish all popcorn hacks for the lesson
- Follow the directions bellow for the XChart Hacks

# Example of Cool Function for the Hacks
- If you are having trouble with thinking of a cool equation to put into a recursion form, follow these tips
    - Look up the shape/symbol you would like to put into the graph
    - Try to split the equation up into what math methods you will need
    - Ask the friend who know most about coding (wink wink)


- Make sure to take a screenshot of the graph and display it next to it's respective code block


```java
%maven org.knowm.xchart:xchart:3.5.2

import org.knowm.xchart.*;
import org.knowm.xchart.style.markers.SeriesMarkers;
import java.util.ArrayList;
import java.util.List;

public class TrainShapeGraph {

    public static void main(String[] args) {
        // Define the coordinates for the train
        List<Double> xData = new ArrayList<>();
        List<Double> yData = new ArrayList<>();

        // Engine
        addRectangle(xData, yData, 0, 0, 3, 2);

        // Stack
        addRectangle(xData, yData, 2.5, 2, 0.5, 1);

        // Connect cars
        addLine(xData, yData, 3, 1, 4, 1);

        // First car
        addRectangle(xData, yData, 4, 0, 3, 2);

        // Wheels
        addCircle(xData, yData, 1, 0.5, 0.5);
        addCircle(xData, yData, 2, 0.5, 0.5);
        addCircle(xData, yData, 5, 0.5, 0.5);
        addCircle(xData, yData, 6, 0.5, 0.5);

        // Convert Lists to arrays for the chart
        double[] xArray = xData.stream().mapToDouble(d -> d).toArray();
        double[] yArray = yData.stream().mapToDouble(d -> d).toArray();

        // Create Chart
        XYChart chart = new XYChartBuilder().width(800).height(600).title("Train Shape").xAxisTitle("X").yAxisTitle("Y").build();

        // Customize Chart
        chart.getStyler().setDefaultSeriesRenderStyle(XYSeries.XYSeriesRenderStyle.Line);
        chart.getStyler().setChartTitleVisible(true);
        chart.getStyler().setMarkerSize(0);

        // Add series
        XYSeries series = chart.addSeries("Train", xArray, yArray);
        series.setMarker(SeriesMarkers.NONE);

        // Show it
        new SwingWrapper(chart).displayChart();
    }

    private static void addRectangle(List<Double> xData, List<Double> yData, double x, double y, double width, double height) {
        // Top left corner
        xData.add(x);
        yData.add(y + height);

        // Top right corner
        xData.add(x + width);
        yData.add(y + height);

        // Bottom right corner
        xData.add(x + width);
        yData.add(y);

        // Bottom left corner
        xData.add(x);
        yData.add(y);

        // Close the rectangle
        xData.add(x);
        yData.add(y + height);
    }

    private static void addLine(List<Double> xData, List<Double> yData, double x1, double y1, double x2, double y2) {
        xData.add(x1);
        yData.add(y1);
        xData.add(x2);
        yData.add(y2);
    }

    private static void addCircle(List<Double> xData, List<Double> yData, double centerX, double centerY, double radius) {
        int numPoints = 20; // The number of points to draw the circle
        for (int i = 0; i <= numPoints; i++) {
            double angle = 2 * Math.PI * i / numPoints;
            xData.add(centerX + radius * Math.cos(angle));
            yData.add(centerY + radius * Math.sin(angle));
        }
    }
}

TrainShapeGraph.main(null);

```


    The Kernel crashed while executing code in the the current cell or a previous cell. Please review the code in the cell(s) to identify a possible cause of the failure. Click <a href='https://aka.ms/vscodeJupyterKernelCrash'>here</a> for more info. View Jupyter <a href='command:jupyter.viewOutput'>log</a> for further details.


![Train](/Rackets-Blog/images/train-shape.png)
