## SDSS Computing Studies Python Assignment
### Assignment Classes and Objects
Objectives:
* create a class to solve a problem
* instantiate the class with a specific set of data
* create multiple instances to solve multiple problems

Think about a circle.  A circle is a round shape, with a radius, circumference and area.  There are many things we can do to describe a circle, but when we think of a specific circle, we can think about actual measurements, the outline color, the fill color, and all kinds of other specifics.

A class is like a generic description along with some basic definitions.  However, when we think of a specific example, we *instantiate* the class, meaning we create a specific instance of a circle, and can then start making some calculations.

Class templates will have class properties (variables) and methods (functions).  Note that within the class, these are referenced as "self", but outside of the class, you use the instantiated objects name.

A very special class method is the **constructor**. In our example file, this is the method defined on line 30.  It is executed or called when an object is instantiated.  It will have parameters/arguments that can be used to help you define some initial values.

Consider example1.py

##### Task 1
Convert the code for this number guessing game from a main block with functions to a class object.

##### Task 2
Convert the code for this quadratic function prgram to a class object.

##### Task 3
Rectangular Prism Object
Create a class that creates a rectangular prism.  You should be able to set all of the important measurements (l,w,h) when the object is instantiated in the constructor and you should have class methods that determine the surface area and volume.
You should have class methods that also allow you to change the dimensions of the object.
Instantiate 3 separate rectangular prisms with the test data given, and check the assertions are correct.

##### Task 4
Compound Interest Calculator
Create a class object that accepts paramters for Principal, Annual Interest Rate, Number of compounding periods.  
Create a class method that calculates the amount of compound interest for a given length of time.

Extension: accept time given in different measurements, but convert them to years for use in your class template.