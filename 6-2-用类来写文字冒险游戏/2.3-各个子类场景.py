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
        self.scene_map = scene_map

    def play(self):
        """开始游玩。所谓游玩，就是在引擎中实例化各种制作好的类，然后将他们当做对象（工具）来制作整个游戏的规则和流程。
        这里我们只实例化了地图这个类，你可以尝试加入更多的类来丰富玩法，例如：加入角色创建系统、战斗系统等"""
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('胜利')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):
    """场景：死亡"""

    def enter(self):
        input("YOU DIED...")

class Victory(Scene):
    """场景：胜利"""

    def enter(self):
        input("你打败了盗贼首领，赏金是你的了！")

class Tavern(Scene):
    """场景：酒馆"""

    def enter(self):
        input(dedent("""
            你走进了一个小酒馆，一大群赏金猎人正在围着一个告示板争论不休。
            上面是一张通缉令，看起来军队正在悬赏一名法外狂徒——罗伯特。
            根据情报，罗伯特在黑暗森林中已经安营扎寨，他是军队的肉中刺，眼中钉。
            你迅速撕下了这份通缉令，头也不回地朝着黑暗森林的方向走去...
        """))
        return "入口"

class Entrance(Scene):
    """场景：入口"""

    def enter(self):
        input(dedent("""
            你来到了入口...
        """))
        return "十字路口"

class CrossRoads(Scene):
    """场景：十字路口"""

    def enter(self):
        input(dedent("""
            你来到了十字路口...
        """))
        return "盗贼营地"

class BanditCamp(Scene):
    """场景：盗贼营地"""

    def enter(self):
        input(dedent("""
            你来到了盗贼营地...
        """))
        return "胜利"

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
