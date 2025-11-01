[app]
title = Tasks
package.name = tasks
package.domain = org.josapha
source.dir = .
source.include_exts = py, kv, png, jpg, jpeg
version = 1.0
requirements = python3, kivy==2.3.0, kivymd==1.2.0, requests
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
log_level = 2
# (optionnel) tu peux changer l'icône plus tard
icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
