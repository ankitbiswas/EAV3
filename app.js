// FitPlan Pro - Main Application Logic

// Workout Data
const workoutPlans = {
    weight_loss: {
        title: "Weight Loss Program",
        days: [
            {
                name: "Day 1 - Full Body HIIT",
                focus: "High Intensity Interval Training for max calorie burn",
                exercises: [
                    { name: "Jumping Jacks", sets: "4 sets", reps: "45 seconds" },
                    { name: "Burpees", sets: "4 sets", reps: "12 reps" },
                    { name: "Mountain Climbers", sets: "4 sets", reps: "45 seconds" },
                    { name: "High Knees", sets: "4 sets", reps: "45 seconds" },
                    { name: "Squat Jumps", sets: "3 sets", reps: "15 reps" },
                    { name: "Plank Hold", sets: "3 sets", reps: "45 seconds" }
                ]
            },
            {
                name: "Day 2 - Lower Body + Cardio",
                focus: "Lower body strength with cardio bursts",
                exercises: [
                    { name: "Bodyweight Squats", sets: "4 sets", reps: "20 reps" },
                    { name: "Lunges", sets: "3 sets", reps: "12 reps/leg" },
                    { name: "Jump Squats", sets: "3 sets", reps: "15 reps" },
                    { name: "Glute Bridges", sets: "3 sets", reps: "15 reps" },
                    { name: "Running in Place", sets: "3 sets", reps: "30 seconds" },
                    { name: "Calf Raises", sets: "3 sets", reps: "20 reps" }
                ]
            },
            {
                name: "Day 3 - Active Recovery & Core",
                focus: "Core strengthening and mobility",
                exercises: [
                    { name: "Plank", sets: "3 sets", reps: "60 seconds" },
                    { name: "Bicycle Crunches", sets: "3 sets", reps: "20 reps" },
                    { name: "Leg Raises", sets: "3 sets", reps: "12 reps" },
                    { name: "Russian Twists", sets: "3 sets", reps: "20 reps" },
                    { name: "Dead Bug", sets: "3 sets", reps: "10 reps" },
                    { name: "Bird Dog", sets: "3 sets", reps: "10 reps/side" }
                ]
            },
            {
                name: "Day 4 - Upper Body + HIIT",
                focus: "Upper body with cardio for overall toning",
                exercises: [
                    { name: "Push-ups", sets: "4 sets", reps: "12 reps" },
                    { name: "Tricep Dips", sets: "3 sets", reps: "12 reps" },
                    { name: "Plank Shoulder Taps", sets: "3 sets", reps: "20 taps" },
                    { name: "Arm Circles", sets: "3 sets", reps: "30 seconds" },
                    { name: "Bear Crawl", sets: "3 sets", reps: "30 seconds" },
                    { name: "Sprint Intervals", sets: "3 sets", reps: "30 seconds" }
                ]
            },
            {
                name: "Day 5 - Full Body Circuit",
                focus: "Complete circuit training for full body conditioning",
                exercises: [
                    { name: "Burpees", sets: "3 sets", reps: "10 reps" },
                    { name: "Squat to Press", sets: "3 sets", reps: "15 reps" },
                    { name: "Plank Jacks", sets: "3 sets", reps: "15 reps" },
                    { name: "Reverse Lunges", sets: "3 sets", reps: "12 reps/leg" },
                    { name: "Superman Hold", sets: "3 sets", reps: "30 seconds" },
                    { name: "High Knee Run", sets: "3 sets", reps: "30 seconds" }
                ]
            }
        ]
    },
    muscle_gain: {
        title: "Muscle Building Program",
        days: [
            {
                name: "Day 1 - Push Day (Chest, Shoulders, Triceps)",
                focus: "Upper body pushing movements",
                exercises: [
                    { name: "Push-ups", sets: "4 sets", reps: "10-15 reps" },
                    { name: "Diamond Push-ups", sets: "3 sets", reps: "8-12 reps" },
                    { name: "Pike Push-ups", sets: "3 sets", reps: "8-12 reps" },
                    { name: "Tricep Dips", sets: "3 sets", reps: "12-15 reps" },
                    { name: "Decline Push-ups", sets: "3 sets", reps: "10-12 reps" },
                    { name: "Wall Push-ups (if needed)", sets: "3 sets", reps: "10 reps" }
                ]
            },
            {
                name: "Day 2 - Pull Day (Back, Biceps)",
                focus: "Upper body pulling movements",
                exercises: [
                    { name: "Superman Hold", sets: "4 sets", reps: "30 seconds" },
                    { name: "Reverse Snow Angels", sets: "3 sets", reps: "12 reps" },
                    { name: "Prone Y Raises", sets: "3 sets", reps: "12 reps" },
                    { name: "Doorframe Rows", sets: "3 sets", reps: "12 reps" },
                    { name: "Bicep Curls (if available)", sets: "3 sets", reps: "12 reps" },
                    { name: "Hold Plank (simulated pull-up)", sets: "3 sets", reps: "20 seconds" }
                ]
            },
            {
                name: "Day 3 - Leg Day (Quads, Glutes, Hamstrings)",
                focus: "Lower body strength training",
                exercises: [
                    { name: "Squats", sets: "4 sets", reps: "12-15 reps" },
                    { name: "Lunges", sets: "4 sets", reps: "10 reps/leg" },
                    { name: "Bulgarian Split Squats", sets: "3 sets", reps: "8 reps/leg" },
                    { name: "Glute Bridges", sets: "3 sets", reps: "15 reps" },
                    { name: "Single Leg Deadlift", sets: "3 sets", reps: "8 reps/leg" },
                    { name: "Calf Raises", sets: "4 sets", reps: "20 reps" }
                ]
            },
            {
                name: "Day 4 - Push Day + Core",
                focus: "Secondary push workout with core emphasis",
                exercises: [
                    { name: "Wide Push-ups", sets: "4 sets", reps: "12 reps" },
                    { name: "Close Grip Push-ups", sets: "3 sets", reps: "10 reps" },
                    { name: "Shoulder Taps", sets: "3 sets", reps: "20 taps" },
                    { name: "Pike Push-ups", sets: "3 sets", reps: "8 reps" },
                    { name: "Hollow Body Hold", sets: "3 sets", reps: "30 seconds" },
                    { name: "Plank to Push-up", sets: "3 sets", reps: "10 reps" }
                ]
            },
            {
                name: "Day 5 - Pull Day + Core",
                focus: "Secondary pull workout with core emphasis",
                exercises: [
                    { name: "Superman Pull-overs", sets: "4 sets", reps: "12 reps" },
                    { name: "Reverse Rows (table)", sets: "3 sets", reps: "12 reps" },
                    { name: "Prone T Raises", sets: "3 sets", reps: "12 reps" },
                    { name: "Bird Dog", sets: "3 sets", reps: "10 reps/side" },
                    { name: "Dead Bug", sets: "3 sets", reps: "10 reps" },
                    { name: "Side Plank", sets: "3 sets", reps: "20 seconds/side" }
                ]
            }
        ]
    },
    endurance: {
        title: "Endurance Building Program",
        days: [
            {
                name: "Day 1 - Cardio Base",
                focus: "Building cardiovascular base",
                exercises: [
                    { name: "Jumping Jacks", sets: "5 sets", reps: "60 seconds" },
                    { name: "High Knees", sets: "5 sets", reps: "45 seconds" },
                    { name: "Butt Kicks", sets: "5 sets", reps: "45 seconds" },
                    { name: "Skaters", sets: "4 sets", reps: "20 reps" },
                    { name: "March in Place", sets: "3 sets", reps: "60 seconds" },
                    { name: "Box Step-ups", sets: "3 sets", reps: "20 reps" }
                ]
            },
            {
                name: "Day 2 - steady State Cardio",
                focus: " sustained cardio efforts",
                exercises: [
                    { name: "Running in Place", sets: "3 sets", reps: "3 minutes" },
                    { name: "Jump Rope (or simulation)", sets: "3 sets", reps: "2 minutes" },
                    { name: "Stair Climbing", sets: "3 sets", reps: "2 minutes" },
                    { name: "Cycle Intervals", sets: "3 sets", reps: "3 minutes" },
                    { name: "Walking Lunges", sets: "3 sets", reps: "20 reps" },
                    { name: "Plank to Push-up", sets: "3 sets", reps: "45 seconds" }
                ]
            },
            {
                name: "Day 3 - Active Recovery",
                focus: "Low intensity active recovery",
                exercises: [
                    { name: "Gentle Stretching", sets: "1 set", reps: "15 minutes" },
                    { name: "Yoga Flow", sets: "1 set", reps: "10 minutes" },
                    { name: "Mobility Work", sets: "1 set", reps: "10 minutes" },
                    { name: "Light Walking", sets: "1 set", reps: "20 minutes" },
                    { name: "Foam Rolling", sets: "1 set", reps: "10 minutes" },
                    { name: "Breathing Exercises", sets: "1 set", reps: "5 minutes" }
                ]
            },
            {
                name: "Day 4 - Interval Training",
                focus: "HIIT for endurance",
                exercises: [
                    { name: "Sprint Intervals", sets: "6 sets", reps: "30 seconds" },
                    { name: "Active Rest", sets: "6 sets", reps: "90 seconds" },
                    { name: "Battle Ropes (or arm swings)", sets: "4 sets", reps: "45 seconds" },
                    { name: "Burpee Mix", sets: "4 sets", reps: "30 seconds" },
                    { name: "Mountain Climbers", sets: "4 sets", reps: "45 seconds" },
                    { name: "Final Sprint", sets: "2 sets", reps: "60 seconds" }
                ]
            },
            {
                name: "Day 5 - Long Cardio Session",
                focus: "Extended cardio session",
                exercises: [
                    { name: "Steady State Cardio", sets: "1 set", reps: "30 minutes" },
                    { name: "Tempo Walk", sets: "1 set", reps: "10 minutes" },
                    { name: "Easy Jog", sets: "1 set", reps: "15 minutes" },
                    { name: "Cool Down Walk", sets: "1 set", reps: "5 minutes" },
                    { name: "Stretching Routine", sets: "1 set", reps: "10 minutes" },
                    { name: "Meditation", sets: "1 set", reps: "5 minutes" }
                ]
            }
        ]
    },
    flexibility: {
        title: "Flexibility & Mobility Program",
        days: [
            {
                name: "Day 1 - Morning Mobility",
                focus: "Dynamic stretching routine",
                exercises: [
                    { name: "Neck Rolls", sets: "3 sets", reps: "10 each direction" },
                    { name: "Shoulder Circles", sets: "3 sets", reps: "15 each direction" },
                    { name: "Arm Swings", sets: "3 sets", reps: "15 each arm" },
                    { name: "Torso Twists", sets: "3 sets", reps: "10 each side" },
                    { name: "Hip Circles", sets: "3 sets", reps: "10 each direction" },
                    { name: "Ankle Rolls", sets: "3 sets", reps: "15 each foot" }
                ]
            },
            {
                name: "Day 2 - Lower Body Flexibility",
                focus: "Lower body stretching",
                exercises: [
                    { name: "Standing Forward Fold", sets: "3 sets", reps: "30 seconds" },
                    { name: "Low Lunge Hold", sets: "3 sets", reps: "30 seconds/side" },
                    { name: "Pigeon Pose", sets: "3 sets", reps: "30 seconds/side" },
                    { name: "Butterfly Stretch", sets: "3 sets", reps: "30 seconds" },
                    { name: "Seated Hamstring Stretch", sets: "3 sets", reps: "30 seconds" },
                    { name: "Calf Stretch", sets: "3 sets", reps: "30 seconds/leg" }
                ]
            },
            {
                name: "Day 3 - Active Recovery",
                focus: "Light movement and stretching",
                exercises: [
                    { name: "Easy Walk", sets: "1 set", reps: "20 minutes" },
                    { name: "Cat-Cow Stretch", sets: "3 sets", reps: "10 reps" },
                    { name: "Child's Pose", sets: "3 sets", reps: "30 seconds" },
                    { name: "Gentle Twists", sets: "3 sets", reps: "30 seconds/side" },
                    { name: "Figure Four Stretch", sets: "3 sets", reps: "30 seconds/side" },
                    { name: "Supine Twist", sets: "3 sets", reps: "30 seconds/side" }
                ]
            },
            {
                name: "Day 4 - Upper Body Flexibility",
                focus: "Upper body and spine mobility",
                exercises: [
                    { name: "Chest Opener", sets: "3 sets", reps: "30 seconds" },
                    { name: "Eagle Arms", sets: "3 sets", reps: "30 seconds/side" },
                    { name: "Thread the Needle", sets: "3 sets", reps: "30 seconds/side" },
                    { name: "Cow Face Arms", sets: "3 sets", reps: "30 seconds/side" },
                    { name: "Wrist Stretches", sets: "3 sets", reps: "30 seconds" },
                    { name: "Neck Side Stretch", sets: "3 sets", reps: "30 seconds/side" }
                ]
            },
            {
                name: "Day 5 - Full Body Flow",
                focus: "Complete stretching routine",
                exercises: [
                    { name: "Sun Salutation", sets: "3 rounds", reps: "5 minutes" },
                    { name: "Standing Stretches", sets: "1 set", reps: "10 minutes" },
                    { name: "Floor Stretches", sets: "1 set", reps: "15 minutes" },
                    { name: "Deep Breathing", sets: "1 set", reps: "5 minutes" },
                    { name: "Progressive Relaxation", sets: "1 set", reps: "5 minutes" },
                    { name: "Meditation", sets: "1 set", reps: "5 minutes" }
                ]
            }
        ]
    },
    general: {
        title: "General Fitness Program",
        days: [
            {
                name: "Day 1 - Full Body A",
                focus: " Balanced full body workout",
                exercises: [
                    { name: "Squats", sets: "3 sets", reps: "15 reps" },
                    { name: "Push-ups", sets: "3 sets", reps: "10 reps" },
                    { name: "Lunges", sets: "3 sets", reps: "10 reps/leg" },
                    { name: "Plank", sets: "3 sets", reps: "45 seconds" },
                    { name: "Glute Bridges", sets: "3 sets", reps: "15 reps" },
                    { name: "Superman Hold", sets: "3 sets", reps: "30 seconds" }
                ]
            },
            {
                name: "Day 2 - Cardio & Core",
                focus: "Cardio with core focus",
                exercises: [
                    { name: "Jumping Jacks", sets: "3 sets", reps: "45 seconds" },
                    { name: "Mountain Climbers", sets: "3 sets", reps: "45 seconds" },
                    { name: "Bicycle Crunches", sets: "3 sets", reps: "20 reps" },
                    { name: "Leg Raises", sets: "3 sets", reps: "12 reps" },
                    { name: "Russian Twists", sets: "3 sets", reps: "20 reps" },
                    { name: "Plank Hold", sets: "3 sets", reps: "45 seconds" }
                ]
            },
            {
                name: "Day 3 - Active Recovery",
                focus: "Light activity and stretching",
                exercises: [
                    { name: "Easy Walk/Jog", sets: "1 set", reps: "20 minutes" },
                    { name: "Stretching Routine", sets: "1 set", reps: "15 minutes" },
                    { name: "Foam Rolling", sets: "1 set", reps: "10 minutes" },
                    { name: "Mobility Drills", sets: "1 set", reps: "10 minutes" },
                    { name: "Yoga Poses", sets: "1 set", reps: "10 minutes" },
                    { name: "Breathing Exercises", sets: "1 set", reps: "5 minutes" }
                ]
            },
            {
                name: "Day 4 - Upper Body Focus",
                focus: "Upper body strength",
                exercises: [
                    { name: "Push-ups", sets: "4 sets", reps: "10-12 reps" },
                    { name: "Tricep Dips", sets: "3 sets", reps: "12 reps" },
                    { name: "Plank Shoulder Taps", sets: "3 sets", reps: "20 taps" },
                    { name: "Reverse Snow Angels", sets: "3 sets", reps: "12 reps" },
                    { name: "Prone Y Raises", sets: "3 sets", reps: "12 reps" },
                    { name: "Arm Circles", sets: "3 sets", reps: "30 seconds" }
                ]
            },
            {
                name: "Day 5 - Lower Body Focus",
                focus: "Lower body strength",
                exercises: [
                    { name: "Squats", sets: "4 sets", reps: "15 reps" },
                    { name: "Bulgarian Split Squats", sets: "3 sets", reps: "10 reps/leg" },
                    { name: "Deadlifts (bodyweight)", sets: "3 sets", reps: "15 reps" },
                    { name: "Single Leg Deadlift", sets: "3 sets", reps: "10 reps/leg" },
                    { name: "Calf Raises", sets: "4 sets", reps: "20 reps" },
                    { name: "Wall Sit", sets: "3 sets", reps: "45 seconds" }
                ]
            }
        ]
    }
};

