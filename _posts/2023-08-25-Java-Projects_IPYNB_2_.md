---
toc: True
comments: True
layout: post
title: Java Projects
description: The complete Hack of the section Linux Shell and Bash. This page is also saved in a jupyter notebook.
type: hacks
courses: {'csse': {'week': 1}, 'csp': {'week': 1, 'categories': ['4.A']}, 'csa': {'week': 0}, 'labnotebook': {'week': 1}}
categories: ['C1.4']
---

### Games
Here is some code for some console games in Java

#### Games
By modifying the logic of the games and splitting them into different classes, it is a lot easer to make edits to them and simplify them, as well as create a new game and simply add it to the menu. Take a look at the following games. 


```java
public class HigherOrLower { // Unit 5
    public static void main(String[] args) { // Unit 9
        System.out.println("Higher or Lower");
        System.out.println("You have three guesses to guess the number I am thinking of between 1-8.");
        System.out.println("If you guess the number correctly, you win!");
        Scanner scHL = new Scanner(System.in);
        int randomG = (int) (Math.random() * 8) + 1;
        int guess = scHL.nextInt(); // UNIT 1
        for(int i = 3; i > 0; i--){ //Unit 3
            if(guess == randomG){
                System.out.println("You win!");
                break;
            }
            else if(guess > randomG){
                System.out.println("The number is lower");
            }
            else if(guess < randomG){
                System.out.println("The number is higher");
            }
            guess = scHL.nextInt();
        }
        System.out.println("Game over.");
        scHL.close();

    }
}
```


```java
HigherOrLower.main(null) // Unit 4
```

    Higher or Lower
    You have three guesses to guess the number I am thinking of between 1-8.
    If you guess the number correctly, you win!
     5
    The number is higher
     7
    The number is higher
     8
    You win!
    Game over.



```java
import java.util.Scanner;
import java.lang.Math;

public class TheLegendOfZelda { // Unit 5
    
    public static void main(String[] args) { // Unit 9
        Scanner sc = new Scanner(System.in);  // using Java Scanner Object

        System.out.println("Your name is Link! You are on a quest to get the legendary Pizza");
        System.out.println("Right now, you are in Kakariko village. To get the Pizza, you have to travel to Hateno Village. However, there are many monsters in your way.");
        System.out.println("Suddenly, a giant pig attacks the village! What would you like to do?");
        System.out.println("1 - Break through to the path to Hateno");
        System.out.println("2 - Fight the pig (without your pizza)");
        System.out.println("3 - Run inside a house and hide like a coward");

        int choice = sc.nextInt(); // UNIT 1
        if(choice == 1){ //Unit 3
            System.out.println("As you try to break through to Hateno, the Giant Pig sees you and stomps on you. Enjoy being a pancake.");
        }
        else if(choice == 2) {
            System.out.println("As you go to draw your sword from its sheath, the pig eats you. Since you don't have your magical pizza, you cannot break out of the pig's stomach and die from the acid.");
        }
        else if(choice == 3) {
            System.out.println("Good job coward! The pig does not see you, and after killing all the inhabitants, goes away to feast on another village. Weakling.");
            System.out.println("You immediatley head towards Hateno, but you get stuck in a ditch. Do you 1) climb an old rope 2) dig a hole 3) Scream and pray to the gods for help");
            int choice2 = sc.nextInt();
            
            if(choice2 == 1){
                System.out.println("As you are reaching the top, the rope snaps and breaks. You fall to the ground, hitting your head and instantly dying. Stupid. Test the rope first.");
            }
            else if(choice2 == 2) {
                System.out.println("You successfuly dig a hole and find an underground stream. You hop into it and it carries you right under Hateno. When you get off the dock, there are two doors for you to pass through to get your legendary pizza, and a trapdoor to exit. Which do you choose? 1 - Door 1, 2 - Door 2, 3 - Trapdoor");
                int choice3 = sc.nextInt();
                if (choice3 == 1) {
                    System.out.println("Wrong door. You fall into a pit and get impaled by spikes. Whoops...");
                }
                else if (choice3 == 2){
                    System.out.println("Wrong door. You get eaten by a family of snakes. I don't think I'll be following");
                }
                else if (choice3 == 3){
                    System.out.println("After cowardly exiting, you head over to the pizza shop, where the owner cooks a new batch of Legendary Pizza. When the monster pig arrives, you easily defeat it after eating the pizza. Well done!");
                    int rand = (int) (Math.random() * 4);
                    String[] GoodJobs = {"Great", "Amazing", "Link is Full", "YOMP"}; // Unit 6/7/8
                    
                    if (rand == 1) {
                        System.out.println(GoodJobs[0]);
                    }
                    else if (rand == 2) {
                        System.out.println(GoodJobs[1]);
                    }
                    
                    if (rand == 3) {
                        System.out.println(GoodJobs[2]);
                    }
                    else if (rand == 4) {
                        System.out.println(GoodJobs[3]);
                    
                    }
                }
            }
            else if (choice2 == 3){
                System.out.println("The gods are pissed that you are too lazy to do anything by yourself, so they strike you down with lightning.");
            }
        }
        System.out.println("Game over!");
    }
}


TheLegendOfZelda.main(null); // Unit 4
```

    Your name is Link! You are on a quest to get the legendary Pizza
    Right now, you are in Kakariko village. To get the Pizza, you have to travel to Hateno Village. However, there are many monsters in your way.
    Suddenly, a giant pig attacks the village! What would you like to do?
    1 - Break through to the path to Hateno
    2 - Fight the pig (without your pizza)
    3 - Run inside a house and hide like a coward
     3
    Good job coward! The pig does not see you, and after killing all the inhabitants, goes away to feast on another village. Weakling.
    You immediatley head towards Hateno, but you get stuck in a ditch. Do you 1) climb an old rope 2) dig a hole 3) Scream and pray to the gods for help
     2
    You successfuly dig a hole and find an underground stream. You hop into it and it carries you right under Hateno. When you get off the dock, there are two doors for you to pass through to get your legendary pizza, and a trapdoor to exit. Which do you choose? 1 - Door 1, 2 - Door 2, 3 - Trapdoor
     3
    After cowardly exiting, you head over to the pizza shop, where the owner cooks a new batch of Legendary Pizza. When the monster pig arrives, you easily defeat it after eating the pizza. Well done!
    Link is Full
    Game over!



