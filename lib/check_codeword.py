# File: lib/check_codeword.py

def check_codeword(codeword):
    if codeword == "horse":
        return "Correct! Come in."
    elif codeword[0] == "h" and codeword[-1] == "e":
        return "Close, but nope."
    else:
        return "WRONG!"


# WHY "" CRASHES INSTEAD OF RETURNING "WRONG!":
# Python must evaluate the elif condition before it can reach else.
# For "", codeword[0] asks for the first character of an empty string,
# which doesn't exist, so Python raises IndexError inside the elif.
# The else is never reached.
#
# FIX: use codeword.startswith("h") and codeword.endswith("e") instead.
# These just return False for "" (no character lookup), so the elif
# is False and Python falls through to else -> "WRONG!".