import json


def find_common_divisors(num1, num2):
    common_divisors = []
    smaller_num = min(num1, num2)

    for i in range(1, smaller_num + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_divisors.append(i)

    return common_divisors


def main():
    try:
        with open("input.json", "r") as file:
            data = json.load(file)
            num1 = data.get("num1")
            num2 = data.get("num2")

            common_divisors = find_common_divisors(num1, num2)

            response = {"common_divisors": common_divisors}

            with open("output.json", "w") as output_file:
                json.dump(response, output_file)

            print("Common divisors have been written to output.json.")
    except FileNotFoundError:
        print("Input JSON file not found.")
    except ValueError:
        print("Invalid JSON format.")


if __name__ == "__main__":
    main()
