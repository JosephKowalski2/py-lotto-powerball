# lotto picker by manny juan  (juanm@wellsfargo.com or manny@bdt.com)

from random import randint


def get_lotto_numbers():
    return randint(1, 69)


def get_powerball_number():
    return randint(1, 26)


def pick_lotto():
    lotto_numbers = []
    for number in range(0, 5):
        number = get_lotto_numbers()
        lotto_numbers.append(number)
    lotto_numbers.sort()
    return tuple(lotto_numbers)


def run():
    done = 0
    while not done:

        try:
            x = input('\npress Enter for Lotto picks (Q to quit). ')
        except EOFError:
            x = 'q'
        if x and (x[0] == 'q' or x[0] == 'Q'):
            done = 1
            print('done')
        else:
            print(f'{pick_lotto()} Powerball: {get_powerball_number()}')


# immediate-mode commands, for drag-and-drop or execfile() execution
if __name__ == '__main__':
    run()
else:
    print("Module lotto imported.")
    print("To run, type: lotto.run()")
    print("To reload after changes to the source, type: reload(lotto)")
# end of lotto.py
