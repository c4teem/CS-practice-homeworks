# EIGHT

def retry(times=5):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < times:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print("Error:", e)
                    if attempt < times - 1:
                        print("Retrying...")
                    attempt += 1
                    
            return "Run the code again for more attempts" 
        return wrapper
    return decorator


@retry(times=2)
def division() -> float:
    x = int(input())
    y = int(input())
    if y == 0: raise ZeroDivisionError("You can't divide by zero!!!")
    return x / y

print(division())
