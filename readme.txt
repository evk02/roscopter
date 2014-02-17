1. In the source folder checkout and build mavlink
git clone https://github.com/mavlink/mavlink.git

2. build the roscopter package using rosmake

3. the rc_control_android_app includes an Android app to use as remote controller.
To connect it to roscopter you will need to start the rc_socket_2_roscopter.py node.
Don't forget to run your roscopter with --enable-rc-control=True to receive RC control from your Android app.