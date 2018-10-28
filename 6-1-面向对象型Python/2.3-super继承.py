'super继承'实际上时'显式覆盖'的一种延伸
刚才我们看到了，如果我们尝试去覆写一个方法，比如__init__，里面的所有内容会被清空
但是这里如果我们用.super()方法，就可以将父类中的属性找回来，然后我们就可以'只修改'那些'需要被改动'的属性，而不是'重写所有属性'
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
class Paladin(Warrior):
    """战士转职后会成为圣骑士，他们拥有更高的属性以及治疗技能"""
    def __init__(self, name): # 这里我们是在显式覆盖，之前所有的属性都会被清空
        super(Paladin, self).__init__(name) # 但是我们通过使用.super().__init__方法，从父类中再次找回了所有的属性
        # 接下来我只改动了一部分属性，让圣骑士相对于战士变得更强，而其他属性保持不变
        self.class_name = "圣骑士"
        self.hp = 250
        self.mp = 100
        self.m_atk = 70

    # 我为圣骑士新增了一个回血技能
    def holylight(self, target):
        """圣光：治疗单个目标，回复目标一定的生命值(25% * 魔法攻击力)。"""
        print("{}对{}施展圣光!".format(self.name, target.name))
        heal = self.atk * 0.25
        print("{}治疗了{}{}点生命！".format(self.name, target.name, heal))
        target.hp += heal


player1 = Mage("甘道夫")
player2 = Warrior("列奥尼达斯")
player3 = Paladin("乌瑟尔")
--------------------------------------------------------------------------------
用 python -i 模式运行这段代码
你会看到一个增强的圣骑士，他的某些属性相较于战士更高，他会使用战士的盾击，也会使用一个新技能——圣光 来为自己或者他人回血！
在__init__中使用super()是一个很常见的手法
