import random

# 法师职业和技能
def Mage(name):
    """这是一个class(类), 你可以把它想象成一个蓝图，它可以创建法师职业的属性和技能"""
    dict = {}
    dict.setdefault("hp", 100)
    dict.setdefault("mp", 300)
    dict.setdefault("atk", 20)
    dict.setdefault("m_atk", 100)
    dict.setdefault("name", name)
    return dict

def fireball(player, target):
    """火球术：对单体目标造成伤害(125% * 法术攻击)。"""
    print("{}对{}施展火球术!".format(player["name"], target["name"]))
    damage = player["m_atk"]
    print("{}对{}造成了{}点伤害！".format(player["name"], target["name"], damage))
    target["hp"] -= damage


# 战士职业和技能
def Warrior(name):
    """这是一个class(类), 你可以把它想象成一个蓝图，它可以创建战士职业的属性和技能"""
    dict = {}
    dict.setdefault("hp", 200)
    dict.setdefault("mp", 50)
    dict.setdefault("atk", 100)
    dict.setdefault("m_atk", 20)
    dict.setdefault("name", name)
    return dict

def shieldbash(player, target):
    """盾击：对单体目标造成伤害(25% * 攻击力)。"""
    print("{}对{}施展盾击!".format(player["name"], target["name"]))
    damage = player["atk"] * 0.25
    print("{}对{}造成了{}点伤害！".format(player["name"], target["name"], damage))
    target["hp"] -= damage


# 将玩家1设定为法师，玩家2设定为战士
player1 = Mage("法师胡")
player2 = Warrior("战士郭")
