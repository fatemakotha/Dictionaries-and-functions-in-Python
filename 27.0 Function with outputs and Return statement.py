#Function with outputs and Return statement
#Functions with Outputs
def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  print(f"Result: {formated_f_name} {formated_l_name}")

format_name("kOTHA", "FATEMA")
# prints:
# Result: Kotha Fatema