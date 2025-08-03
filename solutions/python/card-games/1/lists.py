from math import floor, ceil


def get_rounds(number):
    """

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """
    return list(range(number, number+3))


def concatenate_rounds(rounds_1, rounds_2):
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """
    return number in rounds


def card_average(hand):
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    return sum(hand)/len(hand)


def approx_average_is_average(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - is approximate average the same as true average?
    """

    return (hand[0] + hand[-1])/2 == card_average(hand) or hand[floor(len(hand)/2)] == card_average(hand)


def average_even_is_average_odd(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    sum_odd = sum([i for i in hand if i % 2 == 0])
    sum_even = sum([i for i in hand if i % 2 != 0])
    avg_odd = (sum_odd / floor(len(hand)/2)) if len(hand) % 2 else sum_odd / len(hand)/2
    avg_even = (sum_even / ceil(len(hand)/2)) if len(hand) % 2 else sum_even / len(hand)/2
    return avg_odd == avg_even


def maybe_double_last(hand):
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    return hand[:-1] + [22] if hand[-1] == 11 else hand
