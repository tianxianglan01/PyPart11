import unittest
import unittest.mock
from io import StringIO

import gradebook


class PersonTest(unittest.TestCase):

    def setUp(self) -> None:

        bob = gradebook.Person("Bob", "Smith", "01201970")
        jane = gradebook.Person("Jane", "Doe", "02201984")

        self._people = [
            bob,
            jane
        ]

    def test_update_first_name(self):
        bob = self._people[0]
        bob.update_first_name("John")
        self.assertEqual("John", bob.first_name)

    def test_update_last_name(self):
        bob = self._people[0]
        bob.update_last_name("Doe")
        self.assertEqual("Doe", bob.last_name)

    def test_update_dob(self):
        bob = self._people[0]
        bob.update_dob("01011970")
        self.assertEqual("01011970", bob.dob)

    def test_update_status(self):
        bob = self._people[0]
        bob.update_status(gradebook.AliveStatus.Deceased)
        self.assertEqual(gradebook.AliveStatus.Deceased, bob.alive)


class StudentTest(unittest.TestCase):

    def setUp(self) -> None:
        bob = gradebook.Student("Bob", "Smith", "01201970")
        jane = gradebook.Student("Jane", "Doe", "02201984")

        self._students = [
            bob,
            jane
        ]

    def test_instantiation(self):
        bob = self._students[0]
        self.assertTrue(bob.student_id is not None)
        self.assertTrue(isinstance(bob.student_id, str))
        self.assertEqual(bob.student_id[:8], "Student_")


class InstructorTest(unittest.TestCase):

    def setUp(self) -> None:
        self._bob_marley = gradebook.Instructor("Bob", "Marley", "06021945")

    def test_instantiation(self):
        marley = self._bob_marley
        self.assertTrue(marley.instructor_id is not None)
        self.assertTrue(isinstance(marley.instructor_id, str))
        self.assertEqual(marley.instructor_id[:11], "Instructor_")


class PreKStudentTest(unittest.TestCase):

    def test_instantiation(self):
        bob = gradebook.PreKStudent("Bob", "Smith", "01201970")
        self.assertTrue(isinstance(bob, gradebook.Student))

    def test_is_subclass(self):
        self.assertTrue(issubclass(gradebook.PreKStudent, gradebook.Student))


class ZipCodeStudentTest(unittest.TestCase):

    def test_instantiation(self):
        bob = gradebook.ZipCodeStudent("Bob", "Smith", "01201970")
        self.assertTrue(isinstance(bob, gradebook.Student))

    def test_is_subclass(self):
        self.assertTrue(issubclass(gradebook.ZipCodeStudent, gradebook.Student))


class ClassroomTest(unittest.TestCase):

    def setUp(self) -> None:
        self._zc_cohort = gradebook.Classroom()
        rich = gradebook.ZipCodeStudent("Richmond", "Avenal", "1973")
        jen = gradebook.Instructor("Jen", "Barber", "1977")

        self._zc_cohort.students[rich.student_id] = rich
        self._zc_cohort.instructors[jen.instructor_id] = jen

    def get_rich(self) -> gradebook.Student:
        rich_key = next(iter(self._zc_cohort.students.keys()))
        rich = self._zc_cohort.students.get(rich_key)
        return rich

    def get_jen(self) -> gradebook.Instructor:
        jen_key = next(iter(self._zc_cohort.instructors.keys()))
        jen = self._zc_cohort.instructors.get(jen_key)
        return jen

    def test_add_instructor(self):
        yamamoto = gradebook.Instructor("Unknown", "Yamamoto", "1953")
        self._zc_cohort.add_instructor(yamamoto)

        result = yamamoto.instructor_id in self._zc_cohort.instructors
        self.assertTrue(result)

    def test_remove_instructor(self):
        jen = self.get_jen()

        self._zc_cohort.remove_instructor(jen)
        self.assertEqual(len(self._zc_cohort.instructors), 0)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_print_instructors(self, mock_stdout):
        self._zc_cohort.print_instructors()
        jen = self.get_jen()

        expected = f"{jen.instructor_id}: Jen Barber\n"
        actual = mock_stdout.getvalue()

        self.assertEqual(expected, actual)

    def test_add_student(self):
        moss = gradebook.ZipCodeStudent("Maurice", "Moss", "01011972")
        self._zc_cohort.add_student(moss)

        result = moss.student_id in self._zc_cohort.students
        self.assertTrue(result)

    def test_remove_student(self):
        rich = self.get_rich()

        self._zc_cohort.remove_student(rich)
        self.assertEqual(len(self._zc_cohort.students), 0)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_print_students(self, mock_stdout):

        self._zc_cohort.print_students()
        rich = self.get_rich()

        expected = f"{rich.student_id}: Richmond Avenal\n"
        actual = mock_stdout.getvalue()

        self.assertEqual(expected, actual)

'Student_8af83a95-8658-45a4-9f2b-fa8c060acef1: Richmond Avenal\n'
'Student_8af83a95-8658-45a4-9f2b-fa8c060acef1\n'
