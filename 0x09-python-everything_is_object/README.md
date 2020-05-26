# 0x09. Python - Everything is object
![hero_image](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/252/r_208403_QPSN8.jpg)
## Background Context
Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:
###
    >>> a = 1
    >>> b = a
    >>> a = 2
    >>> b
    1
    >>> 
OK. But what about this?
###    
    >>> l = [1, 2, 3]
    >>> m = l
    >>> l[0] = 'x'
    >>> m
    ['x', 2, 3]
    >>> 
![surprised](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/252/giphy-5.gif)

This project is a little bit different than the usual projects. The first part is only questions about Python’s specificity like “What would be the result of…”. You should read all documentation first (as usual :)), then take the time to think and brainstorm with your peers about what you think and why. Try to do this without coding anything for a few hours.

Trying examples in the Python interpreter will give you most of the answers without having to think about it. Don’t go this route. First read, then think, then brainstorm together. Only then you can test in the interpreter.

It’s important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types. The biggest mandatory task is the blog post and it will count for 50% of the total score of the project.

Note that during interviews for Python positions, you will most likely have to answer to these type of questions.

All your answers should be only one line in a file. No space before or after the answer.

### Resources
#### Read or watch:

* [9.10. Objects and values](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values)
* [9.11. Aliasing](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing)
* [Immutable vs mutable types](https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types)
* [Mutation](http://composingprograms.com/pages/24-mutable-data.html#sequence-objects) (Only this chapter)
* [9.12. Cloning lists](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists)
* [Python tuples: immutable but potentially changing](http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
* Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
* What is an object
* What is the difference between a class and an object or instance
* What is the difference between immutable object and mutable object
* What is a reference
* What is an assignment
* What is an alias
* How to know if two variables are identical
* How to know if two variables are linked to the same object
* How to display the variable identifier (which is the memory address in the CPython implementation)
* What is mutable and immutable
* What are the built-in mutable types
* What are the built-in immutable types
* How does Python pass variables to functions
### Requirements
#### Python Scripts
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the PEP 8 style (version 1.7.*)
* All your files must be executable
* The length of your files will be tested using wc
### .txt Answer Files
* Only one line
* No Shebang
* All your files should end with a new line

## Tasks 

#### 0. Who am I?
What function would you use to print the type of an object?
* 0-answer.txt
##
#### 1. Where are you?
How do you get a variable's identifier (which is the memory address in the CPython implementation)?
* 1-answer.txt
##
#### 2. Right count
In the following code, do `a` and `b` point to the same object?
###
    >>> a = 89
    >>> b = 100
* 2-answer.txt
##
#### 3. Right count =
In the following code, do `a` and `b` point to the same object?
```
>>> a = 89
>>> b = 89
```
* 3-answer.txt
##
#### 4. Right count =
In the following code, do `a` and `b` point to the same object?
```
>>> a = 89
>>> b = a
```
* 4-answer.txt
##
#### 5. Right count =+
In the following code, do `a` and `b` point to the same object?
```
>>> a = 89
>>> b = a + 1
```
* 5-answer.txt
#### 6. Is equal
What do these 3 lines print?
```
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 == s2)
```
* 6-answer.txt
##
#### 7. Is the same
What do these 3 lines print?
```
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 is s2)
```
* 7-answer.txt
##
#### 8. Is really equal
What do these 3 lines print?
```
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 == s2)
```
* 8-answer.txt
##
#### 9. Is really the same
What do these 3 lines print?
```
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 is s2)
```
* 9-answer.txt
##
#### 10. And with a list, is it equal
What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 == l2)
```
* 10-answer.txt
##
#### 11. And with a list, is it the same
What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 is l2)
```
* 11-answer.txt
##
#### 12. And with a list, is it really equal
What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```
* 12-answer.txt
##
#### 13. And with a list, is it really the same
What do these 3 lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```
* 13-answer.txt
##
#### 14. List append
What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```
* 14-answer.txt
##
#### 15. List add
What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```
* 15-answer.txt
##
#### 16. Integer incrementation
What does this script print?
```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```
* 16-answer.txt
##
#### 17. List incrementation
What does this script print?
```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```
* 17-answer.txt
##
#### 18. List assignation
What does this script print?
```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```
* 18-answer.txt
##
#### 19. Copy a list object
Python function `def copy_list(l):` that returns a copy of a list.
* 19-copy_list.py
##
#### 20. Tuple or not?
Is `a` a tuple?
```
a = ()
```
* 20-answer.txt
#### 21. Tuple or not?
Is `a` a tuple?
```
a = (1, 2)
```
* 21-answer.txt
##
#### 22. Tuple or not?
Is `a` a tuple?
```
a = (1)
```
* 22-answer.txt
##
#### 23. Tuple or not?
Is `a` a tuple?
```
a = (1, )
```
* 23-answer.txt
##
#### 24. Richard Sim's special #0
What does this script print?
```
a = (1)
b = (1)
a is b
```
* 24-answer.txt
##
#### 25. Richard Sim's special #1
What does this script print?
```
a = (1, 2)
b = (1, 2)
a is b
```
* 25-answer.txt
#### 26. Richard Sim's special #2
What does this script print?
```
a = ()
b = ()
a is b
```
* 26-answer.txt
##
#### 27. Richard Sim's special #3
Will the last line of this script print `139926795932424`?
```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```
* 27-answer.txt
##
#### 28. Richard Sim's special #4
Will the last line of this script print `139926795932424`?
```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```
* 28-answer.txt
#### 29. Python3: Mutable, Immutable... everything is object! mandatory
Write a blog post about everything you just learned / this project is covering. Your blog post should be articulated this way (one paragraph per item):

* introduction
* id and type
* mutable objects
* immutable objects
* why does it matter and how differently does Python treat mutable and immutable objects
* how arguments are passed to functions and what does that imply for mutable and immutable objects
* If you worked on advanced tasks, please also include what you did learn in those tasks in the blog post.

Your posts should have many code/output examples to illustrate what you are explaining, and at least one picture, at the top. Publish your blog post on Medium or LinkedIn, and share it at least on LinkedIn.

When done, please add all urls below (blog post, LinkedIn post, etc.)

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.

Add URLs here:

**__________________**
##
#### 35. Clear strings
```
guillaume@ubuntu:/python3$ cat string.py 
a = "HBTN"
b = "HBTN"
del a
del b
c = "HBTN"
guillaume@ubuntu:/python3$ 
```
Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):

