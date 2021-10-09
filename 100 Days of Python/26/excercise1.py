# sentence = 'What is the Airspeed Velocity of an Unladen Swallow'
# listt = sentence.split()
# print(listt)
# mydict = {words : len(words) for words in sentence.split()}
# print(mydict)
weather_c ={
    'Monday': 12,
    'Tuesday': 14,
    'Wednesday': 15,
    'Thursday': 14,
    'Friday': 21,
    'Saturday': 22,
    'Sunday': 24
}
weather_f={Day: Frehn*9/5 +32 for (Day, Frehn) in weather_c.items()}
print(weather_f)