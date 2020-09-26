#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = input("Hello, what's your name?")
print("Hello", n)
c = input("How has today been going?")
d = c.lower()
#This command can only accept the words: horrible, bad, fine, good, great
if d == "horrible":
    print("If your day at rock bottom then it can only get better.")
elif d == "bad":
    print("At least your day isn't doing horrible, just do something your enjoy.")
elif d == "fine":
    print("At least your day hasn't been going bad.")
elif d == "good":
    print("That's good, keep working at yur day to make it even better.")
elif d == "great":
    print("If your day has been doing so good, then try to avoid doing anything that would ruin your great mood.")
#This command can only accept the words: sunny, raining, snowing, thunder, blizzard
a = input("What's the weather today?")
w = a.lower()
if w == "sunny":
    print("If it's sunny then you can go outside and play.")
elif w == "raining":
    print("If it's raining then try to stay inside and work on some indoor hobby or else you may catch a cold.")
elif w == "snowing":
    print("If it's snowing then go outside and make snowmen or throw some snowballs with your friends.")
elif w == "thunder":
    print("I don't think you should go outside. If there's thunder then that means you could get wet and cold or you could get struck by lightning.")
elif w == "blizzard":
    print("I reccomend that you wait until this blizzard ends before going out side to play in the snow.")
print("It was nice talking to you but I must go now. Goodbye", n)


# In[ ]:





# In[ ]:




