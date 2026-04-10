import sys


def ft_archive_creation() -> None:
    if len(sys.argv) == 1:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    try:
        f = open(filename, "r")
        print("---\n")
        content = f.read()
        print(content)
        f.close()
        print("\n---")
        print(f"File '{filename}' closed.")
        print("\nTransform data:")
        print("---\n")
        line_list = []
        lines = content.split("\n")
        for line in lines:
            if line == "":
                line = "\n"
            else:
                line = line + "#\n"
            line_list.append(line)
            print(line, end="")
        print("\n---")
    except FileNotFoundError as v:
        print(f"Error opening file '{filename}': {v}")
    except PermissionError as e:
        print(f"Error opening file '{filename}': {e}")

    try:
        new_file = input("Enter new file name (or empty): ")
        if new_file == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_file}'")
            f = open(new_file, "w")
            for line in line_list:
                f.write(line)
            f.close()
            print(f"Data saved in file '{new_file}'")
    except FileNotFoundError as v:
        print(f"Error opening file '{new_file}': {v}")
    except PermissionError as e:
        print(f"Error opening file '{new_file}': {e}")


if __name__ == "__main__":
    ft_archive_creation()
