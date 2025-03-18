class Node:
    def __init__(self, name, studentid, course, grades, totalstudents, totalgrades, ):
        self.name = name
        self.studentid = studentid
        self.course = course
        self.grades = grades 
        self.totalstudents = totalstudents
        self.totalgrades = totalgrades
      
        self.next = None  

    
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, name, studentid, course, grades, totalstudents, totalgrades, totalgpa=None):
     
        new_node = Node(name, studentid, course, grades, totalstudents, totalgrades, )

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
                  f"Total Grades: {current_node.totalgrades}")
            current_node = current_node.next


linked_list = LinkedList()

linked_list.append("Mann", 47590, "B.Tech", [96, 89, 96], 60, [89, 98, 99])
linked_list.append("someone in the universe", 47890, "M.Tech", [80, 85, 90], 60, [85, 90, 95])
linked_list.print_list()
linked_list.append("Mann", 47590, "B.Tech", [96, 89, 96], 60, [89, 98, 99])
linked_list.append("someone in the universe", 47890, "M.Tech", [80, 85, 90], 60, [85, 90, 95])
linked_list.print_list()
