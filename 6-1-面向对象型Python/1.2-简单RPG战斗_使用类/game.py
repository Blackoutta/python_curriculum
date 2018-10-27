class mage(object):
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

class warrior(object):
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


player1 = mage("法师胡")
player2 = warrior("战士郭")
