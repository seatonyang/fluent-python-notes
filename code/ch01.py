# -*- coding: utf-8 -*-
# -------------------------------

    # @软件：PyCharm
    # @PyCharm：2024.2.4
    # @Python：3.12.4
    # @项目：fluent_python_codes

# -------------------------------

    # @文件：ch01.py
    # @时间：2024/11/24 17:06
    # @作者：Seaton
    # @邮箱：seaton.joeng@gmail.com

# -------------------------------

import collections
import random

# 使用collections.namedtuple创建一个不可变的Card对象，只包含变量，不包含方法。
Card = collections.namedtuple("Card", ["rank", "suit"])

class FrenchDeck:
    # 定义静态变量，属于整个类，而不属于某个实例
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        # 初始化时，创建一副牌，每个元素是一个Card对象
        self._card = [Card(rank, suit) for rank in FrenchDeck.ranks for suit in FrenchDeck.suits]
        # 这里不能用zip，zip要求两个变量长度一致且一一对应，如果用了，结果就会只有2，3，4，5四张牌。
        # self._card = [Card(rank, suit) for rank, suit in zip(FrenchDeck.ranks, FrenchDeck.suits)]

    def __len__(self):
        # 返回牌组中牌的数量
        return len(self._card)

    def __getitem__(self, position):
        # 允许通过索引访问牌组中的牌
        return self._card[position]

deck = FrenchDeck()

# 创建一个字典，给每个花色赋值，方便计算排序。
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card: Card) -> int:
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

sorted_deck = sorted(deck._card, key=spades_high)
print(sorted_deck)

