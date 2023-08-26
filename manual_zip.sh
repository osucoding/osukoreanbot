#!/bin/zsh

mkdir package
unzip pynacl-aws-linux-2-3.11.zip -d package/
cp *.py package/
cp *.json package/
cd package/
zip -r package.zip *
mv package.zip ../