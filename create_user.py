from source import user


if __name__ == '__main__' :

    user_name="Monika" 
    first_name="Monika"
    last_name="Sarkar"
    full_name="Smt Monika Sarkar"
    email="Ujjawal@zoho.com"
    policy="Strong"
    role="Administrator"
    is_supper_admin=True
    password="Monika@123"
    department="PMP"
    location="Chennai"
    is_api_user=True
    host_name="monika-2222"
    expiry_date=None
    res = user.createUser(user_name,first_name,last_name,full_name,email,policy,role,is_supper_admin,password,department,location,is_api_user,host_name,expiry_date)
    print(res.responseMessage)
  
