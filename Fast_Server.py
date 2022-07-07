"""This is Docstring"""


def fast_server_compare(_server_a_speed,
                        _server_a_second_type,
                        _server_b_speed,
                        _server_b_second_type):
    """Compare which server are faster between server a and server b"""
    server_a_speed = _server_a_speed
    server_a_second_type = _server_a_second_type
    server_b_speed = _server_b_speed
    server_b_second_type = _server_b_second_type

    if server_a_second_type == "Picosecond":
        server_a_speed = server_a_speed * 1.0 * (10**-12)
    elif server_a_second_type == "Nanosecond":
        server_a_speed = server_a_speed * 1.0 * (10**-9)
    elif server_a_second_type == "Microsecond":
        server_a_speed = server_a_speed * 1.0 * (10**-6)
    elif server_a_second_type == "Millisecond":
        server_a_speed = server_a_speed * 0.001

    if server_b_second_type == "Picosecond":
        server_b_speed = server_b_speed * 1.0 * (10**-12)
    elif server_b_second_type == "Nanosecond":
        server_b_speed = server_b_speed * 1.0 * (10**-9)
    elif server_b_second_type == "Microsecond":
        server_b_speed = server_b_speed * 1.0 * (10**-6)
    elif server_b_second_type == "Millisecond":
        server_b_speed = server_b_speed * 0.001

    if server_a_speed == server_b_speed:
        return print("equal")

    if server_a_speed < server_b_speed:
        print("Server A, %f second" % server_a_speed)
        print("Faster than server B , %d times" %
              (server_b_speed // server_a_speed))
    elif server_a_speed > server_b_speed:
        print("Server B, %f second" % server_b_speed)
        print("Faster than server A , %d times" %
              (server_a_speed // server_b_speed))


def main():
    """Fast Server Calculation"""
    server_a_speed_input = int(input())
    server_a_second_type_input = input()
    server_b_speed_input = int(input())
    server_b_second_type_input = input()
    fast_server_compare(server_a_speed_input, server_a_second_type_input,
                        server_b_speed_input, server_b_second_type_input)


main()
