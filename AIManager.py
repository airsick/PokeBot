from neural import NeuralNetwork
from engine import Engine
from engine2 import Engine as Engine2

class AIManager:
    def __init__(self):
        chal = Engine()
        chal.main()
        play = Engine2()
        play.main()
        play.game(2)
        chal.game(1)
Ai = AIManager()