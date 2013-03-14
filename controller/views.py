from wemo import get, toggle, on, off
import json
from django.http import HttpResponse
from controller.models import Switch


def index(request):
    switches = Switch.objects.all()
    rtval = []
    for wswitch in switches:
        switchInfo = {}
        switchInfo['id'] = wswitch.id
        switchInfo['host'] = wswitch.host
        switchInfo['img'] = wswitch.img
        switchInfo['status'] = wswitch.status
        switchInfo['name'] = wswitch.name
        rtval.append(switchInfo)
    return HttpResponse(rtval, mimetype="application/json")


def turn_on(request, switch_id):
    try:
        switch = Switch.objects.get(id=switch_id)
        on(switch.host)
        rt_data = json.dumps({
            "status": get(switch.host)
        })
    except Exception:
        rt_data = json.dumps({
            "error": "No switch found"
        })
    return HttpResponse(rt_data, mimetype="application/json")


def turn_off(request, switch_id):
    try:
        switch = Switch.objects.get(id=switch_id)
        off(switch.host)
        rt_data = json.dumps({
            "status": get(switch.host)
        })
    except Exception:
        rt_data = json.dumps({
            "error": "No switch found"
        })
    return HttpResponse(rt_data, mimetype="application/json")


def toggle_switch(request, switch_id):
    try:
        switch = Switch.objects.get(id=switch_id)
        toggle(switch.host)
        rt_data = json.dumps({
            "status": get(switch.host)
        })
    except Exception:
        rt_data = json.dumps({
            "error": "No switch found"
        })
    return HttpResponse(rt_data, mimetype="application/json")
