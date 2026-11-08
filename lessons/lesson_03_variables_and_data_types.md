# Lesson 3: Variables and Data Types

- Planned publish date: 2026-11-09
- Target length: about 10 minutes
- Series: Vortex Java, Java Beginner to Advanced, Lesson 3 of 150

## Video title
Java Tutorial for Beginners 3: Variables and Data Types Explained Simply

## Thumbnail text
VARIABLES
Day 3

## Script

**[0:00 to 0:40] Intro**
Narration: A variable is a named box that stores a value. In this lesson you will learn Java's data types, how to declare variables, and how to choose the right type.

**[0:40 to 3:00] Primitive types**
Narration: Java has eight primitive types. Here are the most common ones.
On screen table:
- int: whole numbers, for example 42
- long: large whole numbers, ends with L, for example 10000000000L
- double: decimal numbers, for example 3.14
- float: smaller decimals, ends with f, for example 3.14f
- char: a single character in single quotes, for example 'A'
- boolean: true or false
- byte and short: small whole numbers, less common in beginner code

**[3:00 to 5:30] Declaring and assigning variables**
Narration: To create a variable, write the type, then the name, then optionally a value.
On screen code:

```java
public class Variables {
    public static void main(String[] args) {
        int age = 25;
        double price = 99.99;
        char grade = 'A';
        boolean isStudent = true;
        long population = 8000000000L;

        System.out.println("Age: " + age);
        System.out.println("Price: " + price);
        System.out.println("Grade: " + grade);
        System.out.println("Student: " + isStudent);
        System.out.println("Population: " + population);
    }
}
```

Narration: Notice that a variable name must start with a letter, and Java naming style uses camelCase, such as isStudent.

**[5:30 to 7:00] The var keyword**
Narration: From Java 10 onward you can write var and let Java infer the type. The type is still fixed, so the compiler knows exactly what it is.

```java
var city = "Chennai";   // inferred as String
```

**[7:00 to 8:30] Common mistakes**
Narration: Three common mistakes:
1. Using int for money with decimals. Use double for simple examples, and BigDecimal for real money in later lessons.
2. Forgetting the L on long values.
3. Using a variable before giving it a value. Java will show a compile error.

**[8:30 to 9:40] Recap and outro**
Narration: You learned the main primitive types, how to declare and print variables, and how var works. Tomorrow we use these variables with operators.

## Recap slide
- int, long, double, float, char, boolean are the main primitive types.
- Declare with type name = value.
- Use var when the type is obvious.

## Quiz (end-screen question)
Which type is best for storing true or false? Answer: boolean

## Description (YouTube)
Lesson 3 of the Vortex Java series covers variables and primitive data types, including int, double, char, boolean, long, and var.

Tags: java variables, java data types, primitive types java, java for beginners, vortex java
