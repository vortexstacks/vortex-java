# Lesson 9: Arrays

- Planned publish date: 2026-11-15
- Target length: about 10 minutes
- Series: Vortex Java, Java Beginner to Advanced, Lesson 9 of 150

## Video title
Java Tutorial for Beginners 9: Arrays in Java (Declare, Loop, and Sort)

## Thumbnail text
ARRAYS
Day 9

## Script

**[0:00 to 0:40] Intro**
Narration: An array stores multiple values of the same type in one variable. Today you will create arrays, access elements, and loop through them.

**[0:40 to 2:30] Creating an array**
Narration: Arrays have a fixed size. Index numbers start at zero, so the first element is at index zero.

```java
int[] numbers = {10, 20, 30, 40, 50};
System.out.println(numbers[0]);   // 10
System.out.println(numbers[4]);   // 50
System.out.println(numbers.length); // 5
```

**[2:30 to 4:30] Creating an empty array**
Narration: You can also create an array with a set size and fill it later. All values start as zero for numbers, false for booleans, and null for objects.

```java
int[] marks = new int[3];
marks[0] = 85;
marks[1] = 92;
marks[2] = 78;
```

**[4:30 to 6:30] Looping through an array**
Narration: Use a for loop with the length property, or the enhanced for loop when you only need the values.

```java
for (int i = 0; i < numbers.length; i++) {
    System.out.println("Index " + i + ": " + numbers[i]);
}

for (int n : numbers) {
    System.out.println(n);
}
```

**[6:30 to 8:00] Sorting with Arrays.sort**
Narration: The java.util.Arrays class has helper methods. Arrays.sort sorts the array in place.

```java
import java.util.Arrays;

int[] data = {42, 7, 19, 3};
Arrays.sort(data);
System.out.println(Arrays.toString(data));  // [3, 7, 19, 42]
```

**[8:00 to 9:00] Common mistakes**
Narration: The most common error is an ArrayIndexOutOfBoundsException. This happens when you use an index equal to or greater than the length. The last valid index is length minus one.

**[9:00 to 10:00] Recap and outro**
Narration: You learned to create, access, loop through, and sort arrays. Tomorrow we work with strings, which are a special kind of object in Java.

## Recap slide
- Arrays have a fixed size.
- Indexes start at 0.
- Last index is length minus 1.
- Use Arrays.sort to sort.

## Quiz (end-screen question)
What is the index of the first element in an array? Answer: 0

## Description (YouTube)
Lesson 9 of the Vortex Java series covers arrays: declaring, accessing, looping, and sorting, plus the common out-of-bounds error.

Tags: java arrays, java array tutorial, java for loop array, arrays sort java, vortex java
