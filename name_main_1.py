print("something called outside 'if name main'")

print(f"__name__ = {__name__}")


def main():
    print("something called in 'if name main'")


# will only run "if name main" when file is executed
# if imported __name__ will not be __main__, but the file name
if __name__ == "__main__":
    main()
