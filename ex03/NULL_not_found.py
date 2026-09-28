from typing import Any
import math

def NULL_not_found(object: Any) -> int:
    match object:
        case None:
            print("Nothing: None <class 'NoneType'>")
        # NaN値はNaN==NaNがFalseになるため、math.isnan()で判定する
        case float() if math.isnan(object):
            print("Cheese: nan <class 'float'>")
        case bool() if object is False:
            print("Fake: False <class 'bool'>")
        # PythonではFalse==0がTrueのため、bool型のFalseを先に判定する必要がある
        case 0:
            print("Zero: 0 <class 'int'>")
        case "":
            print("Empty: <class 'str'>")
        case _:
            print("Type not found")
            return 1
    return 0