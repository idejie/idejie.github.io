#! /bin/sh
hexo clean
hexo g
hexo d
cd ./themes/fexo
git add .
git commit -m"modify theme"
git push -f https://github.com/YangDejie/yangdejie.github.io.git feature/theme
cd ../../
git add .
git commit -m"add a post $1"
echo $1
git push https://github.com/YangDejie/yangdejie.github.io.git develop
