def manage_students():
  print("What would you like to do?\n\n1. Add a Student\n2. Delete a Student\n3. Search a Student\n4. Exit/Quit\n")
  selection = int(input("Enter the corresponding number: "))

  while True:
    if selection == 1:
      print("Student added successfully")
      selection_2 = input("Would you like to continue? Yes/No")
        if selection == "yes" or selection == "YES" or selection == "Yes" or selection == "Y" or selection == "y"
      break
    elif selection == 2:
      print("Student deleted successfully")
      break
    elif selection == 3:
      print("You have chosen to search for a student")
      break
    elif selection == 4:
      print("You have chosen to quit/exit")
      break
    else: 
      print("Please enter a valid number.")
      manage_students()
 
manage_students()