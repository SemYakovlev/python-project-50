import argparse
import json


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference"
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()

    f1 = json.load(open(args.first_file))
    f2 = json.load(open(args.second_file))

    print(f1)
    print(f2)


if __name__ == "__main__":
    main()
