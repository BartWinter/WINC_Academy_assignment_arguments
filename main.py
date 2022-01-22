# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

#Part 1 Greet Template
#Define a function greet that takes these arguments, in this order:
#A name (str);
#A greeting template (str). Set this template parameter to 'Hello, <name>!' by default.
#greet should return a string where <name> in the greeting template is replaced by the name given in the first parameter. 
#You do not need to handle the case where <name> is not in the greeting template string.

def greet(name: str, greeting_template: str ='Hello, <name>!'):
        greeting = greeting_template.replace("<name>", name)
        return greeting

print(greet('Janneke', ))

#Part 2 Force
#Write a function force that takes two arguments
#mass(float);
#body (str), with 'earth' as its default. Your implementation should support all 11 bodies listed on the reference website given. 
#Before using the gravity of a celestial body round its gravity factor to 1 decimal. 
#The arguments should be named exactly as listed so that we can call them with keyword arguments. 
#force should return the force that is exerted given the mass and body

celestial_body = {
    'sun': 274,
    'jupiter': 24.9,
    'neptune': 11.2,
    'saturn': 10.4,
    'earth': 9.8,
    'uranus': 8.9,
    'venus': 8.9,
    'mars': 3.7,
    'mercury': 3.7,
    'moon': 1.62,
    'pluto':0.6
    }

def force(mass: float, body: str = 'earth'):
    body_value = celestial_body.get(body)
    force_calculation = mass * body_value
    return force_calculation

print(force(1, 'moon'))
    
#Part 3 Gravity
#write a function pull that takes three arguments:
#m1 an object's mass in kg (float);
#m2 another object's mass in kg (float);
#d their distance in meters (float).
#pull shoult return th gravitional pull that these two objects have on each other. You can test your function by entering in the examples given on the website.

def pull(m1: float, m2: float, d: float):
    gravitational_constant = 6.674e-11
    calculation_pull = gravitational_constant * ((m1 * m2)/d**2)
    return calculation_pull 
    
print(pull(800, 1500, 3))



