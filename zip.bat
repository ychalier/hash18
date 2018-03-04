mkdir src
xcopy "*.py" "src"
powershell.exe -nologo -noprofile -command "& { Add-Type -A 'System.IO.Compression.FileSystem'; [IO.Compression.ZipFile]::CreateFromDirectory('src', 'source.zip'); }"
rmdir "src" /s /q
