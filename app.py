from flask import Flask, render_template, request

app = Flask(__name__)

# Welcome page
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

# Age selection landing page
@app.route('/select_age_group')
def landing():
    return render_template('landing.html')

# Main calorie tracker page
@app.route('/calorie_tracker', methods=['GET', 'POST'])
def calorie_tracker():
    result = None
    age_group = request.args.get('age_group', '20-30')  # Default to '20-30' if not specified
    
    if request.method == 'POST':
        name = request.form['name']
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        activity_level = request.form['activity']
        
        # Calculate calories
        calories = calculate_calories(weight, height, activity_level)
        
        # Prepare result dictionary for rendering
        result = {
            'name': name,
            'calories': calories,
            'age_group': age_group
        }
        
    return render_template('index.html', result=result, age_group=age_group)

# Utility function for calculating calories
def calculate_calories(weight, height, activity_level):
    bmr = 10 * weight + 6.25 * height - 5 * 25 + 5  # Default values for demonstration
    activity_factors = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725
    }
    daily_calories = bmr * activity_factors[activity_level]
    calories_to_burn = daily_calories - 500  # 500-calorie deficit for weight loss
    return round(calories_to_burn, 2)

if __name__ == '__main__':
    app.run(debug=True)
