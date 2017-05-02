import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("number1", help="First number")
    parser.add_argument("number2", help="Second number")
    parser.add_argument("operation", help="operation")
    args = parser.parse_args()

    print(args.number1)
    print(args.number2)
    print(args.operation)


    if args.operation == "add":
        print(int(args.number1) + int(args.number2))

if __name__ == "__main__":
    main()