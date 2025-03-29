import sys

def integerToBinary(integer):
    if not isinstance(integer, (int)):
        raise TypeError("Parameter must be an integer (whole number)")
    
    return bin(integer)[2:]

def main():
    if len(sys.argv) != 2:
        print("Usage: python integerToBinary <integer>")
        print("Example: python integerToBinary.py 12.3456")
        sys.exit(1)

    try:
        integer = int(sys.argv[1])
        binary = integerToBinary(integer)

        print (f"{integer} decimal float equal to {binary} ")

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