from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    """场景类"""

    def enter(self):
        """进入场景"""
        print("场景尚未被设置。")
        print("请设置具体子类场景后，再运行enter()")
        exit(1)

class Engine(object):
    """引擎类"""

    def __init__(self, scene_map):
        """让引擎导入对象，便于操纵"""
        pass

    def play(self):
        """开始游玩。所谓游玩，就是在引擎中实例化各种制作好的类，然后将他们当做对象（工具）来制作整个游戏的规则和流程。
        这里我们只实例化了地图这个类，你可以尝试加入更多的类来丰富玩法，例如：加入角色创建系统、战斗系统等"""
        pass

class Death(Scene):
    """场景：死亡"""

    def enter(self):
        pass

class Victory(Scene):
    """场景：胜利"""

    def enter(self):
        pass

class Tavern(Scene):
    """场景：酒馆"""

    def enter(self):
        pass

class Entrance(Scene):
    """场景：入口"""

    def enter(self):
        pass

class CrossRoads(Scene):
    """场景：十字路口"""

    def enter(self):
        pass

class BanditCamp(Scene):
    """场景：盗贼营地"""

    def enter(self):
        pass

class Map(object):
    """地图类"""

    def __init__(self, start_scene):
        """传递初始场景的名字"""
        pass

    def next_scene(self, scene_name):
        """设定下一个场景"""
        pass

    def opening_scene(self):
        """运行初始场景（将下一个场景设为初始场景）"""
        pass

a_map = Map('酒馆')
a_game = Engine(a_map)
a_game.play()
