'显式覆盖'的意思是：让一个子类继承父类之后，在子类中重新定义一些属性
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
    def __init__(self, name):
        self.class_name = "圣骑士"  # 我尝试使用显式覆盖的方式改写职业名称

player1 = Mage("甘道夫")
player2 = Warrior("列奥尼达斯")
player3 = Paladin("乌瑟尔")
--------------------------------------------------------------------------------
用 python -i 模式运行这段代码
运行 player3.class_name你会得到"圣骑士"，证明class_name这个属性我们修改成功了

但是其他属性呢？
运行player3.hp试试，你会发现程序出错
原因是：如果你尝试去覆写(override)某个方法，程序会首先清空这个方法中的所有内容，再用你重写的内容覆写上去
这里可以看出显示覆盖也'不会节约你太多时间和工作量'
