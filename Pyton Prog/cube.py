"""
Prisca Muleka 
01/19/2025

Description: This program calculates the surface area of a cube based on the length of one edge.
The surface area of a cube is given by the formula:
Surface Area = 6 * (edge length)^2
- Prompt the user to input the length of the edge of the cube.
- Calculate the surface area using the given formula.
- The program will display the surface area as output.
"""

# Input

#cuAsk user for the length of the cube's edge 
    
edge_length = int(input("Enter the length of one edge of the cube: "))

# Calculate the surface area of the cube
surface_area = 6 * (edge_length ** 2)

# Output


# output the surface area
print(f"The surface area of the cube is: {surface_area}")
