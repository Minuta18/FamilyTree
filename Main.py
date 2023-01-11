import Core
import Tests
import sys

if __name__ == '__main__':
    args = sys.argv[:]
    if len(args) > 2:
        print('To many args')
    elif len(args) > 1:
        if args[1] == '--help' or args[1] == '-h':
            print('No usage yet :(')
        elif args[1] == '--test' or args[1] == '-t':
            Tests.run_tests()
    else:
        # throne = Core.Throne(,) # TODO
        # throne.simulate()
        ...