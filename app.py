from flask import Flask, render_template, request, redirect, url_for
from urllib.parse import quote
from datetime import datetime

app = Flask(__name__)

# Health metrics calculations
def calculate_metrics(data):
    height_m = data['height'] / 100
    bmi = data['weight'] / (height_m * height_m)
    
    # BMI Category
    if bmi < 18.5:
        bmi_category = "Underweight"
        bmi_color = "#3b82f6"
    elif bmi < 25:
        bmi_category = "Normal"
        bmi_color = "#10b981"
    elif bmi < 30:
        bmi_category = "Overweight"
        bmi_color = "#f59e0b"
    else:
        bmi_category = "Obese"
        bmi_color = "#ef4444"
    
    # BMR Calculation (Mifflin-St Jeor)
    if data['gender'] == 'male':
        bmr = 10 * data['weight'] + 6.25 * data['height'] - 5 * data['age'] + 5
    else:
        bmr = 10 * data['weight'] + 6.25 * data['height'] - 5 * data['age'] - 161
    
    # Activity multipliers
    activity_multipliers = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'extremely': 1.9
    }
    
    tdee = bmr * activity_multipliers[data['activity_level']]
    
    # Calorie targets based on goal
    if data['fitness_goal'] == 'weight_loss':
        calorie_target = tdee - 500
        weight_change_msg = "Lose ~0.5 kg/week"
    elif data['fitness_goal'] == 'muscle_gain':
        calorie_target = tdee + 300
        weight_change_msg = "Gain ~0.25 kg/week"
    else:
        calorie_target = tdee
        weight_change_msg = "Maintain weight"
    
    return {
        'bmi': round(bmi, 1),
        'bmi_category': bmi_category,
        'bmi_color': bmi_color,
        'bmr': round(bmr),
        'tdee': round(tdee),
        'calorie_target': round(calorie_target),
        'weight_change_msg': weight_change_msg
    }

# Workout Plans
workout_plans = {
    'weight_loss': {
        'title': 'Weight Loss Program',
        'days': [
            {'name': 'Day 1 - Full Body HIIT', 'focus': 'High Intensity Interval Training for max calorie burn', 
             'exercises': [
                 {'name': 'Jumping Jacks', 'sets': '4 sets', 'reps': '45 seconds'},
                 {'name': 'Burpees', 'sets': '4 sets', 'reps': '12 reps'},
                 {'name': 'Mountain Climbers', 'sets': '4 sets', 'reps': '45 seconds'},
                 {'name': 'High Knees', 'sets': '4 sets', 'reps': '45 seconds'},
                 {'name': 'Squat Jumps', 'sets': '3 sets', 'reps': '15 reps'},
                 {'name': 'Plank Hold', 'sets': '3 sets', 'reps': '45 seconds'}
             ]},
            {'name': 'Day 2 - Lower Body + Cardio', 'focus': 'Lower body strength with cardio bursts',
             'exercises': [
                 {'name': 'Bodyweight Squats', 'sets': '4 sets', 'reps': '20 reps'},
                 {'name': 'Lunges', 'sets': '3 sets', 'reps': '12 reps/leg'},
                 {'name': 'Jump Squats', 'sets': '3 sets', 'reps': '15 reps'},
                 {'name': 'Glute Bridges', 'sets': '3 sets', 'reps': '15 reps'},
                 {'name': 'Running in Place', 'sets': '3 sets', 'reps': '30 seconds'},
                 {'name': 'Calf Raises', 'sets': '3 sets', 'reps': '20 reps'}
             ]},
            {'name': 'Day 3 - Active Recovery & Core', 'focus': 'Core strengthening and mobility',
             'exercises': [
                 {'name': 'Plank', 'sets': '3 sets', 'reps': '60 seconds'},
                 {'name': 'Bicycle Crunches', 'sets': '3 sets', 'reps': '20 reps'},
                 {'name': 'Leg Raises', 'sets': '3 sets', 'reps': '12 reps'},
                 {'name': 'Russian Twists', 'sets': '3 sets', 'reps': '20 reps'},
                 {'name': 'Dead Bug', 'sets': '3 sets', 'reps': '10 reps'},
                 {'name': 'Bird Dog', 'sets': '3 sets', 'reps': '10 reps/side'}
             ]},
            {'name': 'Day 4 - Upper Body + HIIT', 'focus': 'Upper body with cardio for overall toning',
             'exercises': [
                 {'name': 'Push-ups', 'sets': '4 sets', 'reps': '12 reps'},
                 {'name': 'Tricep Dips', 'sets': '3 sets', 'reps': '12 reps'},
                 {'name': 'Plank Shoulder Taps', 'sets': '3 sets', 'reps': '20 taps'},
                 {'name': 'Arm Circles', 'sets': '3 sets', 'reps': '30 seconds'},
                 {'name': 'Bear Crawl', 'sets': '3 sets', 'reps': '30 seconds'},
                 {'name': 'Sprint Intervals', 'sets': '3 sets', 'reps': '30 seconds'}
             ]},
            {'name': 'Day 5 - Full Body Circuit', 'focus': 'Complete circuit training for full body conditioning',
             'exercises': [
                 {'name': 'Burpees', 'sets': '3 sets', 'reps': '10 reps'},
                 {'name': 'Mountain Climbers', 'sets': '3 sets', 'reps': '45 seconds'},
                 {'name': 'Plank Hold', 'sets': '3 sets', 'reps': '45 seconds'},
                 {'name': 'Reverse Lunges', 'sets': '3 sets', 'reps': '12 reps/leg'},
                 {'name': 'Superman Hold', 'sets': '3 sets', 'reps': '30 seconds'},
                 {'name': 'High Knee Run', 'sets': '3 sets', 'reps': '30 seconds'}
             ]}
        ]
    },
    'muscle_gain': {
        'title': 'Muscle Building Program',
        'days': [
            {'name': 'Day 1 - Push Day', 'focus': 'Upper body pushing movements',
             'exercises': [
                 {'name': 'Push-ups', 'sets': '4 sets', 'reps': '10-15 reps'},
                 {'name': 'Diamond Push-ups', 'sets': '3 sets', 'reps': '8-12 reps'},
                 {'name': 'Pike Push-ups', 'sets': '3 sets', 'reps': '8-12 reps'},
                 {'name': 'Tricep Dips', 'sets': '3 sets', 'reps': '12-15 reps'},
                 {'name': 'Decline Push-ups', 'sets': '3 sets', 'reps': '10-12 reps'},
                 {'name': 'Wall Push-ups', 'sets': '3 sets', 'reps': '10 reps'}
             ]},
            {'name': 'Day 2 - Pull Day', 'focus': 'Upper body pulling movements',
             'exercises': [
                 {'name': 'Superman Hold', 'sets': '4 sets', 'reps': '30 seconds'},
                 {'name': 'Bicep Curls', 'sets': '3 sets', 'reps': '12 reps'},
                 {'name': 'Arm Circles', 'sets': '3 sets', 'reps': '30 seconds'},
                 {'name': 'Plank Hold', 'sets': '3 sets', 'reps': '45 seconds'}
             ]},
            {'name': 'Day 3 - Leg Day', 'focus': 'Lower body strength training',
             'exercises': [
                 {'name': 'Squats', 'sets': '4 sets', 'reps': '12-15 reps'},
                 {'name': 'Lunges', 'sets': '4 sets', 'reps': '10 reps/leg'},
                 {'name': 'Glute Bridges', 'sets': '3 sets', 'reps': '15 reps'},
                 {'name': 'Calf Raises', 'sets': '4 sets', 'reps': '20 reps'},
                 {'name': 'Deadlifts', 'sets': '3 sets', 'reps': '12 reps'}
             ]},
            {'name': 'Day 4 - Push Day + Core', 'focus': 'Secondary push workout with core emphasis',
             'exercises': [
                 {'name': 'Push-ups', 'sets': '4 sets', 'reps': '12 reps'},
                 {'name': 'Tricep Dips', 'sets': '3 sets', 'reps': '12 reps'},
                 {'name': 'Plank Shoulder Taps', 'sets': '3 sets', 'reps': '20 taps'},
                 {'name': 'Side Plank', 'sets': '3 sets', 'reps': '20 seconds/side'}
             ]},
            {'name': 'Day 5 - Pull Day + Core', 'focus': 'Secondary pull workout with core emphasis',
             'exercises': [
                 {'name': 'Superman Hold', 'sets': '4 sets', 'reps': '30 seconds'},
                 {'name': 'Bicep Curls', 'sets': '3 sets', 'reps': '12 reps'},
                 {'name': 'Bird Dog', 'sets': '3 sets', 'reps': '10 reps/side'},
                 {'name': 'Dead Bug', 'sets': '3 sets', 'reps': '10 reps'},
                 {'name': 'Wall Sit', 'sets': '3 sets', 'reps': '45 seconds'}
             ]}
        ]
    },
    'endurance': {
        'title': 'Endurance Building Program',
        'days': [
            {'name': 'Day 1 - Cardio Base', 'focus': 'Building cardiovascular base',
             'exercises': [
                 {'name': 'Jumping Jacks', 'sets': '5 sets', 'reps': '60 seconds'},
                 {'name': 'High Knees', 'sets': '5 sets', 'reps': '45 seconds'},
                 {'name': 'Butt Kicks', 'sets': '5 sets', 'reps': '45 seconds'},
                 {'name': 'March in Place', 'sets': '3 sets', 'reps': '60 seconds'},
                 {'name': 'Box Step-ups', 'sets': '3 sets', 'reps': '20 reps'}
             ]},
            {'name': 'Day 2 - Steady State Cardio', 'focus': 'Sustained cardio efforts',
             'exercises': [
                 {'name': 'Running in Place', 'sets': '3 sets', 'reps': '3 minutes'},
                 {'name': 'Steady State Cardio', 'sets': '1 set', 'reps': '15 minutes'},
                 {'name': 'Tempo Walk', 'sets': '1 set', 'reps': '10 minutes'}
             ]},
            {'name': 'Day 3 - Active Recovery', 'focus': 'Low intensity active recovery',
             'exercises': [
                 {'name': 'Gentle Stretching', 'sets': '1 set', 'reps': '15 minutes'},
                 {'name': 'Yoga Flow', 'sets': '1 set', 'reps': '10 minutes'},
                 {'name': 'Mobility Work', 'sets': '1 set', 'reps': '10 minutes'},
                 {'name': 'Light Walking', 'sets': '1 set', 'reps': '20 minutes'}
             ]},
            {'name': 'Day 4 - Interval Training', 'focus': 'HIIT for endurance',
             'exercises': [
                 {'name': 'Sprint Intervals', 'sets': '6 sets', 'reps': '30 seconds'},
                 {'name': 'Burpees', 'sets': '4 sets', 'reps': '30 seconds'},
                 {'name': 'Mountain Climbers', 'sets': '4 sets', 'reps': '45 seconds'}
             ]},
            {'name': 'Day 5 - Long Cardio Session', 'focus': 'Extended cardio session',
             'exercises': [
                 {'name': 'Easy Jog', 'sets': '1 set', 'reps': '15 minutes'},
                 {'name': 'Cool Down Walk', 'sets': '1 set', 'reps': '10 minutes'},
                 {'name': 'Stretching Routine', 'sets': '1 set', 'reps': '10 minutes'},
                 {'name': 'Meditation', 'sets': '1 set', 'reps': '5 minutes'}
             ]}
        ]
    },
    'flexibility': {
        'title': 'Flexibility & Mobility Program',
        'days': [
            {'name': 'Day 1 - Morning Mobility', 'focus': 'Dynamic stretching routine',
             'exercises': [
                 {'name': 'Arm Circles', 'sets': '3 sets', 'reps': '15 each direction'},
                 {'name': 'Gentle Stretching', 'sets': '3 sets', 'reps': '30 seconds'},
                 {'name': 'Mobility Work', 'sets': '1 set', 'reps': '10 minutes'}
             ]},
            {'name': 'Day 2 - Lower Body Flexibility', 'focus': 'Lower body stretching',
             'exercises': [
                 {'name': 'Gentle Stretching', 'sets': '3 sets', 'reps': '30 seconds'},
                 {'name': 'Lunges', 'sets': '3 sets', 'reps': '10 reps/leg'},
                 {'name': 'Mobility Work', 'sets': '1 set', 'reps': '15 minutes'}
             ]},
            {'name': 'Day 3 - Active Recovery', 'focus': 'Light movement and stretching',
             'exercises': [
                 {'name': 'Easy Jog', 'sets': '1 set', 'reps': '10 minutes'},
                 {'name': 'Yoga Flow', 'sets': '1 set', 'reps': '15 minutes'},
                 {'name': 'Sun Salutation', 'sets': '3 rounds', 'reps': '5 minutes'}
             ]},
            {'name': 'Day 4 - Upper Body Flexibility', 'focus': 'Upper body and spine mobility',
             'exercises': [
                 {'name': 'Arm Circles', 'sets': '3 sets', 'reps': '30 seconds'},
                 {'name': 'Mobility Work', 'sets': '1 set', 'reps': '15 minutes'},
                 {'name': 'Gentle Stretching', 'sets': '3 sets', 'reps': '30 seconds'}
             ]},
            {'name': 'Day 5 - Full Body Flow', 'focus': 'Complete stretching routine',
             'exercises': [
                 {'name': 'Sun Salutation', 'sets': '5 rounds', 'reps': '10 minutes'},
                 {'name': 'Deep Breathing', 'sets': '1 set', 'reps': '5 minutes'},
                 {'name': 'Meditation', 'sets': '1 set', 'reps': '10 minutes'}
             ]}
        ]
    },
    'general': {
        'title': 'General Fitness Program',
        'days': [
            {'name': 'Day 1 - Full Body A', 'focus': 'Balanced full body workout',
             'exercises': [
                 {'name': 'Squats', 'sets': '3 sets', 'reps': '15 reps'},
                 {'name': 'Push-ups', 'sets': '3 sets', 'reps': '10 reps'},
                 {'name': 'Lunges', 'sets': '3 sets', 'reps': '10 reps/leg'},
                 {'name': 'Plank Hold', 'sets': '3 sets', 'reps': '45 seconds'},
                 {'name': 'Glute Bridges', 'sets': '3 sets', 'reps': '15 reps'}
             ]},
            {'name': 'Day 2 - Cardio & Core', 'focus': 'Cardio with core focus',
             'exercises': [
                 {'name': 'Jumping Jacks', 'sets': '3 sets', 'reps': '45 seconds'},
                 {'name': 'Mountain Climbers', 'sets': '3 sets', 'reps': '45 seconds'},
                 {'name': 'Bicycle Crunches', 'sets': '3 sets', 'reps': '20 reps'},
                 {'name': 'Leg Raises', 'sets': '3 sets', 'reps': '12 reps'},
                 {'name': 'Plank Hold', 'sets': '3 sets', 'reps': '45 seconds'}
             ]},
            {'name': 'Day 3 - Active Recovery', 'focus': 'Light activity and stretching',
             'exercises': [
                 {'name': 'Easy Jog', 'sets': '1 set', 'reps': '20 minutes'},
                 {'name': 'Stretching Routine', 'sets': '1 set', 'reps': '15 minutes'},
                 {'name': 'Mobility Work', 'sets': '1 set', 'reps': '10 minutes'}
             ]},
            {'name': 'Day 4 - Upper Body Focus', 'focus': 'Upper body strength',
             'exercises': [
                 {'name': 'Push-ups', 'sets': '4 sets', 'reps': '10-12 reps'},
                 {'name': 'Tricep Dips', 'sets': '3 sets', 'reps': '12 reps'},
                 {'name': 'Plank Shoulder Taps', 'sets': '3 sets', 'reps': '20 taps'},
                 {'name': 'Arm Circles', 'sets': '3 sets', 'reps': '30 seconds'}
             ]},
            {'name': 'Day 5 - Lower Body Focus', 'focus': 'Lower body strength',
             'exercises': [
                 {'name': 'Squats', 'sets': '4 sets', 'reps': '15 reps'},
                 {'name': 'Lunges', 'sets': '3 sets', 'reps': '10 reps/leg'},
                 {'name': 'Glute Bridges', 'sets': '3 sets', 'reps': '15 reps'},
                 {'name': 'Calf Raises', 'sets': '4 sets', 'reps': '20 reps'},
                 {'name': 'Wall Sit', 'sets': '3 sets', 'reps': '45 seconds'}
             ]}
        ]
    }
}

