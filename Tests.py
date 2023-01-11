from Core import Human

test = 1

def print_test(program_output: list, correct_output: list) -> None:
    global test
    if (correct_output == program_output):
        print(f'\033[92m [+] Test #{test}: passed\033[39m')
    else:
        print(f'\033[91m [-] Test #{test}: failed')
        print(f'Correct output:', *correct_output)
        print(f'Your program output:', *program_output, '\033[39m')
    test += 1

def human_test():
    h1 = Human('test_case_1', 1, 2020)
    print_test([h1.name, ], ['test_case_1', ])
    print_test([h1.father, ], [None, ])
    h2 = Human('father', 1, 1980)
    h1.father = h2
    print_test([h1.father.name, ], ['father', ])
    h1.father.name = 'test_case_2'
    print_test([h1.father.name, ], ['test_case_2', ])

def run_tests():
    human_test()

if __name__ == '__main__':
    run_tests()