'隐式继承'的意思是：让一个'子类'无条件继承一个'父类'的'所有属性和方法'，继承后你可以创建更多的属性和方法
--------------------------------------------------------------------------------.
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
class Paladin(Warrior): # 创建类的时候，将需要继承的类当做参数传递进去即可
    """战士转职后会成为圣骑士，他们拥有更高的属性以及治疗技能"""

player1 = Mage("甘道夫")
player2 = Warrior("列奥尼达斯")
player3 = Paladin("乌瑟尔")
--------------------------------------------------------------------------------
用 python -i 模式运行这段代码，你会发现Paladin这个类跟Warrior类一模一样
他们拥有相同的属性、技能，连职业名称都一样，唯一的不同只是人物名称罢了
这里可以看出隐式继承的'局限性非常大'
