'''

conditionals:

if time == seven:
    leave the beed
else:
    sleep more

'''

""" time = 13
if time >= 14:
    print('It is time, Join the Python lesson')
else:
    print('No one might be in the Zoom') """


a = 5.5

if type(a) == int or type(a) == float:
    if a  > 0:
        print(f'{a} is a positive number')
    elif a < 0:
        print(f'{a} is a negative number')
    elif a == 0:
        print(f'The number is {a}')

else:
    print('All values should a number')


isRaining = False 
if isRaining:
    print('Take an umbrella')
else:
    print('It is a shinny day, go out freely and enjoy your day')


weather = input('Enter the weather today? ').lower()
print(weather)
if weather == 'rainy':
    print('Take an umbrella')
elif weather == 'sunny':
      print('It is a shinny day, go out freely and enjoy your day')
elif weather == 'cloudy':
     print('It may rain')
elif weather == 'foggy' or weather == 'gloomy':
     print('Visibility might be hamperred because it is foggy or gloomy')
elif weather == 'snowy':
     print('Watch out, it migh be slippery')
else:
     print('No one know about the weather today')


weather = input('Enter the weather today? ').lower()
match weather:
    case 'rainy':
        print('Take an umbrella')

    case  'sunny':
        print('It is a shinny day, go out freely and enjoy your day')
    case  'cloudy':
        print('It may rain')
    case  'foggy':
        print('Visibility might be hamperred because it is foggy or gloomy')
    case 'gloomy':
        print(' gloomy')
    case 'snowy':
        print('Watch out, it migh be slippery')
    case _:
        print('No one know about the weather today')







    