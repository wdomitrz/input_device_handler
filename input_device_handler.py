#!/usr/bin/env python3

import json
from os import path
from evdev import InputDevice, InputEvent, categorize, ecodes
from subprocess import Popen

CONFIG_FILE = path.expanduser('~/.config/input_device_handler/config.json')


class DeviceHandler:
    def __init__(self, device_options: dict, bindings: dict):
        self.device = InputDevice(device_options['path'])
        self.bindings = bindings

        if 'exclusive' in device_options and device_options['exclusive']:
            self.device.grab()

    def run(self):
        for event in self.device.read_loop():
            self.process_event(event)

    def process_event(self, event: InputEvent):
        if event.type != ecodes.EV_KEY:
            return

        event = categorize(event)
        if event.keycode not in self.bindings:
            return

        action = self.bindings[event.keycode]
        if event.keystate in [event.key_down, event.key_hold]:
            self.perform_action(action)

    def perform_action(self, action: dict):
        cmd = None
        if 'cmd' in action:
            cmd = action['cmd']
        elif 'key' in action:
            cmd = ['xdotool', 'key'] + [action['key']]

        if cmd is not None:
            Popen(cmd)


if __name__ == '__main__':
    with open(CONFIG_FILE, 'r') as config_file:
        config = json.load(config_file)
    DeviceHandler(**config).run()
