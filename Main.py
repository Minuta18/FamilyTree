import Core
import Visualaser
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
        throne = Core.Throne('Михаил Фёдорович', 1613)
        throne.marry('Михаил Фёдорович', 'Евдокия Стрешникова')
        throne.new_born('Алексей Михаилович', Core.MALE)
        throne.die('Михаил Фёдорович')
        throne.marry('Алексей Михаилович', 'Наталья Нарышкина')
        throne.new_born('Петр I', Core.MALE)
        visualaser = Visualaser.Visualaser(throne)
        visualaser.draw()
        #throne.simulate()
        ...