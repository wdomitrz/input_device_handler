# Input device handler

## Requirements

`python3` with `json`, `os`, `evdev` and `subprocess` modules.

## Configuration

An example of configuration file is in [config.json](config.json). It is adjusted for Razer Naga 2014 and my [i3](https://i3wm.org/) config.

The configuration is stored in `~/.config/input_device_handler/config.json` file.

The configuration file is a `dict` in JSON format with two keys:

* `device_options` - `dict`:
    * `path` - `string`, an absolute path to the device file,
    * `exclusive` - `boolean`, indicates if the device is exclusive for this programme (default value: `false`),

* `bindings` - `dict`, with keys corresponding to keys' names in [python-evdev  format](https://python-evdev.readthedocs.io/en/latest/apidoc.html#evdev.ecodes.keys):
    * `<key name>` - `dict`, with one key. The allowed options are:
        * `cmd` - `list`/`string`, a value is passed as an argument to `subprocess.Popen`,
        * `key` - `string`, a value is passed as an argument to `xdotool key`.

## License

Copyright (c) Witalis Domitrz

Licensed under the [MIT](LICENSE) license.
