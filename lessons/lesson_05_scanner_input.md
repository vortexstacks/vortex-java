# Lesson 5: Taking User Input with Scanner

- Planned publish date: 2026-11-11
- Target length: about 9 minutes
- Series: Vortex Java, Java Beginner to Advanced, Lesson 5 of 150

## Video title
Java Tutorial for Beginners 5: Take User Input with Scanner in Java

## Thumbnail text
SCANNER
Day 5

## Script

**[0:00 to 0:40] Intro**
Narration: So far our programs have only printed fixed text. Today we make them interactive by reading input from the keyboard using the Scanner class.

**[0:40 to 2:00] Import and create a Scanner**
Narration: Scanner lives in the java.util package, so we import it at the top. Then we create an object from it, and pass System.in, which means keyboard input.

```java
import java.util.Scanner;

public class UserInput {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
    }
}
```

**[2:00 to 4:30] Reading text and numbers**
Narration: Scanner has different methods for different types. nextLine reads a full line of text. nextInt reads an integer. nextDouble reads a decimal.

```java
import java.util.Scanner;

public class UserInput {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = scanner.nextLine();

        System.out.print("Enter your age: ");
        int age = scanner.nextInt();

        System.out.println("Hello " + name + ", you are " + age + " years old.");

        scanner.close();
    }
}
```

**[4:30 to 6:30] The nextLine trap**
Narration: This is the most common Scanner problem. After nextInt, the newline character is still in the buffer. If you then call nextLine, it returns an empty string. The fix is to call nextLine once after nextInt to consume the leftover newline.

```java
int age = scanner.nextInt();
scanner.nextLine();   // consume the leftover newline
String city = scanner.nextLine();
```

**[6:30 to 8:00] Closing the Scanner**
Narration: Always close the Scanner when you finish with it, using scanner.close(). Closing it also closes System.in, so do this at the end of the program, not in the middle.

**[8:00 to 9:00] Recap and outro**
Narration: You learned how to import Scanner, read text and numbers, avoid the nextLine trap, and close the Scanner. Tomorrow we use input to make decisions with if and else.

## Recap slide
- import java.util.Scanner.
- nextLine for text, nextInt for integers.
- Call nextLine after nextInt to clear the newline.

## Quiz (end-screen question)
Which method reads a whole line of text? Answer: nextLine()

## Description (YouTube)
Lesson 5 of the Vortex Java series shows how to read user input with Scanner, including the common nextLine problem and how to fix it.

Tags: java scanner, java input, java user input, java beginner tutorial, vortex java
