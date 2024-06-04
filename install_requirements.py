import subprocess


def install(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation de {package}: {e}")
        return False
    return True


def install_requirements(file_path):
    with open(file_path, "r") as f:
        requirements = f.readlines()

    for requirement in requirements:
        requirement = requirement.strip()
        if not install(requirement):
            print(f"Passage à la dépendance suivante après l'échec de l'installation de {requirement}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python install_requirements.py <path_to_requirements.txt>")
        sys.exit(1)

    requirements_file = sys.argv[1]
    install_requirements(requirements_file)
