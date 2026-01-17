# height = 5.7
# weight = 60

# # bmi = weight in kgs / height in meters

# heightinMeter = height * 0.4536

# bmi = weight /(heightinMeter*heightinMeter)

# print("BMI: ", bmi)


# bmi = weight in kgs / height in meters


def bmi(height, weight):
    heightinMeter = height * 0.4536
    bmi = weight / (heightinMeter * heightinMeter)
    return round(bmi,2)

print(bmi(5.5, 60))
print(bmi(6.2, 55))