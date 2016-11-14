# Students-Informations
This application manages the grades of a test. It is driven by a console-based menu user interface.

Each student has a code (e.g. miie0509), a name, a hometown (e.g. Cluj) and a grade (e.g. 7.8). The application will allow to:

  1. Add a student.  Te user will enter the code, the name, the hometown and grade. The application will add the student. In case one of the fields name or hometown has a length less than 3 characters, or if the code is not formed of 4 letters followed by 4 digits, the application will provide an error message. In this case, the student will not be added.

  2. Modify the grade of a given student. The user will enter the code and the new grade and the application will update the student with the given code. 

  3. The students of a given group need to be penalized because they did not prepare the previous labs well and therefore their grades need to be reduced by 10%.The group number is represented by the first 2 digits in the code (in example:05). Create a function that reduces all the grades of the students in a given group by 10%. 

  4. Show all students with a given hometown , sorted decreasing by their grade.
  
NOTE: The application is modular, but it doesn't use classes!

