"""Constants."""
from typing import Final

ROOT_DEVICES: Final = "15001"
ROOT_GATEWAY: Final = "15011"
ROOT_GROUPS: Final = "15004"
ROOT_MOODS: Final = "15005"
ROOT_NOTIFICATION: Final = "15006"  # speculative name
ROOT_REMOTE_CONTROL: Final = "15009"
ROOT_SIGNAL_REPEATER: Final = "15014"
ROOT_SMART_TASKS: Final = "15010"
ROOT_START_ACTION: Final = "15013"  # found under ATTR_START_ACTION
ATTR_START_BLINDS: Final = "15015"
ROOT_AIR_PURIFIER: Final = "15025"

ATTR_ALEXA_PAIR_STATUS: Final = "9093"
ATTR_AUTH: Final = "9063"
ATTR_APPLICATION_TYPE: Final = "5750"
ATTR_APPLICATION_TYPE_BLIND: Final = 7

ATTR_BLIND_CURRENT_POSITION: Final = "5536"
ATTR_BLIND_TRIGGER: Final = "5523"

ATTR_AIR_PURIFIER_MODE: Final = "5900"
ATTR_AIR_PURIFIER_FILTER_RUNTIME: Final = "5902"
ATTR_AIR_PURIFIER_FILTER_STATUS: Final = "5903"
ATTR_AIR_PURIFIER_FILTER_LIFETIME_TOTAL: Final = "5904"
ATTR_AIR_PURIFIER_CONTROLS_LOCKED: Final = "5905"
ATTR_AIR_PURIFIER_LEDS_OFF: Final = "5906"
ATTR_AIR_PURIFIER_AIR_QUALITY: Final = "5907"
ATTR_AIR_PURIFIER_FAN_SPEED: Final = "5908"
ATTR_AIR_PURIFIER_MOTOR_RUNTIME_TOTAL: Final = "5909"
ATTR_AIR_PURIFIER_FILTER_LIFETIME_REMAINING: Final = "5910"
ATTR_AIR_PURIFIER_MODE_AUTO: Final = 1

ATTR_CERTIFICATE_PEM: Final = "9096"
ATTR_CERTIFICATE_PROV: Final = "9092"
ATTR_CLIENT_IDENTITY_PROPOSED: Final = "9090"
ATTR_CREATED_AT: Final = "9002"
ATTR_COGNITO_ID: Final = "9101"
ATTR_COMMISSIONING_MODE: Final = "9061"
ATTR_CURRENT_TIME_UNIX: Final = "9059"
ATTR_CURRENT_TIME_ISO8601: Final = "9060"

ATTR_DEVICE_INFO: Final = "3"

ATTR_GATEWAY_ID_2: Final = "9100"  # stored in IKEA app code as gateway id
ATTR_GATEWAY_TIME_SOURCE: Final = "9071"
ATTR_GATEWAY_UPDATE_PROGRESS: Final = "9055"

ATTR_GROUP_MEMBERS: Final = "9018"
ATTR_GROUP_ID: Final = "9038"

ATTR_HOMEKIT_ID: Final = "9083"
ATTR_HS_LINK: Final = "15002"

ATTR_ID: Final = "9003"
ATTR_IDENTITY: Final = "9090"
ATTR_IOT_ENDPOINT: Final = "9103"

ATTR_KEY_PAIR: Final = "9097"

ATTR_LAST_SEEN: Final = "9020"
ATTR_LIGHT_CONTROL: Final = "3311"  # array

ATTR_MASTER_TOKEN_TAG: Final = "9036"
ATTR_MOOD: Final = "9039"

ATTR_NAME: Final = "9001"
ATTR_NTP: Final = "9023"
ATTR_FIRMWARE_VERSION: Final = "9029"
ATTR_FIRST_SETUP: Final = "9069"  # ??? unix epoch value when gateway first setup

ATTR_GATEWAY_INFO: Final = "15012"
ATTR_GATEWAY_ID: Final = "9081"  # ??? id of the gateway
ATTR_GATEWAY_REBOOT: Final = "9030"  # gw reboot
ATTR_GATEWAY_FACTORY_DEFAULTS: Final = "9031"  # gw to factory defaults
ATTR_GATEWAY_FACTORY_DEFAULTS_MIN_MAX_MSR: Final = "5605"
ATTR_GOOGLE_HOME_PAIR_STATUS: Final = "9105"

ATTR_DEVICE_STATE: Final = "5850"  # 0 / 1
ATTR_LIGHT_DIMMER: Final = "5851"  # Dimmer, not following spec: 0..255
ATTR_LIGHT_COLOR_HEX: Final = "5706"  # string representing a value in hex
ATTR_LIGHT_COLOR_X: Final = "5709"
ATTR_LIGHT_COLOR_Y: Final = "5710"
ATTR_LIGHT_COLOR_HUE: Final = "5707"
ATTR_LIGHT_COLOR_SATURATION: Final = "5708"
ATTR_LIGHT_MIREDS: Final = "5711"

