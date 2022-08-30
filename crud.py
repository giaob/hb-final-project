"""CRUD operations."""

from model import db, User, Route, Transportation, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

def create_route(route_name, point_a, point_b, frequency, preferred_fare, duration, preferred_route, fare):
    """Create and return a route."""

    route = Route(route_name=route_name,
        point_a=point_a,
        frequency=frequency,
        preferred_fare=preferred_fare,
        duration=duration,
        preferred_route=preferred_route,
        fare=fare
    )

    return route

def Transportation(transport_type, day_fare, weekly_fare, monthly_fare):
    """"""

    transportation = Transportation(transport_type=transport_type,
        day_fare=day_fare,
        weekly_fare=weekly_fare,
        monthly_fare=monthly_fare)

    return transportation

def get_routes():
    """Return all routes."""

    return Route.query.all()

def get_route_by_id(route_id):
    """Return routes by id."""

    return Route.query.get(route_id)

def get_users():
    """"Return all users."""

    return User.query.all()

def get_user_by_id(user_id):
    """Return user by id."""

    return User.query.get(user_id)

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)