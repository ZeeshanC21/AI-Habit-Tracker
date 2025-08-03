from flask import Flask, render_template, request, redirect, url_for, session, flash
import openai
import os
from datetime import datetime
import json
import re
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev-key-please-change-in-production')

# Configure OpenAI API
openai.api_key = os.getenv('OPENAI_API_KEY')

# In-memory storage for session data
habit_sessions = {}

def generate_habit_plan(habits):
    """Generate a 7-day habit plan using OpenAI API"""
    try:
        habits_text = ", ".join(habits)
        
        prompt = f"""
        Create a detailed 7-day habit-building plan for these habits: {habits_text}
        
        For each day (Day 1 through Day 7), provide:
        1. Specific, actionable tasks for each habit
        2. A motivational message or tip
        3. Realistic goals that build progressively
        
        Format the response as JSON with this structure:
        {{
            "overview": "Brief overview of the plan",
            "days": [
                {{
                    "day": 1,
                    "date_label": "Day 1",
                    "habits": [
                        {{
                            "habit": "habit name",
                            "task": "specific task for today",
                            "motivation": "motivational message"
                        }}
                    ],
                    "daily_tip": "General tip for the day"
                }}
            ]
        }}
        
        Make it encouraging, realistic, and progressively challenging.
        """
        
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful habit-building coach. Always respond with valid JSON."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2000,
            temperature=0.7
        )
        
        # Parse the JSON response
        plan_text = response.choices[0].message.content.strip()
        
        # Clean up the response to ensure it's valid JSON
        if plan_text.startswith('```json'):
            plan_text = plan_text[7:]
        if plan_text.endswith('```'):
            plan_text = plan_text[:-3]
        
        plan = json.loads(plan_text)
        return plan
        
    except Exception as e:
        print(f"Error generating plan: {e}")
        # Fallback plan if API fails
        return generate_fallback_plan(habits)

def generate_fallback_plan(habits):
    """Generate a simple fallback plan if OpenAI API is unavailable"""
    days = []
    
    motivational_tips = [
        "Start small, think big! Every journey begins with a single step.",
        "Consistency beats perfection. Focus on showing up every day.",
        "Your future self will thank you for the habits you build today.",
        "Progress, not perfection. Celebrate small wins along the way.",
        "Habits are the compound interest of self-improvement.",
        "The best time to start was yesterday. The second best time is now.",
        "You're building a better version of yourself, one day at a time."
    ]
    
    for day in range(1, 8):
        day_habits = []
        for habit in habits:
            if "water" in habit.lower():
                tasks = ["Drink 2 glasses of water", "Carry a water bottle", "Set hourly water reminders", 
                        "Drink water before meals", "Track your intake", "Try infused water", "Celebrate your hydration success"]
            elif "walk" in habit.lower() or "exercise" in habit.lower():
                tasks = ["Take a 10-minute walk", "Walk for 15 minutes", "Try a 20-minute walk", 
                        "Walk 25 minutes today", "Go for a 30-minute walk", "Add some hills or stairs", "Reflect on your progress"]
            elif "sleep" in habit.lower():
                tasks = ["Set a bedtime alarm", "Create a wind-down routine", "Put devices away 1 hour early", 
                        "Try reading before bed", "Practice deep breathing", "Keep your room cool and dark", "Review your sleep improvements"]
            else:
                tasks = [f"Practice {habit} for 5 minutes", f"Spend 10 minutes on {habit}", f"Dedicate 15 minutes to {habit}",
                        f"Work on {habit} for 20 minutes", f"Focus on {habit} for 25 minutes", f"Spend 30 minutes with {habit}", f"Reflect on your {habit} journey"]
            
            day_habits.append({
                "habit": habit,
                "task": tasks[day-1] if day <= len(tasks) else f"Continue practicing {habit}",
                "motivation": f"You're doing great with {habit}! Keep it up!"
            })
        
        days.append({
            "day": day,
            "date_label": f"Day {day}",
            "habits": day_habits,
            "daily_tip": motivational_tips[day-1]
        })
    
    return {
        "overview": f"Your personalized 7-day plan to build these amazing habits: {', '.join(habits)}. Remember, consistency is key!",
        "days": days
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_habits():
    habits = []
    
    # Get habits from form
    habit1 = request.form.get('habit1', '').strip()
    habit2 = request.form.get('habit2', '').strip()
    habit3 = request.form.get('habit3', '').strip()
    
    if habit1:
        habits.append(habit1)
    if habit2:
        habits.append(habit2)
    if habit3:
        habits.append(habit3)
    
    if not habits:
        flash('Please enter at least one habit!', 'error')
        return redirect(url_for('index'))
    
    # Generate session ID
    session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    try:
        # Generate the plan
        plan = generate_habit_plan(habits)
        
        # Store in session
        session['session_id'] = session_id
        session['habits'] = habits
        session['plan'] = plan
        session['created_at'] = datetime.now().isoformat()
        
        # Also store in in-memory storage
        habit_sessions[session_id] = {
            'habits': habits,
            'plan': plan,
            'created_at': datetime.now().isoformat()
        }
        
        return redirect(url_for('results'))
        
    except Exception as e:
        flash(f'Error generating plan: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/results')
def results():
    if 'plan' not in session:
        flash('No habit plan found. Please submit your habits first.', 'error')
        return redirect(url_for('index'))
    
    return render_template('results.html', 
                         habits=session.get('habits', []),
                         plan=session.get('plan', {}),
                         created_at=session.get('created_at', ''))

@app.route('/new')
def new_plan():
    session.clear()
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)