ATTR_NOTIFICATION_EVENT: Final = "9015"
ATTR_NOTIFICATION_NVPAIR: Final = "9017"
ATTR_NOTIFICATION_STATE: Final = "9014"

ATTR_OTA_TYPE: Final = "9066"
ATTR_OTA_UPDATE_STATE: Final = "9054"
ATTR_OTA_UPDATE: Final = "9037"

ATTR_PUBLIC_KEY: Final = "9098"
ATTR_PRIVATE_KEY: Final = "9099"
ATTR_PSK: Final = "9091"

ATTR_REACHABLE_STATE: Final = "9019"
ATTR_REPEAT_DAYS: Final = "9041"

ATTR_SEND_CERT_TO_GATEWAY: Final = "9094"
ATTR_SEND_COGNITO_ID_TO_GATEWAY: Final = "9095"
ATTR_SEND_GH_COGNITO_ID_TO_GATEWAY: Final = "9104"
ATTR_SENSOR: Final = "3300"
ATTR_SENSOR_MAX_RANGE_VALUE: Final = "5604"
ATTR_SENSOR_MAX_MEASURED_VALUE: Final = "5602"
ATTR_SENSOR_MIN_RANGE_VALUE: Final = "5603"
ATTR_SENSOR_MIN_MEASURED_VALUE: Final = "5601"
ATTR_SENSOR_TYPE: Final = "5751"
ATTR_SENSOR_UNIT: Final = "5701"
ATTR_SENSOR_VALUE: Final = "5700"
ATTR_START_ACTION: Final = "9042"  # array
ATTR_SMART_TASK_TYPE: Final = (
    "9040"  # 4: Final = transition | 1: Final = not home | 2: Final = on/off
)
ATTR_SMART_TASK_NOT_AT_HOME: Final = 1
ATTR_SMART_TASK_LIGHTS_OFF: Final = 2
ATTR_SMART_TASK_WAKE_UP: Final = 4
ATTR_SMART_TASK_TRIGGER_TIME_INTERVAL: Final = "9044"
ATTR_SMART_TASK_TRIGGER_TIME_START_HOUR: Final = "9046"
ATTR_SMART_TASK_TRIGGER_TIME_START_MIN: Final = "9047"

ATTR_SWITCH_CUM_ACTIVE_POWER: Final = "5805"
ATTR_SWITCH_ON_TIME: Final = "5852"
ATTR_SWITCH_PLUG: Final = "3312"
ATTR_SWITCH_POWER_FACTOR: Final = "5820"

ATTR_TIME_END_TIME_HOUR: Final = "9048"
ATTR_TIME_END_TIME_MINUTE: Final = "9049"
ATTR_TIME_START_TIME_HOUR: Final = "9046"
ATTR_TIME_START_TIME_MINUTE: Final = "9047"

ATTR_TRANSITION_TIME: Final = "5712"

ATTR_USE_CURRENT_LIGHT_SETTINGS: Final = "9070"

# URL to json-file containing links to all firmware updates
URL_OTA_FW: Final = "http://fw.ota.homesmart.ikea.net/feed/version_info.json"

# Mireds range that white-spectrum bulbs can show
RANGE_MIREDS: Final = (250, 454)

# Hue of a RGB bulb
RANGE_HUE: Final = (0, 65535)
# Effective saturation range of a RGB bulb. The bulb will accept
# slightly higher values, but it won't produce any light.
RANGE_SATURATION: Final = (0, 65279)
# Brightness range of all bulbs. 0 will turn off the lamp
RANGE_BRIGHTNESS: Final = (0, 254)

RANGE_BLIND: Final = (0, 100)

RANGE_AIR_PURIFIER: Final = (2, 50)

# XY color
RANGE_X: Final = (0, 65535)
RANGE_Y: Final = (0, 65535)

SUPPORT_BRIGHTNESS: Final = 1
SUPPORT_COLOR_TEMP: Final = 2
SUPPORT_HEX_COLOR: Final = 4
SUPPORT_RGB_COLOR: Final = 8
SUPPORT_XY_COLOR: Final = 16


class Days:
    """Day constants for SmartTask's set_repeat_days(...)"""

    MONDAY = 1 << 6
    TUESDAY = 1 << 5
    WEDNESDAY = 1 << 4
    THURSDAY = 1 << 3
    FRIDAY = 1 << 2
    SATURDAY = 1 << 1
    SUNDAY = 1


ATTR_DEVICE_MANUFACTURER: Final = "0"
ATTR_DEVICE_MODEL_NUMBER: Final = "1"
ATTR_DEVICE_SERIAL: Final = "2"
ATTR_DEVICE_FIRMWARE_VERSION: Final = "3"
ATTR_DEVICE_POWER_SOURCE: Final = "6"
ATTR_DEVICE_BATTERY: Final = "9"
