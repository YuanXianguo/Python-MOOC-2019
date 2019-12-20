alien_0 = {'x-position': 0, 'y-position': 0, 'speed': 'fast',}
print("Original x-position: " + str(alien_0['x-position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3

alien_0['x-position'] = alien_0['x-position'] + x_increment
print("Now x-position: " + str(alien_0['x-position']))
