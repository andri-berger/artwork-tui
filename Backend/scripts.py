import subprocess


def open_fred(input_path, output_path):
    results = subprocess.run([
        'gmic', str(input_path),
        'tunnel', '20',
        '-output', str(output_path)
    ])
    return results

