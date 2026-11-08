# Lesson 4: Operators

- Planned publish date: 2026-11-10
- Target length: about 9 minutes
- Series: Vortex Java, Java Beginner to Advanced, Lesson 4 of 150

## Video title
Java Tutorial for Beginners 4: Java Operators (Arithmetic, Comparison, Logical)

## Thumbnail text
OPERATORS
Day 4

## Script

**[0:00 to 0:40] Intro**
Narration: Operators are symbols that perform actions on values. Today we cover arithmetic, comparison, logical, and assignment operators.

**[0:40 to 2:30] Arithmetic operators**
Narration: The basic arithmetic operators are plus, minus, multiply, divide, and modulus. Modulus gives the remainder after division.
On screen code:

```java
public class ArithmeticDemo {
    public static void main(String[] args) {
        int a = 10;
        int b = 3;
        System.out.println(a + b);  // 13
        System.out.println(a - b);  // 7
        System.out.println(a * b);  // 30
        System.out.println(a / b);  // 3, integer division
        System.out.println(a % b);  // 1, remainder
    }
}
```

Narration: Watch out: when both numbers are int, the division result drops the decimal part. To keep decimals, use a double, such as 10.0 / 3.

**[2:30 to 4:30] Comparison operators**
Narration: Comparison operators return true or false: equal to, not equal to, greater than, less than, greater or equal, and less or equal. Remember that equal to uses two equal signs.

```java
int x = 5;
int y = 8;
System.out.println(x == y);  // false
System.out.println(x != y);  // true
System.out.println(x < y);   // true
```

**[4:30 to 6:30] Logical operators**
Narration: Logical operators combine boolean values. AND uses two ampersands, OR uses two vertical bars, and NOT uses an exclamation mark.

```java
boolean hasTicket = true;
boolean isAdult = false;
System.out.println(hasTicket && isAdult);  // false
System.out.println(hasTicket || isAdult);  // true
System.out.println(!hasTicket);            // false
```

**[6:30 to 7:40] Assignment and increment**
Narration: The equals sign assigns a value. You can also use shortcuts such as plus-equals, and the increment operator ++ adds one.

```java
int score = 10;
score += 5;   // score is now 15
score++;      // score is now 16
```

**[7:40 to 8:40] Common mistakes**
Narration: Do not confuse the single equals sign with the double equals sign. And remember that integer division truncates the decimal part.

**[8:40 to 9:00] Recap and outro**
Narration: You now know arithmetic, comparison, logical, and assignment operators. Tomorrow we will take input from the user using Scanner.

## Recap slide
- % gives the remainder.
- == compares, = assigns.
- && is AND, || is OR, ! is NOT.

## Quiz (end-screen question)
What is 17 % 5? Answer: 2

## Description (YouTube)
Lesson 4 of the Vortex Java series explains arithmetic, comparison, logical, and assignment operators with simple code examples.

Tags: java operators, java arithmetic, java logical operators, java for beginners, vortex java
