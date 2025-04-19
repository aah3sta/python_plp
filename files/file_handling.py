file = open("example.txt", "x")
file.write('This is a new file. Welcome to file handling with Esther. This is a competely new concept.')
file.close()
print("File created successfully.")


def read_and_modify_file():
    filename = input("Please enter the filename you want to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()

        modified_content = content.upper()

        output_filename = "modified_" + filename
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)

        print(f"File processed successfully. The modified file is saved as '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{filename}' cannot be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_and_modify_file()
