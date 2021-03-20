echo "
   _______       __             _  __
  / ____(_)___  / /_  ___  ____| |/ /
 / /   / / __ \/ __ \/ _ \/ ___/   /
/ /___/ / /_/ / / / /  __/ /  /   |
\____/_/ .___/_/ /_/\___/_/  /_/|_|
      /_/
	    °•° Process Begins •°•
	    °•° Happy Norouz 💐 •°•
	    °•° Support : @FutureTechnologyGuardX •°•
"
echo '
        •• Getting Packages and Installing
'

apt update && apt upgrade -y && apt install --no-install-recommends -y \
    python \
    curl \

echo '
        •• Cloning Repository
'
git clone https://github.com/CipherX-XD/CipherXSelfBot.git

 
echo '
	•• Getting Libraries and Installing
' 
pip install --upgrade pip wheel 

pip install -r requirements.txt
 
echo "
             _______       __             _  __
            / ____(_)___  / /_  ___  ____| |/ /
           / /   / / __ \/ __ \/ _ \/ ___/   /
          / /___/ / /_/ / / / /  __/ /  /   |
          \____/_/ .___/_/ /_/\___/_/  /_/|_|
              /_/
			•°• Installation Successfully °•°
		   •• Wait till python images are pushed
	   •• Give build logs to Support Group if installation fails
"
echo '
	•• Running the Self Bot
'
python3 -m main.py
