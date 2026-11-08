# Lesson 8: Methods

- Planned publish date: 2026-11-14
- Target length: about 10 minutes
- Series: Vortex Java, Java Beginner to Advanced, Lesson 8 of 150

## Video title
Java Tutorial for Beginners 8: Methods in Java (Parameters and Return Values)

## Thumbnail text
METHODS
Day 8

## Script

**[0:00 to 0:40] Intro**
Narration: A method is a named block of code you can call many times. Methods keep programs organized and avoid repetition.

**[0:40 to 2:30] Defining and calling a method**
Narration: A method has an access modifier, a return type, a name, and parameters. This method prints a greeting.

```java
public class Methods {
    public static void main(String[] args) {
        greet();
    }

    public static void greet() {
        System.out.println("Welcome to Vortex Java!");
    }
}
```

Narration: The word void means the method returns nothing. Static lets us call it from main without creating an object. We will explain objects later in the series.

**[2:30 to 5:00] Parameters**
Narration: Parameters let you pass data into a method.

```java
public static void greetUser(String name) {
    System.out.println("Hello, " + name + "!");
}

// called like this:
greetUser("Priya");
```

**[5:00 to 7:00] Return values**
Narration: When a method needs to give back a result, set the return type to that type and use return.

```java
public static int add(int a, int b) {
    return a + b;
}

int total = add(4, 6);   // total is 10
System.out.println(total);
```

**[7:00 to 8:30] Method overloading preview**
Narration: You can have methods with the same name if their parameters differ. We will cover overloading in detail later. For now, know that the compiler picks the right version based on the arguments.

**[8:30 to 9:40] Recap and outro**
Narration: You learned how to define methods, pass parameters, return values, and why methods make code cleaner. Tomorrow we use arrays to store many values together.

## Recap slide
- Methods are reusable blocks of code.
- Parameters pass data in, return sends data out.
- void means no return value.

## Quiz (end-screen question)
What keyword returns a value from a method? Answer: return

## Description (YouTube)
Lesson 8 of the Vortex Java series explains how to define and call methods, use parameters, and return values in Java.

Tags: java methods, java functions, java parameters, java return value, vortex java
