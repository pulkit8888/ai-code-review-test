import sqlite3


DATABASE_PASSWORD = "admin123"


def login(username, password):

    connection = sqlite3.connect(
        "users.db"
    )

    cursor = connection.cursor()


    # Vulnerable SQL query construction
    query = (
        "SELECT * FROM users WHERE username='"
        + username
        + "' AND password='"
        + password
        + "'"
    )


    print(
        "Executing:",
        query
    )


    cursor.execute(query)


    user = cursor.fetchone()


    if user:
        return True


    return False



def delete_user(user_id):

    # Runtime issue: no validation
    query = f"DELETE FROM users WHERE id={user_id}"

    connection = sqlite3.connect(
        "users.db"
    )

    connection.execute(query)

    connection.commit()



def calculate_discount(price, discount):

    # Possible runtime error
    final_price = price / discount

    return final_price



def process_users(users):

    result = []

    for user in users:

        # Inefficient nested loop
        for another_user in users:

            if user["id"] == another_user["id"]:
                result.append(user)


    return result
