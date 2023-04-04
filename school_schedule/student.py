class Student:
    """
    attributes: 
    - name: str
    - grade: str
    - classes: list
    methods:
    - add_class, param: STR
    - get_num_classes
    - summary
    """
    
    def __init__(self, name, grade, classes):
        self.name = name
        self.grade = grade
        self.classes = classes

    def add_class(self, new_class):
        self.classes.append(new_class)
        return self.classes

    def get_num_classes(self):
        return len(self.classes)
    
    def summary(self):
        pass
    
    def display_each_class(self):
        pass

# Extra:
# - create a function that will return the student with more classes
# - create a test for that function

    def student_with_most_classes(self, students):
        most_classes = 0
        for student in students:
            if student.get_num_classes() > most_classes:
                most_classes = student