from typing import Any


def switch_case(choice):
    switch = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    return switch.get(choice)


class Stack:
    def __init__(self):
        self.invalid: bool = False
        self.fh = "./input_file.txt"
        self.stack = []
        self.points = 0

    def push(self, value):
        self.stack.insert(0, value)

    def pop(self) -> str:
        return self.stack.pop(0)

    def main(self):
        fh = open("./input_file.txt")
        for line in map(str.strip, fh):
            for letter in line:

                print(letter)
                if self.invalid:
                    break

                if letter == '[' or letter == '(' or letter == '{' or letter == '<':
                    self.push(letter)
                else:
                    old_letter = self.pop()
                    if old_letter is None:
                        print("incomplete")
                        break

                    if old_letter != letter:
                        invalid = True
                        self.points += switch_case(letter)

        print(f'Points Total: {self.points}')


hi: Stack = Stack()

hi.main()
