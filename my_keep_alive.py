import logging

log = logging.getLogger(__name__)


"""
Poll to see if car is 'on' (Charging or In driving mode) and set autosleep accordingly:
"""


def poll():

    # enable sleep in case anything goes wrong below
    #

    if get_driving() == -1:
        enable_sleep()
    else:
        disable_sleep()


# check if we are driving.  Returns :
# (Not working on Ioniq currently, so will return -1 if no response and garble if on)
#   0 - charging
#   1 - driving
#   -1 - can't read data
def get_driving():
    try:
        args = ['driving']
        kwargs = {
            'mode': '220',
            'pid': '101',
            'header': '7E4',
            'baudrate': 500000,
            'formula': 'bytes_to_int(message.data[53:54])',
            'protocol': '6',
            'verify': False,
            'force': True,
        }
        # note - sums are done outside of the forumla due to autopi failing
        # with 0
        #
        return (int(__salt__['obd.query'](*args, **kwargs)['value'])&4)/4
    except:
        return -1


# enable autopi sleep
#
def enable_sleep():
    args = ['sleep']
    kwargs = {
        'enable': True,
    }
    __salt__['power.sleep_timer'](**kwargs)


# disable autopi sleep
#
def disable_sleep():
    args = ['sleep']
    kwargs = {
        'enable': False,
    }
    __salt__['power.sleep_timer'](**kwargs)
