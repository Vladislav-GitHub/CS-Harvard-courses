import re


def main():
    print(validate(input("IPv4 Address: ")))

# ip = #.#.#.#, where # - [0, 255]
def validate(ip):
    if re.search("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        list_numbers = ip.split('.')
        for num in list_numbers:
            if int(num) < 0 or int(num) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()