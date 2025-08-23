t_p = 20    # talents -> pound
p_l = 32    # pounds -> lots
l_g = 13.3  # lot -> grams
kg = 1000   # grams -> kilograms

# Ask for input
talents = float(input("talents:\n"))
pounds = float(input("pounds:\n"))
lots = float(input("lots:\n"))

# Convert everything to grams
g_t = (talents * t_p * p_l * l_g)
g_p = (pounds * p_l * l_g)
g_l = (lots * l_g)

# Add grams together
total_g = g_t + g_p + g_l

# Split into kilograms and grams
kilograms = total_g // kg
grams = total_g % kg

#Result
print(f"The weight in modern units:\n{int(kilograms)} kilograms and {grams:.2f} grams")