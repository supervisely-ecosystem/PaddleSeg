docker run --rm -it \
			--net=host \
			-v `pwd`/../contrib/EISeg/eiseg:/src \
			--entrypoint="" \
			-e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v ~/.Xauthority:/root/.Xauthority \
			-v /opt/pycharm:/pycharm \
    		-v /home/andrew/pycharm-settings/textgen:/root/.PyCharmCE2018.2 \
    		-v /home/andrew/pycharm-settings/textgen__idea:/workdir/.idea \
			paddleseg bash

