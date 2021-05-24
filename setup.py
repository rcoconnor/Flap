from cx_Freeze import setup, Executable 

setup(
        name="Flap!",
        options={
            "build_exe": {
                "packages":["pygame"], 
                "include_files":["bird_sprite.jpg", 
                    "imageBackground.png", 
                    "Pipe_Bottom.png", 
                    "Pipe_Long.png", 
                    "Pipe_Long_Bottom.png"]
            }
        }, 
        executables = [Executable("FlappyBird.py")]
        )
