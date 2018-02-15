# HashCode2018
Repository for Google Hash Code 2018.

## Team *Brel's Shoeshinners*.

 - [Yohan Chalier](https://github.com/ychalier/)
 - [Gauthier Tallec](https://github.com/gtallec/)

## Links

 - [Repository](https://github.com/ychalier/HashCode2018.git)
 - [Judge System](https://hashcodejudge.withgoogle.com/)
 - [InfRes servers](https://services.infres.enst.fr/services/infres/serveurs.html)
 - [InfRes servers cpu](https://services.infres.enst.fr/cpu/)

## Tools

### ENST servers

First connect via ssh to `ssh.enst.fr`. Then one can reach internal servers
like `lameXX.enst.fr`. Then just clone the repository:

    git clone https://github.com/ychalier/HashCode2018.git

### Create source `zip` archive for submissions

On *Linux*:

    zip -r source *.py

On *Windows*:

    mkdir src
    xcopy "*.py" "src"
    powershell.exe -nologo -noprofile -command "& { Add-Type -A 'System.IO.Compression.FileSystem'; [IO.Compression.ZipFile]::CreateFromDirectory('src', 'source.zip'); }"
    rmdir "src" /s /q

All this is in `zip.bat`.
