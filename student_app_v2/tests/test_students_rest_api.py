import pytest
import requests
from app import db

@pytest.fixture
def base_url():
    return "http://127.0.0.1:5000/students"

@pytest.fixture(autouse=True)
def clear_students():
    db._clear_db()

@pytest.fixture()
def add_students(base_url):
    students = [
        {'age': 21, "name": "Aaa"},
        {'age': 22, "name": "Bbb"},
        {'age': 23, "name": "Ccc"},
    ]
    created_students = []
    for student in students:
        res = requests.post(base_url, json=student)
        created_students.append(res.json())
    return created_students



# THE TESTS ========================


def test_get_all_students(base_url, add_students):
    res = requests.get(base_url)
    assert res.status_code == 200
    assert res.reason == "OK"
    assert res.json() == add_students



@pytest.mark.parametrize(
    "s_id, index",
    [
      [1, 0],
      [2, 1],
      [3, 2],
    ],
    ids=["first student", "second student", "third student"]
)
def test_get_one_student_v2(base_url, add_students, s_id, index):
    res = requests.get(f"{base_url}/{s_id}")
    assert res.status_code == 200
    assert res.reason == "OK"
    assert res.json() == add_students[index]

@pytest.mark.parametrize(
    "s_id",
    [100, 200, 300]
)
def test_get_one_student_negative(base_url, add_students, s_id):
    res = requests.get(f"{base_url}/{s_id}")
    assert res.status_code == 404
    assert res.reason == "NOT FOUND"
    assert res.json() == {'message': f'student not found: {s_id}'}


@pytest.mark.parametrize(
    "student",
    [
        {"name": "AA", "age": 18},
        {"name": "Benny", "age": 25},
        {"name": "Robinson", "age": 120},
    ],
    ids = [
        "minimum value input",
        "average input",
        "high value input"
    ]
)
def test_add_student(base_url, student):
    res = requests.post(base_url, json=student)
    assert res.status_code == 201
    #נבדוק את הערכים של התלמיד שהוספנו ונשווה
    created_student = res.json()
    assert created_student.get("name") == student["name"]
    assert created_student.get("age") == student["age"]
    assert "id" in created_student



@pytest.mark.parametrize(
    "student",
    [
        {"name": "AA", "age": 17},
        {"name": "Benny", "age": 121},
        {"name": "A", "age": 25},
        {"name": "", "age": 25}
        ],
    ids = [
        "too young",
        "too old",
        "name too short",
        "no name",
    ],
)
def test_add_student_negative(base_url, student):
    res = requests.post(base_url, json=student)
    assert res.status_code == 400
    assert res.reason == "BAD REQUEST"


@pytest.mark.parametrize(
    "name, age, expected_status",
    [
    pytest.param("Danny", 25, 201, id="positive_average input"),
    pytest.param("Aa", 18, 201, id="positive_low value input"),
    pytest.param("", 18, 400, id="negative_no name"),
    pytest.param("Ann", 121, 400, id="negative_too old"),
    ]
)
def test_add_student_mixed(base_url, name, age, expected_status):
    payload = {"name":name, "age": age}
    res = requests.post(base_url, json=payload)
    assert res.status_code == expected_status
