'''Here UserData is the Parent Class that has information of the users.
The NutritionLog is a child Class that inherits attributes from the Parent Class. It has it's own attribute to store nutritional data.
Similarly, The Exerciselog is a child Class that inherits attributes from the Parent Class. It has it's own attribute to store exercise data.
The Wellness Dashboard Class uses multiple inheritence to inherit data from both Nutritionlog and Exerciselog.
''' 



class UserData:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class NutritionalLog(UserData):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.nutrition_data = []
    def add_nutrition_entry(self, entry):
        self.nutrition_data.append(entry)

class ExerciseLog(UserData):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.exercise_data = []
    def add_exercise_entry(self, entry):
        self.exercise_data.append(entry)

class ExercisePlan(UserData):
    def __init__(self, name, age, gender, goal):
        super().__init__(name, age, gender)
        self.goal = goal

class WellnessDashboard(NutritionalLog, ExerciseLog):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.wellness_score = 0

    def calculate_wellness_score(self):        
        self.wellness_score = len(self.nutrition_data) + len(self.exercise_data)

user1 = WellnessDashboard("Anurag", 23, "Male")
user2 = NutritionalLog("Raghav", 30, "Male")

user1.add_nutrition_entry("Healthy breakfast")
user1.add_exercise_entry("30-min jog")

user2.add_nutrition_entry("Salad for lunch")

user1.calculate_wellness_score()

print(f"{user1.name}'s Wellness Score: {user1.wellness_score}")
print(f"{user2.name}'s Nutrition Log: {user2.nutrition_data}")
