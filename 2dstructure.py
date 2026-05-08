characters = [
    {"name":"Sadia", "Association":"Forensics", "vehicle": "Evo 9"},
    {"name":"Jordan", "Association":"Detectives", "vehicle": "Civic type R"},
    {"name":"Alcina", "Association":"Mafia", "vehicle": "911 Turbo S"},
    {"name":"Diana", "Association":"Royals", "vehicle":"SF90 Stradale"}
]


for char in characters:
    print(char["name"], char["Association"], char["vehicle"], sep=", ")
