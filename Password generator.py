import secrets
import string

def generate_password(length=12):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    
    if length < 8 :
        raise ValueError("password length is too short")
        
    
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return password
    

generated_password = generate_password()
print("Generated password:", generated_password)
