import os

def create_directory(root_directory):
    directories = [
        'cst8254/linux/labs/lab1',
        'cst8254/linux/labs/lab2',
        'cst8254/linux/labs/lab3',
        'cst8254/linux/lectures/week1',
        'cst8254/linux/lectures/week2',
        'cst8254/linux/lectures/week3',
        'cst8254/backup',
        'cst8254/python'
    ]
    for directory in directories:
        os.makedirs(os.path.join(root_directory, directory), exist_ok=True)
    
if __name__ == "__main__":
    root_directory = "./pi"
    
create_directory(root_directory)