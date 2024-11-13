def add_word_to_each_line(input_file_path, output_file_path, word_to_add):
    try:
        # Open the input file for reading
        with open(input_file_path, 'r') as input_file:
            # Read all lines from the input file
            lines = input_file.readlines()
        
        # Open the output file for writing
        with open(output_file_path, 'w') as output_file:
            # Process each line
            for line in lines:
                # Strip the newline character from the end of the line
                modified_line = line.strip() + ' ' + word_to_add + '\n'
                # Write the modified line to the output file
                output_file.write(modified_line)
    except FileNotFoundError:
        print(f"Error: The file {input_file_path} was not found.")

# Example usage
input_file_path = 'C:/Users/Owner/Downloads/Python bootcamp/Python-bootcamp/exercise/original_file.txt'
output_file_path = 'C:/Users/Owner/Downloads/Python bootcamp/Python-bootcamp/exercise/modified_file.txt'
word_to_add = 'example'

# Call the function to append the word to each line
add_word_to_each_line(input_file_path, output_file_path, word_to_add)
