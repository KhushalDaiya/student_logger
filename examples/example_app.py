from student_logger import get_logger

logger = get_logger("student_app")

_students = {}

def add_student(student_id: int, name: str):
    if student_id in _students:
        logger.warning(f"Student ID {student_id} already exists")
        return False
    _students[student_id] = name
    logger.info(f"Student {name} added successfully")
    return True

def find_student(student_id: int):
    name = _students.get(student_id)
    if not name:
        logger.warning(f"Student ID {student_id} not found")
        return None
    logger.info(f"Student found: {name}")
    return name

def invalid_operation():
    logger.error("Invalid input detected")
    raise ValueError("invalid input")

if __name__ == "__main__":
    add_student(101, "John")
    find_student(105)
    try:
        invalid_operation()
    except Exception:
        pass