# Indian Meal Plans with Macros (protein, carbs, fats in grams)
indian_meal_plans = {
    'non_veg': {
        'name': 'Indian Non-Vegetarian Plan',
        'days': [
            {'name': 'Day 1', 'meals': [
                {'name': 'Poha (Rice Flakes)', 'calories': 280, 'protein': 5, 'carbs': 52, 'fats': 4, 'allergens': []},
                {'name': 'Dal Tadka with Rice', 'calories': 450, 'protein': 18, 'carbs': 65, 'fats': 12, 'allergens': []},
                {'name': 'Roasted Chana', 'calories': 120, 'protein': 6, 'carbs': 18, 'fats': 3, 'allergens': []},
                {'name': 'Chicken Curry with Roti', 'calories': 480, 'protein': 32, 'carbs': 45, 'fats': 18, 'allergens': []}
            ], 'total': 1330},
            {'name': 'Day 2', 'meals': [
                {'name': 'Upma with Vegetables', 'calories': 260, 'protein': 8, 'carbs': 42, 'fats': 6, 'allergens': []},
                {'name': 'Vegetable Khichdi', 'calories': 400, 'protein': 14, 'carbs': 60, 'fats': 10, 'allergens': []},
                {'name': 'Banana', 'calories': 90, 'protein': 1, 'carbs': 23, 'fats': 0, 'allergens': []},
                {'name': 'Fish Curry with Rice', 'calories': 420, 'protein': 28, 'carbs': 50, 'fats': 12, 'allergens': ['fish']}
            ], 'total': 1170},
            {'name': 'Day 3', 'meals': [
                {'name': 'Idli Sambar', 'calories': 250, 'protein': 10, 'carbs': 42, 'fats': 4, 'allergens': []},
                {'name': 'Egg Curry with Toast', 'calories': 350, 'protein': 20, 'carbs': 30, 'fats': 16, 'allergens': ['eggs', 'wheat']},
                {'name': 'Buttermilk', 'calories': 60, 'protein': 3, 'carbs': 8, 'fats': 2, 'allergens': ['dairy']},
                {'name': 'Roti Sabzi', 'calories': 350, 'protein': 8, 'carbs': 55, 'fats': 10, 'allergens': ['wheat']}
            ], 'total': 1010},
            {'name': 'Day 4', 'meals': [
                {'name': 'Moong Dal Cheela', 'calories': 240, 'protein': 12, 'carbs': 35, 'fats': 6, 'allergens': ['wheat']},
                {'name': 'Chicken Biryani', 'calories': 480, 'protein': 25, 'carbs': 55, 'fats': 18, 'allergens': []},
                {'name': 'Cucumber Salad', 'calories': 40, 'protein': 1, 'carbs': 6, 'fats': 0, 'allergens': []},
                {'name': 'Grilled Chicken with Salad', 'calories': 420, 'protein': 38, 'carbs': 15, 'fats': 22, 'allergens': []}
            ], 'total': 1180},
            {'name': 'Day 5', 'meals': [
                {'name': 'Aloo Paratha with Curd', 'calories': 380, 'protein': 12, 'carbs': 55, 'fats': 14, 'allergens': ['wheat', 'dairy']},
                {'name': 'Rajma Chawal', 'calories': 450, 'protein': 18, 'carbs': 70, 'fats': 10, 'allergens': []},
                {'name': 'Sprouts', 'calories': 80, 'protein': 5, 'carbs': 12, 'fats': 1, 'allergens': []},
                {'name': 'Fish Tikka with Salad', 'calories': 400, 'protein': 30, 'carbs': 18, 'fats': 22, 'allergens': ['fish']}
            ], 'total': 1310}
        ]
    },
    'vegetarian': {
        'name': 'Indian Vegetarian Plan',
        'days': [
            {'name': 'Day 1', 'meals': [
                {'name': 'Poha', 'calories': 260, 'protein': 5, 'carbs': 48, 'fats': 4, 'allergens': []},
                {'name': 'Dal Tadka with Rice', 'calories': 420, 'protein': 16, 'carbs': 62, 'fats': 10, 'allergens': []},
                {'name': 'Roasted Peanuts', 'calories': 100, 'protein': 4, 'carbs': 8, 'fats': 6, 'allergens': ['peanuts']},
                {'name': 'Paneer Bhurji with Roti', 'calories': 450, 'protein': 22, 'carbs': 40, 'fats': 22, 'allergens': ['dairy', 'wheat']}
            ], 'total': 1230},
            {'name': 'Day 2', 'meals': [
                {'name': 'Upma', 'calories': 240, 'protein': 7, 'carbs': 38, 'fats': 6, 'allergens': []},
                {'name': 'Mixed Veg Khichdi', 'calories': 380, 'protein': 12, 'carbs': 58, 'fats': 10, 'allergens': []},
                {'name': 'Fruit (Apple)', 'calories': 80, 'protein': 0, 'carbs': 20, 'fats': 0, 'allergens': []},
                {'name': 'Roti Sabzi', 'calories': 320, 'protein': 8, 'carbs': 50, 'fats': 10, 'allergens': ['wheat']}
            ], 'total': 1020},
            {'name': 'Day 3', 'meals': [
                {'name': 'Besan Chilla', 'calories': 250, 'protein': 14, 'carbs': 30, 'fats': 8, 'allergens': ['wheat']},
                {'name': 'Rajma Chawal', 'calories': 440, 'protein': 16, 'carbs': 68, 'fats': 10, 'allergens': []},
                {'name': 'Lassi (Sweet)', 'calories': 150, 'protein': 6, 'carbs': 22, 'fats': 4, 'allergens': ['dairy']},
                {'name': 'Methi Thepla with Curd', 'calories': 380, 'protein': 14, 'carbs': 52, 'fats': 14, 'allergens': ['wheat', 'dairy']}
            ], 'total': 1220},
            {'name': 'Day 4', 'meals': [
                {'name': 'Idli Sambar', 'calories': 230, 'protein': 10, 'carbs': 40, 'fats': 4, 'allergens': []},
                {'name': 'Chole Bhature', 'calories': 480, 'protein': 14, 'carbs': 65, 'fats': 18, 'allergens': ['wheat']},
                {'name': 'Onion Salad', 'calories': 30, 'protein': 1, 'carbs': 6, 'fats': 0, 'allergens': []},
                {'name': 'Mixed Veg Curry with Roti', 'calories': 340, 'protein': 10, 'carbs': 52, 'fats': 10, 'allergens': ['wheat']}
            ], 'total': 1080},
            {'name': 'Day 5', 'meals': [
                {'name': 'Aloo Paratha with Curd', 'calories': 360, 'protein': 10, 'carbs': 52, 'fats': 14, 'allergens': ['wheat', 'dairy']},
                {'name': 'Vegetable Pulao', 'calories': 400, 'protein': 10, 'carbs': 65, 'fats': 12, 'allergens': []},
                {'name': 'Buttermilk', 'calories': 60, 'protein': 3, 'carbs': 8, 'fats': 2, 'allergens': ['dairy']},
                {'name': 'Dal Fry with Rice', 'calories': 380, 'protein': 14, 'carbs': 58, 'fats': 10, 'allergens': []}
            ], 'total': 1200}
        ]
    },
    'vegan': {
        'name': 'Indian Vegan Plan',
        'days': [
            {'name': 'Day 1', 'meals': [
                {'name': 'Poha (no milk)', 'calories': 250, 'protein': 5, 'carbs': 50, 'fats': 3, 'allergens': []},
                {'name': 'Dal Tadka with Rice', 'calories': 420, 'protein': 16, 'carbs': 62, 'fats': 10, 'allergens': []},
                {'name': 'Roasted Chana', 'calories': 120, 'protein': 6, 'carbs': 18, 'fats': 3, 'allergens': []},
                {'name': 'Sabzi with Roti', 'calories': 300, 'protein': 8, 'carbs': 48, 'fats': 8, 'allergens': ['wheat']}
            ], 'total': 1090},
            {'name': 'Day 2', 'meals': [
                {'name': 'Upma', 'calories': 240, 'protein': 7, 'carbs': 38, 'fats': 6, 'allergens': []},
                {'name': 'Vegetable Khichdi', 'calories': 380, 'protein': 12, 'carbs': 58, 'fats': 10, 'allergens': []},
                {'name': 'Banana', 'calories': 90, 'protein': 1, 'carbs': 23, 'fats': 0, 'allergens': []},
                {'name': 'Chole (no yogurt)', 'calories': 340, 'protein': 14, 'carbs': 50, 'fats': 8, 'allergens': []}
            ], 'total': 1050},
            {'name': 'Day 3', 'meals': [
                {'name': 'Moong Dal Cheela', 'calories': 240, 'protein': 12, 'carbs': 35, 'fats': 6, 'allergens': ['wheat']},
                {'name': 'Vegetable Pulao', 'calories': 400, 'protein': 10, 'carbs': 65, 'fats': 12, 'allergens': []},
                {'name': 'Cucumber', 'calories': 40, 'protein': 1, 'carbs': 6, 'fats': 0, 'allergens': []},
                {'name': 'Roti Sabzi', 'calories': 300, 'protein': 8, 'carbs': 48, 'fats': 8, 'allergens': ['wheat']}
            ], 'total': 980},
            {'name': 'Day 4', 'meals': [
                {'name': 'Besan Chilla', 'calories': 250, 'protein': 14, 'carbs': 30, 'fats': 8, 'allergens': ['wheat']},
                {'name': 'Rajma Chawal', 'calories': 430, 'protein': 16, 'carbs': 65, 'fats': 10, 'allergens': []},
                {'name': 'Sprouts', 'calories': 80, 'protein': 5, 'carbs': 12, 'fats': 1, 'allergens': []},
                {'name': 'Dal Fry with Rice', 'calories': 370, 'protein': 14, 'carbs': 55, 'fats': 10, 'allergens': []}
            ], 'total': 1130},
            {'name': 'Day 5', 'meals': [
                {'name': 'Poha with Peanuts', 'calories': 280, 'protein': 8, 'carbs': 45, 'fats': 8, 'allergens': ['peanuts']},
                {'name': 'Chole Bhature (no curd)', 'calories': 450, 'protein': 14, 'carbs': 62, 'fats': 16, 'allergens': ['wheat']},
                {'name': 'Mixed Fruit', 'calories': 80, 'protein': 1, 'carbs': 18, 'fats': 0, 'allergens': []},
                {'name': 'Mixed Veg Curry with Roti', 'calories': 310, 'protein': 8, 'carbs': 48, 'fats': 10, 'allergens': ['wheat']}
            ], 'total': 1120}
        ]
    },
    'pescatarian': {
        'name': 'Indian Pescatarian Plan',
        'days': [
            {'name': 'Day 1', 'meals': [
                {'name': 'Poha', 'calories': 250, 'protein': 5, 'carbs': 48, 'fats': 3, 'allergens': []},
                {'name': 'Fish Curry with Rice', 'calories': 420, 'protein': 28, 'carbs': 50, 'fats': 12, 'allergens': ['fish']},
                {'name': 'Roasted Chana', 'calories': 120, 'protein': 6, 'carbs': 18, 'fats': 3, 'allergens': []},
                {'name': 'Dal Tadka with Roti', 'calories': 350, 'protein': 12, 'carbs': 50, 'fats': 10, 'allergens': ['wheat']}
            ], 'total': 1140},
            {'name': 'Day 2', 'meals': [
                {'name': 'Upma', 'calories': 240, 'protein': 7, 'carbs': 38, 'fats': 6, 'allergens': []},
                {'name': 'Prawns Curry with Rice', 'calories': 400, 'protein': 30, 'carbs': 48, 'fats': 12, 'allergens': ['shellfish']},
                {'name': 'Cucumber Salad', 'calories': 40, 'protein': 1, 'carbs': 6, 'fats': 0, 'allergens': []},
                {'name': 'Vegetable Khichdi', 'calories': 350, 'protein': 12, 'carbs': 55, 'fats': 8, 'allergens': []}
            ], 'total': 1030},
            {'name': 'Day 3', 'meals': [
                {'name': 'Idli Sambar', 'calories': 230, 'protein': 10, 'carbs': 40, 'fats': 4, 'allergens': []},
                {'name': 'Fish Tikka with Salad', 'calories': 380, 'protein': 30, 'carbs': 18, 'fats': 20, 'allergens': ['fish']},
                {'name': 'Sprouts', 'calories': 80, 'protein': 5, 'carbs': 12, 'fats': 1, 'allergens': []},
                {'name': 'Roti Sabzi', 'calories': 300, 'protein': 8, 'carbs': 48, 'fats': 8, 'allergens': ['wheat']}
            ], 'total': 990},
            {'name': 'Day 4', 'meals': [
                {'name': 'Poha', 'calories': 250, 'protein': 5, 'carbs': 48, 'fats': 3, 'allergens': []},
                {'name': 'Egg Curry with Rice', 'calories': 400, 'protein': 22, 'carbs': 48, 'fats': 14, 'allergens': ['eggs']},
                {'name': 'Buttermilk', 'calories': 60, 'protein': 3, 'carbs': 8, 'fats': 2, 'allergens': ['dairy']},
                {'name': 'Grilled Fish with Salad', 'calories': 350, 'protein': 32, 'carbs': 15, 'fats': 18, 'allergens': ['fish']}
            ], 'total': 1060},
            {'name': 'Day 5', 'meals': [
                {'name': 'Upma', 'calories': 240, 'protein': 7, 'carbs': 38, 'fats': 6, 'allergens': []},
                {'name': 'Fish Biryani', 'calories': 450, 'protein': 28, 'carbs': 55, 'fats': 16, 'allergens': ['fish']},
                {'name': 'Roasted Makhana', 'calories': 100, 'protein': 4, 'carbs': 15, 'fats': 3, 'allergens': []},
                {'name': 'Dal with Rice', 'calories': 360, 'protein': 14, 'carbs': 55, 'fats': 8, 'allergens': []}
            ], 'total': 1150}
        ]
    }
}

