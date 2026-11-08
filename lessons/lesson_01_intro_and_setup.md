# Lesson 1: Introduction to Java and Setting Up Your Environment

- Planned publish date: 2026-11-07
- Target length: about 9 minutes
- Language: English
- Series: Vortex Java, Java Beginner to Advanced, Lesson 1 of 150

## Video title
Java Tutorial for Beginners 1: What Is Java and How to Set It Up (JDK 21 + IntelliJ)

## Thumbnail text
JAVA SETUP
Day 1

## Script

**[0:00 to 0:40] Intro**
Narration: Welcome to Vortex Java. This is Java tutorial lesson one of one hundred and fifty. In this series we go from absolute beginner to advanced Java, one topic every day. Today we will learn what Java is and set up everything you need to start coding.

**[0:40 to 2:00] What is Java?**
Narration: Java is a programming language used for web applications, Android apps, enterprise systems, and big data tools. Its main promise is "write once, run anywhere." You write code once, and it runs on Windows, Mac, and Linux, because Java code runs on the Java Virtual Machine.
On screen: a simple diagram with three boxes: Your code (.java), Compiler (javac), and JVM (runs bytecode).

**[2:00 to 4:30] Install the JDK**
Narration: The JDK is the Java Development Kit. It contains the compiler, javac, and the tools you need. We will use JDK 21, which is a Long Term Support release, so it will be supported for years.
On screen steps:
1. Go to the Adoptium website (adoptium.net) and download the Temurin JDK 21 installer for your operating system.
2. Run the installer and keep the default options. On Windows, tick "Set JAVA_HOME" and "Add to PATH".
3. Open a terminal and type the command below. You should see a version number starting with 21.

```
java -version
javac -version
```

**[4:30 to 6:30] Install an IDE**
Narration: An IDE is an editor with extra help: it highlights errors, completes code, and runs your programs with one click. We will use IntelliJ IDEA Community Edition, which is free.
On screen steps:
1. Download IntelliJ IDEA Community Edition from the JetBrains website.
2. Install it and open it.
3. Choose New Project, select Java, pick JDK 21, and name the project VortexJava.

**[6:30 to 8:20] Check your setup**
Narration: Let's confirm everything works. Create a class named Main, and inside it, print a message. We will do the full Hello World program in lesson two. For now, just check that you can run a program and see the output.
On screen code:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Java is ready!");
    }
}
```

Narration: Press the green run button. If you see "Java is ready!" in the console, your setup is complete.

**[8:20 to 9:00] Recap and outro**
Narration: Today you learned what Java is, how the JDK and JVM work together, and how to install Java and IntelliJ. In the next lesson we will write our first real program. Please like the video, subscribe to Vortex Java, and comment your operating system so I know where you are coming from.

## Recap slide
- Java runs on the JVM, which is why it works on many systems.
- Install JDK 21 (Temurin) and verify with java -version.
- Use IntelliJ IDEA Community for coding.

## Quiz (end-screen question)
What does JVM stand for? Answer: Java Virtual Machine.

## Description (YouTube)
In this lesson of the Vortex Java series, you will learn what Java is and how to install the JDK 21 and IntelliJ IDEA. Full playlist: Java Beginner to Advanced.

Tags: java tutorial, java for beginners, install java, jdk 21, intellij idea, vortex java, learn java
