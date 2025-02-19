# run_streamlit.py
import streamlit.web.cli as stcli
import sys
import subprocess

try:
    import streamlit  # Проверяем, установлен ли streamlit
except ImportError:
    print("Streamlit is not installed. Running installer...")
    subprocess.call([sys.executable, "install_dependencies.py"])
    print("Please restart the application after installation.")
    sys.exit()

if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "app.py"]
    stcli.main()