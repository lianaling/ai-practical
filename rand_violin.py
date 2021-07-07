import random

# List decalration

keys = [
    "A",
    "A flat",
    "B",
    "B flat",
    "D",
    "E",
    "G"
]

scale_or_arp = [
    "arpeggios",
    "scale"
]

chords = [
    "major",
    "minor harmonic",
    "minor melodic"
]

notes = [
    "even notes",
    "long tonic"
]

bowing = [
    "slur bow",
    "separate bow"
]

# Randomise
cont = "y"
count = 0
while cont == "y":
    print(random.choice(keys), random.choice(chords), ",", random.choice(scale_or_arp), ",",
          random.choice(notes), ",", random.choice(bowing))
    count += 1
    print("Times practised: ", count, "\n")
    cont = input("'y' for continue, 'n' for stop: ")
    print("=" * 20)
