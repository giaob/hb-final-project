"""Models for transit cost comparison app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

class Route(db.Model):
    """The starting and end point of the user's transportation route."""

    __tablename__ = "routes"

    route_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    #routeName is an alias the user assigns to their route, such as "Commute to work".
    route_name = db.Column(db.String)
    point_a = db.Column(db.String)
    point_b = db.Column(db.String)
    #frequency is the amount of the days the user travels on the route per week
    frequency = db.Column(db.Integer)
    #this is the fare and duration for the route preference the user chooses
    #this should come from the details table, where the preferredRoute is True
    fare = db.Column(db.Float)
    #duration of transportation in hours
    duration = db.Column(db.Float)
    
    def __repr__(self):
        return f"<Route route_id={self.route_id} routeName={self.routeName}>"

class Transportation(db.Model):
    """The type of transportation such as bus or train."""

    __tablename__ = "transportations"

    transportation_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    #This will be hardcoded fares for AC Transit, BART, and MUNI
    #Single fare is not included because the assumption is that the Google Maps estimate is for a single fare.
    #This table is not connected to any others
    transport_type = db.Column(db.String)
    day_fare = db.Column(db.Float)
    weekly_fare = db.Column(db.Float)
    monthly_fare = db.Column(db.Float)
    per_trip = db.Column(db.Float)
    prepay = db.Column(db.Float)
 
    def __repr__(self):
        return f"<Transportation transportation_id={self.transportation_id} transportType={self.transportType}>"

#change this when you have database
def connect_to_db(flask_app, db_uri="postgresql:///mydb", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
    db.create_all()
