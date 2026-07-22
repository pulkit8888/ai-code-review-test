def login(username, password):

    query = (
        "SELECT * FROM users "
        "WHERE username='"
        + username
        + "'"
    )

    print(query)
