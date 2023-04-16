import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        url = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([\w\d_]+)", s)
        if url:
            split_url = url.groups()
            return "https://youtu.be/" + split_url[-1]


if __name__ == "__main__":
    main()