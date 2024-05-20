
from cx_Freeze import setup, Executable

# ...

setup(
    name="MyApp",
    version="0.1",
    description="My Application",
    options={
        'build_exe': {
            'include_files': [
                ('base_datos.db', 'base_datos.db'),  # Include the first database file
                ('database/DataBase.DB', 'database/DataBase.DB')  # Include the second database file
            ]
            
        },
    },
    executables=[Executable("Instand_Power.py", base="Win32GUI")]
)