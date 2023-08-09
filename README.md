# Test-Score-Tracker
Here, I have constructed a function that ingests a filename, from which it will read and parse student grades to determine the minimal average test score among the students.
The file format consists of comma-separated values, representing the student name followed by five numerical test scores in the form of student_name, test1_score, test2_score,
test3_score, test4_score, test5_score. The function also employs an anonymous lambda function and leverage the built-in min() function to ascertain the student possessing the 
minimum average test score. The argument passed to the min function is a list of string lines.
The output of this function will be a tuple, encompassing the lambda function utilized and the string line that corresponds to the student with the lowest test average, 
formatted as (lambda_func, 'student1,33,34,35,36,45')


