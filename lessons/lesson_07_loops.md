# Lesson 7: Loops (for, while, do-while)

- Planned publish date: 2026-11-13
- Target length: about 10 minutes
- Series: Vortex Java, Java Beginner to Advanced, Lesson 7 of 150

## Video title
Java Tutorial for Beginners 7: for, while, and do-while Loops in Java

## Thumbnail text
LOOPS
Day 7

## Script

**[0:00 to 0:40] Intro**
Narration: Loops let you repeat code without copying it. Today we cover the for loop, the while loop, and the do-while loop.

**[0:40 to 3:00] for loop**
Narration: A for loop has three parts: the starting value, the condition, and the update. This example prints numbers one to five.

```java
for (int i = 1; i <= 5; i++) {
    System.out.println("Count: " + i);
}
```

Narration: The loop starts at 1, keeps going while i is less than or equal to 5, and adds 1 each time.

**[3:00 to 5:00] while loop**
Narration: A while loop checks the condition before each run. Use it when you do not know in advance how many times to repeat.

```java
int number = 1;
while (number <= 5) {
    System.out.println(number);
    number++;
}
```

**[5:00 to 6:30] do-while loop**
Narration: A do-while loop runs the body at least once, then checks the condition. This is useful for menus that must show at least once.

```java
int choice;
do {
    System.out.println("Menu shown once");
    choice = 0;
} while (choice != 0);
```

**[6:30 to 8:00] break and continue**
Narration: break exits the loop immediately. continue skips the rest of the current iteration and goes to the next one.

```java
for (int i = 1; i <= 10; i++) {
    if (i == 3) continue;   // skip 3
    if (i == 6) break;      // stop at 6
    System.out.println(i);
}
```

Narration: This prints 1, 2, 4, 5.

**[8:00 to 9:00] Common mistakes**
Narration: The most common mistake is an infinite loop, which happens when the condition never becomes false. Always check that your loop variable changes.

**[9:00 to 10:00] Recap and outro**
Narration: You now know for, while, and do-while loops, plus break and continue. Tomorrow we group code into methods.

## Recap slide
- for: when you know the count.
- while: check first, repeat while true.
- do-while: runs at least once.
- break exits, continue skips.

## Quiz (end-screen question)
Which loop always runs at least once? Answer: do-while

## Description (YouTube)
Lesson 7 of the Vortex Java series explains for, while, and do-while loops, plus break and continue, with examples you can run.

Tags: java loops, java for loop, java while loop, do while java, vortex java
