printf "\033c\033[43;30m\n"
python3 flasks.py &
ngrok http http://0.0.0.0:5000 &