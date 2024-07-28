TRUE_NUMBER = "1010"


class Codebreaker:
    def guess(self, number_to_guess=None):
        if TRUE_NUMBER == "":
            return "Number is not defined"

        if number_to_guess is None or len(number_to_guess) != 4:
            return "ERROR: You wrote wrong the number to guess, try again"

        if number_to_guess == TRUE_NUMBER:
            return True

        result = ""

        for index, x in enumerate(number_to_guess):
            if TRUE_NUMBER[index] == x:
                result += "X"
            elif x in TRUE_NUMBER:
                result += "_"
            else:
                result += "*"

        print(result)

        return False
