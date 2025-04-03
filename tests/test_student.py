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
    # Arrange
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
    assert samara.classes == # may be an expected result var instead; better to have independent # new_classes  # Is it necessary?
    assert len(samara.classes) == class_old_length + 1 # the length is already checked on line 31


def test_get_num_classes():
    # Arrange
    name = "Samara"
    grade = "junior"
    classes = [ "Pre-Calc", "English III", "World History", "Gym", "Chemistry", "Music Composition" ]
    classes_length = len(classes) # => 6

    #Act
    samara = Student(name, grade, classes)
    number_classes = samara.get_num_classes()

    # Assert
    assert number_classes == 6 # classes_length


def test_display_classes():
    # Arrange
    name = "Samara"
    grade = "junior"
    classes = [ "Pre-Calc", "English III", "World History", "Gym", "Chemistry", "Music Composition" ] # assuming the items are valid; 0, 1, and many items are key things to check

    #Act
    samara = Student(name, grade, classes)
    class_display_message = samara.display_classes()

    #Assert
    assert class_display_message == f"Pre-Calc, English III, World History, Gym, Chemistry, Music Composition"


def test_summary():
    # Arrange
    name = "Samara"
    grade = "junior"
    classes = [ "Pre-Calc", "English III", "World History", "Gym", "Chemistry", "Music Composition" ]

    #Act
    samara = Student(name, grade, classes)
    summary_message = samara.summary()
    #Assert
    assert summary_message == f"Samara is a junior enrolled in 6 classes: Pre-Calc, English III, World History, Gym, Chemistry, Music Composition"