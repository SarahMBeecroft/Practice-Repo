def manage_students():
  print("What would you like to do?\n\n1. Add a Student\n2. Delete a Student\n3. Search a Student\n4. Exit/Quit\n")
  selection = int(input("Enter the corresponding number: "))

  while True:
    if selection == 1:
      print("Student added successfully")
      selection_2 = input("Would you like to continue? Yes/No\n")
      if selection_2 == "yes" or selection_2 == "YES" or selection_2 == "Yes" or selection_2 == "Y" or selection_2 == "y":
        manage_students()
      else:
        break
      break
    elif selection == 2:
      print("Student deleted successfully")
      selection_2 = input("Would you like to continue? Yes/No\n")
      if selection_2 == "yes" or selection_2 == "YES" or selection_2 == "Yes" or selection_2 == "Y" or selection_2 == "y":
        manage_students()
      else:
        break
      break
    elif selection == 3:
      print("You have chosen to search for a student")
      selection_2 = input("Would you like to continue? Yes/No\n")
      if selection_2 == "yes" or selection_2 == "YES" or selection_2 == "Yes" or selection_2 == "Y" or selection_2 == "y":
        manage_students()
      else:
        break
      break
    elif selection == 4:
      print("You have chosen to quit/exit")
      break
    else: 
      print("Please enter a valid number.")
      manage_students()
 
manage_students()