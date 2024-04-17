import os
import subprocess
from zipfile import ZipFile
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    if os.path.exists("tabby\\tabby_config.7z"):
        os.remove("tabby\\tabby_config.7z")
    subprocess.run(
        [
            "7z",
            "a",
            os.getcwd() + "\\tabby\\tabby_config.7z",
            os.getcwd() + "\\tabby\\*.yml",
            "-r",
            "-t7z",
            "-mx=9",
            "-mhe=on",
            "-p" + os.getenv("TABBY_ENCRYPTION_PASSWORD"),
        ]
    )
