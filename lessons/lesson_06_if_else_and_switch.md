# Lesson 6: Decisions with if, else, and switch

- Planned publish date: 2026-11-12
- Target length: about 10 minutes
- Series: Vortex Java, Java Beginner to Advanced, Lesson 6 of 150

## Video title
Java Tutorial for Beginners 6: if, else, and switch Statements Explained

## Thumbnail text
DECISIONS
Day 6

## Script

**[0:00 to 0:40] Intro**
Narration: Programs need to make decisions. In this lesson you will learn if, else if, else, and switch.

**[0:40 to 3:00] if and else**
Narration: An if statement runs a block of code only when a condition is true. Else runs when the condition is false.

```java
int temperature = 32;

if (temperature > 30) {
    System.out.println("It is hot.");
} else {
    System.out.println("It is comfortable.");
}
```

**[3:00 to 5:00] else if**
Narration: Use else if to check more than one condition, in order. Java runs the first block whose condition is true and skips the rest.

```java
int score = 72;

if (score >= 90) {
    System.out.println("Grade A");
} else if (score >= 75) {
    System.out.println("Grade B");
} else if (score >= 60) {
    System.out.println("Grade C");
} else {
    System.out.println("Grade D");
}
```

Narration: Score 72 prints Grade C. Order matters, so put the most specific checks first.

**[5:00 to 7:30] switch statement**
Narration: When you compare one variable against many fixed values, switch is cleaner. Each case ends with break, otherwise the code falls through to the next case.

```java
int day = 3;

switch (day) {
    case 1:
        System.out.println("Monday");
        break;
    case 2:
        System.out.println("Tuesday");
        break;
    case 3:
        System.out.println("Wednesday");
        break;
    default:
        System.out.println("Other day");
}
```

**[7:30 to 9:00] Modern switch expression**
Narration: Since Java 14, you can write a switch expression that returns a value and uses arrows, so you do not need break.

```java
String dayName = switch (day) {
    case 1 -> "Monday";
    case 2 -> "Tuesday";
    case 3 -> "Wednesday";
    default -> "Other day";
};
System.out.println(dayName);
```

**[9:00 to 9:50] Recap and outro**
Narration: You learned if, else if, else, and both styles of switch. Tomorrow we move on to loops, which repeat code.

## Recap slide
- if runs when a condition is true.
- else if checks conditions in order.
- Switch expressions with arrows return values and avoid break.

## Quiz (end-screen question)
In a classic switch, what keyword stops fall-through? Answer: break

## Description (YouTube)
Lesson 6 of the Vortex Java series covers if, else if, else, and both the classic and modern switch statements in Java.

Tags: java if else, java switch, java switch expression, java decision making, vortex java
