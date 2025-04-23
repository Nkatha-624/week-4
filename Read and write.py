def read_and_write_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        modified_content = content.upper()

        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"Content has been successfully modified and written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except IOError as e:
        print(f"Error: An error occurred while reading or writing the file. {e}")

input_file = "input.txt"  
output_file = "output.txt"
read_and_write_file(input_file, output_file)
