#!/usr/bin/env python3

import subprocess

#//Clear the terminal window//
subprocess.call('clear', shell=True)

def f_to_c (f_temp):
    c_temp = (f_temp - 32) * (5/9)
    return c_temp

def c_to_f (c_temp):
    f_temp = c_temp * (9/5) + 32
    return f_temp

def get_temp (unit):

    isfloat = False
    while not isfloat:
        print("Enter a tempurature.")
        if str(unit) == "F":
            temp = float(input("Fahrenheit: "))
            if isinstance(temp, float):
                print(temp,"F will be converted to Celcius.")
                isfloat = True
            else:
                print("\n[Error]: Input must be an integer or float!")
        elif str(unit) == "C":
            temp = float(input("Celcius: "))
            if isinstance(temp, float):
                print(temp,"C will be converted to Fahrenheit.")
                isfloat = True
            else:
                print("\n[Error]: Input must be an integer or float!")
        else:
            print('[Flag invalid]: Must be either "F" or "C"!')
    return temp

def get_force (mass, acceleration):
    return mass * acceleration

def get_energy(mass, c):
    return mass*c**2

def get_work (mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance
f100_in_celsius = f_to_c(100)
print(f100_in_celsius, "C")
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit, "F")
c_temp = f_to_c(get_temp("F"))
print(c_temp, "C" )
f_temp = c_to_f(get_temp("C"))
print(f_temp, "F")

train_mass = 10000
train_acceleration = 25
train_force = get_force(train_mass, train_acceleration)
print(train_force)
print('The GE train supplies ' + str(train_force) + ' Newtons of force.')
c = 3*10**8
bomb_mass = 10000
bomb_energy = get_energy(bomb_mass, c)
print('A 1kg bomb supplies ' + str(bomb_energy) + ' Joules.')

train_distance = 10000
train_work = get_work(train_mass, train_acceleration, train_distance)
print('The GE train does ' + str(train_work) + ' Joules of work over ' + str(train_distance) + ' meters.')

