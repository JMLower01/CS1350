class Workout:
    def __init__(self, name, duration_minutes, date):
        self.name = name
        self._duration_minutes = 0
        self.duration_minutes = duration_minutes # Use setter
        self.date = date
    @property
    def duration_minutes(self):
        return self._duration_minutes

    @duration_minutes.setter
    def duration_minutes(self, value):
        if value > 0:
            self._duration_minutes = value
        else:
            print("Error: set value must be greater than 0")
    
    def calories_burned(self):
        return 0

    def __str__(self):
        return f"{self.name} - {self._duration_minutes} min on {self.date} ({self.calories_burned():.0f} cal) "
class CardioWorkout(Workout):
    def __init__(self, name, duration_minutes, date, avg_heart_rate):
       super().__init__(name, duration_minutes, date) 
       self.avg_heart_rate = avg_heart_rate
    def calories_burned(self):
        return self._duration_minutes * (self.avg_heart_rate / 100) * 5
    @property
    def intensity(self):
        if self.avg_heart_rate >= 150:
            return "High"
        elif self.avg_heart_rate >= 120:
            return "Medium"
        else:
            return "Low"
class StrengthWorkout(Workout):
    def __init__(self, name, duration_minutes, date, sets, reps_per_set, weight_lbs):
        super().__init__(name, duration_minutes, date)
        self.sets = sets
        self.reps_per_set = reps_per_set
        self.weight_lbs = weight_lbs
    def calories_burned(self):
        return self.sets * self.reps_per_set * (self.weight_lbs / 100) * 3
    @property
    def total_volume(self):
        return self.sets * self.reps_per_set * self.weight_lbs
class WeeklyLog:
    def __init__(self, week_label):
        self.week_label = week_label
        self.private_workouts = []
    def add_workout(self, workout):
        self.private_workouts.append(workout)
    @property
    def total_minutes(self):
        sum = 0
        for workout in self.private_workouts:
            sum += workout.duration_minutes
        return sum
    @property
    def total_calories(self):
        calories = 0
        for workout in self.private_workouts:
            calories += workout.calories_burned()
        return calories
    def summary(self):
    # TODO: Print week label, each workout, and totals
        print(f"--- {self.week_label} ---")
        for workout in self.private_workouts:
            print(f"  {workout.__str__()}")
        print(f"Totals: {self.total_minutes} min, {self.total_calories:.0f} cal")
    def hardest_workout(self):
        highest = 0
        hardest = 0
        if self.private_workouts:
            for workout in self.private_workouts:
                if workout.calories_burned() > highest:
                    highest = workout.calories_burned()
                    hardest = workout
            return hardest
        else:
            return None
            
        
# Test your code
if __name__ == "__main__":
    log = WeeklyLog("Week 7")
    run = CardioWorkout("Morning Run", 30, "2026-02-23", 155)
    lift = StrengthWorkout("Bench Press", 45, "2026-02-24", 4, 10, 135)
    bike = CardioWorkout("Cycling", 60, "2026-02-25", 130)
    log.add_workout(run)
    log.add_workout(lift)
    log.add_workout(bike)
    log.summary()
    print(f"\nRun intensity: {run.intensity}")
    print(f"Bench press volume: {lift.total_volume} lbs")
    hardest = log.hardest_workout()
    print(f"Hardest workout: {hardest.name} ({hardest.calories_burned():.0f} cal)")
#Expected Output
#--- Week 7 ---
#Morning Run - 30min on 2026-02-23 (232 cal)
#Bench Press - 45min on 2026-02-24 (162 cal)
#Cycling - 60min on 2026-02-25 (390 cal)
#Totals: 135 min, 784 cal
#Run intensity: High
#Bench press volume: 5400 lbs
#Hardest workout: Cycling (390 cal)