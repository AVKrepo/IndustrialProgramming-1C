#OPEN_CV_SOURCE_DIR="/home/user/opencv-3.4.1"
#echo $OPEN_CV_SOURCE_DIR
mkdir build
cd build
cmake ..
make
./DisplayImage
