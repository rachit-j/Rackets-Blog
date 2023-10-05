---

---

### Reverse an Array


```java
public static void reverseArray() {
    System.out.println("Array");
    int[] arr = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
    for(int length = 0; length < arr.length; length++)
    {
        System.out.print(arr[length]+ " ");
    }
    for(int length = 0; length <= arr.length -1; length++)
    {
        System.out.print(arr[9 - (length)] + " ");
    }
}

reverseArray()
```

    Array
    10 8 5 7 6 5 4 3 2 1 1 2 3 4 5 6 7 5 8 10 

### Initialize Random Letters in ArrayList


```java
import java.util.ArrayList;

public static String randomLetters(int max, int min) {
    int randomNum = (int) (Math.random() * (max - min + 1) + min);
    String[] strArray = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"};
    // System.out.print(strArray[randomNum]);
    return strArray[randomNum];
}

ArrayList<String> letters = new ArrayList<>();

// myArray[0] = randomLetters(0, 32);
// myArray[1] = randomLetters(0, 32);
// myArray[2] = randomLetters(0, 32);
// myArray[3] = randomLetters(0, 32);
// myArray[4] = randomLetters(0, 32);
for(int length = 0; length <= 4; length++) {
    letters.add(randomLetters(0,32));
}

System.out.println(letters);
```

    [p, f, i, n, c]

