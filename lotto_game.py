import random


class Card:

    def __init__(self):
        self.player_name = ''
        self.count_number = 0
        self.line0 = []
        self.line1 = []
        self.line2 = []

    def __str__(self):
        return f'Имя игрока: {self.player_name}\n' \
               f'Количество незачеркнутых номеров в карточке: {self.count_number}\n' \
               f'Карточка:\n{self.line0}\n{self.line1}\n{self.line2}'

    def __eq__(self, other):
        return self.line0 == other.line0 and self.line1 == other.line1 and self.line2 == other.line2

    def create_card(self, sim_empt):
        for index in range(9):
            self.line0.append(sim_empt*2)
            self.line1.append(sim_empt*2)
            self.line2.append(sim_empt*2)

        number_in_card = random.sample(range(1, 91), 15)
        number_in_line0 = sorted(number_in_card[:5])
        position_in_line0 = sorted(random.sample(range(0, 9), 5))
        number_in_line1 = sorted(number_in_card[5:10])
        position_in_line1 = sorted(random.sample(range(0, 9), 5))
        number_in_line2 = sorted(number_in_card[10:])
        position_in_line2 = sorted(random.sample(range(0, 9), 5))

        for index in range(5):
            self.line0[position_in_line0[index]] = do_str_2simbol(str(number_in_line0[index]))
            self.line1[position_in_line1[index]] = do_str_2simbol(str(number_in_line1[index]))
            self.line2[position_in_line2[index]] = do_str_2simbol(str(number_in_line2[index]))

    def cross_number(self, current_number, sim_cros):
        for index in range(9):
            if self.line0[index] == current_number:
                self.line0[index] = sim_cros*2
                self.count_number -= 1
                break
            if self.line1[index] == current_number:
                self.line1[index] = sim_cros*2
                self.count_number -= 1
                break
            if self.line2[index] == current_number:
                self.line2[index] = sim_cros*2
                self.count_number -= 1
                break

    def print_card(self):
        print('*' * 26)
        print('Карточка игрока:', self.player_name)
        print('*' * 26)

        print_list_in_line(self.line0, ' ')
        print_list_in_line(self.line1, ' ')
        print_list_in_line(self.line2, ' ')


class Bag:

    def __init__(self):
        self.numbers = random.sample(range(1, 91), 90)

    def __str__(self):
        return f'В мешке: {self.numbers}'

    def __eq__(self, other):
        return self.numbers == other.numbers

    def get_from_bag(self):
        current_number = random.choices(self.numbers)[0]
        self.numbers.remove(current_number)
        return current_number


def do_str_2simbol(work_string):
    return work_string if len(work_string) == 2 else '0' + work_string


def print_list_in_line(work_list, separator):
    len_work_list = len(work_list)
    for index in range(len_work_list):
        if index == len_work_list - 1:
            end_string = '\n'
        else:
            end_string = separator
        print(work_list[index], end=end_string)


def print_star():
    print('*' * 26)


if __name__ == '__main__':
    sim_empty = '_'   # Символ для обозначения пустых ячеек (1 символ. Ячейка карточки состоит из 2-х символов)
    sim_crossed = 'x'   # Символ для обозначения зачеркнутых ячеек (1 символ. Ячейка карточки состоит из 2-х символов)

    # Создание игровых карточек
    pc_card = Card()
    pc_card.player_name = 'PC'
    pc_card.count_number = 15
    pc_card.create_card(sim_empty)

    my_card = Card()
    my_card.player_name = input('Введите Ваше имя: ')
    my_card.count_number = 15
    my_card.create_card(sim_empty)

    # Создаём новый мешок с номерами
    bag = Bag()
    for index in range(90):
        bag.numbers[index] = do_str_2simbol(str(bag.numbers[index]))

    # Игра
    print_star()
    print('Игра началась!!!')
    for i in range(90):
        current_number = bag.get_from_bag()
        print_star()
        print('Боченок №', current_number)
        pc_card.print_card()
        my_card.print_card()
        pc_card.cross_number(current_number, sim_crossed)

        in_card = my_card.line0.count(current_number) + my_card.line1.count(current_number) + my_card.line2.count(current_number)

        indicator = False  # Указатель принят ли ответ
        answer = ''
        while indicator is False:
            answer = input('Зачеркнуть номер в карточке? Ваш ответ (д/н): ').lower()
            if answer in ['да', 'д', 'y', 'yes', '1']:
                answer = 'д'
                indicator = True
            elif answer in ['нет', 'н', 'n', 'no', '0']:
                answer = 'н'
                indicator = True
            else:
                print('Не понял Ваш ответ...')  # Переспросить, что делать
                indicator = False

        if answer == 'д' and in_card == 1:
            my_card.cross_number()
        elif answer == 'д' and in_card == 0 or answer == 'н' and in_card == 1:
            pc_card.count_number = 777

        if pc_card.count_number == 0 and my_card.count_number == 0:
            print_star()
            print('Игра окончена!')
            print(pc_card.player_name, ' ', my_card.player_name, ' Вы одновременно закрыли карточки! ', sep=',')
            break
        elif pc_card.count_number == 777:
            print_star()
            print('Игра окончена!')
            print(my_card.player_name, ' Вы совершили ошибку! ', sep=',')
            print(pc_card.player_name, 'выиграл!!!')
            break
        elif pc_card.count_number > 0 and my_card.count_number == 0:
            print_star()
            print('Игра окончена!')
            print(my_card.player_name, ' Вы выиграли! ', sep=',')
            break
        elif pc_card.count_number == 0 and my_card.count_number > 0:
            print_star()
            print('Игра окончена!')
            print(pc_card.player_name, 'выиграл!!!')
            break
