def calculate_volume_of_sphere(radius):
	pi = 3.14
	volume  = (4/3) * pi * (radius)**3
	return volume

radius1 = 30
area1 = calculate_volume_of_sphere(radius1)
print(f"The volume of a sphere with radius {radius1} is: {area1}")

radius2 = 40
area2 = calculate_volume_of_sphere(radius2)
print(f"The volume of a sphere with radius {radius2} is: {area2}")