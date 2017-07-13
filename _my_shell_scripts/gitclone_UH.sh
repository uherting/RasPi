if [ ! -d UH ]
then
  echo "dir UH does not exist!"
  exit 1
fi

cd UH

git clone https://github.com/uherting/RasPi.git
git clone https://github.com/uherting/PyLibs.git
git clone https://github.com/uherting/TimeCheck.git

cd -

