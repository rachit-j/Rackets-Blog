---
title: Algorythmic
description: Algorythmic notebook
toc: True
layout: post
type: hacks
comments: True
---

## Class

```Java
import java.util.ArrayList;
import java.util.Collections;

public class Bachelor implements Comparable<Bachelor> {
    private String name;
    private int rating;

    // Constructor
    public Bachelor(String name, int rating) {
        this.name = name;
        this.rating = rating;
    }

    // Getter methods
    public String getName() {
        return name;
    }

    public int getRating() {
        return rating;
    }

    @Override
    public int compareTo(Bachelor other) {
        return Integer.compare(this.rating, other.rating);
    }

    public static ArrayList<Bachelor> createList() {
        Bachelor b1 = new Bachelor("Theo", 1);
        Bachelor b2 = new Bachelor("Jake", 2);
        Bachelor b3 = new Bachelor("Liam", 3);
        Bachelor b4 = new Bachelor("Noah", 4);
        Bachelor b5 = new Bachelor("James", 5);
        Bachelor b6 = new Bachelor("William", 6);
        Bachelor b7 = new Bachelor("Oliver", 7);
        Bachelor b8 = new Bachelor("Benjamin", 8);
        Bachelor b9 = new Bachelor("Lucas", 9);
        Bachelor b10 = new Bachelor("Henry", 10);
        Bachelor b11 = new Bachelor("Alexander", 11);
        Bachelor b12 = new Bachelor("Michael", 12);
        Bachelor b13 = new Bachelor("Daniel", 13);

        // Creating a list of Bachelor objects
        ArrayList<Bachelor> bachelorList = new ArrayList<>();
        bachelorList.add(b1);
        bachelorList.add(b2);
        bachelorList.add(b3);
        bachelorList.add(b4);
        bachelorList.add(b5);
        bachelorList.add(b6);
        bachelorList.add(b7);
        bachelorList.add(b8);
        bachelorList.add(b9);
        bachelorList.add(b10);
        bachelorList.add(b11);
        bachelorList.add(b12);
        bachelorList.add(b13);
        
        Collections.shuffle(bachelorList);

        return bachelorList;
    }

    public static void main(String[] args) {
        // Creating objects of Bachelor
        ArrayList<Bachelor> bachelorList = createList();

        // Print original list
        System.out.println("Original List:");
        for (Bachelor bachelor : bachelorList) {
            System.out.println("Name: " + bachelor.getName() + ", Rating: " + bachelor.getRating());
        }
    }
}
Bachelor.main(null);
```

    Original List:
    Name: Alexander, Rating: 11
    Name: Henry, Rating: 10
    Name: Theo, Rating: 1
    Name: Noah, Rating: 4
    Name: Daniel, Rating: 13
    Name: Lucas, Rating: 9
    Name: Michael, Rating: 12
    Name: Liam, Rating: 3
    Name: Jake, Rating: 2
    Name: Oliver, Rating: 7
    Name: James, Rating: 5
    Name: Benjamin, Rating: 8
    Name: William, Rating: 6


## Bubble Sort (our sort)


