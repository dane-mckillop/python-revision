import sys
import math

def degreesToRadians(degrees):
    if not isinstance(degrees, (int, float)):
        raise TypeError("Parameter must be a number (int or float)")
    
    return degrees * math.pi / 180

def main():
    if len(sys.argv) != 2:
        print("Usage: python degreesToRadians.py <degrees>")
        print("Example: python degreesToRadians.py 57.29578")
        sys.exit(1)

    try:
        degrees = float(sys.argv[1])
        radians = degreesToRadians(degrees)

        print (f"{degrees} degrees equal to {radians} radians")

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