from abc import ABC, abstractmethod


class MedicalEntity(ABC):
    def __init__(self, name, id_number, department):
        self.name = name
        self.id_number = id_number
        self.department = department

    @abstractmethod
    def get_info(self):
        pass


class Staff(ABC):
    def __init__(self, salary, experience, shift):
        self.salary = salary
        self.experience = experience
        self.shift = shift

    @abstractmethod
    def work(self):
        pass



class Doctor(MedicalEntity, Staff): 
    def __init__(self, name, id_number, department, salary, experience, shift, specialization):
        MedicalEntity.__init__(self, name, id_number, department)
        Staff.__init__(self, salary, experience, shift)
        self.specialization = specialization

    def get_info(self): 
        return f"Doctor {self.name}, {self.specialization}"

    def work(self):    
        return f"Doctor {self.name} is treating patients."

    def diagnose(self, patient):
        return f"{self.name} diagnoses {patient}"


class Nurse(MedicalEntity, Staff):
    def __init__(self, name, id_number, department, salary, experience, shift, level):
        super().__init__(name, id_number, department)  
        Staff.__init__(self, salary, experience, shift)
        self.level = level

    def get_info(self):
        return f"Nurse {self.name}, Level {self.level}"

    def work(self):
        return f"Nurse {self.name} is assisting."

    def assist(self, doctor):
        return f"{self.name} assists Dr. {doctor}"


class Patient(MedicalEntity):
    def __init__(self, name, id_number, department, illness, age, room):
        super().__init__(name, id_number, department)
        self.illness = illness
        self.age = age
        self.room = room

    def get_info(self):
        return f"Patient {self.name}, Illness: {self.illness}"

    def request_help(self):
        return f"{self.name} is requesting help."


class Surgeon(Doctor):  
    def __init__(self, name, id_number, department, salary, experience, shift, specialization, operations_done):
        super().__init__(name, id_number, department, salary, experience, shift, specialization)
        self.operations_done = operations_done

    def perform_surgery(self):
        return f"Surgeon {self.name} performs surgery."

    def get_info(self):
        return f"Surgeon {self.name}, Ops done: {self.operations_done}"


class Pharmacist(MedicalEntity, Staff):
    def __init__(self, name, id_number, department, salary, experience, shift, certificate):
        MedicalEntity.__init__(self, name, id_number, department)
        Staff.__init__(self, salary, experience, shift)
        self.certificate = certificate

    def get_info(self):
        return f"Pharmacist {self.name}, Certificate: {self.certificate}"

    def work(self):
        return f"{self.name} is preparing medicine."

    def give_medicine(self, patient):
        return f"{self.name} gives medicine to {patient}"


class Receptionist(Staff):
    def __init__(self, salary, experience, shift, desk_number, language, building):
        super().__init__(salary, experience, shift)
        self.desk_number = desk_number
        self.language = language
        self.building = building

    def work(self):
        return f"Receptionist at desk {self.desk_number} is checking in patients."

    def greet(self, name):
        return f"Welcome, {name}!"


doctor = Doctor("Alice", 1, "Cardiology", 5000, 10, "Day", "Therapist")
nurse = Nurse("Bob", 2, "Surgery", 3000, 5, "Night", "Senior")
surgeon = Surgeon("Clara", 3, "Surgery", 8000, 12, "Day", "General Surgery", 300)

print(doctor.get_info())
print(nurse.get_info())
print(surgeon.get_info())
print(doctor.work())
print(nurse.assist("Alice"))
print(surgeon.perform_surgery())
