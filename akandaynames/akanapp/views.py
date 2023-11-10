from django.shortcuts import render
import datetime

day_names = {
    0: ("Kwadwo", "Adwoa"),     # Monday
    1: ("Kwabena", "Abena"),    # Tuesday
    2: ("Kweku", "Akua"),      # Wednesday
    3: ("Yaw", "Yaa"),         # Thursday
    4: ("Kofi", "Afia"),       # Friday
    5: ("Kwame", "Ama"),       # Saturday
    6: ("Kwasi", "Akosua")     # Sunday
}

def get_akan_name(day_of_week, gender):
    # Determine Akan name based on the day of the week and gender
    if gender.lower() == 'male':
        return day_names[day_of_week][0]
    elif gender.lower() == 'female':
        return day_names[day_of_week][1]
    else:
        return None

def get_akan_meaning(name):
    # Define a dictionary with meanings for each Akan name (you can extend this)
    name_meanings = {
        "Kwadwo": "Born on Monday",
        "Adwoa": "Born on Monday",
        "Kwabena": "Born on Tuesday",
        "Abena": "Born on Tuesday",
        "Kweku": "Born on Wednesday",
        "Akua": "Born on Wednesday",
        "Yaw": "Born on Thursday",
        "Yaa": "Born on Thursday",
        "Kofi": "Born on Friday",
        "Afia": "Born on Friday",
        "Kwame": "Born on Saturday",
        "Ama": "Born on Saturday",
        "Kwasi": "Born on Sunday",
        "Akosua": "Born on Sunday",
    }
    return name_meanings.get(name, "Meaning not available")

def home(request):
    if request.method == 'POST':
        # Retrieve user input from the form
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')

        # Parse the date of birth and get the day of the week (0-6, Monday-Sunday)
        birth_date = datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')
        day_of_week = birth_date.weekday()

        # Get the Akan name based on the day of the week and gender
        akan_name = get_akan_name(day_of_week, gender)

        # Get the meaning of the Akan name
        akan_meaning = get_akan_meaning(akan_name)

        return render(request, 'akanapp/home.html', {'akan_name': akan_name, 'akan_meaning': akan_meaning})

    return render(request, 'akanapp/home.html')

def about(request):
    return render(request, 'akanapp/about.html')


