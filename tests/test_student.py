from school_schedule.student import Student

def test_returns_attributes():
    # Arrange
    name = "Samara"
    grade = "junior"
    classes = [ "Pre-Calc", "English III", "World History", "Gym", "Chemistry", "Music Composition" ]
    
    #Act
    samara = Student(name, grade, classes)

    #Assert
    assert samara.name == "Samara"
    assert samara.grade == "junior"
    assert samara.classes == [ "Pre-Calc", "English III", "World History", "Gym", "Chemistry", "Music Composition" ]


def test_add_class():
    name = "Samara"
    grade = "junior"
    classes = [ "Pre-Calc", "English III", "World History", "Gym", "Chemistry", "Music Composition" ]
    new_class = "Physics"
    class_old_length = len(classes)

    #Act
    samara = Student(name, grade, classes)
    new_classes = samara.add_class(new_class)

    #Assert
    assert new_classes == [ "Pre-Calc", "English III", "World History", "Gym", "Chemistry", "Music Composition","Physics"]
    assert samara.classes == new_classes # Is it necessary?
    assert len(samara.classes) == class_old_length + 1

def test_get_num_classes():
    
    pass


def test_display_classes():
    pass


def test_summary():
    pass