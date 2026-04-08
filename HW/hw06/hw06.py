from math import prod
from time import sleep


passphrase = 'REPLACE_THIS_WITH_PASSPHRASE'

def midsem_survey(p):
    """
    你不需要理解这段代码。
    >>> midsem_survey(passphrase)
    '2bf925d47c03503d3ebe5a6fc12d479b8d12f14c0494b43deba963a0'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()


class Product:
    """商品类，包含名称、价格和库存属性。"""
    def __init__(self, name, price):
        self.name = name      # 商品名称
        self.price = price    # 商品价格
        self.count = 0        # 库存数量


class VendingMachine:
    """一台售卖某种商品的自动售货机，售价为指定价格。

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'Please add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'Please add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self, product, price):
        """设置商品及其价格，以及其他实例属性。"""
        # 创建 Product 对象，这样 product 就有 name, price, count 属性了
        self.product = Product(product, price)
        self.money = 0

    def restock(self, n):
        """向库存中添加 n 个商品，并返回更新后的库存信息。

        例如：Current candy stock: 3
        """
        self.product.count += n
        return f"Current {self.product.name} stock: {self.product.count}"

    def add_funds(self, n):
        """如果机器缺货，返回提示用户补货的信息
        （并退还他们的 n 美元）。

        例如：Nothing left to vend. Please restock. Here is your $4.

        否则，将 n 添加到余额中，并返回更新后的余额信息。

        例如：Current balance: $4
        """
        if self.product.count == 0:
            return f"Nothing left to vend. Please restock. Here is your ${n}."
        else:
            self.money += n
            return f"Current balance: ${self.money}"

    def vend(self):
        """如果有足够的库存和资金，则发放商品并返回信息。
        相应地更新库存和余额。

        例如：Here is your candy and $2 change.

        如果条件不满足，返回提示如何解决问题的信息。

        例如：Nothing left to vend. Please restock.
              Please add $3 more funds.
        """
        if self.money >= self.product.price and self.product.count > 0:
            change = self.money - self.product.price
            self.product.count -= 1
            self.money = 0
            if change > 0:
                return f"Here is your {self.product.name} and ${change} change."
            else:
                return f"Here is your {self.product.name}."
        else:
            if self.product.count == 0:
                return "Nothing left to vend. Please restock."
            else:
                return f"Please add ${self.product.price - self.money} more funds."


def store_digits(n):
    """将正整数 n 的各位数字存储在一个链表中。

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    >>> store_digits(2450)
    Link(2, Link(4, Link(5, Link(0))))
    >>> store_digits(20105)
    Link(2, Link(0, Link(1, Link(0, Link(5)))))
    >>> # 检查是否使用了受限函数
    >>> import inspect, re
    >>> cleaned = re.sub(r"#.*\\n", '', re.sub(r'"{3}[\s\S]*?"{3}', '', inspect.getsource(store_digits)))
    >>> print("Do not use str or reversed!") if any([r in cleaned for r in ["str", "reversed"]]) else None
    """
    "*** 请在这里填写代码 ***"


def deep_map_mut(func, s):
    """通过将链表 s 中的每个元素替换为调用 func 后的结果来修改深层链表。
    不创建新的 Link（因此不使用 Link 的构造函数）。

    不返回修改后的 Link 对象。

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print(link1)
    <3 <4> 5 6>
    >>> # 禁止在调用 deep_map_mut 之前创建新的 Links
    >>> Link.__init__, hold = lambda *args: print("Do not create any new Links."), Link.__init__
    >>> try:
    ...     deep_map_mut(lambda x: x * x, link1)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(link1)
    <9 <16> 25 36>
    """
    "*** 请在这里填写代码 ***"


def two_list(vals, counts):
    """
    根据传入的两个列表返回一个链表。假设 vals 和 counts 大小相同。
    vals 中的元素表示值，counts 中对应的元素表示该值在最终链表中出现的次数。
    假设 counts 中的所有元素都大于 0。假设两个列表都至少有一个元素。
    >>> a = [1, 3]
    >>> b = [1, 1]
    >>> c = two_list(a, b)
    >>> c
    Link(1, Link(3))
    >>> a = [1, 3, 2]
    >>> b = [2, 2, 1]
    >>> c = two_list(a, b)
    >>> c
    Link(1, Link(1, Link(3, Link(3, Link(2)))))
    """
    "*** 请在这里填写代码 ***"


class Link:
    """一个链表。

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # 显示 repr(s) 的内容
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # 打印 str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
