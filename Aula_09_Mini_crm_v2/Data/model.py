from datetime import date

def model_lead(name, email, status):
    return   {
    "name": name,
    "e-mail": email,
    "status": status,
    "created": date.today().isoformat()
  }
