class PersonalDiary:
    def __init__(self, source_filename):
        self.filename = source_filename

    def write_to_diary(self):
        try:
            with open(self.filename, 'w') as file:
                while True:
                    line = input('Enter line: ')
                    file.write(line + '\n')

                    choice = input('Are there more line y/n')

                    if choice == 'n':
                        print(f'\nLines have been saved to {self.filename}.')
                        break
                    elif choice != 'y':
                        print('Invalid input. Please try again.')
                        break
        except Exception as e:
            print(f'An error occured while writing: {e}')