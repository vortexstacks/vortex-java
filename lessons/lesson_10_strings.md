# Lesson 10: Strings

- Planned publish date: 2026-11-16
- Target length: about 10 minutes
- Series: Vortex Java, Java Beginner to Advanced, Lesson 10 of 150

## Video title
Java Tutorial for Beginners 10: Strings in Java and Common String Methods

## Thumbnail text
STRINGS
Day 10

## Script

**[0:00 to 0:40] Intro**
Narration: Strings store text. In Java, String is a class, not a primitive type, and this lesson shows the most useful methods you will use every day.

**[0:40 to 2:00] Creating strings**
Narration: You can create a string with double quotes. Strings are immutable, which means they cannot change after creation.

```java
String language = "Java";
String greeting = "Hello, " + language;
System.out.println(greeting);   // Hello, Java
```

**[2:00 to 4:30] Common methods**
Narration: Here are the methods you will use most often.

```java
String text = "  Vortex Java  ";

System.out.println(text.length());        // 15
System.out.println(text.trim());          // Vortex Java
System.out.println(text.toUpperCase());   // VORTEX JAVA
System.out.println(text.toLowerCase());   // vortex java
System.out.println(text.contains("Java")); // true
System.out.println(text.trim().charAt(0)); // V
```

Narration: Notice that trim removes spaces at the start and end, but not in the middle.

**[4:30 to 6:30] Comparing strings**
Narration: Never use double equals to compare string content. Use the equals method. It checks the text, while double equals checks whether two references point to the same object.

```java
String a = "Java";
String b = "Java";
System.out.println(a.equals(b));              // true
System.out.println("java".equalsIgnoreCase(a)); // true
```

**[6:30 to 8:00] Splitting and joining**
Narration: split breaks a string into an array. String.join combines values with a separator.

```java
String csv = "red,green,blue";
String[] colors = csv.split(",");
System.out.println(colors[1]);   // green

String joined = String.join(" | ", colors);
System.out.println(joined);      // red | green | blue
```

**[8:00 to 9:00] Common mistakes**
Narration: Avoid building long strings in a loop with plus, because each step creates a new object. Use StringBuilder instead, which we will cover in a later lesson.

**[9:00 to 10:00] Recap and outro**
Narration: You learned to create strings, use common methods, compare them correctly with equals, and split and join text. You have now finished the first ten lessons of the beginner phase. Thanks for following along.

## Recap slide
- String is a class and is immutable.
- Use equals, not double equals, to compare text.
- split turns text into an array, join turns an array into text.

## Quiz (end-screen question)
Which method compares the contents of two strings? Answer: equals()

## Description (YouTube)
Lesson 10 of the Vortex Java series covers strings: creating them, common methods, comparing with equals, and splitting and joining text.

Tags: java string, java string methods, java equals, java split, vortex java