```Java
import java.util.ArrayList;
import java.util.Collections;

public class BachelorBubbleSort {
    public static void bubbleSort(ArrayList<Bachelor> bachelors) {
        int n = bachelors.size();
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (bachelors.get(j).compareTo(bachelors.get(j + 1)) > 0) {
                    // Swap bachelors
                    Collections.swap(bachelors, j, j + 1);
                }
            }
        }
    }

    public static void main(String[] args) {
        // Create a list of Bachelor objects
        ArrayList<Bachelor> bachelorList = Bachelor.createList();

        // Print original list
        System.out.println("Original List:");
        for (Bachelor bachelor : bachelorList) {
            System.out.println("Name: " + bachelor.getName() + ", Rating: " + bachelor.getRating());
        }

        // Sort the list using Bubble Sort
        bubbleSort(bachelorList);

        // Print sorted list
        System.out.println("\nSorted List:");
        for (Bachelor bachelor : bachelorList) {
            System.out.println("Name: " + bachelor.getName() + ", Rating: " + bachelor.getRating());
        }
    }
}
BachelorBubbleSort.main(null);
```

    Original List:
    Name: Alexander, Rating: 11
    Name: Lucas, Rating: 9
    Name: William, Rating: 6
    Name: Daniel, Rating: 13
    Name: Noah, Rating: 4
    Name: Theo, Rating: 1
    Name: Oliver, Rating: 7
    Name: Benjamin, Rating: 8
    Name: Jake, Rating: 2
    Name: James, Rating: 5
    Name: Michael, Rating: 12
    Name: Henry, Rating: 10
    Name: Liam, Rating: 3
    
    Sorted List:
    Name: Theo, Rating: 1
    Name: Jake, Rating: 2
    Name: Liam, Rating: 3
    Name: Noah, Rating: 4
    Name: James, Rating: 5
    Name: William, Rating: 6
    Name: Oliver, Rating: 7
    Name: Benjamin, Rating: 8
    Name: Lucas, Rating: 9
    Name: Henry, Rating: 10
    Name: Alexander, Rating: 11
    Name: Michael, Rating: 12
    Name: Daniel, Rating: 13


## Insertion Sort


```Java
import java.util.ArrayList;

public class BachelorInsertionSort {
    public static void insertionSort(ArrayList<Bachelor> bachelors) {
        int n = bachelors.size();
        for (int i = 1; i < n; i++) {
            Bachelor key = bachelors.get(i);
            int j = i - 1;
            while (j >= 0 && bachelors.get(j).compareTo(key) > 0) {
                bachelors.set(j + 1, bachelors.get(j));
                j = j - 1;
            }
            bachelors.set(j + 1, key);
        }
    }

    public static void main(String[] args) {
        // Create a list of Bachelor objects
        ArrayList<Bachelor> bachelorList = Bachelor.createList();

        // Print original list
        System.out.println("Original List:");
        for (Bachelor bachelor : bachelorList) {
            System.out.println("Name: " + bachelor.getName() + ", Rating: " + bachelor.getRating());
        }

        // Sort the list using Insertion Sort
        insertionSort(bachelorList);

        // Print sorted list
        System.out.println("\nSorted List:");
        for (Bachelor bachelor : bachelorList) {
            System.out.println("Name: " + bachelor.getName() + ", Rating: " + bachelor.getRating());
        }
    }
}
BachelorInsertionSort.main(null);
```

    Original List:
    Name: Jake, Rating: 2
    Name: Daniel, Rating: 13
    Name: Noah, Rating: 4
    Name: Lucas, Rating: 9
    Name: Benjamin, Rating: 8
    Name: James, Rating: 5
    Name: Oliver, Rating: 7
    Name: Alexander, Rating: 11
    Name: Michael, Rating: 12
    Name: Theo, Rating: 1
    Name: Henry, Rating: 10
    Name: Liam, Rating: 3
    Name: William, Rating: 6
    
    Sorted List:
    Name: Theo, Rating: 1
    Name: Jake, Rating: 2
    Name: Liam, Rating: 3
    Name: Noah, Rating: 4
    Name: James, Rating: 5
    Name: William, Rating: 6
    Name: Oliver, Rating: 7
    Name: Benjamin, Rating: 8
    Name: Lucas, Rating: 9
    Name: Henry, Rating: 10
    Name: Alexander, Rating: 11
    Name: Michael, Rating: 12
    Name: Daniel, Rating: 13


## Selection Sort


