import sys
import random

try:
    print(f"First Argument {sys.argv[1]}")
    args = sys.argv
    random.shuffle(args)
    print(f"Random arguments {args[0]}")
except (IndexError, KeyError) as err:
    print(f"Error: no arguments, please provide at least once ({err})")
#    sys.exit(1)
except NameError:
    print(f"Error: random module not loaded")
#   sys.exit(1)
else:
    print("else is running")
finally:
    print("finally running")
