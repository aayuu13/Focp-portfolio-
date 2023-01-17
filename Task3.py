#Importing Modules------------
import sys
import random
#Function to generate email---------------------
def generate_email(line):
    student_id, name = line.strip().split(' ', 1)
    surname, firstname = name.split(',')
    surname = ''.join(c for c in surname if c.isalpha())
    initials = '.'.join(c[0] for c in firstname.split())
    random_digits = ''.join(str(random.randint(0, 9)) for _ in range(4))
    email = f"{initials.lower()}.{surname.lower()}{random_digits}@poppleton.ac.uk"
    return f"{student_id} {email}\n"

def main():
    if len(sys.argv) != 2:
        print("Error: Missing command-line argument.")
        return

    try:
        with open(sys.argv[1], 'r') as input_file:
            with open('students_email.txt', 'w') as output_file:
                output_file.writelines(generate_email(line) for line in input_file)
    except IOError:
        print(f"Error: Cannot open {sys.argv[1]}. Sorry about that.")

if __name__ == '__main__':
    main()
