#Developer: Kevin Robbs
#Title: MadLibs
#Description: This is a short example of string concantenation using madlibs

def madlibs(adj1, name, emotion1, verb1, noun, food, verb2, school, adj2, animal, location, ing1, emotion2, adj3, verb3, family_member, ing2, adj4):
	print(f"""One {adj1} morning, {name} woke up feeling {emotion1}. They quickly {verb1} out of bed and headed to the {noun} to start their day. After a hearty breakfast of {food}, they {verb2} to get ready for {school}.

On the way to {school}, {name} encountered a {adj2} {animal} in the {location}. It was {ing1} and seemed to be {emotion2}.

At {school}, {name} had to tackle a {adj3} project that required them to {verb3} for hours. Despite the challenge, they remained {emotion2} and eventually {verb1} it.

After a long day, {name} returned home and decided to {verb2} with their {family_member} before {ing2} into bed.

What an {adj4} day it had been!""")

print("""Welcome to Madlibs!
Please follow the prompts and enter the specific details of the madlibs. I hope you enjoy this fun little program!""")

madlibs(
adj1 = input("Adjective 1: "),
adj2 = input("Adjective 2: "),
adj3 = input("Adjective 3: "),
adj4 = input("Adjective 4: "),
emotion1 = input("Emotion 1: "),
emotion2 = input("Emotion 2: "),
verb1 = input("Verb 1 - not ending in ing: "),
verb2 = input("Verb 2 - not ending in ing: "),
verb3 = input("Verb 3 - not ending in ing: "),
food = input("Food: "),
name = input("Any name: "),
school = input("School: "),
animal = input("Animal: "),
location = input("Location: "),
ing1 = input("Verb ending in -ing: "),
ing2 = input("Verb ending in -ing: "),
noun = input("Noun: "),
family_member = input("Family Member: ")
)