def is_meal_safe(meal_allergens, user_allergens):
    if not user_allergens:
        return True
    for allergen in user_allergens:
        if allergen in meal_allergens:
            return False
    return True

def filter_meals_by_allergens(meal_plan, allergens):
    filtered_days = []
    skipped_meals = []
    
    for day in meal_plan['days']:
        filtered_meals = []
        for meal in day['meals']:
            if is_meal_safe(meal['allergens'], allergens):
                filtered_meals.append(meal)
            else:
                for allergen in meal['allergens']:
                    if allergen in allergens:
                        skipped_meals.append(f"{meal['name']} (contains {allergen})")
        
        if filtered_meals:
            day_total = sum(m['calories'] for m in filtered_meals)
            filtered_days.append({
                'name': day['name'],
                'meals': filtered_meals,
                'total': day_total
            })
    
    return filtered_days, skipped_meals

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_plan', methods=['POST'])
def generate_plan():
    # Collect form data
    data = {
        'name': request.form.get('name'),
        'age': int(request.form.get('age')),
        'gender': request.form.get('gender'),
        'height': int(request.form.get('height')),
        'weight': int(request.form.get('weight')),
        'activity_level': request.form.get('activity_level'),
        'fitness_goal': request.form.get('fitness_goal'),
        'diet_preference': request.form.get('diet_preference'),
        'allergens': request.form.getlist('allergens')
    }
    
    # Calculate metrics
    metrics = calculate_metrics(data)
    
    # Get workout plan
    workout_plan = workout_plans[data['fitness_goal']]
    
    # Get and filter meal plan
    meal_plan = indian_meal_plans[data['diet_preference']]
    filtered_days, skipped_meals = filter_meals_by_allergens(meal_plan, data['allergens'])
    filtered_meal_plan = {
        'name': meal_plan['name'],
        'days': filtered_days
    }
    
    # Scale calories
    scale_factor = (metrics['calorie_target'] / 4) / 350
    if scale_factor < 0.7:
        scale_factor = 0.7
    if scale_factor > 1.3:
        scale_factor = 1.3
    
    # Calculate macros
    total_protein = 0
    total_carbs = 0
    total_fats = 0
    
    for day in filtered_meal_plan['days']:
        day['total'] = round(day['total'] * scale_factor)
        for meal in day['meals']:
            meal['scaled_calories'] = round(meal['calories'] * scale_factor)
            meal['protein'] = round(meal['protein'] * scale_factor)
            meal['carbs'] = round(meal['carbs'] * scale_factor)
            meal['fats'] = round(meal['fats'] * scale_factor)
            total_protein += meal['protein']
            total_carbs += meal['carbs']
            total_fats += meal['fats']
    
    # Macro percentages (based on calories: protein/carbs=4cal, fats=9cal)
    total_macro_cal = (total_protein * 4) + (total_carbs * 4) + (total_fats * 9)
    macros = {
        'protein': total_protein,
        'carbs': total_carbs,
        'fats': total_fats,
        'protein_pct': 30 if total_macro_cal == 0 else round((total_protein * 4 / total_macro_cal) * 100),
        'carbs_pct': 40 if total_macro_cal == 0 else round((total_carbs * 4 / total_macro_cal) * 100),
        'fats_pct': 30 if total_macro_cal == 0 else round((total_fats * 9 / total_macro_cal) * 100)
    }
    
    return render_template('result.html', 
                         name=data['name'],
                         metrics=metrics,
                         workout_plan=workout_plan,
                         meal_plan=filtered_meal_plan,
                         macros=macros,
                         skipped_meals=skipped_meals,
                         allergens=data['allergens'])

@app.route('/send_email', methods=['POST'])
def send_email():
    email = request.form.get('email')
    
    if not email or '@' not in email:
        return render_template('result.html', error="Invalid email address")
    
    name = request.form.get('name', "User")
    metrics = request.form.get('metrics', '')
    workout = request.form.get('workout', '')
    meal_plan = request.form.get('meal_plan', '')
    
    # Create email body
    subject = f"FitPlan Pro - {name}'s Fitness Plan"
    body = f"""FITPLAN PRO - PERSONALIZED FITNESS & MEAL PLAN

Hello {name}!

Here is your personalized fitness and meal plan:

HEALTH METRICS
-------------
{metrics}

WORKOUT ROUTINE
---------------
{workout}

MEAL PLAN
---------
{meal_plan}

Generated by FitPlan Pro
Date: {datetime.now().strftime('%Y-%m-%d')}
"""
    
    # Use mailto to open email client
    mailto_url = f"mailto:{email}?subject={quote(subject)}&body={quote(body)}"
    return redirect(mailto_url)

if __name__ == '__main__':
    app.run(debug=True, port=5000)