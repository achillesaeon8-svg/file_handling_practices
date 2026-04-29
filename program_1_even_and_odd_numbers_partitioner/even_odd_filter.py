class OddAndEvenSettings:
    def __init__(self, source_filename):
        self.chosen_file = source_filename
    
    def sort_numbers(self):
        try:
            with open(self.chosen_file, 'r') as file, \
                open('even.txt', 'w') as even_text_file, \
                open('odd.txt', 'w') as odd_text_file:
                    
                for line in file:
                    clean_line = line.strip()
                    if not clean_line:
                        continue

                    number = int(clean_line)

                    if number % 2 == 0:
                        even_text_file.write(f'{number}\n')
                    else:
                        odd_text_file.write(f'{number}\n')
                    
            print('Analyzing complete successfully.')

        except FileNotFoundError:
            print('Error: File not found')
        except ValueError:
            print('Error: The file contains text that is not a number')
        except Exception as e:
            print(f'An unexpected error occured: {e}')