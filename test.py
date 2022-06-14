from main import process_coins

from tud_test_base import set_keyboard_input


def test_case_process_coins():

    set_keyboard_input(["100", "100", "10", "10"])

    assert process_coins() == 100 * 0.25 + 100 * 0.1 + 10 * 0.05 + 10 * 0.01
