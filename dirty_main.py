from application.salary import *
from application.db.people import *
from datetime import *

if __name__ == '__main__':
    dt = datetime.now().strftime("%A, %d. %B %Y %H:%M")
    print(dt)
    calculate_salary()
    get_employees()
