class Mage(object):
    """这是一个class(类), 你可以把它想象成一个蓝图，它可以创建法师职业的属性和技能"""
    def __init__(self, name):
        self.class_name = "法师"
        self.hp = 100
        self.mp = 300
        self.atk = 20
        self.m_atk = 100
        self.name = name

    def fireball(self, target):
        """火球术：对单体目标造成伤害(125% * 法术攻击)。"""
        print("{}对{}施展火球术!".format(self.name, target.name))
        damage = self.m_atk * 1.25
        print("{}对{}造成了{}点伤害！".format(self.name, target.name, damage))
        target.hp -= damage
class Warrior(object):
    """这是一个class(类), 你可以把它想象成一个蓝图，它可以创建战士职业的属性和技能"""
    def __init__(self, name):
        self.class_name = "战士"
        self.hp = 200
        self.mp = 50
        self.atk = 100
        self.m_atk = 20
        self.name = name

    def shieldbash(self, target):
        """盾击：对单体目标造成伤害(25% * 攻击力)。"""
        print("{}对{}施展盾击!".format(self.name, target.name))
        damage = self.atk * 0.25
        print("{}对{}造成了{}点伤害！".format(self.name, target.name, damage))
        target.hp -= damage

player1 = Mage("法师胡")
player2 = Warrior("战士郭")

# TODO: 以上是1.2文件夹中，game.py的代码， 创 建一个文件 my_game.py, 将上方代码复制进去
# TODO: 现在你来为这个游戏创建一个新职业，发挥你的想象力！（比如：猎人，术士，盗贼，牧师等）
# TODO: 在 def __init__ 中赋予你的职业各种属性
# TODO: 然后使用 def 为你的职业创建几个技能，可以是攻击技能，回复技能，或者BUFF技能。脑洞开大！
# TODO: 最后通过 player3 这个变量 让你的职业实体化
# TODO: 测试下你创造的职业，释放他/她的技能，看看是否会对自身或其他玩家的数值造成影响。
