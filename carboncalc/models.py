from django.db import models

class CarbonFootprintEntry(models.Model):
    name = models.CharField(max_length=100)
    transport = models.FloatField()  # km traveled
    electricity = models.FloatField()  # kWh used
    diet = models.CharField(max_length=20, choices=[("vegan", "Vegan"), ("vegetarian", "Vegetarian"), ("non-veg", "Non-Vegetarian")])
    total_emission = models.FloatField()  # Calculated CO2 footprint

    def __str__(self):
        return f"{self.name} - {self.total_emission} kg CO2"
