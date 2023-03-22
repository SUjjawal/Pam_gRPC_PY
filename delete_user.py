from source import user


if __name__ == '__main__' :

    user_id="Monika" 
    res = user.deleteUser(user_id)
    print(res.responseMessage)
  
