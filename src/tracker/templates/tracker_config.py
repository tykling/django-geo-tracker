CONFIG = {
    "NAME": "{{ name }}",
    "DESCRIPTION": "{{ description }}",
    "LORA": {
        "COUNTRY": "EU",
        "DEVICE_ADDRESS": bytearray([{{ lora_device_address|join:"," }}]),
        "ABP_NETWORK_SESSION_KEY": bytearray([{{ lora_network_session_key|join:"," }}]),
        "ABP_APPLICATION_SESSION_KEY": bytearray([{{ lora_app_session_key|join:"," }}]),
    },
    "SLEEP_SECONDS": {{ sleep_seconds }},
}