* How many string objects are created by the execution of the first line of the script? (106-line1.txt)
* How many string objects are created by the execution of the second line of the script (106-line2.txt)
* After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (106-line3.txt)
* After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (106-line4.txt)
* How many string objects are created by the execution of the last line of the script (106-line5.txt)
```
* Files: 106-line1.txt, 106-line2.txt, 106-line3.txt, 106-line4.txt, 106-line5.txt
```
##
## Advanced Tasks
#### 30. #pythonic
Python function `magic_string()` that returns the string `"Holberton"` n times the number of iteration.
* 100-magic_string.py
##
#### 30. Low memory cost
Python class `LockedClass` with no attributes that prevents the user from dynamically creating any new instance attributes not called `first_name`.
* 101-locked_class.py
##
#### 31. int 1/3
how many `int` objects are created by the execution:
* 103-line1.txt

How many `int` objects are created by the execution
of the second line in this script?
* 104-line2.txt
```
a = 1
b = 1
```
##
#### 32. int 2/3
How many `int` objects are created by the execution of the first line in this script?
* 104-line1.txt

How many `int` objects are created by the execution of the second line in this script?
* 104-line2.txt

After the execution of line 3, is the `int` object pointed to by `a` deleted?
* 104-line3.txt

After the execution of line 4, is the `int` object pointed to by `b` deleted?
* 104-line4.txt

How many `int` objects are created by the execution of the last line in this script?
* 104-line5.txt
```
a = 1024
b = 1024
del a
del b
c = 1024
```
##
#### 33. int 3/3
Before the execution of line 2 in this script, how many `int` objects have been created and are still in memory?
```
print("I")
print("Love")
print("Python")
```
* 105-line1.txt
##
#### 34. Clear strings
How many `str` objects are created by the execution of the first line in this script?
* 106-line1.txt

How many `str` objects are created by the execution of the second line in this script?
* 106-line2.txt

After the execution of line 3, is the `str` object pointed to by `a` deleted?
* 106-line3.txt

After the execution of line 4, is the `str` object pointed to by `b` deleted?
* 106-line4.txt

How many `str` objects are created by the execution of the last line in this script?
* 106-line5.txt
```
a = "HBTN"
b = "HBTN"
del a
del b
c = "HBTN"
```
#
## Author ✒️
* **Luis Angel Vargas Mosquera** - [LuAnVaRmO](https://github.com/LuAnVaRmO)
