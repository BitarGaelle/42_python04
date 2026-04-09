_This project has been created as part of the 42 curriculum by gbitar_


---

## 📚 Exercises  

### 🔹 Exercise 0: Ancient Text Recovery  
- Read a file from command-line arguments  
- Display its contents safely  
- Handle errors like:
  - File not found  
  - Permission denied  

---

### 🔹 Exercise 1: Archive Creation  
- Modify file content by adding a special character (`#`) at the end of each line  
- Display transformed content  
- Ask the user for a filename to save  
- Create or overwrite the file if provided  

---

### 🔹 Exercise 2: Stream Management  
- Handle input/output using:
  - `sys.stdin` instead of `input()`  
  - `sys.stderr` for errors  
- Display error messages using a dedicated error stream  
- Continue improving file handling logic  

---

### 🔹 Exercise 3: Vault Security  
- Create a secure function:
  - `secure_archive(filename, action, content)` having the first argument as mandatory,
and the last two optional
- Use the `with` statement to ensure safe file handling  
- Support:
  - Reading a file  
  - Writing to a file  
- Return a tuple:
  - `(True, content)` on success  
  - `(False, error_message)` on failure  
- Handle exceptions properly:
  - `FileNotFoundError`  
  - `PermissionError`  

---

## 📌 Key Concepts Learned  

- File handling (`open`, `read`, `write`)  
- Context managers (`with`)  
- Standard streams (`stdin`, `stdout`, `stderr`)  
- Error handling with exceptions  
- Type hinting and static analysis  
- Writing clean and maintainable Python code  
