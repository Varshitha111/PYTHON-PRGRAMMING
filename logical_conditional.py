# 4. Logical Operators + Conditions
# Given a person's age and has_id, a person can enter a club if:
# Age is at least 18 AND they have an ID.
# Print "Allowed" or "Not Allowed"
def permit(age,has_id):
    if age>=18 and has_id:
        print("Allowed")
    else:
        print("Not Allowed")
permit(18,True)