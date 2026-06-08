import subprocess

VOLATILITY_PATH = "/opt/volatility3/bin/vol"

def run_plugin(memory_file, plugin_name):
    command = [
        VOLATILITY_PATH,
        "-f",
        memory_file,
        plugin_name
    ]
    
    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )
    
    return result.stdout, result.stderr