// Meal Data
const mealPlans = {
    non_veg: {
        name: "Non-Vegetarian Plan",
        days: [
            {
                name: "Day 1",
                meals: [
                    { name: "Breakfast - Oatmeal with Eggs", calories: 450 },
                    { name: "Lunch - Grilled Chicken Salad", calories: 550 },
                    { name: "Snack - Greek Yogurt with Nuts", calories: 200 },
                    { name: "Dinner - Baked Salmon with Vegetables", calories: 500 }
                ],
                totalCalories: 1700
            },
            {
                name: "Day 2",
                meals: [
                    { name: "Breakfast - Scrambled Eggs with Toast", calories: 400 },
                    { name: "Lunch - Chicken Wrap with Salad", calories: 500 },
                    { name: "Snack - Protein Shake", calories: 250 },
                    { name: "Dinner - Grilled Fish with Rice", calories: 550 }
                ],
                totalCalories: 1700
            },
            {
                name: "Day 3",
                meals: [
                    { name: "Breakfast - Greek Yogurt Parfait", calories: 350 },
                    { name: "Lunch - Turkey Sandwich", calories: 450 },
                    { name: "Snack - Hard Boiled Eggs", calories: 150 },
                    { name: "Dinner - Chicken Stir-Fry", calories: 550 }
                ],
                totalCalories: 1500
            },
            {
                name: "Day 4",
                meals: [
                    { name: "Breakfast - Eggs Benedict", calories: 500 },
                    { name: "Lunch - Chicken Quinoa Bowl", calories: 550 },
                    { name: "Snack - Cottage Cheese", calories: 150 },
                    { name: "Dinner - Grilled Meat with Salad", calories: 500 }
                ],
                totalCalories: 1700
            },
            {
                name: "Day 5",
                meals: [
                    { name: "Breakfast - Protein Pancakes", calories: 400 },
                    { name: "Lunch - Tuna Salad", calories: 450 },
                    { name: "Snack - Trail Mix", calories: 250 },
                    { name: "Dinner - Baked Chicken with Veggies", calories: 550 }
                ],
                totalCalories: 1650
            }
        ]
    },
    vegetarian: {
        name: "Vegetarian Plan",
        days: [
            {
                name: "Day 1",
                meals: [
                    { name: "Breakfast - Oatmeal with Fruits", calories: 400 },
                    { name: "Lunch - Veggie Hummus Wrap", calories: 500 },
                    { name: "Snack - Greek Yogurt", calories: 200 },
                    { name: "Dinner - Lentil Curry with Rice", calories: 550 }
                ],
                totalCalories: 1650
            },
            {
                name: "Day 2",
                meals: [
                    { name: "Breakfast - Veggie Omelette", calories: 400 },
                    { name: "Lunch - Quinoa Salad", calories: 450 },
                    { name: "Snack - Nuts and Seeds", calories: 200 },
                    { name: "Dinner - Veggie Stir-Fry", calories: 500 }
                ],
                totalCalories: 1550
            },
            {
                name: "Day 3",
                meals: [
                    { name: "Breakfast - Smoothie Bowl", calories: 350 },
                    { name: "Lunch - Veggie Sandwich", calories: 450 },
                    { name: "Snack - Cheese and Crackers", calories: 250 },
                    { name: "Dinner - Pasta with Veggies", calories: 550 }
                ],
                totalCalories: 1600
            },
            {
                name: "Day 4",
                meals: [
                    { name: "Breakfast - Pancakes with Maple", calories: 450 },
                    { name: "Lunch - Bean Burrito Bowl", calories: 500 },
                    { name: "Snack - Fruit Salad", calories: 150 },
                    { name: "Dinner - Tofu Curry", calories: 500 }
                ],
                totalCalories: 1600
            },
            {
                name: "Day 5",
                meals: [
                    { name: "Breakfast - Toast with Peanut Butter", calories: 350 },
                    { name: "Lunch - Caprese Salad", calories: 400 },
                    { name: "Snack - Veggie Sticks with Dip", calories: 200 },
                    { name: "Dinner - Veggie Lasagna", calories: 550 }
                ],
                totalCalories: 1500
            }
        ]
    },
    vegan: {
        name: "Vegan Plan",
        days: [
            {
                name: "Day 1",
                meals: [
                    { name: "Breakfast - Tofu Scramble", calories: 350 },
                    { name: "Lunch - Vegan Buddha Bowl", calories: 500 },
                    { name: "Snack - Fruit Smoothie", calories: 200 },
                    { name: "Dinner - Vegan Chili", calories: 500 }
                ],
                totalCalories: 1550
            },
            {
                name: "Day 2",
                meals: [
                    { name: "Breakfast - Overnight Oats", calories: 400 },
                    { name: "Lunch - Veggie Wrap", calories: 450 },
                    { name: "Snack - Roasted Chickpeas", calories: 200 },
                    { name: "Dinner - Stir-Fried Tofu", calories: 500 }
                ],
                totalCalories: 1550
            },
            {
                name: "Day 3",
                meals: [
                    { name: "Breakfast - Fruit Salad", calories: 300 },
                    { name: "Lunch - Lentil Soup", calories: 450 },
                    { name: "Snack - Vegan Cookie", calories: 200 },
                    { name: "Dinner - Bean Tacos", calories: 500 }
                ],
                totalCalories: 1450
            },
            {
                name: "Day 4",
                meals: [
                    { name: "Breakfast - Avocado Toast", calories: 400 },
                    { name: "Lunch - Quinoa Salad", calories: 450 },
                    { name: "Snack - Mixed Nuts", calories: 200 },
                    { name: "Dinner - Vegetable Curry", calories: 500 }
                ],
                totalCalories: 1550
            },
            {
                name: "Day 5",
                meals: [
                    { name: "Breakfast - Smoothie Bowl", calories: 350 },
                    { name: "Lunch - Buddha Bowl", calories: 500 },
                    { name: "Snack - Veggie Sticks", calories: 150 },
                    { name: "Dinner - Pasta Primavera", calories: 500 }
                ],
                totalCalories: 1500
            }
        ]
    },
    pescatarian: {
        name: "Pescatarian Plan",
        days: [
            {
                name: "Day 1",
                meals: [
                    { name: "Breakfast - Eggs with Smoked Salmon", calories: 450 },
                    { name: "Lunch - Tuna Salad", calories: 500 },
                    { name: "Snack - Seaweed Snacks", calories: 150 },
                    { name: "Dinner - Grilled Shrimp with Veggies", calories: 500 }
                ],
                totalCalories: 1600
            },
            {
                name: "Day 2",
                meals: [
                    { name: "Breakfast - Oatmeal with Fish", calories: 400 },
                    { name: "Lunch - Salmon Poke Bowl", calories: 550 },
                    { name: "Snack - CalciumRich Snack", calories: 200 },
                    { name: "Dinner - Baked Fish with Rice", calories: 500 }
                ],
                totalCalories: 1650
            },
            {
                name: "Day 3",
                meals: [
                    { name: "Breakfast - Mediterranean Bowl", calories: 400 },
                    { name: "Lunch - Fish Sandwich", calories: 500 },
                    { name: "Snack - Dried Fish", calories: 150 },
                    { name: "Dinner - Fish Stew", calories: 550 }
                ],
                totalCalories: 1600
            },
            {
                name: "Day 4",
                meals: [
                    { name: "Breakfast - Seafood Omelette", calories: 450 },
                    { name: "Lunch - Crab Salad", calories: 450 },
                    { name: "Snack - Omega3 Rich Nuts", calories: 200 },
                    { name: "Dinner - Grilled Fish", calories: 500 }
                ],
                totalCalories: 1600
            },
            {
                name: "Day 5",
                meals: [
                    { name: "Breakfast - Protein Smoothie", calories: 350 },
                    { name: "Lunch - Sashimi Bowl", calories: 500 },
                    { name: "Snack - Edamame", calories: 150 },
                    { name: "Dinner - Miso Glazed Fish", calories: 550 }
                ],
                totalCalories: 1550
            }
        ]
    }
};

