#!/usr/bin/env python3
from calculator_adapter import run

### ADD AT LEAST TWO TESTS HERE!
# Checks that the program outputs "-1" for an input of "19 + -1"
assert run("19 + -1").output == "18"
# Checks that the program outputs "24" for an input of "3 * 8"
assert run("8 * 3").output == "24"
#Checls that the program outputs "-45" for an input of "45 - 90"
assert run("45 - 90").output == "-45"
# Checks that the program exists successfully (no error) for input "9 / 6"
assert run("2 / 4").exit_status == 0
# Checks that the program fails (correctly errors) for input "1 @ 1"
assert run("1 [ 1").exit_status != 0
###

print("All tests passed!")
