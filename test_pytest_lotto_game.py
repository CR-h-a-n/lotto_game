import pytest
from lotto_game import Card, Bag, do_str_2simbol


class TestCard:
    def test_init(self):
        test_card = Card()
        assert test_card.player_name == ''
        assert test_card.count_number == 0
        assert test_card.line0 == []
        assert test_card.line1 == []
        assert test_card.line2 == []

    def test_create_card(self):
        # этот тест для случайных строк в карточках, но вдруг когда-нибудь хотябы одна из строк когда-нибудь совпадёт...
        sim_empty = '_'
        test_card0 = Card()
        test_card0.create_card(sim_empty)
        test_card1 = Card()
        test_card1.create_card(sim_empty)
        test_card2 = Card()
        test_card2.create_card(sim_empty)
        assert test_card0.line0 != test_card1.line0
        assert test_card0.line0 != test_card2.line0
        assert test_card1.line0 != test_card2.line0
        assert test_card0.line1 != test_card1.line1
        assert test_card0.line1 != test_card2.line1
        assert test_card1.line1 != test_card2.line1
        assert test_card0.line2 != test_card1.line2
        assert test_card0.line2 != test_card2.line2
        assert test_card1.line2 != test_card2.line2

    def test_cross_number(self):
        current_number = '11'
        sim_crossed = 'x'
        test_card = Card()
        test_card.line0 = ['11', '__', '__', '__', '__', '__', '__', '__', '__']
        test_card.line1 = ['__', '__', '__', '__', '11', '__', '__', '__', '__']
        test_card.line2 = ['__', '__', '__', '__', '__', '__', '__', '__', '11']
        test_card.cross_number(current_number, sim_crossed)
        assert test_card.line0 == ['xx', '__', '__', '__', '__', '__', '__', '__', '__']
        assert test_card.line1 == ['__', '__', '__', '__', '11', '__', '__', '__', '__']
        assert test_card.line2 == ['__', '__', '__', '__', '__', '__', '__', '__', '11']
        test_card.cross_number(current_number, sim_crossed)
        assert test_card.line0 == ['xx', '__', '__', '__', '__', '__', '__', '__', '__']
        assert test_card.line1 == ['__', '__', '__', '__', 'xx', '__', '__', '__', '__']
        assert test_card.line2 == ['__', '__', '__', '__', '__', '__', '__', '__', '11']
        test_card.cross_number(current_number, sim_crossed)
        assert test_card.line0 == ['xx', '__', '__', '__', '__', '__', '__', '__', '__']
        assert test_card.line1 == ['__', '__', '__', '__', 'xx', '__', '__', '__', '__']
        assert test_card.line2 == ['__', '__', '__', '__', '__', '__', '__', '__', 'xx']


class TestBag:
    def test_init(self):
        test_bag = Bag()
        # проверка на уникальность значений в случайном списке
        random_bag = tuple(test_bag.numbers)
        assert len(random_bag) == 90

    def test_get_from_bag(self):
        # проверим все ли числа есть в мешке после инициализации
        test_bag = Bag()
        for i in range(1,91):
            assert i in test_bag.numbers
        # проверим после get_from_bag исчезнет ли current_number из мешка
        current_number = test_bag.get_from_bag()
        assert current_number not in test_bag.numbers


def test_do_str_2simbol():
    test_string = ' '
    assert do_str_2simbol(test_string) == '0 '
    test_string = '  '
    assert do_str_2simbol(test_string) == '  '
