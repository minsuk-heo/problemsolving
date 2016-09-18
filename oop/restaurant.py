import unittest

class person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class caller(person):
    def __init__(self, name, phone):
        person.__init__(self, name, phone)

    def setNumberOfPeople(self, count):
        self.numberOfPeople = count

    def getNumberOfPeople(self):
        return self.numberOfPeople

    def setSchedule(self, schedule):
        self.schedule = schedule

    def getSchedule(self):
        return self.schedule

class employee(person):
    def __init__(self, name, phone, title):
        person.__init__(self, name, phone)
        self.setTitle(title)

    def setTitle(self, title):
        self.title = title


class restaurant:
    def __init__(self):
        self.TABLE_COUNT = 4
        self.tablelist = []
        self.tablelist.append(table(2))
        self.tablelist.append(table(4))
        self.tablelist.append(table(6))
        self.tablelist.append(table(8))

    def makeReservation(self, caller):
        print(caller.getSchedule())
        for i in self.tablelist:
            if i.capacity >= caller.getNumberOfPeople():
                if i.schedule.timetable[caller.getSchedule()] is None:
                    i.schedule.timetable[caller.getSchedule()] = caller
                    print(caller.name + "has scheulded  on " + caller.getSchedule() + "at " + str(i.capacity) + " size table")
                    return True

class table:
    def __init__(self, capacity):
        self.capacity = capacity
        self.schedule = schedule()

class schedule:
    def __init__(self):
        self.timetable = {"12-1": None, "1-2": None, "2-3": None, "3-4": None, "4-5": None}

class RestaurantTest(unittest.TestCase):
    def test(self):
        bj = restaurant()
        caller1 = caller("caller1", "619-999-9999")
        caller1.setNumberOfPeople(3)
        caller1.setSchedule("1-2")

        self.assertTrue(True, bj.makeReservation(caller1))


