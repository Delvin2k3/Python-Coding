from rich import print
iphone_info = {
    "model": "iPhone 13 Pro",
    "release_year": 2021,
    "specs": {
        "display": {
            "type": "Super Retina XDR display",
            "size": "6.1 inches",
            "resolution": "2532 x 1170 pixels",
            "refresh_rate": "120Hz"
        },
        "processor": {
            "chip": "A15 Bionic chip",
            "architecture": "64-bit",
            "neural_engine": "16-core"
        },
        "camera": {
            "rear": {
                "triple_camera": {
                    "ultra_wide": "12MP",
                    "wide": "12MP",
                    "telephoto": "12MP"
                },
                "features": [
                    "Night mode",
                    "Deep Fusion",
                    "Smart HDR 4",
                    "4K Dolby Vision HDR recording"
                ]
            },
            "front": {
                "single_camera": "12MP",
                "features": [
                    "Night mode",
                    "Deep Fusion",
                    "Smart HDR 4",
                    "4K Dolby Vision HDR recording"
                ]
            }
        },
        "battery": {
            "capacity": "3095 mAh",
            "charging": {
                "fast_charging": "20W",
                "wireless_charging": "MagSafe and Qi"
            }
        },
        "storage_options": ["128GB", "256GB", "512GB", "1TB"],
        "operating_system": "iOS 15",
        "connectivity": [
            "5G",
            "Wi-Fi 6",
            "Bluetooth 5.0",
            "Ultra Wideband (UWB)"
        ],
        "biometrics": "Face ID",
        "water_resistance": "IP68"
    },
    "price": {
        "base_model": 999,
        "max_storage_model": 1499
    },
    "colors": ["Graphite", "Gold", "Silver", "Sierra Blue"]
}

print(iphone_info)