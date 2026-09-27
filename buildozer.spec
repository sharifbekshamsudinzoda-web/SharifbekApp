[app]

title = Барномаи Шарифбек
package.name = sharifbekapp
package.domain = org.sharifbek

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0

android.api = 35
android.minapi = 24

android.archs = arm64-v8a, armeabi-v7a

android.accept_sdk_license = True

# Uncomment and set this if you later add an icon:
# icon.filename = %(source.dir)s/icon.png

[buildozer]

log_level = 2
warn_on_root = 1
