"""
Exercise 5
Create a list with this content:
ACTION  ADVENTURE   SPORTS
GTA     ASSINS      FIFA 21
COD     CRASH       PRO 21
PUGB    THE SIMS    MOTO GP 21
"""
print("Exercise 5")
print("First option:")
print()

games = [
    [
        'ACTION',
        'GTA',
        'COD',
        'PUGB'
    ],

    [
        'ADVENTURE',
        'ASSINS',
        'CRASH',
        'THE SIMS'
    ],
    [
        'SPORTS',
        'FIFA 21',
        'PRO 21',
        'MOTO GP 21'
    ],
]
print("**** ACTION GAMES: ****")
print(games[0][1:])
print()

print("**** ADVENTURE GAMES: ****")
print(games[1][1:])
print()

print("**** SPORT GAMES: ****")
print(games[2][1:])
print()

print("Second option:")
gamesTable = [
    {
        "category": 'ACTION',
        "gamescat": ['GTA', 'COD', 'PUGB']
    },

    {
        "category": 'ADVENTURE',
        "gamescat": ['ASSINS', 'CRASH', 'THE SIMS']
    },
    {
        "category": 'SPORTS',
        "gamescat": ['FIFA 21', 'PRO 21', 'MOTO GP 21']
    },
]

for countcategory in gamesTable:
    print(f"---- {countcategory['category']} ----")
    for game in countcategory['gamescat']:
        print(game)