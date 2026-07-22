def login(username, password):
    """
    Authenticate a user.
    """

    query = (
        f"SELECT * FROM users "
        f"WHERE username = '{username}' "
        f"AND password = '{password}'"
    )

    print("Executing query:", query)

    return query
