def ask_for_filename_and_read():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except IOError as e:
        print(f"Error: An error occurred while reading the file. {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

ask_for_filename_and_read()
