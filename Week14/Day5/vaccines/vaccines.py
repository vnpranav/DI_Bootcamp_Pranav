class Human:
    def __init__(self):
        self.family = []

    def add_family_member(self, person):
        self.family.append(person)
        person.family = self.family
        

class Queue:
    def __init__(self, patients=[]):
        self.__humans = [*patients]

    def add_person(self, person):
        if person.age > 60 or person.priority:
            self.__humans.insert(0, person)
        else:
            self.__humans.append(person)

    def find_in_queue(self, person):
        if person in self.__humans:
            return self.__humans.index(person)
        else:
            return None
        
    def swap(self, person1, person2):
        index1 = self.find_in_queue(person1)
        index2 = self.find_in_queue(person2)

        if index1 != -1 and index2 != -1:
            self.__humans[index1], self.__humans[index2] = self.__humans[index2], self.__humans[index1]
        else:
            print("One of the persons was not found")

    def get_next(self):
        if len(self.__humans) > 0:
            return self.__humans[0]
        else:
            return None
        
    def get_next_blood_type(self, blood_type):
        for person in self.__humans:
            if person.blood_type == blood_type:
                return person
        return None
    
    def sort_by_age(self):
        # self.__humans.sort(key=lambda x: (-x.priority, -x.age))
        pass

    def rearrange_queue(self):
        pass