#!/usr/bin/python3
'''
    module to start a flask app
'''

from ..models import storage


def remove_session(error):
    '''
        tears down the session
    '''
    storage.close()


def states_list():
    '''returns a template of unordered lists of state
        objects
    '''
    states = storage.all('State')
    my_list = []
    for obj in states.values():
        tup = (obj.name, obj.id)
        print(tup)
        my_list.append(tup)
    my_list.sort()
    return render_template("7-states_list.html", states=my_list)


states_list()
