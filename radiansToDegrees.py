import sys
import math

def radiansToDegrees(radians):
    if not isinstance(radians, (int, float)):
        raise TypeError("Parameter must be a number (int or float)")
    
    return radians * 180 / math.pi

def main():
    if len(sys.argv) != 2:
        print("Usage: python radiansToDegrees.py <radians>")
        print("Example: python radiansToDegrees.py 3.14159")
        sys.exit(1)

    try:
        radians = float(sys.argv[1])
        degrees = radiansToDegrees(radians)

        print (f"{radians} radians is equal to {degrees} degrees")

    except ValueError:
        print("Error: Please provide a valid number")
        sys.exit(1)
    except TypeError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        sys.exit(1)

#Check if script is being run directly, or imported as a module.
if __name__ == "__main__":
    main()