from typing import List, Union, Tuple, Dict     #This helps in mentoning what type of object it is

n : int = 8   #explictly adding ': int' or ': str' will help intellisence in further code to suggest methods for that variable type

name : str = "Jilesh"

def sum(a: int, b: int) -> int:     #Writing :int and -> int makes code readable & will suggest which type of variable to assign when further using the function
    return a + b

l1 : List[int, str] = [6, 14, 5, 9, 'Jilesh']

t1 : Tuple[str, int] = ("Ronak", 56, 1, "C")

d1 : Dict[int, str] = {"Jilesh" : 51, "Ronak" : 87}

U1 : Union[int, str] = "ID321"
