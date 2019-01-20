type = {"Dragon": 0, "Rock": 1, "Steel": 2, "Ghost": 3, "Fairy": 4, "Normal": 5, "Fighting": 6, "Ice": 7, "Dark": 8,
         "Psychic": 9, "Electric": 10, "Bug": 11, "Ground": 12, "Flying": 13, "Grass": 14, "Fire": 15, "Poison": 16,
		 "None": 18, "Water": 17}


class Pokemon():
    def __init__(self):
        self.types =[type.get("None"),type.get("None")]
        self.moves = {}
        self.hp = 0
        self.level = 0

class Team():
	def __init__(self):
		self.myTeam = {}
		self.active = 0

class gameData():
	def __init__(self):
		self.teams = {}