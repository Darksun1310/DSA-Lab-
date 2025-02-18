class Node:
    def __init__(self, name, studentid, course, grades, totalstudents, totalgrades, totalgpa):
        self.name = name
        self.studentid = studentid
        self.course = course
        self.grades = grades 
        self.totalstudents = totalstudents
        self.totalgrades = totalgrades
        self.totalgpa = totalgpa
        self.next = None  

    def calculate_gpa(self):
        """Calculates the GPA based on grades (Assuming scale of 100 to 4.0 GPA)."""
        if not self.grades: 
            return 0.0
        average_grade = sum(self.grades) / len(self.grades) 
        
        gpa = (average_grade / 100) * 4.0  
        return round(gpa, 2)  

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, name, studentid, course, grades, totalstudents, totalgrades, totalgpa=None):
        """Appends a new node and auto-calculates GPA from grades."""
        calculated_gpa = (sum(grades) / len(grades) / 3) * 4.0 if grades else 0.0
        new_node = Node(name, studentid, course, grades, totalstudents, totalgrades, round(calculated_gpa, 2))

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        """Prints the linked list data."""
        current_node = self.head
        while current_node:
            print(f"Name: {current_node.name}, Student ID: {current_node.studentid}, Course: {current_node.course}, "
                  f"Grades: {current_node.grades}, Total Students: {current_node.totalstudents}, "
                  f"Total Grades: {current_node.totalgrades}, Calculated GPA: {current_node.calculate_gpa()}")
            current_node = current_node.next


linked_list = LinkedList()

linked_list.append("Mann", 47590, "B.Tech", [96, 89, 96], 60, [89, 98, 99])
linked_list.append("someone in the universe", 47890, "M.Tech", [80, 85, 90], 60, [85, 90, 95])
linked_list.print_list()