// Activity multipliers for TDEE calculation
const activityMultipliers = {
    sedentary: 1.2,
    light: 1.375,
    moderate: 1.55,
    active: 1.725,
    extremely: 1.9
};

// BMI Categories
function getBMICategory(bmi) {
    if (bmi < 18.5) return { category: "Underweight", class: "bmi-underweight" };
    if (bmi < 25) return { category: "Normal", class: "bmi-normal" };
    if (bmi < 30) return { category: "Overweight", class: "bmi-overweight" };
    return { category: "Obese", class: "bmi-obese" };
}

// Calculate health metrics
function calculateMetrics(data) {
    const heightM = data.height / 100;
    const bmi = data.weight / (heightM * heightM);
    const bmiInfo = getBMICategory(bmi);
    
    // BMR Calculation (Mifflin-St Jeor)
    let bmr;
    if (data.gender === "male") {
        bmr = 10 * data.weight + 6.25 * data.height - 5 * data.age + 5;
    } else {
        bmr = 10 * data.weight + 6.25 * data.height - 5 * data.age - 161;
    }
    
    const tdee = bmr * activityMultipliers[data.activityLevel];
    
    // Calorie targets based on goal
    let calorieTarget;
    let weightChangeMsg;
    
    switch (data.fitnessGoal) {
        case "weight_loss":
            calorieTarget = tdee - 500;
            weightChangeMsg = "Lose ~0.5 kg/week";
            break;
        case "muscle_gain":
            calorieTarget = tdee + 300;
            weightChangeMsg = "Gain ~0.25 kg/week";
            break;
        default:
            calorieTarget = tdee;
            weightChangeMsg = "Maintain weight";
    }
    
    return {
        bmi: bmi.toFixed(1),
        bmiCategory: bmiInfo.category,
        bmiClass: bmiInfo.class,
        bmr: Math.round(bmr),
        tdee: Math.round(tdee),
        calorieTarget: Math.round(calorieTarget),
        weightChangeMsg
    };
}