```java
public class RockPaperScissors{ // Unit 5
    public static void main(String[] args) { // Unit 9
            System.out.println("Rock Paper Scissors");
            System.out.println("Type r for rock, p for paper, or s for scissors");
            Scanner scRPS = new Scanner(System.in); // UNIT 1
            String userChoice = scRPS.nextLine().toLowerCase(); // UNIT 1
            Boolean quit = false; // Unit 3
            int random = (int) (Math.random() * 3); // UNIT 1
            while(quit == false){ //Unit 3
                if(userChoice.equals("r")){
                    if(random == 1){
                        System.out.println("You chose rock \nThe computer chose paper \nYou lose!");
                    }
                    else if(random == 2){
                        System.out.println("You chose rock \nThe computer chose scissors \nYou win!");
                    }
                    else{
                        System.out.println("You chose rock \nThe computer chose rock \nIt's a tie!");
                    }
                    quit = true; //Unit 3
                }
                else if(userChoice.equals("p")){
                    if(random == 1){
                        System.out.println("You chose paper \nThe computer chose paper \nIt's a tie!");
                    }
                    else if(random == 2){
                        System.out.println("You chose paper \nThe computer chose scissors \nYou lose!");
                    }
                    else{
                        System.out.println("You chose paper \nThe computer chose rock \nYou win!");
                    }
                    quit = true; //Unit 3
    
                }
                else if(userChoice.equals("s")){
                    if(random == 1){
                        System.out.println("You chose scissors \nThe computer chose paper \nYou win!");
                    }
                    else if(random == 2){
                        System.out.println("You chose scissors \nThe computer chose scissors \nIt's a tie!");
                    }
                    else{
                        System.out.println("You chose scissors \nThe computer chose rock \nYou lose!");
                    }
                    quit = true; //Unit 3
    
                }
                else{
                    System.out.println("Invalid input, try again");
                    userChoice = scRPS.nextLine();
                }            
            }
            scRPS.close();
        }
}
```


```java
RockPaperScissors.main(null)// Unit 4
```

    Rock Paper Scissors
    Type r for rock, p for paper, or s for scissors
     p
    You chose paper 
    The computer chose rock 
    You win!



