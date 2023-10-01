[app]

# (str) Title of your application
title = Enat

# (str) Package name
package.name = yourapppackage

# (str) Package domain (needed for android/ios packaging)
package.domain = com.yourdomain

# (str) Source code where the main.py lives
source.dir = .

# (str) Source filename
source.main = main.py

# (list) Application requirements
requirements = python3,kivy==2.2.1,Pillow==10.0.1,kivymd

# (str) Presplash of the application
presplash.filename = logo.jpg

# (str) Icon of the application
icon.filename = path/to/your/icon/image.png

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (str) Fullscreen (True/False)
fullscreen = False

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 26

# (int) Android NDK version to use
android.ndk = 21.1.6352462

# (int) Gradle version to use
android.gradle = 7.0.0

# (list) Permissions
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# (list) Services
android.services =

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
android.sdk_path =

# (str) Python for android location
p4a.source_dir =

# (str) Costum source folders into the python-for-android
p4a.local_recipes =

# (list) Application meta-data to include
android.meta_data =

# (list) Presplash background color (for the new android toolchain)
# android.presplash_color = #FFFFFF

# (str) Android logcat filters to use
# android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
# android.copy_libs = 1

# (bool) uses the new android toolchain
# p4a.use_p4a = 0

# (str) The configuration file to use
# p4a.config =

# (str) Application log filename
# p4a.log_filename =

# (str) Application log formatting
# p4a.log_format =

# (str) Log verbosity
# p4a.log_level =

# (bool) Enable android arch
# p4a.arch = armeabi-v7a

# (list) Android add-ons
# p4a.additionnal_arch =

# (list) Extra Java dependencies
# android.add_jars =

# (list) Gradle dependencies
# android.gradle_dependencies =

# (list) Android AAR dependencies
# android.aars =

# (list) Java classes to add to the build. Deprecated!
# android.add_libs = libs/foo.jar:libs/bar.jar

# (str) XML file to include with the config
# p4a.extra_google_services =

# (str) launch mode
# android.launch_mode = singleTop

# (list) Java options
# android.add_activity =

# (bool) Enable the android builtin accelerometer
# android.hardware_accelerometer = False

# (str) Android packaging mode (apk or aab)
# android.package_mode = apk

# (bool) Android X compatibility mode
# android.use_androidx = True

# (bool) Enable Android Instant App support
# android.enable_instant_app = False

# (list) Android App Bundle metadata
# android.appbundle =

# (str) Type of app (service, gui, widget)
# android.app_type = gui

# (int) Android notification priority
# android.notification_priority = 2

# (str) Android build toolchain (new or old)
# android.toolchain =

# (str) Android builder
# android.build_mode = debug

# (bool) Allow putting python in sdcard
# android.allow_external_storage = False

# (str) Android orientation
# android.orientation = unspecified

# (bool) Preserve old build artifact when build.sh is run
# preserve_build_artifacts = False

# (str) build.py directory (not the python-for-android dir)
# build_dir = ./.buildozer

# (str) bin_dir
# bin_dir = ./bin