```Java
import java.util.ArrayList;

public class BachelorSelectionSort {
    public static void selectionSort(ArrayList<Bachelor> bachelors) {
        int n = bachelors.size();
        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (bachelors.get(j).compareTo(bachelors.get(minIndex)) < 0) {
                    minIndex = j;
                }
            }
            // Swap the minimum element with the first element of the unsorted subarray
            Bachelor temp = bachelors.get(minIndex);
            bachelors.set(minIndex, bachelors.get(i));
            bachelors.set(i, temp);
        }
    }

    public static void main(String[] args) {
        // Create a list of Bachelor objects
        ArrayList<Bachelor> bachelorList = Bachelor.createList();

        // Print original list
        System.out.println("Original List:");
        for (Bachelor bachelor : bachelorList) {
            System.out.println("Name: " + bachelor.getName() + ", Rating: " + bachelor.getRating());
        }

        // Sort the list using Selection Sort
        selectionSort(bachelorList);

        // Print sorted list
        System.out.println("\nSorted List:");
        for (Bachelor bachelor : bachelorList) {
            System.out.println("Name: " + bachelor.getName() + ", Rating: " + bachelor.getRating());
        }
    }
}
BachelorSelectionSort.main(null);
```

    Original List:
    Name: Alexander, Rating: 11
    Name: Theo, Rating: 1
    Name: Michael, Rating: 12
    Name: Noah, Rating: 4
    Name: William, Rating: 6
    Name: Benjamin, Rating: 8
    Name: Lucas, Rating: 9
    Name: Jake, Rating: 2
    Name: James, Rating: 5
    Name: Henry, Rating: 10
    Name: Oliver, Rating: 7
    Name: Liam, Rating: 3
    Name: Daniel, Rating: 13
    
    Sorted List:
    Name: Theo, Rating: 1
    Name: Jake, Rating: 2
    Name: Liam, Rating: 3
    Name: Noah, Rating: 4
    Name: James, Rating: 5
    Name: William, Rating: 6
    Name: Oliver, Rating: 7
    Name: Benjamin, Rating: 8
    Name: Lucas, Rating: 9
    Name: Henry, Rating: 10
    Name: Alexander, Rating: 11
    Name: Michael, Rating: 12
    Name: Daniel, Rating: 13


## Merge Sort


```Java
import java.util.ArrayList;

public class BachelorMergeSort {

    public static void mergeSort(ArrayList<Bachelor> bachelors) {
        if (bachelors.size() > 1) {
            int mid = bachelors.size() / 2;

            // Split the list into two halves
            ArrayList<Bachelor> leftHalf = new ArrayList<>(bachelors.subList(0, mid));
            ArrayList<Bachelor> rightHalf = new ArrayList<>(bachelors.subList(mid, bachelors.size()));

            // Recursively sort each half
            mergeSort(leftHalf);
            mergeSort(rightHalf);

            // Merge the sorted halves
            int i = 0, j = 0, k = 0;
            while (i < leftHalf.size() && j < rightHalf.size()) {
                if (leftHalf.get(i).compareTo(rightHalf.get(j)) <= 0) {
                    bachelors.set(k++, leftHalf.get(i++));
                } else {
                    bachelors.set(k++, rightHalf.get(j++));
                }
            }

            // Copy remaining elements from left half
            while (i < leftHalf.size()) {
                bachelors.set(k++, leftHalf.get(i++));
            }

            // Copy remaining elements from right half
            while (j < rightHalf.size()) {
                bachelors.set(k++, rightHalf.get(j++));
            }
        }
    }

    public static void main(String[] args) {
        ArrayList<Bachelor> bachelorList = Bachelor.createList();
        
        // Printing the original list of bachelors
        System.out.println("Original List:");
        for (Bachelor bachelor : bachelorList) {
            System.out.println(bachelor.getName() + " (" + bachelor.getRating() + ")");
        }

        // Applying merge sort
        mergeSort(bachelorList);

        // Printing the sorted list of bachelors
        System.out.println("\nSorted List:");
        for (Bachelor bachelor : bachelorList) {
            System.out.println(bachelor.getName() + " (" + bachelor.getRating() + ")");
        }
    }
}

BachelorMergeSort.main(null);
```

    Original List:
    Lucas (9)
    Noah (4)
    Theo (1)
    William (6)
    Alexander (11)
    Henry (10)
    Liam (3)
    James (5)
    Michael (12)
    Jake (2)
    Benjamin (8)
    Oliver (7)
    Daniel (13)
    
    Sorted List:
    Theo (1)
    Jake (2)
    Liam (3)
    Noah (4)
    James (5)
    William (6)
    Oliver (7)
    Benjamin (8)
    Lucas (9)
    Henry (10)
    Alexander (11)
    Michael (12)
    Daniel (13)


