from unittest import TestCase
from unittest.mock import patch, Mock
from app import service
from app.service import ServiceError


class TestService(TestCase):

   @patch("app.service.db.get_student")
   def test_get_student_positive(self, mock_get_student:    Mock):
  # AAA

  # Arrange - set up the mock object
    mock_get_student.return_value = {'id': 1, 'name': 'Mock Student'}
  # Act - use the mock
    result = service.get_student(1)
  # Assert
    self.assertEqual({'id': 1, 'name': 'Mock Student'}, result)
  # validation - make sure we actually used the mock
    mock_get_student.assert_called_with(1)


   @patch("app.service.db.get_student")
   def test_get_student_negative(self, mock_get_student: Mock):
       mock_get_student.side_effect = KeyError("not found: 1")
       self.assertRaises(KeyError, service.get_student, 111)
       mock_get_student.assert_called_with(111)


   @patch("app.service.db.add_student")
   def test_add_student_positive(self, mock_add_student: Mock):
       # arrange
       mock_add_student.return_value = {'name': 'Mock Student', 'age': 25, 'id': 101}

       # create students with age cases
       students = [
           {'name': 'Mock Student', 'age': 18, 'id': 101},
           {'name': 'Mock Student', 'age': 30, 'id': 101},
           {'name': 'Mock Student', 'age': 120, 'id': 101}]

       for student in students:
           # act
           result = service.add_student(student)
           # assert
           self.assertEqual({'name': 'Mock Student', 'age': 25, 'id': 101}, result)

       # validate
       self.assertEqual(3, mock_add_student.call_count)


   @patch("app.service.db.add_student")
   def test_add_student_too_young(self, mock_add_student: Mock):
       mock_add_student.side_effect = ServiceError("add student failed")
       self.assertRaises(ServiceError, service.add_student, {'name': 'Mock Student', 'age': 11, 'id': 101})
       mock_add_student.assert_not_called()



   @patch("app.service.db.update_student")
   def test_update_student_age_too_young(self, mock_update_student: Mock):
       # Arrange
       student = {"name": "Alice", "age": 17}
       # Act
       with self.assertRaises(ServiceError):
           service.update_student(student)
       # Validation
       mock_update_student.assert_not_called()

   # age

   @patch("app.service.db.update_student")
   def test_update_student_age_too_old(self, mock_update_student: Mock):
           # Arrange
           student = {"name": "Alice", "age": 121}
           # Act
           with self.assertRaises(ServiceError):
               service.update_student(student)
           # Validation
           mock_update_student.assert_not_called()


   @patch("app.service.db.update_student")
   def test_update_student_minimum_age(self, mock_update_student: Mock):
       # Arrange
        student = {"name": "Alice", "age": 18}
        mock_update_student.return_value = student
       # Act
        result = service.update_student(student)
       # Assert
        self.assertEqual(student, result)
       # Validation
        mock_update_student.assert_called_with(student)



   # name

   @patch("app.service.db.update_student")
   def test_update_student_positive(self, mock_update_student: Mock):
       # Arrange
       student = {"name": "Alice", "age": 25}
       mock_update_student.return_value = student
       # Act
       result = service.update_student(student)
       # Assert
       self.assertEqual(student, result)
       # Validation
       mock_update_student.assert_called_with(student)