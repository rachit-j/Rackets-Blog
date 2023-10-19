A class has three main parts: variable declarations, constructors, and methods.

Initialize an object of a class: Classname objectname = new Classname();

This one line after the class header is the variable declaration. In this class, we have a private integer named side, which represents the side length of the square. We have set this variable to private because we want to restrict access to the data in the class from other classes. Otherwise, anyone could change the data without permission. This has the potential for other classes and programmers to break the code. This the principle of encapsulation, keeping information private and only allowing approved methods to access such data.


An object’s state refers to its attributes and their values at a given time; the state is defined by instance variables belonging to the object. Constructors are used to set the initial state of an object, which should include initial values for all instance variables.

Default data types: 
Data Type	Value
Boolean	false
Double	0.0
Integer	0
Objects/Reference Types	Null


Comments:
// single line
/* */ double line

Accessor Methods **

Mutator methods: we can change the name of an object instance of a class by using a .[somefunction]

Method header format: <access modifier> <return type> <method name> (<parameters>)
Examples:
    public static void main (String args[])
    private String sayHello ()
    protected static int addNums (int a, int b)
    public void printSum (double a, double b, int c, boolean flag, String text)


Static variables and methods