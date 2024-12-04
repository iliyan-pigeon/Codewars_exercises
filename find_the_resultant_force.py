import math

def find_resultant_force(F1, F2, theta):
    # Convert the angle theta from degrees to radians
    theta_radians = math.radians(theta)
    
    # Calculate the resultant force R using the Law of Cosines
    R = math.sqrt(F1**2 + F2**2 + 2 * F1 * F2 * math.cos(theta_radians))
    
    # Calculate the angle φ using the formula
    phi = math.atan2(F2 * math.sin(theta_radians), F1 + F2 * math.cos(theta_radians))
    
    # Convert φ from radians to degrees
    phi_degrees = math.degrees(phi)
    
    # Return the results as a list
    return [R, phi_degrees]
  