// Render health metrics
function renderMetrics(name, metrics) {
    const grid = document.getElementById("metricsGrid");
    grid.innerHTML = `
        <div class="metric-card">
            <div class="label">Welcome, ${name}!</div>
            <div class="unit">Let's achieve your goals together</div>
        </div>
        <div class="metric-card">
            <div class="label">BMI</div>
            <div class="value ${metrics.bmiClass}">${metrics.bmi}</div>
            <div class="unit">${metrics.bmiCategory}</div>
        </div>
        <div class="metric-card">
            <div class="label">Daily Calories</div>
            <div class="value">${metrics.calorieTarget}</div>
            <div class="unit">${metrics.weightChangeMsg}</div>
        </div>
        <div class="metric-card">
            <div class="label">TDEE</div>
            <div class="value">${metrics.tdee}</div>
            <div class="unit">Maintenance calories</div>
        </div>
        <div class="metric-card">
            <div class="label">BMR</div>
            <div class="value">${metrics.bmr}</div>
            <div class="unit">At rest calories</div>
        </div>
    `;
}

// Render workout routine
function renderWorkout(workoutPlan) {
    const subtitle = document.getElementById("workoutSubtitle");
    subtitle.textContent = `Specially designed for ${workoutPlan.title}`;
    
    const container = document.getElementById("workoutDays");
    container.innerHTML = workoutPlan.days.map(day => `
        <div class="workout-day">
            <h3>${day.name}</h3>
            <div class="focus">${day.focus}</div>
            <ul>
                ${day.exercises.map(ex => `
                    <li>
                        ${ex.name}
                        <span class="sets-reps"> - ${ex.sets} x ${ex.reps}</span>
                    </li>
                `).join("")}
            </ul>
        </div>
    `).join("");
}

