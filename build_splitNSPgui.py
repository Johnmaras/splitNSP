import subprocess

build_prc = subprocess.Popen(
    'pyinstaller -y -F -n splitNSP --distpath . --specpath ./build '
    '"C:\\Users\\johnm\\PycharmProjects\\splitNSP\\splitNSPgui.py"')
return_code = build_prc.wait()

print(f"Build ended with {return_code}")