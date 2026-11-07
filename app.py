import yaml


def load_config():
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)

    return config


def main():
    config = load_config()

    print("Application Configuration:")
    print(f"App Name: {config['app_name']}")
    print(f"Debug: {config['debug']}")
    print(f"Port: {config['port']}")


if __name__ == "__main__":
    main()
