import sys


def ft_ancient_text() -> None:
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    try:
        f = open(filename, "r")
        print("---")
        content = f.read()
        print(content)
        f.close()
        print("---")
        print(f"File '{filename}' closed.")
    except FileNotFoundError as v:
        print(f"Error opening file '{filename}': {v}")
    except PermissionError as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    ft_ancient_text()
