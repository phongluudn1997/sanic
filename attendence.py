from datetime import datetime


class Event(object):
    """docstring for Event"""

    def __init__(self, time, user):
        self.time = time
        self.user = user

    def __repr__(self):
        return "Event: <Time: {}, User: {}>".format(self.time, self.user)


class User(object):
    """docstring for User"""

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "{}".format(self.name)


class Session(object):
    """docstring for Session"""
    list_event = []

    def __init__(self, status):
        self.status = status

    def add_event(self, event):
        self.list_event.append(event)

    def invalid_event(self, event):
        def check_if_exist(event):
            return event in self.list_event

        if check_if_exist(event):
            self.list_event.remove(event)
        else:
            print('No event found')
            return

    def __repr__(self):
        '''@TODO: Make it return decorator'''

        return "{}".format(self.list_event)


user = User('Phong Luu')

event = Event(time=datetime(2020, 3, 20, 7, 0, 0), user=user)
session = Session(status='active')
session.add_event(event=event)

print(session)
