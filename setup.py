
from cx_Freeze import setup, Executable

# ...

setup(
    name="MyApp",
    version="0.1",
    description="My Application",
    options={
        'build_exe': {
            'include_files': [
                ('database', 'database')  # Include the entire 'database' folder
            ]
        },
    },
    executables=[Executable("Instand_Power.py", base="Win32GUI")]
)