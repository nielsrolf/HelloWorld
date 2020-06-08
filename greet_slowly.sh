ls -R

git config --global user.email "niels.warncke@gmail.com"
git config --global user.name "CI of mandelbrotjs"

mkdir ~/.ssh
echo $SSH_KEY > tmp && sed '/\\n/G;s/\\n\(.*\)\(.\)/\2\1/;P;D' tmp > ~/.ssh/id_rsa
chmod 600 ~/.ssh/id_rsa
