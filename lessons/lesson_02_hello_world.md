# Lesson 2: Hello World and How Java Runs

- Planned publish date: 2026-11-08
- Target length: about 9 minutes
- Series: Vortex Java, Java Beginner to Advanced, Lesson 2 of 150

## Video title
Java Tutorial for Beginners 2: Your First Java Program (Hello World Explained)

## Thumbnail text
HELLO WORLD
Day 2

## Script

**[0:00 to 0:30] Intro**
Narration: Welcome back to Vortex Java. Today you will write your first real Java program, and you will learn exactly what happens when you press run.

**[0:30 to 2:30] Code**
Narration: Here is the classic Hello World program. Let's read it line by line.
On screen code:

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

On screen annotations:
- public class HelloWorld: every Java file has a class. The class name must match the file name, HelloWorld.java.
- public static void main(String[] args): this is the entry point. Java starts running from this method.
- System.out.println: prints text to the console and moves to a new line.

**[2:30 to 5:00] Compile and run**
Narration: Java uses two steps. First, the compiler turns your source code into bytecode. Then the JVM runs the bytecode.
On screen commands:

```
javac HelloWorld.java
java HelloWorld
```

Narration: The first command creates HelloWorld.class. The second command runs it. Notice that we do not add ".class" when we run it.

**[5:00 to 7:00] JDK, JRE, and JVM**
Narration: These three terms confuse many beginners. The JVM runs your bytecode. The JRE is the JVM plus the standard libraries needed to run programs. The JDK is the JRE plus development tools, such as the compiler. As a developer, you install the JDK.
On screen: a nested diagram: JDK contains JRE, JRE contains JVM.

**[7:00 to 8:30] Common mistakes**
Narration: Three mistakes to avoid:
1. Mismatched names: a class named HelloWorld must be saved as HelloWorld.java.
2. Missing semicolon at the end of statements.
3. Capital letters matter. System is correct, system is not.

**[8:30 to 9:00] Recap and outro**
Narration: You wrote your first Java program, learned the main method, and saw the compile and run steps. Tomorrow we start with variables and data types. See you then.

## Recap slide
- Every Java program starts at main.
- javac compiles, java runs.
- JDK contains JRE, which contains JVM.

## Quiz (end-screen question)
Which command compiles a Java file named Test.java? Answer: javac Test.java

## Description (YouTube)
Lesson 2 of the Vortex Java series. Learn how to write Hello World, compile with javac, and run with java. Also covers the difference between JDK, JRE, and JVM.

Tags: hello world java, java first program, javac, java compile and run, vortex java, java for beginners
