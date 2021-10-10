#!/usr/bin/env python3
from flask import Flask
from flask_restx import Resource, Api
import pyric.utils.rfkill as rfkill

app = Flask(__name__)
api = Api(app)


class BluetoothInterface:
    """
    Holder class for information about the system Bluetooth interface.
    We assume the system only has one.... for now.
    """
    name = 'hci0'
    _bt_int_detail = rfkill.rfkill_list().get(name)
    if not _bt_int_detail:
        raise Exception("No interface named %s found." % name)
    idx = _bt_int_detail.get('idx')


@api.route('/api/v1/network/bluetooth')
class BluetoothStatusEndpoint(Resource):
    """
    Endpoint to get the detailed status of the Bluetooth
    interface(s) on this system.
    """
    def get(self):
        return rfkill.rfkill_list()


@api.route('/api/v1/network/bluetooth/enable')
class BluetoothEnableEndpoint(Resource):
    """
    Enable the system Bluetooth interface.
    """
    def get(self):
        rfkill.rfkill_unblock(BluetoothInterface.idx)


@api.route('/api/v1/network/bluetooth/disable')
class BluetoothEnableEndpoint(Resource):
    """
    Disable the system Bluetooth interface.
    """
    def get(self):
        rfkill.rfkill_block(BluetoothInterface.idx)


@api.route('/api/v1/network/bluetooth/sensor')
class BluetoothEnableEndpoint(Resource):
    """
    This provides a HomeAssistant RESTful sensor response.
    https://www.home-assistant.io/integrations/sensor.rest/
    Value template of the sensor should be: "{{ value_json.blocked }}"
    """
    def get(self):
        # The logical or here will factor in whether there is a hard or soft block
        # on the interface. If either is true then the interface is assumed to be
        # blocked/disabled.
        bt_int_state = rfkill.hard_blocked(BluetoothInterface.idx) | rfkill.soft_blocked(BluetoothInterface.idx)
        return {'blocked': bt_int_state}


if __name__ == '__main__':
    app.run(debug=True)
