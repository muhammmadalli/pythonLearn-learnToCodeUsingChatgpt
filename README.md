# LEARN TO CODE USING CHATGPT
This repo contains all the exercises done during the course **LEARN TO CODE USING CHATGPT** done on *Quantic*.\
\
ChatGPT can be a tool of astronomical assistance for programmers - with the right prompt.\
\
Programmers can be at times frustrated with the coding-related responses generated by ChatGPT and use up valuable time in debugging and integrating the generated code. Well, this can be circumvented by employing a structured approach to prompting ChatGPT for coding assistance and debugging.\
\
LEARN TO CODE USING CHATGPT - Unlock the synergy between coding and natural language by prompting ChatGPT to create working programs for you. Master prompting techniques and coding basics as you optimize code evaluation, testing, and refactoring with ChatGPT's guidance.\
\
Here is the link to take on the course offered for free by Quantic School of Business and Technology.\
https://app.quantic.edu/course/learn-to-code-using-chatgpt/fe3304f1-8733-4d74-b130-cc806a8f090d\
\
\
*This repo only contains exercise 5 onwards codes*\
Links to previous exercises are appended below: -\
https://github.com/muhammmadalli/learnPython-HelloWorld - **Exercise 1**\
https://github.com/muhammmadalli/learnPython-SortExpensesAndSumThem - **Exercise 2**\
https://github.com/muhammmadalli/learnPython-websiteLivenessCheck - **Exercise 3**\
https://github.com/muhammmadalli/learnPython-extractSentencesHavingAKeyword - **Exercise 4**\


## **BELOW ARE THE LESSONS LEARNT**
a repository of all python projects and libraries: [text](https://pypi.org/)\
pyinstall is dead, long live pip!: [text](https://ianbicking.org/blog/2008/10/pyinstall-is-dead-long-live-pip.html)\

### LEAST-TO-MOST STRATEGY
*Building program from simpler to complex incrementally*
1. ChatGPT could introduce new error in the previous working code\
&emsp;Must take step-by-steo verification of the code. *VERSION CONTROL WILL HELP A LOT*
2. MORE THOUGHT IS REQUIRED BY THE PROGRAMMER  
&emsp;Promrammer is to use his intelligence for breaking down and integrating the modules
3. Overall time taken is more.

#### The advantages of least-to-most strategy. 
1. It gives ChatGPT simpler problems to solve. 
2. It gives you working code to fall back on, if a later step fails. 
3. It gets you at least some of the capability you want, even if ChatGPT can't deliver everything. 

### Prompt - Question Refinement by asking ChatGPT
I want an app that *does some function*. Tell me what I should include in my prompt to you. Don't write any code at this point.

# NOTES ON OOP (Object-oriented Programming)
OOP encapsulates attributes and methods together in objects. This encapsulation makes organizing complex code easier. It allows programmers to divide and conquer a complex task by breaking it into smaller parts, each of which can be developed and tested separately. Following are the major sub-components of OOP: -  
1. **CONTRUCTOR** creates an instance, or object which was not previously there.
2. **ATTRIBUTES** contain data in the class.
3. **METHODS** work on and manipulate the attributes.
4. **CLASS** is like a blueprint or a template for creating objects. 
    1. It defines the structure and behavior that its objects will have. It has both *attributes* and *methods*.
5. **OBJECT** is an instance of a class. A *working thing* made by using the class.
    1. They are made/created using *CONSTRUCTORS*.
    2. Once you have created an object, you can access its attributes and call its methods.
    3. It is a self-contained unit that bundles data and functions on that operate on that data.
    4. One can create multiple objects from the same class, each with its own set of attributes and the ability to perform actions defined by the class methods. 

**In summary**, classes are a way to define the structure and behavior of objects in OOP (Python). They encapsulate data (attributes) and functions (methods) into a single unit, making it easier to work with complex data and behaviors in your programs. One can create multiple objects from the same class, each with its own set of attributes and the ability to perform actions defined by the class methods.


# Notes on Debugging Techniques. 
1. It's early in the debugging process, and you get a trace back. | **Paste the trace back** in prompt.
2. Has been getting closer to the correct code. But there is an apparently minor logic error. | **Explain the problem**. 
3. ChatGPT isn't getting closer to the correct code. But you think you might be able to recognize a problem in its logic. | Ask ChatGPT to **explain the approach**.
4. You've isolated the problem to a single line of code that involves a call to an external library. | **Search the Internet** for correct syntax and calling method. 
5. ChatGPT isn't getting closer to the correct code. And you are unable to pinpoint the problem. | Ask ChatGPT to **change the approach**. 