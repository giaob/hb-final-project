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
    routeName = db.Column(db.String)
    pointA = db.Column(db.String)
    pointB = db.Column(db.String)
    #frequency is the amount of the days the user travels on the route per week
    frequency = db.Column(db.Integer)
    #this is the fare and duraiton for the route preference the use chooses
    #this should come from the details table, where the preferredRoute is True
    preferredFare = db.Column(db.Float, db.ForeignKey("details.fare_id"))
    #duration of transportation in hours
    #this should come from the details table, where the preferredRoute is True
    preferredDuration = db.Column(db.Float, db.ForeignKey("details.fare_id"))
    
    def __repr__(self):
        return f"<Route route_id={self.route_id} routeName={self.routeName}>"

class Details(db.Model):
    """The fare and duration of each route based on preference."""

    __tablename__ = "details"
    detail_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey("routes.route_id"))
    #This is true if the user selects this as their preferred route
    preferredRoute = db.Comlumn(db.Boolean)
    #routeType can bus, subway, train, and tram are the preferences
    #these are the preferences that can be selected in Google Maps
    routeType = db.Comlumn(db.String)
    #these are the fares for the route preferences that can be selected in Google Maps
    fare = db.Column(db.Float)
    #the are the duration of each trip based on the type of transportation chosen in hours
    duration = db.Column(db.Float)

    def __repr__(self):
        return f"<Detail detail_id={self.detail_id}"

class Transportation(db.Model):
    """The type of transportation such as bus or train."""

    __tablename__ = "transportations"

    transportation_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    #This will be hardcoded fares for AC Transit, BART, and MUNI
    #Single fare is not included because the assumption is that the Google Maps estimate is for a single fare.
    #This table is not connected to any others
    transportType = db.Column(db.String)
    dayFare = db.Column(db.Float)
    weeklyFare = db.Column(db.Float)
    monthlyFare = db.Column(db.Float)
 
    def __repr__(self):
        return f"<Transportation transportation_id={self.transportation_id} transportType={self.transportType}>"

def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
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
