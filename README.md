# FitPlan Pro - Personalized Fitness & Nutrition Application

## Overview

FitPlan Pro is a comprehensive web application that generates personalized fitness and meal plans based on user-provided health parameters. The application uses a modern Flask (Python) backend with responsive HTML/CSS frontend.

## Features

### 1. Health Metrics Calculator
- **BMI (Body Mass Index)** - Calculates BMI with color-coded categories (Underweight, Normal, Overweight, Obese)
- **BMR (Basal Metabolic Rate)** - Calculates calories burned at rest using Mifflin-St Jeor equation
- **TDEE (Total Daily Energy Expenditure)** - Accounts for activity level
- **Personalized Calorie Target** - Adjusted based on fitness goals (lose weight, gain muscle, maintain)

### 2. Personalized Workout Routines
- **5-Day Workout Plans** customized to fitness goals:
  - Weight Loss Program (HIIT-focused)
  - Muscle Building Program (Push/Pull/Legs split)
  - Endurance Building Program (Cardio-focused)
  - Flexibility & Mobility Program (Stretching/Yoga)
  - General Fitness Program (Balanced)
- **YouTube Tutorial Links** for each exercise
- Detailed sets and reps for each workout

### 3. Indian Meal Plans
- **4 Diet Preferences**: Non-Vegetarian, Vegetarian, Vegan, Pescatarian
- **Simple, Household Ingredients**: All meals use affordable, accessible Indian kitchen staples
- **Allergen Filtering**: Automatically excludes meals containing user's allergens
- **8 Common Allergens Supported**: Peanuts, Tree Nuts, Dairy, Eggs, Wheat/Gluten, Soy, Fish, Shellfish
- **YouTube Recipe Links** for each meal
- **Calorie Scaling** based on user's daily calorie target

### 4. Email Plan Feature
- Send complete fitness plan via email using system mail client
- Includes all health metrics, workout details, and meal plans

## Technology Stack

### Backend
- **Python 3.x** - Core programming language
- **Flask 3.x** - Lightweight web framework
- **Jinja2** - Template engine for dynamic HTML

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern responsive design with CSS Grid and Flexbox
- **Vanilla JavaScript** - Client-side interactivity (original version)

### Development Tools
- **Virtual Environment (venv)** - Python dependency isolation
- **pip** - Package manager

## Project Structure

```
EAV3/
├── app.py                 # Flask application with all backend logic
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   ├── index.html        # User input form template
│   └── result.html      # Results display template
├── venv/                 # Virtual environment (created during setup)
├── styles.css            # Original CSS file (standalone version)
└── app.js              # Original JavaScript file (standalone version)
```

## Installation & Setup

### Prerequisites
- Python 3.x installed
- Internet connection (for YouTube links)

### Setup Steps

1. **Navigate to project directory:**
   ```bash
   cd c:\EAV3
   ```

2. **Create virtual environment (if not exists):**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment:**
   ```bash
   venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```

6. **Open in browser:**
   Navigate to `http://127.0.0.1:5000`

## Usage Guide

### Step 1: Enter Personal Information
- Fill in your name, age, gender, height (cm), and weight (kg)

### Step 2: Select Activity Level
- Sedentary: Little or no exercise
- Light: 1-3 days/week
- Moderate: 3-5 days/week
- Active: 6-7 days/week
- Extremely Active: Athlete-level

### Step 3: Choose Fitness Goal
- Lose Weight: Calorie deficit (-500 cal/day)
- Build Muscle: Calorie surplus (+300 cal/day)
- Improve Endurance: Cardio-focused
- Improve Flexibility: Stretching/Yoga focused
- General Health: Balanced approach

### Step 4: Select Diet Preference
- Non-Vegetarian: Includes chicken, fish, eggs
- Vegetarian: No meat, includes dairy
- Vegan: No animal products
- Pescatarian: Fish/sea food, eggs, dairy

### Step 5: Specify Allergies
- Select any allergens from the checklist
- Meals containing selected allergens will be automatically filtered out

### Step 6: Generate & View Plan
- Click "Generate My Plan"
- View personalized health metrics
- Browse 5-day workout routine
- Explore 5-day meal plan
- Click "Watch" buttons for exercise tutorials
- Click "Recipe" buttons for meal preparation videos

### Step 7: Send via Email
- Enter email address
- Click "Send Plan" to open email client with complete plan

## AI Agent Information

### Development Assistant
This project was developed with the assistance of **Cline** - an AI coding assistant integrated into Visual Studio Code.

**About Cline:**
- **Developer**: Cline
- **Type**: AI-powered coding assistant / autonomous coding agent
- **Capabilities**:
  - File creation and modification
  - Command execution
  - Code analysis and generation
  - Problem-solving across multiple programming languages
  - Web development support (HTML, CSS, JavaScript, Python, Flask)

### Prompt Engineering
The application was built iteratively through conversation:
1. Initial requirements for fitness tracking app
2. Addition of workout generation
3. Integration of Indian meal plans
4. Allergen filtering system
5. YouTube video integration
6. Email functionality
7. Flask/Python conversion
8. Final polish and documentation

### Key Development Decisions

1. **Flask over Django**: Chosen for lightweight, straightforward routing
2. **Jinja2 Templates**: Server-side rendering for dynamic content
3. **mailto: Protocol**: Simple email solution without SMTP configuration
4. **YouTube Search Links**: Reliable video discovery without dead links
5. **Indian Meal Database**: Curated list of simple, affordable household meals

## Nutritional Information

### Indian Kitchen Staples Used
- **Grains**: Rice, Wheat (roti), Poha (rice flakes)
- **Legumes**: Dal (lentils), Rajma (kidney beans), Chana (chickpeas)
- **Vegetables**: Potato, Paneer, Mixed vegetables
- **Proteins**: Chicken, Fish, Eggs
- **Dairy**: Milk, Curd, Buttermilk, Paneer, Lassi
- **Snacks**: Roasted chana, Makhana, Sprouts

### Sample Meal Day (Vegetarian)
- **Breakfast**: Poha (250 cal)
- **Lunch**: Dal Tadka with Rice (420 cal)
- **Snack**: Roasted Peanuts (100 cal)
- **Dinner**: Paneer Bhurji with Roti (450 cal)

## Health Disclaimer

> ⚠️ **Important**: This application provides general fitness and nutrition guidance. It is not a substitute for professional medical advice. Please consult a healthcare provider or certified nutritionist before starting any fitness or diet program, especially if you have pre-existing health conditions.

## Future Enhancements

Potential additions for future versions:
- [ ] User authentication and profile saving
- [ ] Progress tracking over time
- [ ] Integration with fitness wearables
- [ ] Expanded meal database with more regional cuisines
- [ ] Macro nutrient breakdown (protein, carbs, fats)
- [ ] Shopping list generation
- [ ] Real SMTP email integration
- [ ] Mobile app version

## License

This project is provided as-is for educational and personal use.

## Contact

For questions or feedback about this application, please refer to the developer.

---

**Built with ❤️ using Flask + Python + HTML/CSS**

**AI Assistant**: Cline (VS Code Extension)
