from enum import IntEnum

# states characters can be in from the eval function
class Power(IntEnum):
    WEAK = 20
    MEDIUM = 30
    STRONG = 40

def attack(target, power):
    target.damage(power)

def weak_attack(user, target):
    user.threat += 1
    attack(target, Power.WEAK)

def medium_attack(user, target):
    user.threat += 2
    attack(target, Power.MEDIUM)

def strong_attack(user, target):
    user.threat += 3
    attack(target, Power.STRONG)
