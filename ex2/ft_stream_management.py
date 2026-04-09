import sys


def ft_stream_management() -> None:
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
        print("---")
        line_list = []
        lines = content.split("\n")
        for line in lines:
            if line == "":
                line = "\n"
            else:
                line = line + "#\n"
            line_list.append(line)
            print(line, end="")
        print("---")
        print("Enter new file name (or empty): ", end="", flush=True)
        filename = sys.stdin.readline().strip()
        if filename == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{filename}'")
            f = open(filename, "w")
            for line in line_list:
                f.write(line)
            f.close()
            print(f"Data saved in file '{filename}'")
    except FileNotFoundError as v:
        print(f" [STDERR] Error opening file '{filename}': {v}",
              file=sys.stderr)
    except PermissionError as e:
        print(f" [STDERR] Error opening file '{filename}': {e}",
              file=sys.stderr)
        print("Data not saved.")


if __name__ == "__main__":
    ft_stream_management()
