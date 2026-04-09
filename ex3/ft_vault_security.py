def secure_archive(filename: str, action: str = "read",
                   content: str = "") -> tuple[bool, str]:
    try:
        if action == "read":
            mode = "r"
        elif action == "write":
            mode = "w"
        else:
            return (False, "Not valid mode")
        with open(filename, mode) as f:
            if action == "read":
                content = f.read()
                return (True, content)
            elif action == "write":
                f.write(content)
                return (True, "Content successfully written to file")
            else:
                return (False, "Cannot access the file")
    except FileNotFoundError as v:
        return (False, f"{v}")
    except PermissionError as e:
        return (False, f"{e}")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("non_exist.txt"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("test.txt", action="read"))

    prev_content = secure_archive("test.txt", action="read")
    print("\nUsing 'secure_archive' to write previous content to a new file")
    print(secure_archive("test2.txt", action="write", content=prev_content[1]))