```java
import java.util.Scanner;

public class ConsoleGame {
    public static final String DEFAULT = "\u001B[0m"; // UNIT 1
    public static final String ANSI_BLUE = "\u001B[34m"; // UNIT 1

    public ConsoleGame() { // Unit 10
        Scanner sc = new Scanner(System.in);

        this.menuString();
        try {
            int choice = sc.nextInt();
            System.out.print(ANSI_BLUE + choice + ": " + DEFAULT);
            if (!this.action(choice)) {
                new ConsoleGame(); // Recursively create a new instance of ConsoleGame to display the menu again.
            }
        } catch (Exception e) {
            sc.nextLine(); // error: clear buffer
            System.out.println(ANSI_BLUE + e + ": Not a number, try again." + DEFAULT);
            new ConsoleGame(); // Recursively create a new instance of ConsoleGame to display the menu again.
        }
        
        sc.close();
    }

    public void menuString() {
        String menuText = ANSI_BLUE 
            + "+------------------------------------+\n"
            + "| Sintendo Nitch - low quality, free |\n"
            + "+------------------------------------+\n"
            + "| 0 - Quit                           |\n"
            + "| 1 - The Legend of Zelda: Link the  |\n"
            + "|     shorty                         |\n"
            + "| 2 - Higher or Lower (improved)     |\n"
            + "| 3 - Rock Paper Scissors            |\n"
            + "+------------------------------------+\n" 
            + DEFAULT;
        System.out.println(menuText);
    }

    private boolean action(int selection) {
        boolean quit = false;
        switch (selection) {
            case 0:
                System.out.print(ANSI_BLUE + "Goodbye, World!" + DEFAULT); 
                quit = true; 
                break;
            case 1:
                tloz();
                break; 
            case 2:
                horl();
                break;
            case 3:
                rps();
                break;
            default:
                System.out.print(ANSI_BLUE + "Unexpected choice, try again." + DEFAULT);
        }
        System.out.println(DEFAULT);
        return quit;
    }

    public void horl() {
        HigherOrLower.main(null); // Unit 2/4
    }

    public void tloz() {
        TheLegendOfZelda.main(null); // Unit 2/4
    }

    // Assuming you have a rps() method or you can add it
    public void rps() {
        RockPaperScissors.main(null); // Unit 2/4
    }

    public static void main(String[] args) {
        new ConsoleGame(); 
    }

}

ConsoleGame.main(null); // Unit 2/4

```

    [34m+------------------------------------+
    | Sintendo Nitch - low quality, free |
    +------------------------------------+
    | 0 - Quit                           |
    | 1 - The Legend of Zelda: Link the  |
    |     shorty                         |
    | 2 - Higher or Lower (improved)     |
    | 3 - Rock Paper Scissors            |
    +------------------------------------+
    [0m
     1
    [34m1: [0mYour name is Link! You are on a quest to get the legendary Pizza
    Right now, you are in Kakariko village. To get the Pizza, you have to travel to Hateno Village. However, there are many monsters in your way.
    Suddenly, a giant pig attacks the village! What would you like to do?
    1 - Break through to the path to Hateno
    2 - Fight the pig (without your pizza)
    3 - Run inside a house and hide like a coward
     3
    Good job coward! The pig does not see you, and after killing all the inhabitants, goes away to feast on another village. Weakling.
    You immediatley head towards Hateno, but you get stuck in a ditch. Do you 1) climb an old rope 2) dig a hole 3) Scream and pray to the gods for help
     2
    You successfuly dig a hole and find an underground stream. You hop into it and it carries you right under Hateno. When you get off the dock, there are two doors for you to pass through to get your legendary pizza, and a trapdoor to exit. Which do you choose? 1 - Door 1, 2 - Door 2, 3 - Trapdoor
     3
    After cowardly exiting, you head over to the pizza shop, where the owner cooks a new batch of Legendary Pizza. When the monster pig arrives, you easily defeat it after eating the pizza. Well done!
    Game over!
    [0m
    [34m+------------------------------------+
    | Sintendo Nitch - low quality, free |
    +------------------------------------+
    | 0 - Quit                           |
    | 1 - The Legend of Zelda: Link the  |
    |     shorty                         |
    | 2 - Higher or Lower (improved)     |
    | 3 - Rock Paper Scissors            |
    +------------------------------------+
    [0m
     2
    [34m2: [0mHigher or Lower
    You have three guesses to guess the number I am thinking of between 1-8.
    If you guess the number correctly, you win!
     5
    The number is lower
     3
    The number is lower
     2
    You win!
    Game over.
    [0m
    [34m+------------------------------------+
    | Sintendo Nitch - low quality, free |
    +------------------------------------+
    | 0 - Quit                           |
    | 1 - The Legend of Zelda: Link the  |
    |     shorty                         |
    | 2 - Higher or Lower (improved)     |
    | 3 - Rock Paper Scissors            |
    +------------------------------------+
    [0m
     3
    [34m3: [0mRock Paper Scissors
    Type r for rock, p for paper, or s for scissors
     s
    You chose scissors 
    The computer chose rock 
    You lose!
    [0m
    [34m+------------------------------------+
    | Sintendo Nitch - low quality, free |
    +------------------------------------+
    | 0 - Quit                           |
    | 1 - The Legend of Zelda: Link the  |
    |     shorty                         |
    | 2 - Higher or Lower (improved)     |
    | 3 - Rock Paper Scissors            |
    +------------------------------------+
    [0m
     0
    [34m0: [0m[34mGoodbye, World![0m[0m


#### Answering the Question: Why do you think reorganization and AP indetification is important?
I think reorgainization is important so that people can understand the code and modify more easily. If the code is split into different classes, it is very easy to just change the class instead of changing the code, just like a function. 

AP Identification is important because it shows that we are able to understand the code, not just copy it from a source. AP Identification shows our mastery of the code, and proves that we know what we're doing. 