// Render meal plan
function renderMealPlan(mealPlan, calorieTarget) {
    const adjusted = adjustCalories(mealPlan, calorieTarget);
    const subtitle = document.getElementById("mealSubtitle");
    subtitle.textContent = `${adjusted.name} - ~${Math.round(calorieTarget)} calories/day`;
    
    const container = document.getElementById("mealDays");
    container.innerHTML = adjusted.days.map(day => `
        <div class="meal-day">
            <h3>${day.name} - ${day.totalCalories} cal</h3>
            ${day.meals.map(meal => `
                <div class="meal-item">
                    <div class="meal-name">${meal.name}</div>
                    <div class="calories">${meal.calories} cal</div>
                </div>
            `).join("")}
        </div>
    `).join("");
}

// Simple calorie adjustment
function adjustCalories(mealPlan, targetCalorie) {
    const targetPerMeal = targetCalorie / 4;
    const scaleFactor = targetPerMeal / 400; // Assume average 400 cal per meal
    
    const adjusted = JSON.parse(JSON.stringify(mealPlan));
    adjusted.days.forEach(day => {
        day.totalCalories = Math.round(day.totalCalories * scaleFactor);
        day.meals.forEach(meal => {
            meal.calories = Math.round(meal.calories * scaleFactor);
        });
    });
    
    return adjusted;
}

// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
    console.log("FitPlan Pro is ready!");
    
    // Form handler
    document.getElementById("profileForm").addEventListener("submit", function(e) {
        e.preventDefault();
        
        const formData = {
            name: document.getElementById("name").value,
            age: parseInt(document.getElementById("age").value),
            gender: document.getElementById("gender").value,
            height: parseInt(document.getElementById("height").value),
            weight: parseInt(document.getElementById("weight").value),
            activityLevel: document.getElementById("activityLevel").value,
            fitnessGoal: document.getElementById("fitnessGoal").value,
            dietPreference: document.getElementById("dietPreference").value
        };
        
        // Calculate metrics
        const metrics = calculateMetrics(formData);
        
        // Get workout and meal plans
        const workoutPlan = workoutPlans[formData.fitnessGoal];
        const mealPlan = mealPlans[formData.dietPreference];
        
        // Render results
        renderMetrics(formData.name, metrics);
        renderWorkout(workoutPlan);
        renderMealPlan(mealPlan, metrics.calorieTarget);
        
        // Show results section
        document.getElementById("inputSection").classList.add("hidden");
        document.getElementById("resultsSection").classList.remove("hidden");
        
        // Scroll to results
        document.getElementById("resultsSection").scrollIntoView({ behavior: "smooth" });
    });
});

// Reset form - make it global so onclick works
window.resetForm = function() {
    document.getElementById("profileForm").reset();
    document.getElementById("inputSection").classList.remove("hidden");
    document.getElementById("resultsSection").classList.add("hidden");
    window.scrollTo({ top: 0, behavior: "smooth" });
}
