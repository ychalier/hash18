# HashCode2018
Repository for Google Hash Code 2018.

## Team *Brel's Shoeshinners*.

 - [Yohan Chalier](https://github.com/ychalier/)
 - [Gauthier Tallec](https://github.com/gtallec/)
 - [François Amat](https://github.com/Fran-cois)
 - [Felix Gaschi]()

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

Servers `lameXX` from 10 to 19 are running on Fedora, 20 to 22 on Ubuntu.

### Parallelization

A basic framework is implemented in `parallel.py`. It implements both *multithreading* (multiple threads on single core) and *multiprocessing* (multiple cores with one thread). Here is a little guide to use it:

First, import `parallel.py` in your file.

    from parallel import *

The define the processing function you want to parallelize. This function must take *one and only one* positional argument.

    def target(arg):
      print(arg)

From here, all you are going to write must be written under the condition:

    if __name__ == "__main__":

Then create the jobs (either threads or processes) with the `dispatch` function.
 - First argument is the mode, either `"p"` for processes or `"t"` for threads.
 - Second argument is the function, `target`.
 - Third argument is the dataset, i.e. a *list* of the elements to use the function on
 - Fourth argument (*optional*) is the number of threads/processes to use. If none is provided, it uses the number of cores detected on the machine.


    jobs = dispatch("p", target, [k for k in range(100)])

Finally, you can start each job with the method `.start()`, and wait till it terminates with `.join()`. The function `start_and_wait` will do that for you. This function returns the elpased in seconds (and prints it before).

    start_and_wait(jobs)

### Create source `zip` archive for submissions

On *Linux*:

    zip -r source *.py

On *Windows*:

    mkdir src
    xcopy "*.py" "src"
    powershell.exe -nologo -noprofile -command "& { Add-Type -A 'System.IO.Compression.FileSystem'; [IO.Compression.ZipFile]::CreateFromDirectory('src', 'source.zip'); }"
    rmdir "src" /s /q

All this is in `zip.bat`.

### Using virtual environments

Remark: can not use virtual environments for Python3 on remote ENST servers,
but most modules are already installed.

    python -m virtualenv venv/

On *Linux*:

    source venv/bin/activate

On *Windows*:

    venv\Scripts\activate.bat

**Exporting modules:**

    pip freeze

Then copy/paste everything to `requirements.txt`.
