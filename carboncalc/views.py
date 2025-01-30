from django.shortcuts import render
from .forms import CarbonFootprintForm

def calculate_footprint(request):
    result = None
    if request.method == "POST":
        form = CarbonFootprintForm(request.POST)
        if form.is_valid():
            transport = form.cleaned_data['transport'] * 0.21  # Avg CO2 emission per km (kg)
            electricity = form.cleaned_data['electricity'] * 0.5  # Avg CO2 emission per kWh (kg)
            
            diet_emission = {
                "vegan": 2.0,
                "vegetarian": 3.0,
                "non-veg": 7.0
            }
            diet = diet_emission[form.cleaned_data['diet']]  # Assign CO2 based on diet

            total_emission = transport + electricity + diet

            result = f"Your estimated daily carbon footprint is {total_emission:.2f} kg CO2."
    else:
        form = CarbonFootprintForm()

    return render(request, 'calculator/index.html', {'form': form, 'result': result})