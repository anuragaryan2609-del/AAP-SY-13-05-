#Design and implement a Configurable Payment Processing System using the Strategy Pattern.


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

# Verification
obj1 = Singleton()
obj2 = Singleton()
print(f"Object 1 ID: {id(obj1)}")
print(f"Object 2 ID: {id(obj2)}")
print(f"Are they the same instance? {obj1 is obj2}")

