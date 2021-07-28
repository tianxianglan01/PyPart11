import uuid
from enum import Enum
#help(enumerate)


class AliveStatus(Enum):
    Deceased = 0
    Alive = 1

# the enum module allows values bound to symbolic names
# in the above case, the symbolic names are 'Deceased' and 'Alive', and the values are 0 and 1

class Person:

    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive = AliveStatus.Alive
        # when you pass a person, a person's status starts at alive, and that's why you don't __init__
    
    def update_first_name(self, fname):
        self.first_name = fname

    def update_last_name(self, lname):
        self.last_name = lname

    def update_dob(self, dob):
        self.dob = dob

    def update_status(self, status):
        self.alive = status

# okay so in the update_status method, 
        

class Instructor(Person):

    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name, last_name, dob)
        # don't have to redo self.'x' = x
        self.instructor_id = 'Instructor_' + str(uuid.uuid4())

class Student(Person):
    
    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name, last_name, dob)
        self.student_id = 'Student_' + str(uuid.uuid4())
        # don't need to init student_id cause every student is initialized with a value when created
        # don't have to pass student_id as a variable cause it hasn't been created it

class ZipCodeStudent(Student):
    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name, last_name, dob)
        # don't need to call student_id because by creating a ZipCodeStudent, it would automatically
        # create a stuent_id

Sean = ZipCodeStudent('Sean', 'Lan', '1/1/11')
print(Sean.alive)

class PreKStudent(Student):
    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name, last_name, dob)

class MiddleSchool(Student):
    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name, last_name, dob)

class College(Student):
    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name, last_name, dob)

class Classroom:

    def __init__(self):
        self.students = {}
        self.instructors = {}
    
    def add_instructor(self, instructor):
        
        self.instructors[instructor.instructor_id] = instructor
       

    def remove_instructor(self, instructor):
        if instructor.instructor_id in self.instructors.keys():
            del self.instructors[instructor.instructor_id]
        else:
            print('Your instructor to remove does not exist')


    def add_student(self, student):
        
        self.students[student.student_id] = str(student) + '\n'
        

    def remove_student(self, student):
        if student.student_id not in self.students.keys():
            print('Student to remove does not exist in database')
        else:
            del self.students[student.student_id]

    def print_instructors(self):
        for instructor in self.instructors:
            print(instructor + ': ' + str(self.instructors[instructor].first_name) + ' ' + str(self.instructors[instructor].last_name))

    def print_students(self):
        for student in self.students:
            print(student + ': ' + str(self.students[student].first_name) + ' ' + str(self.students[student].last_name))
new = Classroom()