## Deep dive into Our Sort (Bubble Sort)


```Java
import java.util.ArrayList;
import java.util.Collections;

public class DeepBachelorBubbleSort {
    public static void bubbleSort(ArrayList<Bachelor> bachelors) {
        int n = bachelors.size();
        for (int i = 0; i < n - 1; i++) {
            System.out.println("Pass " + (i + 1) + ":");
            for (int j = 0; j < n - i - 1; j++) {
                System.out.println("\tComparing " + bachelors.get(j).getName() + " (" + bachelors.get(j).getRating() + 
                                   ") with " + bachelors.get(j + 1).getName() + " (" + bachelors.get(j + 1).getRating() + ")");
                if (bachelors.get(j).compareTo(bachelors.get(j + 1)) > 0) {
                    System.out.println("\t\tSwapping " + bachelors.get(j).getName() + " and " + bachelors.get(j + 1).getName());
                    Collections.swap(bachelors, j, j + 1);
                }
            }
            System.out.println("\tList after pass " + (i + 1) + ":");
            for (Bachelor bachelor : bachelors) {
                System.out.println("\t\t" + bachelor.getName() + " (" + bachelor.getRating() + ")");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        // Create a list of Bachelor objects
        ArrayList<Bachelor> bachelorList = Bachelor.createList();

        // Print original list
        System.out.println("Original List:");
        for (Bachelor bachelor : bachelorList) {
            System.out.println(bachelor.getName() + " (" + bachelor.getRating() + ")");
        }

        // Sort the list using Bubble Sort
        bubbleSort(bachelorList);

        // Print sorted list
        System.out.println("\nSorted List:");
        for (Bachelor bachelor : bachelorList) {
            System.out.println(bachelor.getName() + " (" + bachelor.getRating() + ")");
        }
    }
}
DeepBachelorBubbleSort.main(null);
```

    Original List:
    Benjamin (8)
    Lucas (9)
    Alexander (11)
    Liam (3)
    Theo (1)
    Daniel (13)
    Michael (12)
    Henry (10)
    William (6)
    Jake (2)
    James (5)
    Noah (4)
    Oliver (7)
    Pass 1:
    	Comparing Benjamin (8) with Lucas (9)
    	Comparing Lucas (9) with Alexander (11)
    	Comparing Alexander (11) with Liam (3)
    		Swapping Alexander and Liam
    	Comparing Alexander (11) with Theo (1)
    		Swapping Alexander and Theo
    	Comparing Alexander (11) with Daniel (13)
    	Comparing Daniel (13) with Michael (12)
    		Swapping Daniel and Michael
    	Comparing Daniel (13) with Henry (10)
    		Swapping Daniel and Henry
    	Comparing Daniel (13) with William (6)
    		Swapping Daniel and William
    	Comparing Daniel (13) with Jake (2)
    		Swapping Daniel and Jake
    	Comparing Daniel (13) with James (5)
    		Swapping Daniel and James
    	Comparing Daniel (13) with Noah (4)
    		Swapping Daniel and Noah
    	Comparing Daniel (13) with Oliver (7)
    		Swapping Daniel and Oliver
    	List after pass 1:
    		Benjamin (8)
    		Lucas (9)
    		Liam (3)
    		Theo (1)
    		Alexander (11)
    		Michael (12)
    		Henry (10)
    		William (6)
    		Jake (2)
    		James (5)
    		Noah (4)
    		Oliver (7)
    		Daniel (13)
    
    Pass 2:
    	Comparing Benjamin (8) with Lucas (9)
    	Comparing Lucas (9) with Liam (3)
    		Swapping Lucas and Liam
    	Comparing Lucas (9) with Theo (1)
    		Swapping Lucas and Theo
    	Comparing Lucas (9) with Alexander (11)
    	Comparing Alexander (11) with Michael (12)
    	Comparing Michael (12) with Henry (10)
    		Swapping Michael and Henry
    	Comparing Michael (12) with William (6)
    		Swapping Michael and William
    	Comparing Michael (12) with Jake (2)
    		Swapping Michael and Jake
    	Comparing Michael (12) with James (5)
    		Swapping Michael and James
    	Comparing Michael (12) with Noah (4)
    		Swapping Michael and Noah
    	Comparing Michael (12) with Oliver (7)
    		Swapping Michael and Oliver
    	List after pass 2:
    		Benjamin (8)
    		Liam (3)
    		Theo (1)
    		Lucas (9)
    		Alexander (11)
    		Henry (10)
    		William (6)
    		Jake (2)
    		James (5)
    		Noah (4)
    		Oliver (7)
    		Michael (12)
    		Daniel (13)
    
    Pass 3:
    	Comparing Benjamin (8) with Liam (3)
    		Swapping Benjamin and Liam
    	Comparing Benjamin (8) with Theo (1)
    		Swapping Benjamin and Theo
    	Comparing Benjamin (8) with Lucas (9)
    	Comparing Lucas (9) with Alexander (11)
    	Comparing Alexander (11) with Henry (10)
    		Swapping Alexander and Henry
    	Comparing Alexander (11) with William (6)
    		Swapping Alexander and William
    	Comparing Alexander (11) with Jake (2)
    		Swapping Alexander and Jake
    	Comparing Alexander (11) with James (5)
    		Swapping Alexander and James
    	Comparing Alexander (11) with Noah (4)
    		Swapping Alexander and Noah
    	Comparing Alexander (11) with Oliver (7)
    		Swapping Alexander and Oliver
    	List after pass 3:
    		Liam (3)
    		Theo (1)
    		Benjamin (8)
    		Lucas (9)
    		Henry (10)
    		William (6)
    		Jake (2)
    		James (5)
    		Noah (4)
    		Oliver (7)
    		Alexander (11)
    		Michael (12)
    		Daniel (13)
    
    Pass 4:
    	Comparing Liam (3) with Theo (1)
    		Swapping Liam and Theo
    	Comparing Liam (3) with Benjamin (8)
    	Comparing Benjamin (8) with Lucas (9)
    	Comparing Lucas (9) with Henry (10)
    	Comparing Henry (10) with William (6)
    		Swapping Henry and William
    	Comparing Henry (10) with Jake (2)
    		Swapping Henry and Jake
    	Comparing Henry (10) with James (5)
    		Swapping Henry and James
    	Comparing Henry (10) with Noah (4)
    		Swapping Henry and Noah
    	Comparing Henry (10) with Oliver (7)
    		Swapping Henry and Oliver
    	List after pass 4:
    		Theo (1)
    		Liam (3)
    		Benjamin (8)
    		Lucas (9)
    		William (6)
    		Jake (2)
    		James (5)
    		Noah (4)
    		Oliver (7)
    		Henry (10)
    		Alexander (11)
    		Michael (12)
    		Daniel (13)
    
    Pass 5:
    	Comparing Theo (1) with Liam (3)
    	Comparing Liam (3) with Benjamin (8)
    	Comparing Benjamin (8) with Lucas (9)
    	Comparing Lucas (9) with William (6)
    		Swapping Lucas and William
    	Comparing Lucas (9) with Jake (2)
    		Swapping Lucas and Jake
    	Comparing Lucas (9) with James (5)
    		Swapping Lucas and James
    	Comparing Lucas (9) with Noah (4)
    		Swapping Lucas and Noah
    	Comparing Lucas (9) with Oliver (7)
    		Swapping Lucas and Oliver
    	List after pass 5:
    		Theo (1)
    		Liam (3)
    		Benjamin (8)
    		William (6)
    		Jake (2)
    		James (5)
    		Noah (4)
    		Oliver (7)
    		Lucas (9)
    		Henry (10)
    		Alexander (11)
    		Michael (12)
    		Daniel (13)
    
    Pass 6:
    	Comparing Theo (1) with Liam (3)
    	Comparing Liam (3) with Benjamin (8)
    	Comparing Benjamin (8) with William (6)
    		Swapping Benjamin and William
    	Comparing Benjamin (8) with Jake (2)
    		Swapping Benjamin and Jake
    	Comparing Benjamin (8) with James (5)
    		Swapping Benjamin and James
    	Comparing Benjamin (8) with Noah (4)
    		Swapping Benjamin and Noah
    	Comparing Benjamin (8) with Oliver (7)
    		Swapping Benjamin and Oliver
    	List after pass 6:
    		Theo (1)
    		Liam (3)
    		William (6)
    		Jake (2)
    		James (5)
    		Noah (4)
    		Oliver (7)
    		Benjamin (8)
    		Lucas (9)
    		Henry (10)
    		Alexander (11)
    		Michael (12)
    		Daniel (13)
    
    Pass 7:
    	Comparing Theo (1) with Liam (3)
    	Comparing Liam (3) with William (6)
    	Comparing William (6) with Jake (2)
    		Swapping William and Jake
    	Comparing William (6) with James (5)
    		Swapping William and James
    	Comparing William (6) with Noah (4)
    		Swapping William and Noah
    	Comparing William (6) with Oliver (7)
    	List after pass 7:
    		Theo (1)
    		Liam (3)
    		Jake (2)
    		James (5)
    		Noah (4)
    		William (6)
    		Oliver (7)
    		Benjamin (8)
    		Lucas (9)
    		Henry (10)
    		Alexander (11)
    		Michael (12)
    		Daniel (13)
    
    Pass 8:
    	Comparing Theo (1) with Liam (3)
    	Comparing Liam (3) with Jake (2)
    		Swapping Liam and Jake
    	Comparing Liam (3) with James (5)
    	Comparing James (5) with Noah (4)
    		Swapping James and Noah
    	Comparing James (5) with William (6)
    	List after pass 8:
    		Theo (1)
    		Jake (2)
    		Liam (3)
    		Noah (4)
    		James (5)
    		William (6)
    		Oliver (7)
    		Benjamin (8)
    		Lucas (9)
    		Henry (10)
    		Alexander (11)
    		Michael (12)
    		Daniel (13)
    
    Pass 9:
    	Comparing Theo (1) with Jake (2)
    	Comparing Jake (2) with Liam (3)
    	Comparing Liam (3) with Noah (4)
    	Comparing Noah (4) with James (5)
    	List after pass 9:
    		Theo (1)
    		Jake (2)
    		Liam (3)
    		Noah (4)
    		James (5)
    		William (6)
    		Oliver (7)
    		Benjamin (8)
    		Lucas (9)
    		Henry (10)
    		Alexander (11)
    		Michael (12)
    		Daniel (13)
    
    Pass 10:
    	Comparing Theo (1) with Jake (2)
    	Comparing Jake (2) with Liam (3)
    	Comparing Liam (3) with Noah (4)
    	List after pass 10:
    		Theo (1)
    		Jake (2)
    		Liam (3)
    		Noah (4)
    		James (5)
    		William (6)
    		Oliver (7)
    		Benjamin (8)
    		Lucas (9)
    		Henry (10)
    		Alexander (11)
    		Michael (12)
    		Daniel (13)
    
    Pass 11:
    	Comparing Theo (1) with Jake (2)
    	Comparing Jake (2) with Liam (3)
    	List after pass 11:
    		Theo (1)
    		Jake (2)
    		Liam (3)
    		Noah (4)
    		James (5)
    		William (6)
    		Oliver (7)
    		Benjamin (8)
    		Lucas (9)
    		Henry (10)
    		Alexander (11)
    		Michael (12)
    		Daniel (13)
    
    Pass 12:
    	Comparing Theo (1) with Jake (2)
    	List after pass 12:
    		Theo (1)
    		Jake (2)
    		Liam (3)
    		Noah (4)
    		James (5)
    		William (6)
    		Oliver (7)
    		Benjamin (8)
    		Lucas (9)
    		Henry (10)
    		Alexander (11)
    		Michael (12)
    		Daniel (13)
    
    
    Sorted List:
    Theo (1)
    Jake (2)
    Liam (3)
    Noah (4)
    James (5)
    William (6)
    Oliver (7)
    Benjamin (8)
    Lucas (9)
    Henry (10)
    Alexander (11)
    Michael (12)
    Daniel (13)

