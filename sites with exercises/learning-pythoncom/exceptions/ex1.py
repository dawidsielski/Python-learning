def oopc():
    raise IndexError

def test_oopc():
    try:
        oopc()
    except IndexError:
        print("Index Error exception")


if __name__ == "__main__":
    test_oopc()