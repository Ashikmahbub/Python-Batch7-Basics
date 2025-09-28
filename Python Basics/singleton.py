#singleton pattern
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    
ob1 = Singleton()
ob2 = Singleton()   
print(ob1 is ob2)  # True
 