import os
import sys
import time
import traceback

def safe_call(func, label):
    try:
        func()
    except Exception as e:
        print("\n******************************************************************************")
        print(f"ERROR while running '{label}':")
        print(f"  Reason: {type(e).__name__}: {e}")
        print("------------------------------------------------------------------------------")
        traceback.print_exc()
        print("******************************************************************************")
        print("Restarting the Main Menu in 3 seconds...\n")
        time.sleep(3)
        restart_program()

def restart_program():
    """Restart the current program cleanly."""
    try:
        python = sys.executable
        os.execl(python, python, *sys.argv)
    except Exception as e:
        print(f"Could not auto-restart ({e}). Please run 'python mainmenu.py' again.")
        sys.exit(1)

def mainmenu():
    while True:
        try:
            print("******************************************************************************")
            print("==============================================================================")
            print("*****************STUDENT RECORD MANAGEMENT SYSTEM - MAIN MENU*****************")
            print("==============================================================================")
            print("******************************************************************************")
            print()
            print("================================================================================")
            print("\t1.**********************STUDENT DETAILS**************************")
            print("\t2.*********************ATTENDANCE RECORD*************************")
            print("\t3.**********************MARKS / GRADES***************************")
            print("\t4.***********************FEE RECORDS*****************************")
            print("\t5.*******************SHOW PERFORMANCE GRAPH**********************")
            print("\t6.****************************EXIT*******************************")
            print("================================================================================")
            print()

            raw = input("ENTER CHOICE : ").strip()
            if not raw.isdigit():
                print("***********INVALID INPUT — please enter a number between 1 and 6***********")
                continue
            ch = int(raw)

            if ch == 1:
                import students
                safe_call(students.menu, "Student Details")
            elif ch == 2:
                import attendance
                safe_call(attendance.menu, "Attendance Record")
            elif ch == 3:
                import marks
                safe_call(marks.menu, "Marks / Grades")
            elif ch == 4:
                import fees
                safe_call(fees.menu, "Fee Records")
            elif ch == 5:
                import graphs
                safe_call(graphs.show_graph, "Performance Graph")
            elif ch == 6:
                print("Exiting... Goodbye!")
                break
            else:
                print("***********WRONG CHOICE — pick a number between 1 and 6***********")
        except KeyboardInterrupt:
            print("\nInterrupted by user. Exiting.")
            break
        except Exception as e:
            print("\n******************************************************************************")
            print("UNEXPECTED ERROR in Main Menu:")
            print(f"  Reason: {type(e).__name__}: {e}")
            traceback.print_exc()
            print("******************************************************************************")
            print("Restarting in 3 seconds...\n")
            time.sleep(3)
            restart_program()

if __name__ == "__main__":
    mainmenu()
