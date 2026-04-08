# FitPlan Pro - Personalized Fitness & Nutrition Application

## Overview

FitPlan Pro is a comprehensive web application that generates personalized fitness and meal plans based on user-provided health parameters. The application uses a modern Flask (Python) backend with responsive HTML/CSS frontend.

Video Recording Link - https://youtu.be/V6l-3WFFaWc

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
This entire project was **100% generated and implemented by Cline** - an advanced autonomous AI coding agent integrated into Visual Studio Code. No manual code modifications were performed.

**About Cline AI Agent:**
| Attribute | Details |
|-----------|---------|
| **Agent Type** | Autonomous Software Engineer / AI Coding Assistant |
| **Integration** | Visual Studio Code Extension |
| **Capabilities** | Full-stack development, file system operations, command execution, code analysis, debugging, documentation |
| **Languages Supported** | Python, JavaScript/TypeScript, HTML, CSS, SQL, Shell, and more |
| **Development Model** | Iterative conversational development with natural language instructions |

### AI Development Workflow
Cline autonomously built this application following this complete lifecycle:
✅ **Requirements Analysis** - Understood fitness & nutrition application requirements  
✅ **Architecture Design** - Selected Flask backend with Jinja2 templates  
✅ **Database Design** - Created structured workout and meal plan datasets  
✅ **Algorithm Implementation** - BMI/BMR/TDEE calculation logic  
✅ **Frontend Development** - Responsive HTML/CSS interface  
✅ **Feature Integration** - Allergen filtering, email functionality, YouTube links  
✅ **Testing & Debugging** - Iterative bug fixing and improvements  
✅ **Documentation** - Complete README.md and project documentation  

### AI Development Timeline
1. ✅ Initial project concept & requirements gathering
2. ✅ Health metrics calculator implementation
3. ✅ 5-day workout plan system with 5 different programs
4. ✅ Indian meal plan database with 4 diet types
5. ✅ Allergen filtering and exclusion system
6. ✅ YouTube tutorial & recipe link integration
7. ✅ Email export functionality using mailto protocol
8. ✅ Flask backend conversion from vanilla JS
9. ✅ UI/UX polishing and responsive design
10. ✅ Complete documentation & final testing

### AI Agent Design Decisions
Cline independently made these architectural choices:
1. **Flask Framework** - Selected for minimal overhead and fast development
2. **Jinja2 Templates** - Server-side rendering for dynamic plan generation
3. **No External APIs** - All logic runs locally without external dependencies
4. **mailto Protocol** - Zero-configuration email solution
5. **Static Dataset Design** - All plans embedded directly for reliability
6. **Responsive CSS Grid** - Modern layout that works on all devices
7. **Progressive Enhancement** - Works without JavaScript enabled

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
- [ ] Real SMTP email integration
- [ ] Mobile app version

## License

This project is provided as-is for educational and personal use.

## Contact

For questions or feedback about this application, please refer to the developer.

---

**Built with ❤️ using Flask + Python + HTML/CSS**

**AI Assistant**: Cline (VS Code Extension)
