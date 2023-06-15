from decorators import interger_validator

@interger_validator
def add(a:int, b:int) -> int:
    return a + b

if __name__ == "__main__":
    result_add = add(1,'3')
    print(result_add)